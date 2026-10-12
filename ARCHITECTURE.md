# ARIADNE architecture

## Status

This document describes a proposed system, not implemented software, an approved ELEGANCE architecture, or a production deployment. See the proposed [Pilot](PILOT.md) and [Open questions](OPEN_QUESTIONS.md).

## Proposed flow

```text
researchers provide the scientific files they already use
  -> ARIADNE preserves the original files and records their origin
  -> the extraction agent drafts an EnzymeML record from the input
  -> the deterministic verifier checks the draft and raises issues
  -> the verification agent checks the draft against the input and the issues, and writes a report
  -> the inquiry agent turns the report into concise questions for the scientist
  -> the scientist answers the questions and approves the record
  -> ARIADNE generates and checks the approved EnzymeML record
  -> data owners approve any exchange
  -> approved records are shared with an authorized destination
```

## Components

- **Extraction agent:** extracts only. It copies what the input states into a draft EnzymeML record and cites the source location of every value. Where the input lacks information, the field stays empty, even if EnzymeML requires it.
- **Deterministic verifier:** software, not an agent. It checks structure, units, and internal references, and raises every empty required field as an issue. It reads the input only to confirm that each citation exists and contains the cited value.
- **Verification agent:** compares the draft with the input and the raised issues, confirms or rejects each issue, and adds any it finds. It reports only and never edits the record.
- **Inquiry agent:** reads the report and asks the scientist concise questions about gaps, conflicts, and proposed corrections. Each question is tagged with the issues it addresses, so that the answer can be applied to the right fields.
- **Scientist:** answers the questions and approves the final record. Answers fill the open fields and become their evidence.

All components share one issue format, so that an issue raised by the verifier can be followed through the report to the question that resolves it.

## Principles

- **Human-centered:** Researchers begin with familiar files and receive useful guidance without first mastering EnzymeML.
- **Evidence-linked:** Every value in a record links to its exact source: a location in the input, a quoted passage, or the scientist's answer.
- **Extract, do not guess:** Missing information stays empty and becomes a question. When a structured field and free text in the same input disagree, the structured value is kept and the conflict is raised.
- **Separated roles:** Each agent has one task and its own prompts and examples. Few-shot examples come only from reviewed records.
- **Controlled:** Agents cannot approve their own outputs or bypass deterministic checks, scientific review, or data-owner authority.
- **Standards-aware:** EnzymeML represents enzyme reaction and kinetics data. Linked companion schemas cover data outside its scope; the initial pilot itself is limited to EnzymeML.
