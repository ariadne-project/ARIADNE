#!/usr/bin/env python3
"""Check the ARIADNE provenance ledger in README.md.

The ledger is the section between "## Provenance ledger" and "## License".
Each entry must follow the template in CONTRIBUTING.md, and entries that
already exist on the base revision (default: origin/main) must be unchanged,
because the ledger is append-only.

Uses only the Python standard library (3.9+), so it runs on a fresh machine
and in GitHub Actions without installing anything.

Exit status: 0 = no errors (warnings allowed), 1 = errors found,
2 = the check could not run.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

LEDGER_START = "## Provenance ledger"
LEDGER_END = "## License"
FIELDS = ("Type", "Claim", "Evidence", "Recorded by", "Supersedes")
TYPES = ("Observed", "User-reported", "Proposal", "Decision", "Result", "Correction")
HEADING = re.compile(r"^### (\d{4}-\d{2}-\d{2})(?: to (\d{4}-\d{2}-\d{2}))? - (\S.*)$")
FIELD_LINE = re.compile(r"^\*\*(?P<name>[A-Za-z -]+):\*\* ?(?P<value>.*?)(?P<brk>\\?)$")
LINK = re.compile(r"\]\(([^)\s]+)\)")

# <root>/.claude/skills/ariadne-editor/scripts/check_ledger.py
DEFAULT_ROOT = Path(__file__).resolve().parents[4]


@dataclass
class Entry:
    line: int  # 1-based line number of the heading
    heading: str  # heading text without "### "
    block: str  # whole entry, used for the append-only comparison
    fields: dict = field(default_factory=dict)
    start: dt.date | None = None


@dataclass
class Report:
    path: str
    messages: list = field(default_factory=list)

    def error(self, line, msg):
        self.messages.append(("error", line, msg))

    def warning(self, line, msg):
        self.messages.append(("warning", line, msg))

    @property
    def errors(self):
        return [m for m in self.messages if m[0] == "error"]

    def print(self):
        in_ci = os.environ.get("GITHUB_ACTIONS") == "true"
        for level, line, msg in self.messages:
            print(f"{self.path}:{line}: {level}: {msg}")
            if in_ci:
                print(f"::{level} file={self.path},line={line}::{msg}")


def parse_date(text, line, report):
    try:
        return dt.date.fromisoformat(text)
    except ValueError:
        report.error(line, f"'{text}' is not a real calendar date")
        return None


def parse_ledger(text, report):
    """Split the ledger section into entries and check each entry's shape."""
    lines = text.split("\n")
    try:
        start = lines.index(LEDGER_START)
    except ValueError:
        report.error(1, f"no '{LEDGER_START}' heading found")
        return []
    try:
        end = lines.index(LEDGER_END, start)
    except ValueError:
        report.error(start + 1, f"no '{LEDGER_END}' heading after the ledger")
        return []

    heads = [i for i in range(start + 1, end) if lines[i].startswith("### ")]
    entries = []
    for n, i in enumerate(heads):
        stop = heads[n + 1] if n + 1 < len(heads) else end
        body = lines[i:stop]
        while body and not body[-1].strip():
            body.pop()
        entry = Entry(line=i + 1, heading=lines[i][4:], block="\n".join(body))
        entries.append(entry)

        m = HEADING.match(lines[i])
        if not m:
            report.error(i + 1, "heading must look like '### YYYY-MM-DD - Short title' "
                                "or '### YYYY-MM-DD to YYYY-MM-DD - Short title'")
        else:
            entry.start = parse_date(m.group(1), i + 1, report)
            if m.group(2):
                end_date = parse_date(m.group(2), i + 1, report)
                if entry.start and end_date and end_date < entry.start:
                    report.error(i + 1, "the date range ends before it starts")

        if len(body) < 2 or body[1].strip():
            report.error(i + 1, "leave one blank line between the heading and the fields")
        field_lines = [ln for ln in body[1:] if ln.strip()]
        if len(field_lines) != len(FIELDS):
            report.error(i + 1, f"expected {len(FIELDS)} field lines "
                                f"({', '.join(FIELDS)}), found {len(field_lines)}")
        offset = i + 1 + body[1:].index(field_lines[0]) + 1 if field_lines else i + 1
        for k, (raw, name) in enumerate(zip(field_lines, FIELDS)):
            ln = offset + k
            fm = FIELD_LINE.match(raw)
            if not fm or fm.group("name") != name:
                report.error(ln, f"field {k + 1} should start with '**{name}:** '")
                continue
            value = fm.group("value").strip()
            entry.fields[name] = value
            last = k == len(FIELDS) - 1
            if not last and not fm.group("brk"):
                report.error(ln, f"'{name}' line must end with a backslash (\\) "
                                 "so GitHub shows the next field on its own line")
            if last and fm.group("brk"):
                report.error(ln, f"'{name}' is the last field and must not end with a backslash")
            if not value:
                report.error(ln, f"'{name}' is empty")
    return entries


