# Derived schema files

**Status:** Derived files for a proposed system that is not implemented. Written on 2026-10-20 under decision D8 A, which [Handoffs, section 5](../HANDOFFS.md#5-derived-schema-files) describes. The run-record files and the files of Evaluation interfaces 1.1 were added on 2026-10-21, in phase P6, and corrected against the final text of those documents in the final review of phase P7. On 2026-10-22 the files were derived again for the design changes C01 to C11 ([ledger](../../README.md#2026-10-29---workflow-and-review-design-consolidated)): the Issue format files from version 0.6, the run-record files from Run records 1.1, and the files of Evaluation interfaces 1.2, three expected-side files among them. No pipeline uses them yet. The documents they follow are preliminary for Stage 1 since 2026-10-21 ([ledger](../../README.md#2026-10-29---workflow-and-review-design-consolidated)), amended on 2026-10-22 (changes C01 to C11) ([ledger](../../README.md#2026-10-29---workflow-and-review-design-consolidated)); each file keeps the label of the document version it was derived from until it is next derived (D29 A), and the documents win. On 2026-10-27 the files whose shape the decisions AD-D01, AD-D04 and AD-D06 change were derived again ([ledger](../../README.md#2026-10-29---workflow-and-review-design-consolidated)): `evidence-entry` and `question` from Issue format 0.7, `run-log-entry` and `report-index-line` from Run records 1.2, and `evaluation-run-record` and `evaluation-batch-record` from Evaluation interfaces 1.3; the other files keep their labels, because those versions do not change their shape. On 2026-10-28 the files whose shape the decisions of that day change were derived again ([ledger](../../README.md#2026-10-29---workflow-and-review-design-consolidated)): `issue` from Issue format 0.8, `run-log-entry` and `report-index-line` from Run records 1.3, and `evaluation-batch-record` from Evaluation interfaces 1.4, which also adds `evaluation-plan`. `answer` and `evidence-entry` keep their labels, because their shape does not change; their descriptions now say what version 0.8 settles and which names were accepted on 2026-10-28. Later that day, `run-log-entry` was derived again from Run records 1.4 and `evaluation-batch-record` from Evaluation interfaces 1.5 ([ledger](../../README.md#2026-10-29---workflow-and-review-design-consolidated); [ledger](../../README.md#2026-10-29---workflow-and-review-design-consolidated); [ledger](../../README.md#2026-10-29---workflow-and-review-design-consolidated)); Issue format 0.9 changes the shape of no file, so the issue-format files keep their labels (D29 A; [ledger](../../README.md#2026-10-29---workflow-and-review-design-consolidated)); Issue format 0.10 changes none either ([ledger](../../README.md#2026-10-29---workflow-and-review-design-consolidated)).\
**Precedence:** The documents win. Where a file here differs from the document it is derived from, the document governs and the file is corrected.\
**Stage:** Stage 1 ([stage legend](../PACKAGE_ADOPTION.md#41-stage-legend)). Every section of this README and every file it lists describes a Stage 1 format.

## What the files are

**Stage:** Stage 1.

Each file describes the shape of one kind of JSON object in machine-readable form, as a JSON Schema (draft 2020-12): which fields the object has, which of them are required, their types and their allowed values. Software can use a file to check that an object has the right shape before anyone uses it.

A schema file checks shape only. It cannot tell whether a value is right, whether a citation holds, or whether an id names something that exists.

The files come in four groups:

1. **Issue format files.** They follow [Issue format](../../ISSUE_FORMAT.md) version 0.10, the decided Stage 1 format as amended three times on 2026-10-28; versions 0.9 and 0.10 change no file's shape. Each carries the label of the version it was last derived from: `issue` that of version 0.8, `evidence-entry` and `question` that of version 0.7, and the files that neither version changed in shape that of version 0.6.
2. **Expected-side files for evaluation.** They are proposals. [Evaluation interfaces, section 4](../EVALUATION_INTERFACES.md#4-expected-side-proposed) proposes these formats, and Tillman Heisner accepts, changes or replaces each one. Until he does, the matching file is a proposal too. Where section 4 gives no key name, the file proposes one, and that key's description starts with "Proposed name". Three of them, the expected issue list, the expected judgments and issues and the inquiry expectations, follow Evaluation interfaces version 1.2 and carry the required `mode` of change C05; the others still follow version 1.0.
3. **Run-record files.** They follow [Run records](../RUN_RECORDS.md) version 1.4, whose Stage 1 status is preliminary and decided (its Stage 2 sections remain proposed): the entries of the run log and of the batch logs, the request log, the monitor log, the report index and the budget profiles. The run log carries the label of version 1.4 and the report index that of version 1.3; the files that versions 1.2 to 1.4 did not change, the request log, the monitor log and the budget profiles, still carry the label of version 1.1. These derived schemas remain drafts; this is separate from the governing document's preliminary-decided Stage 1 status and does not freeze proposed key names. Their checksums are lowercase, as [Run records, section 1.2](../RUN_RECORDS.md#12-terms) defines a checksum (D13 A). Where the document gives no key name, the file proposes one, marked "Proposed name", as in group 2.
4. **Evaluation input-side and run-record files.** They follow [Evaluation interfaces](../EVALUATION_INTERFACES.md) version 1.5 (Draft): the batch record carries the label of version 1.5, the evaluation plan that of version 1.4, the evaluation run record that of version 1.3, and the files that neither version changed that of version 1.2. ARIADNE specifies these formats and Tillman Heisner freezes each version (D9 A), so they stay drafts until he does. Their checksums are lowercase too ([Evaluation interfaces, section 3](../EVALUATION_INTERFACES.md#3-input-side)). Where the document gives no key name, the file proposes one, marked "Proposed name", as in group 2.

In groups 3 and 4, a key is not marked where the other of the two documents, or [Issue format](../../ISSUE_FORMAT.md), already gives that name for the same field, for example the usage categories of [Run records, section 2.5](../RUN_RECORDS.md#25-the-request-log) in the evaluation run record. Nor is a name that Tillman Heisner accepted on 2026-10-28 ([ledger](../../README.md#2026-10-29---workflow-and-review-design-consolidated)), such as `base`, `result`, `environment` or the line kinds `monitor_hold` and `monitor_release`; acceptance fixes the name only, not what the field does.

The examples in the files are illustrative: ids, times, sizes, counts, model names and most checksums are made up. The exceptions are the pins (the Hermes tag and its commit, the EnzymeML commit and the SHA-256 of its schema) and the size and SHA-256 of the stored T9HQ4X input, which carry their real values wherever they appear. Where an example holds sizes that depend on each other, such as the blocks of a packet and the packet, they add up, and the file's `$comment` says how.

## The document wins

**Stage:** Stage 1.

The first sentence of each file's `description` names the document and the version the file is derived from, and says that the document wins. The same sentence opens the file's `$comment`, as Handoffs section 5 asks.

The files add no rule of their own. Where a document leaves something open, the file leaves it open too and says so in a `$comment`. When a document changes, the file is changed to match.

## The files

**Stage:** Stage 1.

| File | What it describes | Derived from | Status | Stage |
|---|---|---|---|---|
| `issue.schema.json` | One issue in the record's issue list | Issue format 0.8, sections 4, 4.1 and 4.2, and section 7.1 for `closed_by` on re-check | Follows the decided format | Stage 1 |
| `judgment.schema.json` | One judgment of the verification agent | Issue format 0.6, section 4.2 | Follows the decided format | Stage 1 |
| `question.schema.json` | One question, with the shape of a fully bound rate-law option's value (`$defs/rate_law_option_value`) | Issue format 0.7, sections 3.1 and 5.1; key names of the rate-law option from Handoffs 2.9 | Follows the decided format | Stage 1 |
| `answer.schema.json` | One answer to one question | Issue format 0.6, section 5.2, and section 5.1 for the note that "The question does not fit" needs; the value `does_not_fit` from Handoffs 2.9; `not_available: true`, as version 0.8, section 5.2 rule 6, settles it | Follows the decided format | Stage 1 |
| `evidence-entry.schema.json` | One entry of the evidence file | Issue format 0.7, sections 3.1, 6, 7.2 and 8.1; key names it leaves open from Handoffs 2.6, 2.11 and 2.15, among them `model`, `bindings` and `question_id` or `action_id` on each `S-RATELAW` entry | Follows the decided format | Stage 1 |
| `not-mapped-entry.schema.json` | One entry of the not-mapped report, and the same entry as the draft proposal holds it | Issue format 0.6, sections 7.1 and 8.1; key names from Handoffs 2.5 and 2.14 | Follows the decided format | Stage 1 |
| `expected-value-table.schema.json` | Expected values for an extraction item | Evaluation interfaces 1.0 (Draft), section 4.2 | Proposal | Stage 1 |
| `unit-table.schema.json` | The unit table | Evaluation interfaces 1.0 (Draft), section 4.2 | Proposal | Stage 1 |
| `expected-not-mapped-list.schema.json` | Expected not-mapped list | Evaluation interfaces 1.0 (Draft), section 4.2 | Proposal | Stage 1 |
| `expected-issue-list.schema.json` | Expected round-1 issues of the deterministic verifier, mode A | Evaluation interfaces 1.2 (Draft), sections 4.1 rule 12 and 4.3 | Proposal | Stage 1 |
| `expected-judgments-and-issues.schema.json` | Expected judgments, added issues and traps for the verification agent, mode A rows keyed by frozen issue id, kind and pointers, mode B rows by source anchor, field and kind | Evaluation interfaces 1.2 (Draft), sections 4.1 rule 12 and 4.4 | Proposal | Stage 1 |
| `inquiry-expectations.schema.json` | Inquiry expectations, mode A or mode B | Evaluation interfaces 1.2 (Draft), sections 2.2, 4.1 rule 12 and 4.5 | Proposal | Stage 1 |
| `change-list.schema.json` | Change list of an entry variant | Evaluation interfaces 1.0 (Draft), section 4.1 rule 6 | Proposal | Stage 1 |
| `planted-defect-list.schema.json` | Planted-defect list | Evaluation interfaces 1.0 (Draft), section 4.1 rule 7 | Proposal | Stage 1 |
| `run-log-entry.schema.json` | One entry of a run's run log or of a batch's batch log: the common fields, and the fields of each of the 36 entry kinds, attempt entries, batch-log entries, the pointer entries of live pointers, the versions of a round's working copy, the stored approval summary and the status of the monitoring deadlines included | [Run records](../RUN_RECORDS.md) 1.4, sections 1.2, 2.3, 2.4, 2.7 and 2.8 | Draft derived schema; document governs | Stage 1 |
| `request-log-entry.schema.json` | One request entry, response entry or status entry of the model gateway's request log | Run records 1.1, sections 2.3, 2.5 and 4.4 | Draft derived schema; document governs | Stage 1 |
| `monitor-record.schema.json` | One record of the monitor log: an observation of monitor M1, M2 or M3 on one attempt | Run records 1.1, sections 2.3 and 2.6 | Draft derived schema; document governs | Stage 1 |
| `report-index-line.schema.json` | One line of the report index: a report line for each containment report, a hit line for each containment hit in a real run, or a monitor hold, repair or release line for an execution environment | Run records 1.3, sections 2.3 and 2.7 | Draft derived schema; document governs | Stage 1 |
| `budget-profile.schema.json` | One budget profile file, the development profile or the evaluation profile | Run records 1.1, sections 4.1, 4.5 and 4.6 | Draft derived schema; document governs | Stage 1 |
| `evaluation-packet-manifest.schema.json` | The packet manifest of a packet of an evaluation or measurement batch, in its run-log form | [Evaluation interfaces](../EVALUATION_INTERFACES.md) 1.2 (Draft), section 3.6; the fields of [Handoffs, section 2.4](../HANDOFFS.md#24-input-packets) with proposed key names | Draft, until Tillman Heisner freezes the version (D9 A) | Stage 1 |
| `evaluation-run-record.schema.json` | The evaluation run record of one run, with one row per agent attempt | Evaluation interfaces 1.3 (Draft), sections 10.1 to 10.4 | Draft, until Tillman Heisner freezes the version (D9 A) | Stage 1 |
| `evaluation-batch-record.schema.json` | The batch record of one evaluation or measurement batch, with the evaluation-plan reference and the tuning disclosure of a held-out assessment | Evaluation interfaces 1.5 (Draft), sections 4.8, 7.1, 10.1 and 10.4 | Draft, until Tillman Heisner freezes the version (D9 A) | Stage 1 |
| `evaluation-plan.schema.json` | One version of the evaluation plan: the continuation criteria for Stage 1 held-out assessment, with the plan's version, its approval and its freeze; no threshold | Evaluation interfaces 1.4 (Draft), section 4.8 | Draft, until Tillman Heisner freezes the version (D9 A) | Stage 1 |
| `input-set-manifest.schema.json` | The input-set manifest | Evaluation interfaces 1.2 (Draft), section 3 (introduction) and section 3.1 | Draft, until Tillman Heisner freezes the version (D9 A) | Stage 1 |
| `variant-list.schema.json` | The variant list of entry variants, measurement-only size variants included | Evaluation interfaces 1.2 (Draft), section 3 (introduction) and section 3.2 | Draft, until Tillman Heisner freezes the version (D9 A) | Stage 1 |
| `example-manifest.schema.json` | One example manifest, per agent, condition and fold; the fold is the actual one in both conditions | Evaluation interfaces 1.2 (Draft), section 3 (introduction) and section 3.3 | Draft, until Tillman Heisner freezes the version (D9 A) | Stage 1 |
| `item-list.schema.json` | One item list, per step under test | Evaluation interfaces 1.2 (Draft), section 3 (introduction) and section 3.4 | Draft, until Tillman Heisner freezes the version (D9 A) | Stage 1 |

The wording-rating sheet of Evaluation interfaces 4.5 has no file here, because it belongs to the scores folder, not to the expected side. The handoff files that [Handoffs, section 5](../HANDOFFS.md#5-derived-schema-files) lists, such as the deterministic report or the question round, are not written yet; under D29 A they are written in phase P8, with the implementation. They will hold the objects described here.

## Names, not addresses

**Stage:** Stage 1.

Each file's `$id` has the form `urn:ariadne:design:<name>:v<version>`, for example `urn:ariadne:design:issue:v0.8`. It is a name, not a web address, and nothing is hosted under it. In group 1, `v0.8` names the file written for Issue format 0.8 (`issue`), `v0.7` the files written for version 0.7 (`evidence-entry`, `question`), and `v0.6` the files that neither version changed in shape. The run-record files carry `v1.4` where Run records 1.4 changed them (`run-log-entry`), `v1.3` where version 1.3 last changed them (`report-index-line`) and `v1.1` otherwise, and the files of group 4 carry `v1.5` where Evaluation interfaces 1.5 changed them (`evaluation-batch-record`), `v1.4` where version 1.4 added them (`evaluation-plan`), `v1.3` where version 1.3 last changed them (`evaluation-run-record`) and `v1.2` otherwise: each carries the version of the document it was last derived from, for example `urn:ariadne:design:run-log-entry:v1.4`. Of the expected-side files, the three that version 1.2 changed carry `v1.2`; the others follow Evaluation interfaces 1.0 (Draft), as their `description` says, and keep `v0.5` until they are derived again from a frozen version ([Evaluation interfaces, section 10.8](../EVALUATION_INTERFACES.md#108-derived-schema-files-proposed)).

Each file stands alone and refers to no other file. Some definitions therefore appear in several files: the list of issue kinds, the id patterns, the JSON Pointer grammar and the time pattern. They must stay identical; when one changes, all copies change. Groups 3 and 4 add further shared definitions, among them `checksum`, `date`, `file_ref`, `generation_settings`, `usage_totals`, `usage_unknown_summary`, `requests_summary`, `served_model`, `stop_cause`, `batch_end`, `evaluation_plan_ref` and `tuning_disclosure`. `run-log-entry.schema.json` and `evaluation-packet-manifest.schema.json` share `packet_manifest_part` and `evaluation_packet_part`. Two checksum definitions exist: `checksum` in groups 3 and 4, 64 lowercase hexadecimal characters as [Run records, section 1.2](../RUN_RECORDS.md#12-terms) and [Evaluation interfaces, section 3](../EVALUATION_INTERFACES.md#3-input-side) write a checksum, and `sha256` in group 2, which still accepts either letter case; it takes the lowercase form when those files are derived again from the frozen version (Evaluation interfaces, section 10.8).

**Whole strings.** Every identifier and checksum pattern matches the whole string and nothing else ([Run records, section 1.2](../RUN_RECORDS.md#12-terms), Whole-string grammar): the ARIADNE ids, EnzymeML object ids, issue and question ids, git commits and both checksum definitions end in `$(?![\s\S])`, and so do the date and timestamp patterns. In ECMA-262 the lookahead changes nothing, since `$` matches only at the end there; in Python's `re`, which the `jsonschema` library uses, `$` also matches before a final line feed, and the lookahead makes such a value fail. So a value with a trailing line feed, a carriage return and line feed, leading or trailing whitespace, or more or fewer characters than its grammar allows does not match. Each grammar keeps its own characters, case and length; no value is trimmed or rewritten to make it match.

Four files also hold an object in the form one writer supplies it, for the handoff files that are still to come:

- `issue.schema.json`, `$defs/raiser_part`: the fields the raiser writes, before software adds the id, round, raiser and status. Issues the verification agent adds carry no `rule_id` (Issue format 4; Handoffs 2.8), so the verification-report file is to use this part with `rule_id: false`;
- `question.schema.json`, `$defs/inquiry_agent_part`: the fields the inquiry agent writes;
- `answer.schema.json`, `$defs/as_supplied`: an answer as the person supplies it, before software adds `answered_by` and `answered_at` (Handoffs 2.10). The answer of Issue format 10.2 has this form;
- `not-mapped-entry.schema.json`, `$defs/as_drafted`: a not-mapped entry as the extraction agent writes it in the draft proposal, with `candidate_field` as `{object, field}`, before the assembly step replaces it with the field's pointer (Handoffs 2.5, 2.6 and 2.14).

Another schema reaches such a part through the `$id`, for example `urn:ariadne:design:issue:v0.8#/$defs/raiser_part`.

**Log files.** The run log, batch log, request log, monitor log and report index are JSON Lines files: one JSON object per line ([Run records, section 2.3](../RUN_RECORDS.md#23-run-log-entries)). Each line is checked on its own against its file; the way of checking shown below applies to one line at a time.

## What the files do not check

**Stage:** Stage 1.

- **Rules that need another file or the input**, for example that an answer item names an issue its question tags, that a pointer exists in the record, or that each issue gets one verdict. These stay software checks ([Handoffs, section 2.2](../HANDOFFS.md#22-format-check-content-checks-and-technical-failures)).
- **Rules across the entries of a log**, for example that `seq` runs without gaps, that entry ids are unique, that an entry named in `cause` exists, that each attempt has one `attempt_started` and one `attempt_ended` entry, and that totals equal the sums of the request log. These are software checks ([Run records, sections 2.3 and 2.10](../RUN_RECORDS.md#210-write-once-and-append-only-rules)), as are the separation and manifest checks of [Evaluation interfaces, sections 3.3, 3.6 and 6](../EVALUATION_INTERFACES.md#6-separation-rules).
- **Which of several conditions applied**, for example which code an attempt gets when more than one void condition holds: the first of `containment_hit`, `canary_hit`, `monitor_incomplete`, `route_refused` and `startup_check_failed` ([Run records, section 2.4](../RUN_RECORDS.md#24-attempt-entries); the order of the first four decided on 2026-10-28), while the other observations, request counts and usage stay recorded. A file sees one entry, so it cannot tell which conditions held. It does check the code against the entry's other fields, for example that a start-up self-check that failed before the turn leaves the attempt without an outcome, that an attempt with no forwarded request is not followed by a re-run, and that an unexplained monitor record in a real run makes the attempt void with code `containment_hit`, and incomplete monitoring evidence without one makes the attempt void with code `canary_hit` or `monitor_incomplete`, also where the start-up self-check failed before the turn. Whether a rate-law option or its bindings pass the checks of [Issue format 3.1](../../ISSUE_FORMAT.md#31-software-fields) needs the record, and whether a human action's `base` names the current working copy needs the run log; software checks both.
- **Which issues an override may close.** [Issue format 6.1](../../ISSUE_FORMAT.md#61-override) allows `wrong_type`, `broken_reference` and `bad_citation`, and any issue on a SOFTWARE field. Whether a field is a SOFTWARE field needs the role table of [Issue format 3](../../ISSUE_FORMAT.md#3-field-roles), so `issue.schema.json` lets an override close an issue of any kind, and software checks the rule.
- **Live pointers and human judgment.** That a `pointer_retarget` or `pointer_hold` entry agrees with the binding map and the record, that a bound id exists exactly once, that a hold's reason `split_or_merged` or `list_changed` matches the edit's `split_ids` and `merged_ids` or the lists it changed, and whether a source cited in the `basis` of a structural edit is clear enough to stand without a statement ([Issue format 6.2](../../ISSUE_FORMAT.md#62-structural-edit) and [7.1](../../ISSUE_FORMAT.md#71-flow)). The run-log file does check that every structural edit has a basis with a source, a statement or both, that a held issue keeps the status a mapping returns it to, and that assisted entry names the person who entered it together with the original.
- **Held-out assessment, approval summaries and monitor holds.** Whether a batch is a held-out assessment needs its item lists, so the run-log and batch-record files do not require `evaluation_plan` and `tuning_disclosure`; software checks rules 9 and 10 of [Evaluation interfaces, section 7.1](../EVALUATION_INTERFACES.md#71-admission-proposed), the second that a batch holds development items or test items, never both, and no file judges the criteria of a plan. Whether provisional monitoring deadlines admit a run's kind needs the run's configuration ([Containment, section 12.4](../CONTAINMENT.md#124-the-admission-check)). Whether an approval statement names the current stored approval summary needs the run log. Whether a release line names the latest hold of its environment, after a readiness check made after that hold, needs the whole index ([Containment, section 12.4](../CONTAINMENT.md#124-the-admission-check)).
- **Request counts.** That `first`, `retry` and `continuation` add up to the forwarded requests and that `unclassifiable` is at most the refused requests. The files check that an `unclassifiable` request is refused with its reason, never forwarded.
- **Citations.** The Locator rule (an absolute XPath 1.0 path that selects exactly one node, and a verbatim quote) needs the input. Evidence entries accept a missing or failing citation on purpose: it must reach the citation check and become a `bad_citation` issue, not fail a format check (Handoffs 2.2).
- **The EnzymeML document.** It is checked against the pinned EnzymeML V2.0 schema under the validation profile ([Issue format 9](../../ISSUE_FORMAT.md#9-validation-profile)). No copy of that schema is kept here.
- **Strict parsing.** Duplicate keys, `NaN`, `Infinity` and text around the object are refused by the parser (Handoffs 2.1), not by these files.
- **Formats.** Many validators treat `"format": "date-time"` as a note only. Where a format matters, the files also give a `pattern`, so the check holds either way.

## Points the documents leave open

**Stage:** Stage 1.

Under D30 A two points were carried to the next version of Issue format. Version 0.8 settles both ([ledger](../../README.md#2026-10-29---workflow-and-review-design-consolidated)), so neither is left open in these files; the points open now ([register, section 4.4](../PACKAGE_ADOPTION.md#44-open-decisions)) change no file's shape:

1. **`closed_by` of reopened issues.** An issue holds `closed_by` only while it is `closed`: `issue.schema.json` requires it for a closed issue and refuses it on an `open`, `unavailable` or `held` one, and in a run log's `issue_list` entry only a change `closed` carries it. The stored history of the issue list keeps earlier closures.
2. **`not_available` in an answer item.** Written as `not_available: true`; an item that declares nothing unavailable leaves the key out, and `false` is no answer of its own. `answer.schema.json` already read it this way.

## How to check a file

**Stage:** Stage 1.

Any validator that supports JSON Schema draft 2020-12 can be used. One way, with Python and the `jsonschema` library (version 4.18 or later), run from the repository root:

```sh
python3 -m venv .venv
.venv/bin/pip install "jsonschema>=4.18"
.venv/bin/python - design/specs/issue.schema.json my-issue.json <<'EOF'
import json, sys
from jsonschema import Draft202012Validator

with open(sys.argv[1], encoding="utf-8") as fh:
    schema = json.load(fh)
with open(sys.argv[2], encoding="utf-8") as fh:
    instance = json.load(fh)

Draft202012Validator.check_schema(schema)
validator = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path))
for error in errors:
    print("/" + "/".join(str(p) for p in error.absolute_path), error.message)
sys.exit(1 if errors else 0)
EOF
```

It prints one line per problem, with the place in the object, and exits with 0 when the object fits. Python's `json.load` accepts duplicate keys and `NaN`, so this does not replace the strict parsing of Handoffs 2.1.

The recipe reads each value exactly as stored and never trims it. The identifier and checksum patterns are whole-string under Python's `re` as under ECMA-262 (see Whole strings, above), so a value with a trailing line feed fails here too. A quick test, run from the repository root:

```sh
.venv/bin/python - <<'EOF'
import json
from jsonschema import Draft202012Validator

with open("design/specs/issue.schema.json", encoding="utf-8") as fh:
    schema = json.load(fh)
issue_id = Draft202012Validator(schema["$defs"]["issue_id"])
print([issue_id.is_valid(v) for v in ["ISS-021", "ISS-021\n", "ISS-021\r\n", "ISS-021 "]])
EOF
```

It prints `[True, False, False, False]`. Without the lookahead, the second value would pass.

To check an object against one of the parts, such as `$defs/as_supplied`, register the file under its `$id` and refer to the part:

```python
from referencing import Registry, Resource
registry = Registry().with_resource(schema["$id"], Resource.from_contents(schema))
validator = Draft202012Validator({"$ref": schema["$id"] + "#/$defs/as_supplied"}, registry=registry)
```
