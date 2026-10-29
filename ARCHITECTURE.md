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
  -> the scientist answers the questions and makes, with a recorded basis, the structural edits that answers cannot make
  -> ARIADNE applies the answers and checks the record again, until no questions remain
  -> ARIADNE generates the final EnzymeML record, and the scientist approves it
  -> data owners approve any exchange
  -> approved records are shared with an authorized destination
```

## Components

- **Extraction agent:** extracts only. It copies what the input states into a draft EnzymeML record and cites the source location of every value. Where the input lacks information, the field stays empty, even if EnzymeML requires it.
- **Deterministic verifier:** software, not an agent. It checks structure, units, and internal references, and raises every empty field as an issue, classed by the field roles of the issue format. It reads the input only to confirm that each citation exists and contains the cited value.
- **Verification agent:** compares the draft with the input and the raised issues, confirms or rejects each issue, and adds any it finds. It reports only and never edits the record.
- **Inquiry agent:** reads the report and asks the scientist concise questions about gaps, conflicts, and proposed corrections. Each question is tagged with the issues it addresses, so that the answer can be applied to the right fields.
- **Scientist:** the scientist working on the record answers the questions and may make the structural edits that answers cannot make, without switching roles. Only one named scientist who is listed among the creators approves the final record ([Issue format 7.2](ISSUE_FORMAT.md#72-approval)). Answers fill the open fields and become their evidence. Each structural edit records its basis: a source location that clearly states the change, an explicit statement by the person, or both. The person may also close a mechanical issue that the verification agent rejected, giving a reason; such overrides stay limited to mechanical issues. Every action is recorded as evidence with the name of the person who took it. Another named person may assist by entering an answer or approval received from its author; the record keeps the original author and message and who entered it, and entry assistance never confers approval authority.

All components share one issue format, so that an issue raised by the verifier can be followed through the report to the question that resolves it. The preliminary Stage 1 format is defined in [Issue format](ISSUE_FORMAT.md).

## Principles

- **Human-centered:** Researchers begin with familiar files and receive useful guidance without first mastering EnzymeML.
- **Evidence-linked:** Every value in a record links to its exact source: a location in the input, a quoted passage, the scientist's answer, a person's recorded action, or the software rule that filled it.
- **Extract, do not guess:** Missing information stays empty and becomes a question. When a structured field and free text in the same input disagree, the structured value is kept and the conflict is raised.
- **Separated roles:** Each agent has one task and its own prompts and examples. Few-shot examples come only from reviewed records.
- **Controlled:** Agents cannot approve their own outputs or bypass deterministic checks, scientific review, or data-owner authority.
- **Standards-aware:** EnzymeML represents enzyme reaction and kinetics data. Linked companion schemas cover data outside its scope; the initial pilot itself is limited to EnzymeML.

## Supporting software (proposed)

**Stage:** Stage 1 and 2.

The software below supports the components and makes no scientific judgment; each entry says in one or two sentences what it would do and links to the design document that defines it, which is the source; this describes proposed software, not implemented software.

| Software | What it does (proposed) | Defined in | Stage |
|---|---|---|---|
| Workflow controller | Moves each record through its states, prepares the packets and checks each agent output against its format. It assigns issue and question ids, round numbers and times. | [Roles, section 3.1](design/ROLES.md#31-components); [Workflow](design/WORKFLOW.md) | Stage 1 |
| Launcher | Prepares each agent attempt's folder and container, and stops the container at its deadline. | [Runtime, section 10](design/RUNTIME.md#10-the-attempt-sequence) | Stage 1 |
| Runner | Runs inside the container: runs the agent once on its packet and writes the result. | [Runtime, section 10](design/RUNTIME.md#10-the-attempt-sequence) | Stage 1 |
| Model gateway | Holds the provider key, forwards the agents' requests only to the one recorded model route, and counts and logs every request. | [Runtime, section 11](design/RUNTIME.md#11-the-model-gateway) | Stage 1; broker Stage 2 |
| Packet preparation (part of the workflow controller) | Builds every packet from stored files (the input where the agent receives it, the reviewed reference text and examples, and earlier outputs), runs the packet check, and never shortens a packet. | [Roles, sections 7.2](design/ROLES.md#72-packet-layout) and [8.2](design/ROLES.md#82-operations); contents in [Handoffs, section 2.4](design/HANDOFFS.md#24-input-packets) | Stage 1 |
| Assembly step | Fills the software fields of a draft except the dates, including the ids inside the record. It never reads the input. | [Roles, section 3.1](design/ROLES.md#31-components); [Handoffs, section 2.6](design/HANDOFFS.md#26-assembled-draft) | Stage 1 |
| Answer application | Writes the scientist's answers and then, one at a time, the recorded human actions (structural edits and overrides) into a working copy of the round's record, which is committed as the next snapshot. | [Roles, section 3.1](design/ROLES.md#31-components); [Workflow, section 4.2](design/WORKFLOW.md#42-applying-answers) | Stage 1 |
| Final generation step | Sets the dates and writes the final files, before approval. | [Roles, section 3.1](design/ROLES.md#31-components); [Workflow, section 4.3](design/WORKFLOW.md#43-final-generation-and-approval) | Stage 1 |
| Run log | ARIADNE's record of runs, attempts, requests and checksums, written only by software. It is not the provenance ledger. | [Run records, section 2](design/RUN_RECORDS.md#2-record-keeping-stage-1) | Stage 1; record store Stage 2 |

**Terms.** Only ARIADNE's own terms; each links to the section that defines it.

| Term | Meaning | Stage |
|---|---|---|
| Agent attempt | One run of one agent on one packet; it ends with an output or a technical failure ([Runtime, section 1.2](design/RUNTIME.md#12-terms)) | Stage 1 |
| Packet | Everything an agent attempt receives besides its role prompt, sent to the model as one message and built by software from stored files ([Handoffs, section 2.4](design/HANDOFFS.md#24-input-packets)) | Stage 1 |
| Container | The isolated environment in which one agent attempt runs; one container per attempt ([Runtime, section 1.2](design/RUNTIME.md#12-terms)) | Stage 1 |
| Model route | The one recorded model, with its provider and protocol, that receives the agents' requests ([Runtime, section 12.1](design/RUNTIME.md#121-the-route-record)) | Stage 1 |
| Containment test suite | The automated tests that must pass for the runtime configuration in use before any model call ([Containment](design/CONTAINMENT.md)) | Stage 1 |
| Run log and provenance ledger | The run log is ARIADNE's record of its runs, written only by software. The provenance ledger is the project's list of entries in the [README](README.md#provenance-ledger). In these documents, "ledger" means only the provenance ledger ([Run records, section 1.2](design/RUN_RECORDS.md#12-terms)) | Stage 1 and 2 |
| Stage 1 and Stage 2 | Stage 1 establishes the workflow on 15 to 25 public STRENDA DB entries, with one approving scientist and no separate curator role; Stage 2 applies it with researchers ([stage legend](design/PACKAGE_ADOPTION.md#41-stage-legend)) | Stage 1 and 2 |

## Design documents

**Stage:** Stage 1 and 2.

The documents in the `design` folder describe in more detail how the proposed pipeline would run. Their Stage 1 sections are preliminary, decided on 2026-10-21 under interim authority ([ledger](README.md#2026-10-29---workflow-and-review-design-consolidated)); their Stage 2 sections are proposed ([ledger](README.md#2026-10-29---workflow-and-review-design-consolidated)). Where they differ from the provenance ledger, the decided sections of this document (Status, Proposed flow, Components, Principles) and of [Open questions](OPEN_QUESTIONS.md) (Q1-Q4), or [Issue format](ISSUE_FORMAT.md), those texts take precedence (order in [Package adoption register, section 3](design/PACKAGE_ADOPTION.md#3-precedence-and-pins)). The design documents, Issue format and the decided sections of this document were amended on 2026-10-22 (changes C01 to C11; [ledger](README.md#2026-10-29---workflow-and-review-design-consolidated)), and the design documents and Issue format on 2026-10-27 (decisions AD-D01 to AD-D06; [ledger](README.md#2026-10-29---workflow-and-review-design-consolidated)) and three times on 2026-10-28 ([ledger](README.md#2026-10-29---workflow-and-review-design-consolidated); [ledger](README.md#2026-10-29---workflow-and-review-design-consolidated); [ledger](README.md#2026-10-29---workflow-and-review-design-consolidated)). Stage labels are explained in the [stage legend](design/PACKAGE_ADOPTION.md#41-stage-legend). The supporting software is summarised in [Supporting software (proposed)](#supporting-software-proposed).

| Document | Covers | Stage |
|---|---|---|
| [Package adoption register](design/PACKAGE_ADOPTION.md) | Proposed handling of each part of an external, AI-generated design package: adopted, adapted, superseded by decided text, deferred to Stage 2 or left out | Stage 1 and 2 |
| [Roles](design/ROLES.md) | Proposed agents, supporting software and people: duties, procedures, prompts, tools and operations | Stage 1 and 2 |
| [Handoffs](design/HANDOFFS.md) | Proposed formats passed between the roles, with who writes each field | Stage 1 and 2 |
| [Workflow](design/WORKFLOW.md) | Proposed states of a record, transitions tied to the issue-format rounds, procedures and traces | Stage 1 and 2 |
| [Runtime](design/RUNTIME.md) | Proposed Stage 1 runtime: Hermes Agent at a pinned tag, re-checked facts, one fresh process in its own container per agent attempt, the model gateway, the model route and the limits | Stage 1 and 2 |
| [Containment](design/CONTAINMENT.md) | Proposed containment test suite that must pass before any model call, and the admission rule bound to the runtime configuration | Stage 1 and 2 |
| [Run records](design/RUN_RECORDS.md) | Proposed run log, request log and checksums in Stage 1, the record store in Stage 2, and budgets: measurement now, evaluation caps from measurements | Stage 1 and 2 |
| [Evaluation interfaces](design/EVALUATION_INTERFACES.md) | Proposed interfaces between the dataset builder, the workflow controller and the scorer: evaluation modes, input and packet manifests, expected outputs, planted defects, separation rules, the admission rule for evaluation runs and the evaluation run record | Stage 1 and 2 |
| [Derived schema files](design/specs/README.md) | Machine-readable JSON Schema files derived from the formats above; the documents win | Stage 1 |