def check_content(entries, readme_dir, report):
    """Rules that relate entries to each other and to the repository."""
    today = dt.date.today()
    seen = {}
    previous = None
    for e in entries:
        if e.heading in seen:
            report.error(e.line, f"duplicate heading; the same heading is on line {seen[e.heading]}")
        seen.setdefault(e.heading, e.line)

        if e.start:
            if e.start > today:
                report.warning(e.line, "date is in the future")
            if previous and e.start < previous:
                report.warning(e.line, "dated earlier than the entry above it; "
                                       "fine when recording a past event late")
            previous = e.start

        etype = e.fields.get("Type")
        if etype is not None and etype not in TYPES:
            report.error(e.line, f"type '{etype}' is not one of: {', '.join(TYPES)}")

        sup = e.fields.get("Supersedes")
        if sup is not None:
            if sup.lower() == "none":
                if etype == "Correction":
                    report.error(e.line, "a Correction must name the entry it corrects in "
                                         "'Supersedes', as 'YYYY-MM-DD - Short title'")
            elif sup == e.heading:
                report.error(e.line, "an entry cannot supersede itself")
            elif sup not in seen:
                report.error(e.line, f"'Supersedes' names '{sup}', which is not an earlier "
                                     "entry heading (copy the heading text exactly)")

        for target in LINK.findall(e.block):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
                continue  # external URL, mailto: or same-page anchor
            path = target.split("#", 1)[0]
            if path and not (readme_dir / path).exists():
                report.error(e.line, f"link target '{path}' does not exist in the repository")


def check_append_only(entries, base_text, base, report):
    """Every entry on the base revision must still be present, unchanged and in order."""
    old = parse_ledger(base_text, Report(path="(base)"))
    for k, before in enumerate(old):
        if k >= len(entries):
            report.error(entries[-1].line if entries else 1,
                         f"entry '{before.heading}' from {base} is missing")
            return 0
        after = entries[k]
        if after.block != before.block:
            what = "changed" if after.heading == before.heading else "removed, moved or renamed"
            report.error(after.line, f"entry '{before.heading}' from {base} was {what}; "
                                     "the ledger is append-only, so add a Correction instead")
            return 0
    return len(entries) - len(old)


def git_show(root, base, relpath):
    try:
        out = subprocess.run(["git", "-C", str(root), "show", f"{base}:{relpath}"],
                             capture_output=True, text=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return None
    return out.stdout


def main(argv=None):
    p = argparse.ArgumentParser(description="Check the ARIADNE provenance ledger.")
    p.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="repository root")
    p.add_argument("--file", default="README.md", help="file that holds the ledger")
    p.add_argument("--base", default="origin/main",
                   help="git revision whose entries must be unchanged (default: origin/main)")
    p.add_argument("--no-history", action="store_true", help="skip the append-only check")
    p.add_argument("--list", action="store_true",
                   help="list entry headings and types (for 'Supersedes'), then exit")
    args = p.parse_args(argv)

    path = args.root / args.file
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"cannot read {path}: {exc}", file=sys.stderr)
        return 2

    report = Report(path=args.file)
    entries = parse_ledger(text, report)

    if args.list:
        for e in entries:
            print(f"line {e.line}: {e.heading}  [{e.fields.get('Type', '?')}]")
        return 0

    check_content(entries, path.parent, report)

    added = None
    if not args.no_history:
        base_text = git_show(args.root, args.base, args.file)
        if base_text is None:
            report.warning(1, f"could not read {args.file} at '{args.base}', so the "
                              "append-only check was skipped (run 'git fetch' and retry)")
        else:
            added = check_append_only(entries, base_text, args.base, report)

    report.print()
    summary = f"{len(entries)} ledger entries checked"
    if added is not None:
        summary += f", {added} new since {args.base}"
    n_err = len(report.errors)
    n_warn = len(report.messages) - n_err
    print(f"{summary}: {n_err} error(s), {n_warn} warning(s)")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
