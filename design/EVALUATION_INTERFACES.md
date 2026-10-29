# Evaluation interfaces

**Version:** 1.5, not frozen. Only Tillman Heisner freezes a version; the freeze date will then be added here. Versions 1.0 to 1.4 were not frozen.\
**Status:** Preliminary for Stage 1, decided on 2026-10-21 under interim authority ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)), amended on 2026-10-22 (changes C01 to C11) ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)) and on 2026-10-27 (decisions AD-D02 and AD-D03) ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated); [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)) and on 2026-10-28 (continuation criteria, the held-out gate and the tuning disclosure) ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated); [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated); [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)), and again on 2026-10-28 (the refusal of mixed batches) ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)); Stage 2 sections proposed ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)). Written in phase P6 of the integration plan ([Package adoption register, section 4.5](PACKAGE_ADOPTION.md#45-phases-of-the-integration-plan)), 2026-10-21. Version 1.0 was written in phase P3 (2026-10-19); version 1.1 adds what version 1.0 left for it (section 7.2); version 1.2 applies the design changes of 2026-10-22, version 1.3 the decisions of 2026-10-27, version 1.4 those of 2026-10-28 and version 1.5 the later decisions of that day that concern this document (section 1.4). This describes proposed interfaces for a system that is not implemented; nothing described here has been built or run. A frozen interface version can be used by the dataset builder; freezing a version is separate from the status of this document (D9 A).\
**Precedence:** Where this document differs from the provenance ledger, the decided sections of [Architecture](../ARCHITECTURE.md) and [Open questions](../OPEN_QUESTIONS.md) (Q1-Q4), or [Issue format](../ISSUE_FORMAT.md), those texts take precedence (order in [Package adoption register, section 3](PACKAGE_ADOPTION.md#3-precedence-and-pins)). Issue format version 0.10 (version 0.5 decided on 2026-10-20, amended on 2026-10-22, 2026-10-27 and three times on 2026-10-28; [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)) ranks above the decisions of Tillman Heisner listed in [register, section 4.3](PACKAGE_ADOPTION.md#43-decided-by-tillman-heisner-on-2026-10-19-not-yet-in-the-ledger); this document links to its rules and never restates them. Expected issue lists name the issue-format version they follow (section 4.3).\
**Rests on:** [Open questions, Q1](../OPEN_QUESTIONS.md#q1---which-existing-datasets-should-be-used) and [Q4](../OPEN_QUESTIONS.md#q4---how-should-extraction-and-verification-be-evaluated); Issue format v0.10 (version 0.5 decided on 2026-10-20, [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated); amended on 2026-10-22, [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated), on 2026-10-27, [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated), on 2026-10-28, [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated), again that day, [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated), and once more that day, [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)), including its [notes for the evaluation datasets](../ISSUE_FORMAT.md#notes-for-the-evaluation-datasets-not-part-of-the-format); the documented Decision [Hermes Agent chosen as Stage 1 runtime](../README.md#2026-10-29---workflow-and-review-design-consolidated), which says that no run starts before the containment test suite passes; and decisions Tillman Heisner made, documented in the Stage 1 design ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated); [register, section 4.3](PACKAGE_ADOPTION.md#43-decided-by-tillman-heisner-on-2026-10-19-not-yet-in-the-ledger)): of 2026-10-19, D3, D4 A (ledger Results and Decisions, such as the Result entries for containment reports and the Decision that freezes the evaluation caps), D9 A and the token-cap decision; of 2026-10-20, D6 A, D8 A, D10 A, D11 A1, D12 A, D13 A, D14 A, D15 A, D16 A, D17 B and D18 A to D24 A; of 2026-10-21, D25 A, D26 A (the inquiry packet, which section 3.5 follows in its row Inquiry agent (mode A)), D27 B, D28 A to D32 A, D33 A (unwanted questions in mode B, section 2.2), D34 A (the parent-and-variant rule, section 3.5, rule 5) and D35 A (the readings of families DV1 and DV11, section 5.1); and the design changes C01 to C11 of 2026-10-22 ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)), of which C03, C04, C05, C07, C08, C10 and C11 change this document (section 1.4); and the decisions of 2026-10-27 AD-D02 ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)) and AD-D03 ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)), which change this document, and AD-D01 and AD-D06, which touch it at sections 4.5 and 5.1, and at sections 2 and 10.4 (section 1.4); and the decisions of 2026-10-28 on the [continuation criteria](../README.md#2026-10-29---workflow-and-review-design-consolidated), the [held-out gate](../README.md#2026-10-29---workflow-and-review-design-consolidated) and the [tuning disclosure](../README.md#2026-10-29---workflow-and-review-design-consolidated), which change sections 1.3, 4.7, 4.8 (new), 6, 7.1, 9 and 10 (section 1.4); and the later decisions of that day on [mixed batches](../README.md#2026-10-29---workflow-and-review-design-consolidated), which changes sections 7.1, 7.4 (new) and 10.7, and on [provisional monitoring deadlines](../README.md#2026-10-29---workflow-and-review-design-consolidated), which touches it through [Containment, section 12.4](CONTAINMENT.md#124-the-admission-check) (section 1.4). The points open in [register, section 4.4](PACKAGE_ADOPTION.md#44-open-decisions) do not change this document.\
**Stage:** Stage 1 and 2 ([stage legend](PACKAGE_ADOPTION.md#41-stage-legend)). Stage 1 is written in full; mode C (section 2.3) and section 12 are Stage 2, as compact tables. Every section and every table row carries its own label.\
**Attribution:** Sections 3.3 (the manifest check), 3.5, 3.6, 5, 6, 7, 10, 11 and 12, and the mapping in section 13, use ideas from an external design package. Adapted in part from design package ARIADNE-AGENT-ARCH-001 v1.2.1 (AI-generated for Tillman Heisner, 2026-10-12).

This describes a proposed system, not implemented software. Nothing described here has been built or run.

## 1. Purpose, ownership and change log

**Stage:** Stage 1 and 2.

### 1.1 Purpose

**Stage:** Stage 1.

Q4 evaluates each agent on its own dataset, built from the Q1 entries. This document proposes the interfaces between three pieces of software and the files that pass between them:

- the **dataset builder**, which Tillman Heisner owns and builds. It turns the stored STRENDA DB entries into evaluation items and expected outputs;
- the **workflow controller**, which in an evaluation run builds each item's packets, starts each agent attempt in its own container, keeps the outputs and writes the evaluation run records (sections 3.5 and 10). It is the program that also runs the pipeline ([Workflow, section 1.4](WORKFLOW.md#14-how-evaluation-runs-use-the-workflow); [Runtime, section 10](RUNTIME.md#10-the-attempt-sequence)). Version 1.0 called it "the runner". In [Runtime, section 1.2](RUNTIME.md#12-terms) the runner is only the program inside one attempt's container, and this document now uses the word in that sense only;
- the **scorer**, which compares outputs with the expected outputs.

How the builder works inside is not specified (section 6, rule 10).

**What the benchmark measures** (AD-D02). The STRENDA DB Export XML entries of Q1 are a controlled benchmark for developing a workflow that is intended later to take the varied scientific files researchers use. On this one input format, and through the round-1 questions, it measures the workflow's parts alone (mode A) and in sequence (mode B), zero-shot and few-shot: extraction with a citation for every value and empty fields left empty, the deterministic verifier's checks, which hold no knowledge of the input format ([Issue format 8](../ISSUE_FORMAT.md#8-what-the-deterministic-verifier-checks)), the verification agent's judgments and own issues, the inquiry agent's questions, and the evidence, issue and question handoffs between them. It does not show that the workflow handles other file types, and Stage 1 adds none. No deterministic extraction comparator is part of it. Development entries are used for tuning; test entries are held out for assessment, and an entry used repeatedly for tuning no longer counts as an untouched test (section 6, rule 9).

### 1.2 Terms

**Stage:** Stage 1.

- **Entry:** one STRENDA DB Export XML file from the Q1 selection, stored unchanged.
- **Variant:** a copy of an entry, or of a record, in which values were removed, changed or planted on purpose (sections 3.2 and 5).
- **Reviewed draft:** the draft that a correct extraction and assembly would produce for an input, empty where the input is silent, reviewed by Tillman Heisner. Record variants and clean controls start from it.
- **Item:** one evaluation case for one step: an input (an entry or a variant) plus, for the later steps, the frozen files the step starts from, for example a draft and its round-1 issues.
- **Condition:** zero-shot (no examples) or few-shot (examples from an example manifest, section 3.3).
- **Fold:** the group of items that share one set of few-shot examples under leave-one-out: items from T9HQ4X, items from GNICYO, or test items (section 3.3).
- **Natural finding:** a problem that a stored entry itself contains, such as the pH conflict in T9HQ4X, as opposed to a planted one (section 5.2).
- **Packet:** what one agent attempt receives besides its role prompt. Software builds it with the same packet preparation as the pipeline ([Roles, section 8.2](ROLES.md#82-operations), row 4). Its contents are set in [Handoffs, section 2.4](HANDOFFS.md#24-input-packets), its blocks in [Roles, section 7.2](ROLES.md#72-packet-layout), and how an item's files enter it in section 3.5.
- **Packet manifest:** the run-log record of one packet ([Handoffs, section 2.4](HANDOFFS.md#24-input-packets)). Agents never see it. Section 3.6 lists what evaluation adds to it.
- **Input side:** entries, variants, items, manifests, example files and packets. An agent sees what its packet holds and nothing else.
- **Expected side:** the files that say what a correct output is, together with change lists, planted-defect lists and the unit table. Only the builder writes them, and only the scorer reads them.
- **Source anchor:** the place in the input that an EnzymeML object comes from, given as an xpath, plus a label for objects that only free text states (section 4.2).
- **Run:** one item in one condition and one repetition: in mode A one step, in mode B the sequence through round 1. Software gives it a run id. It is not the pipeline run of [Workflow, section 1.2](WORKFLOW.md#12-terms): a mode B run covers only the round-1 part of one.
- **Batch:** the runs that one admission starts together (section 7.1), under one runtime manifest and one budget profile (section 10.1): an evaluation batch or a measurement batch, never both. "Evaluation run" in sections 7.1 and 9 means a batch, and a "test-set run" is a batch of test items.
- **Measurement run:** a run of a measurement batch (section 10.1): one item in one condition and one repetition, in mode A or B, on a development entry, a variant of one or a measurement-only size variant (section 3.2), under the development profile. It scores nothing and reads no expected-side file. Its evaluation run record is marked as a measurement run, and the scorer refuses it (section 11, rule 3). The measured maxima from which the evaluation caps are set come only from the measurement runs that [Run records, section 4.8](RUN_RECORDS.md#48-measurement-plan) defines (section 10.6).
- **Agent attempt:** one execution of one agent on one packet, in its own container ([Runtime, section 1.2](RUNTIME.md#12-terms)).
- **Evaluation run record:** the stored record of one run of a batch, named in the run log (section 10.1). **Batch log:** the run log of one batch ([Run records, section 2.2](RUN_RECORDS.md#22-where-it-is-kept)). **Batch record:** the stored summary of one batch, written once when the batch ends or is refused, and named by its batch log (section 10.1).
- **Budget profile:** the named, versioned set of limits a run works under: the development profile or the frozen evaluation profile ([Run records, section 4.1](RUN_RECORDS.md#41-budget-profiles); section 10.6).
- **First-try result and final result:** a run read without and with its technical re-runs (section 10.5).
- **Diagnostic views:** the three separate groupings of a score report, integrity, usefulness and operational completion (section 4.7). Each is given for the first-try result and for the final result; they are not the two results of section 10.5. Proposed names.
- **Held-out assessment:** an evaluation batch of test items, as opposed to a development batch (section 7.1, rule 9).
- **Evaluation plan** and **tuning disclosure:** the versioned file that holds the continuation criteria, and the record of whether test information informed the workflow being assessed (section 4.8).
- **Residual unflagged error:** in mode B, an extraction error that no issue on its field catches and no question asks about by the end of round 1 (section 2.2). Proposed name.
- **Containment run:** a run of the containment test suite, whose attempts call only a scripted stub model ([Containment, section 2.7](CONTAINMENT.md#27-containment-runs-and-real-runs)). Section 11 keeps containment runs apart from evaluation.
- **Run log:** ARIADNE's Stage 1 record of runs and attempts: the log files of each run folder and batch folder, the report index of containment reports, and the stored files that software writes only to record a run or a batch and that those entries name, such as `binding.json`, containment reports, evaluation run records and batch records ([Run records, sections 1.2](RUN_RECORDS.md#12-terms) and [2](RUN_RECORDS.md#2-record-keeping-stage-1)). Record files, handoffs and packets are named by the run log, with their checksums, but are not part of it. In ARIADNE, "ledger" means only the provenance ledger.
- **Q4.1 to Q4.5:** items 1 to 5 of [Open questions, Q4](../OPEN_QUESTIONS.md#q4---how-should-extraction-and-verification-be-evaluated).

### 1.3 Who decides what

**Stage:** Stage 1 and 2.

Under D9 A:

| Part | ARIADNE | Tillman Heisner | Stage |
|---|---|---|---|
| Evaluation modes (section 2) | Specifies | Freezes the version | Stage 1 |
| Input-set manifest, variants (input side), example manifest, item list (section 3) | Specifies | Freezes the version | Stage 1 |
| Packets for evaluation, their manifest, the evaluation run record and the batch record (sections 3.5, 3.6 and 10) | Specifies | Freezes the version | Stage 1 |
| Separation rules, admission rule and keeping containment runs apart (sections 6, 7 and 11) | Specifies | Freezes the version | Stage 1 |
| Expected-side formats, including the unit table (section 4) | Proposes | Accepts, changes or replaces each one | Stage 1 |
| Planted-defect families, expectations for natural cases, and canary strings (section 5) | Proposes lists to choose from | Chooses, changes or replaces | Stage 1 |
| The dataset builder, the expected outputs, the example files and the hand marks | Not specified | Owns and builds | Stage 1 |
| The evaluation plan with the continuation criteria (section 4.8) | Specifies its form and the admission check | Sets, approves and freezes each version, under his interim Stage 1 authority | Stage 1 |
| The tuning disclosure before each held-out assessment (section 4.8) | Specifies its form | Records it | Stage 1 |
| Mode C and the Stage 2 tables (sections 2.3 and 12) | Proposes | May propose them for Stage 2; whether Stage 2 takes them up is for the pilot's decision authority once it is confirmed (the interim authority covers only the Stage 1 design); moving one into Stage 1 needs a ledger Decision | Stage 2 |

A change after a freeze makes a new version, listed in the change log.

### 1.4 Change log

**Stage:** Stage 1 and 2.

| Version | Date | Change | Stage |
|---|---|---|---|
| 1.0 (Draft) | 2026-10-19 | First version (phase P3): modes, input side, proposed expected side, planted-defect families, natural cases and canary strings, separation rules, admission rule, traceability. Not frozen. | Stage 1 and 2 |
| 1.1 (Draft) | 2026-10-21 | Phase P6: packets for evaluation and their manifest (sections 3.5 and 3.6); the evaluation run record, the batch log and batch record, how runs and batches end, first-try and final results, usage and budget profiles, score reports, and the derived schema files written in this phase (section 10.8); measurement runs and the measurement-only size variants (sections 1.2, 3.2 and 10.1); list-level fields and lowercase checksums of the input-side lists (section 3); containment runs kept apart (section 11; section 6, rule 11; section 7.1, rules 7 and 8); every batch admitted under a current VERIFIED report, a batch of deterministic-verifier items only included (section 7.1, rule 1); changes proposed for other documents (section 1.5); Stage 2 tables (section 12) and a register mapping note (section 13). "The runner" renamed the workflow controller; links to [Containment](CONTAINMENT.md) in place of "planned"; the decided D10 A, D11 A1 and D12 A in place of "pending"; decisions now written without an equals sign, for example "D12 A", as in Runtime and Containment; the inquiry checks aligned with [Handoffs, section 2.9](HANDOFFS.md#29-question-round); a Stage label on every section and table row; section 7.2 is now a pointer. Not yet frozen. Phase P7, same version: pointers to Containment, Runtime, Roles, Handoffs and Workflow updated after their alignment; the corrections of section 10.8 made in design/specs. After the phase P7 review, same version: the prompt check covers the ids and DOIs of every entry of the input-set manifest (section 3.3); the prompt, reference-text and packet checksums are fields of the Handoffs packet manifest (section 3.6); how unwanted questions are found in modes A and B, with an alternative reading (sections 2.2, 3.5, 4.5 and 9); what the workflow controller's configuration names in containment and behaviour-variant runs (section 6, rule 2); attempts with no forwarded request (sections 10.4 and 10.5); the request guard and request cap in `failure_class` (section 10.3); and the Stage 2 row of section 1.3. After the second phase P7 review, same version: the open decision D26 named (Rests on; section 3.5); whitespace-only text read as only `missing_*`, for Tillman Heisner to confirm (section 5.1, DV11); the manifest and prompt checks read the canary list (sections 1.5, 5.3 and 6); the report index also named for appending hit lines after a containment hit (section 1.5; section 6, rule 2); example files keep the ids their entries state (section 6, rule 6); two different verdicts count as not judged (section 4.6); a cap hit without a re-run ends the run (section 10.4); a containment run told apart by its label, confirmed by the gateway (section 11, rule 1); and the packet-manifest schema row (section 10.8). After decisions D26 A to D32 A of 2026-10-21, same version: D26 A stated as decided (Rests on; section 3.5); section 10.4, row of void attempts, cites D28 A and, after a containment hit, D27 B. After decisions D33 A and D34 A of 2026-10-21, same version: unwanted questions are counted in mode B against the step that let their issue through, and the alternative reading is gone (sections 2.2, 3.5, 4.5 and 9, item 5); the parent-and-variant rule covers only an item's own input and frozen files (sections 3.5, rule 5, and 6, rule 6). After the final phase P7 review, same version: the content checks of the inquiry agent are named as in Handoffs 2.9 (section 4.5); mixed questions follow D33 A (sections 2.2 and 4.5); the attempt fields of section 10.3 follow Run records 2.4 (new field `input_above_cap`; the `outcome` row names the exception for an unexplained monitor record). After decision D35 A and the Stage 1 Decision of 2026-10-21, same version: the readings of families DV1 and DV11 are confirmed (sections 5.1 and 9), and the status line says preliminary for Stage 1. | Stage 1 and 2 |
| 1.2 (Draft) | 2026-10-22 | The design changes decided on 2026-10-22 ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)) that concern this document. C03: every example manifest names the actual fold, `dev-T9HQ4X`, `dev-GNICYO` or `test`, in both conditions, equal to the fold of the items that use it; the fold `all` is removed; a zero-shot manifest lists no example, and there is one per agent and fold (section 3.3; section 10.3, `example_manifest_id`). C04: identical frozen data blocks across conditions and repetitions hold in mode A only; in mode B the original input and the fixed configuration are identical, and the downstream blocks hold each run's own outputs (sections 2.1, 2.2 and 3.5, rule 4; section 8, row Q4.4). C05: expected judgments, expected issues, expected issue lists and inquiry expectations carry a required `mode`; mode A rows are keyed by frozen issue id, kind and pointers, mode B rows by (source anchor, field, kind), mapped by the scorer through the draft's evidence entries, with unmappable or ambiguous results on the review list (sections 2.2, 4.1 rule 12, 4.3, 4.4, 4.5 and 10.8). C07: a provider-reported count that is incomplete is kept as a provisional count and flagged, never used for cap calibration (sections 10.3, 10.6 and 10.7). C08: a technical failure always has a `failure_class`, except the coded `runaway_guard` and `cap_hit` cases (section 10.3). C10: no separate curator role; issues formerly routed to the curator go to human review, and override and review reporting names human actions (sections 2.3, 4.3, 4.5 and 5.1, DV6; section 12). C11: the shared model-facing material is free of worked demonstrations, only EXAMPLES differs between the conditions, the future check covers the whole assembled model input, and the extra tokens of the examples are reported (sections 3.5, 6 rule 8 and 10.7). The Issue format version that this document follows is 0.6. Not yet frozen. | Stage 1 and 2 |
| 1.3 (Draft) | 2026-10-27 | The decisions of 2026-10-27 that concern this document. AD-D02 ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)): what the STRENDA benchmark measures and does not show, with no deterministic extraction comparator (section 1.1); evaluation stops with the round-1 questions, and software tests with stored fixtures are not evaluation or mode C (sections 2, 2.3 and 12); development results are tuning results, and the test-set run of a version changed after test-set scores were seen is reported as not held out (sections 4.6, 6 rule 9 and 10.7). AD-D03 ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)): three separate diagnostic views, integrity, usefulness and operational completion, with no overall score, and continuation criteria set before test-set results are read, with no threshold selected (sections 1.2, 4.7, 8, 9 item 13 and 10.7); residual unflagged errors in mode B (sections 2.2 and 10.5); recovery of stated facts apart from correctly empty fields (section 4.2); grouping by entry and publication group (sections 4.1 rule 11 and 4.6); failures and cap hits reported under operational completion (sections 4.6, 10.4 and 10.6). AD-D01: the inquiry expectations of family I5 and a content check follow the bound rate-law options (sections 4.5 and 5.1). AD-D06: the lifecycle slice tests are software tests (section 2), and incomplete monitoring evidence, code `monitor_incomplete`, voids an attempt and stops the batch without D27 B (section 10.4). Of the derived schema files, only `evaluation-run-record.schema.json` and `evaluation-batch-record.schema.json` change, for the new code, and are derived again; the others keep their labels (section 10.8). The Issue format version that this document follows is 0.7. Not yet frozen. | Stage 1 and 2 |
| 1.4 (Draft) | 2026-10-28 | The decisions of 2026-10-28 that concern this document ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated); [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated); [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)): Tillman Heisner sets and approves the continuation criteria in a versioned evaluation plan, and meeting them means technical readiness for proposing a bounded researcher trial, not authorization of a wider pilot step (sections 1.3 and 4.7, rule 4); the evaluation plan and the tuning disclosure (section 4.8, new); a held-out assessment batch must name an approved, frozen plan version with criteria and carry its disclosure before it starts, and keeps that reference (section 7.1, rule 9; section 10.1), with the cases EP-01 to EP-06 (section 7.3, new); test-informed follow-ups are reported as not held out, whatever their version (sections 6, rule 9, and 10.7). `evaluation-batch-record.schema.json` is derived again, and `evaluation-plan.schema.json` is added (section 10.8). The Issue format version that this document follows is 0.8. Not yet frozen. | Stage 1 and 2 |
| 1.5 (Draft) | 2026-10-28 | The later decisions of 2026-10-28 that concern this document ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated); [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)): a batch holds development items or test items, never both, and a mixed batch is refused before any model call, a measurement batch counting as a development batch (section 7.1, rule 10), with the cases EP-07 to EP-09 (section 7.4, new); development results are never pooled into a held-out score (section 10.7); and provisional monitoring deadlines admit development and measurement batches but no test batch ([Containment, section 12.4](CONTAINMENT.md#124-the-admission-check)). `evaluation-batch-record.schema.json` is derived again for rule 10 (section 10.8). The Issue format version that this document follows is 0.9. Not yet frozen. | Stage 1 and 2 |

### 1.5 Changes proposed for other documents

**Stage:** Stage 1 and 2.

Items (a) and the first part of (g) were carried out in phase P6; all others in phase P7. The list is kept as a record. In each item, section numbers outside parentheses are those of the other document, and those in parentheses are this document's.

- (a) [Run records](RUN_RECORDS.md#14-changes-proposed-for-other-documents) (P6): nothing is left open. The alignments that this version asked for there are in the Run records draft of 2026-10-21, and [Run records, section 1.4](RUN_RECORDS.md#14-changes-proposed-for-other-documents), item (f), lists the alignments taken over here.
- (b) [Containment](CONTAINMENT.md#9-evaluation-separation-test-es-01-to-es-03) (P7): items (i) and (j) of [section 1.4](CONTAINMENT.md#14-decisions-in-force-and-open-decisions) are done for this document (sections 1.1, 5.1 row E7, 5.3, 6, 7.1 and 7.2); ES-02 names the workflow controller instead of "the runner", and adds to what the workflow controller's configuration may name the canary list, for the packet check and the manifest and prompt checks, and, for the admission check and for appending hit lines after a containment hit, the report index and the suite runs' folders (section 6, rule 2; [Run records, section 2.7](RUN_RECORDS.md#27-containment-reports)); sections 2.2 (Fixture store) and 12.2 (Fixtures) keep the test copy of the expected folder in the fixture store and bind it as a fixture (section 11, rule 4); section 12.4 extends the fixture-store reading of admission item 3 to the behaviour variants of section 7.5 (section 11, rule 7).
- (c) [Runtime](RUNTIME.md#85-corrections-to-the-package-for-phase-p7) (P7): items (i) and (j) of section 8.5 are done for this document (sections 1.1, 5.1 row E7, 5.3, 6, 7.1 and 7.2); section 12.2, item 3, gets the same fixture-store exception for behaviour variants as item (b).
- (d) [Roles](ROLES.md#82-operations) (P7): section 8.2, row 4, links section 3.5 instead of section 7.2; row 14 applies rules 1, 7 and 8 of section 7.1 before every attempt of an evaluation run.
- (e) [Handoffs](HANDOFFS.md#24-input-packets) (P7): section 1.1 links sections 3.5 and 3.6 instead of section 7.2; the notes "to be aligned in version 1.1" (section 2.2), "to be reflected in version 1.1" (section 2.4, Askable issues) and "to be carried into Evaluation interfaces version 1.1" (section 2.13) are done (sections 3.5, 4.5 and 10.5); section 2.4 (Packet manifest) names the prompt and reference-text checksums of [Roles, section 7.1](ROLES.md#71-rules-for-all-prompts), rule 7, and links section 3.6 for the evaluation additions.
- (f) [Workflow](WORKFLOW.md#14-how-evaluation-runs-use-the-workflow) (P7): sections 1.4 and 4.4.2 link section 10.5 instead of "Evaluation interfaces 7.2, to follow in version 1.1"; section 1.4 links section 10.4 for void attempts, batch stops and items not run, and names measurement runs (section 1.2); section 1.2 (Run) notes that an evaluation run is not a pipeline run (section 1.2 here).
- (g) [design/specs](specs/README.md): the files of section 10.8, with the README rows that list them, are written in phase P6 with this version; the corrections to `inquiry-expectations.schema.json` of section 10.8 are for phase P7, and the lowercase checksums of the expected-side files follow when those files are derived again (section 10.8).
- (h) [Register](PACKAGE_ADOPTION.md#6-coverage-register) (P7): the rows of section 13 are marked as covered by this version, and the resolution of conflict C-30 names sections 2, 3.5, 3.6, 4, 10 and 11 under D9 A.

## 2. Evaluation modes

**Stage:** Stage 1 (modes A and B); Stage 2 (mode C).

Every model call in any mode, evaluation included, requires a current VERIFIED containment report ([Containment, section 12.4](CONTAINMENT.md#124-the-admission-check); section 7.1).

Evaluation in Stage 1 stops after round 1, with the round-1 questions. Later rounds involve people, and in them only the deterministic verifier re-runs ([Issue format 7.1](../ISSUE_FORMAT.md#71-flow)).

Software tests that drive later rounds with stored fixtures, such as the lifecycle slice of [Workflow, section 5.5](WORKFLOW.md#55-lifecycle-slice-tests-specified-not-implemented), are not evaluation and not mode C (AD-D02). They score no agent, and their fixture answers and approvals are not scientific approvals, a usability study or evidence of time saved.

### 2.1 Mode A - each agent alone on a frozen packet

**Stage:** Stage 1.

| Step under test | Starts from (frozen) | Produces | Scored against (section 4) | Stage |
|---|---|---|---|---|
| Extraction agent | An entry or an entry variant | Draft, evidence entries and not-mapped entries ([Issue format 7.1](../ISSUE_FORMAT.md#71-flow) step 1) | Expected-value table; expected not-mapped list | Stage 1 |
| Deterministic verifier (software) | An assembled draft with its evidence entries; the input, read only to check citations | Round-1 issues | Expected issue list (exact match) | Stage 1 |
| Verification agent | The input; an assembled draft with its evidence entries; round-1 issues, either from the deterministic verifier run on that draft or planted by the builder | Judgments and its own issues | Expected judgments and issues | Stage 1 |
| Inquiry agent | The report (the round-1 issues, including the verification agent's own, and the judgments) and the evidence the issues refer to; software filters the report before the agent sees it (sections 3.5 and 4.5) | Questions | Inquiry expectations; wording-rating sheet | Stage 1 |

- Each agent runs in both conditions on the same items (Q4.4). The deterministic verifier is software: it has no condition and makes no model call, but it is tested on items in the same way.
- An item's frozen files are the same for every condition and every repetition, so in mode A the packets of an item hold identical frozen data blocks in both conditions and every repetition; only EXAMPLES differs between the conditions. How they enter the packet is set in section 3.5 (rule 4).
- Nothing in an item marks a file as planted, changed or clean. The interface requires only that planted round-1 issues cannot be told apart from the deterministic verifier's own: the same fields (including `raised_by: deterministic_verifier` and a fitting `rule_id`), the same id sequence and the same summary style. How the builder achieves this is its own choice.

### 2.2 Mode B - in sequence through round 1

**Stage:** Stage 1.

One input runs through the extraction agent, the assembly step, the deterministic verifier, the verification agent and the inquiry agent, as in Issue format 7.1 steps 1 to 5. Each agent runs in its own attempt, with its own prompt and examples, and software passes outputs on as in the pipeline (packets: section 3.5). The run stops after the inquiry agent's round-1 questions: no answers and no later rounds.

**Proposed:**
- **Condition:** one condition for all three agents in a run (all zero-shot or all few-shot). Mixed combinations can be added later.
- **Examples:** each agent uses its own example manifest for the item's fold (section 3.3).
- **What stays the same, and what may differ:** the zero-shot and few-shot runs of an item, and its repetitions, share the original input and the fixed configuration: the role prompts, reference texts, output formats and the other settings of the batch, in the same versions. Only EXAMPLES differs between the conditions. Every packet after the extraction packet holds that run's own outputs (DRAFT, ISSUES and the other downstream blocks), so these blocks differ legitimately between conditions and repetitions; for example, if the zero-shot extraction misses a temperature that the few-shot extraction finds, the two verification packets hold those two different drafts. Software never replaces a run's outputs to make packets equal (section 3.5, rule 4).
- **Keys:** pointers and issue IDs differ from run to run, so mode B expectations are keyed by (source anchor, field, kind) and say so by `mode: B` (section 4.1, rule 12). The scorer maps the draft's objects to anchors through the draft's own evidence entries (section 4.2), and so maps each generated issue and question topic to (anchor, field, kind). The same source pH conflict may be `ISS-001` at `/measurements/0/ph` in one run and `ISS-007` at `/measurements/1/ph` in another; both map to the same expected row.
- **What is scored:**
  - the extraction agent, as in mode A, including unit errors against the expected-value table;
  - the deterministic verifier's issues are recorded but not scored, because mode A tests it;
  - **caught downstream**, for each extraction error. An error counts as caught only as follows, because every empty field draws a `missing_*` issue anyway:
    - *missed value* in a field: the verification agent judges the `missing_*` issue on that field `rejected` and raises a `missed_value`; for an omitted object, it raises a `missed_value` at the parent pointer. A `missing_*` issue judged `confirmed` still reaches the scientist, but without the source value; it is reported as "asked, not caught";
    - *wrong value*: a `wrong_value`, `wrong_unit` or `bad_citation` issue on that field, judged `confirmed` or `uncertain` where it has a verdict;
    - *invented value*: a `bad_citation` or `wrong_value` issue on that field, judged `confirmed` or `uncertain` where it has a verdict;
    - catches that rest only on a deterministic verifier issue are reported separately from catches by the verification agent's own issues;
    - **residual unflagged errors** (AD-D03): every extraction error that is neither caught nor "asked, not caught" by the end of round 1 is counted, per error class, beside the two kinds of catch and the "asked, not caught" count; missed values in LIST fields, which are listed but never asked, are shown apart. An error whose downstream step failed or was not reached in a result (section 10.5) is counted under operational completion, not as unflagged. These errors never drop out of the report (section 4.7);
  - whether every expected source conflict was raised (matching as in section 4.1 rule 8);
  - the questions (section 4.5):
    - **must-ask topics**, keyed by (anchor, field, kind), are fixed only for what every correct pipeline must ask: ASK-REQ and ASK fields the input does not state, and the expected source conflicts;
    - other questions are scored conditionally: wanted if their issue was validly raised (it matches an expected issue, or the expected row of its field is empty); otherwise they are reported, not scored;
    - unwanted questions are found through the routing table ([Issue format 4.2](../ISSUE_FORMAT.md#42-judgment-verification-agents-report) rule 6) applied with the expected verdict where an issue matches an expected judgment (section 4.4), and with the run's own verdict otherwise, and the question count is reported. Decided by Tillman Heisner on 2026-10-21 (D33 A): unwanted questions are counted in mode B. Each one is listed against the step whose output let its issue reach the inquiry agent: normally the verification agent's verdict (for example, a checker defect that it confirmed instead of rejecting) and, where the issue should not have been raised at all, the step that raised it. It is never listed against the inquiry agent, which asks only about the issues its packet holds. A mixed question (section 4.5) is listed in the same way, against the step that let its unwanted issue through. The filter check of section 3.5 is reported as well, separately.
- An object, issue or question tag that the scorer cannot map to an anchor, or that maps to several, is listed for review, not scored silently as right or wrong (section 4.1, rule 12).

### 2.3 Mode C - the full loop with stored answers (Stage 2, later)

**Stage:** Stage 2.

Later rounds would run with answers stored in advance and replayed through answer application and re-checks. Nothing is specified for Stage 1: D9 A leaves scripted later rounds out. Software tests of later rounds with stored fixtures are not mode C (section 2). If mode C is taken up, each stored answer should record where it comes from, for example confirmed by the data owner or settled by the named person working on the record ([Issue format 6](../ISSUE_FORMAT.md#6-human-actions)). Its row in the Stage 2 tables is in section 12.

The answer-item count and the override rate per record ([Issue format, notes 6](../ISSUE_FORMAT.md#notes-for-the-evaluation-datasets-not-part-of-the-format); [register conflict C-09](PACKAGE_ADOPTION.md#7-conflict-register)) need answers and human actions on review items ([Issue format 6](../ISSUE_FORMAT.md#6-human-actions)), and are reported as human actions, never as the work of a separate role. They belong to mode C and are not measured in Stage 1. The question count is measured in modes A and B.

## 3. Input side

**Stage:** Stage 1.

Everything in this section may be read by the workflow controller, so none of it carries expected-side information: no field, id or file name says what was changed, planted, conflicting or clean. What reaches a packet is narrower still (section 6, rule 6; section 3.5).

The input-set manifest's checksums are the ones Q1 item 1 asks for. The variant list, the item list, the example manifests and the expected files carry checksums too, so that software can check the dataset's files (sections 3.3, 3.5 and 4.1). Software computes all of them. It writes each of them as [Run records, section 1.2](RUN_RECORDS.md#12-terms) defines a checksum: the SHA-256 of the file's exact bytes, as 64 lowercase hexadecimal characters, so that a list's checksum and one that software computes again compare as equal text (section 3.6). None of these lists is a record file: record files carry no checksum, and software keeps every checksum about a run (prompts, packets, outputs, the runtime) in the run log only. The run log includes the stored files that software writes only to record a run or a batch and that its entries name, such as `binding.json`, evaluation run records and batch records; none of these is a record file, handoff or packet ([Issue format 11](../ISSUE_FORMAT.md#11-deliberately-left-out); D13 A; [Run records, sections 1.2](RUN_RECORDS.md#12-terms) and [2.9](RUN_RECORDS.md#29-checksums-d13-a); sections 3.6 and 10).

**List-level fields** (proposed key names). Besides its rows, each list of sections 3.1 to 3.4 records `evaluation_interfaces_version`, the version of this document it follows, and `frozen_on`, the date Tillman Heisner froze it, absent while it is a draft, so that a run record can mark each version frozen or draft (section 6, rule 8; section 10.2, `versions`). The input-set manifest and each example manifest record their own version as `manifest_version`, the variant list and each item list as `list_version`. Each item list also has an opaque id, `item_list_id`, which batch logs, batch records and run records quote with its version (section 10.1; [Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries)).

The derived schema files of sections 3.1 to 3.4 and 3.6 are listed in section 10.8.

### 3.1 Input-set manifest

**Stage:** Stage 1.

One row per stored entry (Q1).

| Field | Content | T9HQ4X (illustrative) | Stage |
|---|---|---|---|
| `entry_id` | STRENDA DB identifier | `T9HQ4X` | Stage 1 |
| `split` | `development` or `test` | `development` | Stage 1 |
| `publication_group` | A label shared by all entries from one publication | `<group label>` | Stage 1 |
| `publication_ref` | The publication's DOI, or `none found` | Filled when the entry is downloaded | Stage 1 |
| `publication_ref_source` | Where the publication reference was read, and on which date. The Export XML does not name the publication, so the reference comes from outside the file. | Filled when the entry is downloaded | Stage 1 |
| `file_name` | Name of the stored Export XML file | `T9HQ4X.xml` | Stage 1 |
| `sha256` | SHA-256 of the stored file, computed by software | 64 lowercase hexadecimal characters | Stage 1 |
| `download_date` | Date the file was downloaded | `YYYY-MM-DD` | Stage 1 |
| `doi_or_url` | The entry's DOI, or its URL if it has none | `https://doi.org/10.22011/strenda_db.T9HQ4X` | Stage 1 |
| `terms_of_use` | STRENDA DB terms of use as read on the download date: where they were read, and what they say about reuse, in one or two sentences | Filled when the entry is downloaded | Stage 1 |

The manifest as a whole also records its own version, the version of this document it follows, and the date Tillman Heisner froze it (`manifest_version`, `evaluation_interfaces_version` and `frozen_on`; section 3, List-level fields).

Only the entries of this manifest and their variants (section 3.2) are admitted as evaluation input ([Handoffs, section 2.3](HANDOFFS.md#23-input-file-record)). Researcher data, and the data owner's admission it needs, are Stage 2 ([Open questions, Q6](../OPEN_QUESTIONS.md#q6---which-researcher-workflows-and-data-may-be-used); section 12).

**Manifest check (software, before every run; proposed):**
1. Each stored file's SHA-256 matches its row, so the file is unchanged since download (Q1 item 1).
2. All entries of one publication group have the same split (Q1 item 3), and every row has a `publication_ref` and its source, so that the grouping can be audited.
3. T9HQ4X and GNICYO are `development`; every other entry is `test` (Q1 item 3).
4. Before a test-set run, the manifest lists 15 to 25 entries (Q1 item 2).

A coverage note per entry (enzyme, kinetic parameters, units, compound roles, number of datasets, methodology text present or not) may be added to show the spread Q1 item 2 asks for. It describes only what the file visibly contains, never an expected outcome such as "has a conflict".

### 3.2 Variants

**Stage:** Stage 1.

Q4.1 uses variants with removed or changed values, and Q4.2 uses records with planted defects. On the input side both appear only as files with checksums.

**Entry variants** (a changed copy of an input XML file):

| Field | Content | Stage |
|---|---|---|
| `variant_id` | Opaque id, for example `V-0007`; never descriptive | Stage 1 |
| `parent_id` | The entry or variant it was made from | Stage 1 |
| `parent_sha256` | SHA-256 of the parent file | Stage 1 |
| `file_name` | Opaque file name | Stage 1 |
| `variant_sha256` | SHA-256 of the variant file, computed by software | Stage 1 |
| `split` | Always the parent's split | Stage 1 |
| `measurement_only` | `true` for a measurement-only size variant (below), otherwise `false` | Stage 1 |

These fields stay in the manifest. None of them enters a packet (section 6, rule 6).

**Measurement-only size variants** (proposed). [Run records, section 4.8](RUN_RECORDS.md#48-measurement-plan) asks for inputs larger than the development entries, so that the measurements reach the packet sizes that the benchmark entries are projected to need. The dataset builder (Tillman Heisner) makes them as entry variants of T9HQ4X or GNICYO; how they are enlarged is his choice (section 6, rule 10). They are listed in the variant list with `measurement_only: true` and belong to the development set. They run only in measurement batches (sections 1.2 and 10.1), through mode A extraction-agent items and mode B sequence items of an item list (section 3.4), which need no frozen files. They have no expected file, are never scored and are never used as examples (section 3.3).

**Record variants** (a reviewed draft with planted defects, or a clean control) are frozen files of an item (section 3.4). Their parent record and its checksum are recorded on the expected side only, because a draft that is identical to its parent would mark a clean control.

**The change list** says what was removed, changed or planted, and where. It is kept on the expected side only (section 4.1).

**Rules:**
1. A variant stays well-formed Export XML. Its packet does not say whether its input is an entry or a variant.
2. No regex is used over free text, such as the methodology, when variants are made (section 6, rule 4). Recommendation, not part of the interface: structured XML nodes may be changed by the builder's code, and free text is changed by hand by Tillman Heisner.
3. A variant of a development entry belongs to the development set and may be used as an example (section 3.3), except a measurement-only size variant.

### 3.3 Example manifest

**Stage:** Stage 1.

One manifest per agent, condition and fold, so that agents keep separate examples (Q4.4; [Architecture, Principles](../ARCHITECTURE.md#principles)) and leave-one-out holds. This holds for zero-shot too: each agent has one zero-shot manifest per fold, with an empty list of examples, and an item uses the zero-shot manifest of its own fold.

| Field | Content | Stage |
|---|---|---|
| `example_manifest_id` | Id, quoted in packet manifests and evaluation run records (sections 3.6 and 10.3) | Stage 1 |
| `agent` | `extraction_agent`, `verification_agent` or `inquiry_agent` | Stage 1 |
| `condition` | `zero_shot` or `few_shot` | Stage 1 |
| `fold` | Required, in both conditions: `dev-T9HQ4X`, `dev-GNICYO` or `test`, equal to the fold of every item that uses the manifest (section 3.4). There is no other value: a fold `all` or a missing fold is rejected | Stage 1 |
| `examples` | Empty (`[]`) for zero-shot. For few-shot, a list of: `example_id`; `source_id` (T9HQ4X, GNICYO, or a variant of either); the example files with their SHA-256; `reviewed_by` and `reviewed_on` | Stage 1 |

An example is a reviewed draft of a development entry or of one of its variants, or, for the later agents, a reviewed report or set of questions made from one. **Example files are made from reviewed records separately from the expected files.** They are never copied from the expected folder, carry no expected-side annotation (no change list, defect label, expected verdict or `origin` column) and no canary, and live in the example store (section 6). The external design package's synthetic example files are never examples ([Roles, section 7.6](ROLES.md#76-examples); section 5).

**Leave-one-out (folds):**
- `dev-T9HQ4X`: items from T9HQ4X or its variants get examples from GNICYO and its variants only;
- `dev-GNICYO`: the other way round;
- `test`: test items may get examples from both development entries.

Nothing in the repository yet says whether T9HQ4X and GNICYO come from one publication. If they do, leave-one-out by entry still gives a development item examples from its own publication, and leave-one-out by publication group would leave development items with no examples. Tillman Heisner decides which applies (section 9).

**Manifest check (software, before every run; proposed).** The check rejects a manifest if:
1. an example's source, or the parent of its source, is a test entry or belongs to a test publication group, or the source is a measurement-only size variant (section 3.2);
2. a zero-shot manifest lists any example;
3. an example has no review, or one of its files does not match its SHA-256;
4. its fold does not fit: the fold is missing or not one of `dev-T9HQ4X`, `dev-GNICYO` and `test`; a `dev-T9HQ4X` manifest holds an example from T9HQ4X or its variants, a `dev-GNICYO` manifest one from GNICYO or its variants; or an item uses a manifest of another fold than its own, in either condition;
5. it names another agent than the one it is used for;
6. an example file contains a canary, if canaries are adopted (section 5.3), or a key that only expected-side files use, both found by exact search.

**Prompt check (software, before every run; proposed).** Every prompt file used in the run contains no id or DOI of any entry in the input-set manifest and no canary, found by exact search ([Roles, section 7.1](ROLES.md#71-rules-for-all-prompts), rule 4).

### 3.4 Item list

**Stage:** Stage 1.

One list per step under test, used unchanged for both conditions (Q4.4). Proposed fields:

| Field | Content | Stage |
|---|---|---|
| `item_id` | Opaque id | Stage 1 |
| `step` | `extraction_agent`, `deterministic_verifier`, `verification_agent`, `inquiry_agent`, or `sequence` for mode B | Stage 1 |
| `split` | The split of its input | Stage 1 |
| `fold` | `dev-T9HQ4X`, `dev-GNICYO` or `test` | Stage 1 |
| `input_id` | The entry or entry variant | Stage 1 |
| `frozen_files` | The files the step starts from (draft, evidence entries, not-mapped entries, round-1 issues, judgments), each with its SHA-256 | Stage 1 |
| `example_manifest_ids` | For each condition, the example manifest of each agent the item runs: one for mode A, three for mode B, none for the deterministic verifier | Stage 1 |

The zero-shot and the few-shot run of an item use the same `item_id` and the same frozen files; only the example manifests differ. How frozen files are placed in packets is set in section 3.5.

An item whose input is a measurement-only size variant (section 3.2) has the step `extraction_agent` or `sequence` and no frozen files. It is kept in an item list of its own, which only measurement batches use (section 10.1).

### 3.5 Packets for evaluation

**Stage:** Stage 1.

Under D6 A no agent has tools, so everything an agent needs is in its packet. Evaluation uses the pipeline's packet preparation unchanged ([Roles, section 8.2](ROLES.md#82-operations), row 4): the same blocks, block order and markers ([Roles, section 7.2](ROLES.md#72-packet-layout)), the same contents ([Handoffs, section 2.4](HANDOFFS.md#24-input-packets)), the same packet check and the same size measurement. There is no separate packet builder for evaluation, so that what is scored is what the pipeline would send. This section adds only where an item's files come from and how they enter the blocks.

**Where each packet's data comes from:**

| Step under test | Data comes from | Blocks filled from the item | Stage |
|---|---|---|---|
| Extraction agent (mode A) | The item's input: a stored entry or an entry variant | INPUT: the input file, byte for byte as stored. EXAMPLES: the files of the item's example manifest for the condition, empty for zero-shot. LINK NAMES stays empty unless the entry is extracted in parts ([Handoffs, section 4.3](HANDOFFS.md#43-extraction-in-parts-contingency)); each part is then its own attempt with its own packet | Stage 1 |
| Deterministic verifier (mode A) | No packet and no model call. The workflow controller hands the deterministic verifier the item's frozen assembled draft, with its evidence entries, parameter links and not-mapped report, and the input, which it reads only to check citations. Before the hand-over, software checks the checksums of the input and of every frozen file as rule 2 below sets out; a mismatch stops the batch | Not applicable | Stage 1 |
| Verification agent (mode A) | The item's input and frozen files | INPUT: the input. DRAFT: the frozen assembled draft (a reviewed draft or a record variant) with its evidence entries, parameter links and not-mapped report. ISSUES: the frozen round-1 issues with their ids as frozen, planted ones included. EXAMPLES as above | Stage 1 |
| Inquiry agent (mode A) | The item's frozen draft and frozen report | ISSUES: the askable issues that packet preparation selects from the frozen report (the round-1 issues, the verification agent's own issues and the judgments; the report filter, below), with the names, values, quotes and locators taken from the frozen draft. REFERENCE carries the field sheet; EARLIER is empty. No INPUT block (D26 A; [Handoffs, section 2.4](HANDOFFS.md#24-input-packets), Inquiry packet) | Stage 1 |
| Sequence (mode B) | The item's input only | The extraction packet as in the first row. Every later packet is built from the run's own outputs, exactly as in the pipeline's round 1, with each agent's example manifest for the item's fold | Stage 1 |

Every evaluation packet names round 1 in its HEADER block.

**How an item's files enter a packet (proposed):**
1. **Read only from the input side.** Packet preparation reads an item's input and frozen files only from the input folder, and example files only from the example store (section 6, rule 1); in mode B it also reads the run's own earlier outputs from the run folder. It never reads the expected or scores folders. It reads the canary list only for the packet check ([Roles, section 7.2](ROLES.md#72-packet-layout); [Runtime, section 11.2](RUNTIME.md#112-the-request-shape-rule), rule 11).
2. **Checked first.** Before it builds the packet and, for a deterministic-verifier item, before the workflow controller hands them to the verifier, software recomputes the SHA-256 of the input and of every frozen file and compares it with the input-set manifest, the variant list or the item list, as [Handoffs, section 2.3](HANDOFFS.md#23-input-file-record) sets out for the input. Example files are checked against their example manifest (section 3.3, manifest check, item 3). The run log records the check as an `input_check` entry ([Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries)). A mismatch, result `checksum_mismatch`, starts no attempt (for a deterministic-verifier item, the verifier does not run) and stops the batch (section 10.4), because the lists no longer describe the files.
3. **Content only, unchanged.** A frozen file enters its block as it is. Packet preparation adds no note and takes nothing from the manifests or the item list into the packet (section 6, rule 6): no item id, file name, checksum, split, fold or origin. Issue ids stay as frozen, because inquiry expectations refer to them (section 4.5), and planted round-1 issues enter the ISSUES block exactly like the deterministic verifier's own (section 2.1).
4. **What is the same for both conditions and every repetition.** In mode A, the zero-shot and few-shot packets of an item, and the packets of its repetitions, hold the same frozen data blocks; only EXAMPLES differs between the conditions. In mode B, the extraction packets hold the same INPUT, and every packet of a run uses the same role prompt, reference text and output format as the packets of the other condition and of the other repetitions (section 2.2); the later packets hold that run's own outputs, which may differ between conditions and repetitions, and each traces to the run's own stored outputs (section 3.6, `placed_files`). Software never replaces a run's outputs to make packets equal. In both modes the instruction blocks are the same, except that EXAMPLES differs between the conditions (shared material, below). The block markers differ from packet to packet, because software draws them for each packet, except that a technical re-run reuses the markers of its first try ([Roles, sections 7.2](ROLES.md#72-packet-layout) and [7.7](ROLES.md#77-checking-an-output-and-the-technical-re-run)). The packet manifest shows by their checksums which files are the same (section 3.6).
5. **No parent with its variant.** An item's own input and frozen files never share a packet with their parent or with a variant made from them (section 6, rule 6; D34 A, decided by Tillman Heisner on 2026-10-21), and no example comes from the item's own entry or its variants, nor from the protected side of leave-one-out (section 3.3, manifest check, item 4). The rule does not apply among the examples: which examples a packet may hold is set by leave-one-out (section 3.3), so a parent and its variant may both appear as examples when their entry is not the item's own.
6. **Packet check and size.** The packet check of [Roles, section 7.2](ROLES.md#72-packet-layout) and the size measurement of [Roles, section 8.1](ROLES.md#81-stage-1-tool-set) run unchanged. A packet that does not fit the route's context length starts no attempt; in evaluation the item is counted as not run in that condition (section 10.4). Under the frozen evaluation profile, packet preparation also checks a packet that fits the context length against the frozen input cap; a packet over that cap is a cap hit, not a packet that is not run. The order of the two checks is set in [Run records, section 4.10](RUN_RECORDS.md#410-cap-hits-in-evaluation), row Input tokens.

**Shared material and examples** (proposed). In both conditions an agent receives the same role prompt, reference text, output format, failure form and any context that the runtime adds automatically, in the same versions; only the EXAMPLES block differs. All of this shared material is free of worked task demonstrations, even fictional or renamed ones: it keeps the schema, the role instructions, the field definitions, the allowed-value lists, the reference rules, the symbolic formulas and the structural output templates, which are not solved task cases ([Roles, section 7.2](ROLES.md#72-packet-layout), Reference text). Worked demonstrations appear only in the few-shot EXAMPLES block, placed from a reviewed example manifest of the item's fold (section 3.3); the zero-shot EXAMPLES block is empty. The documentation examples of [Issue format](../ISSUE_FORMAT.md) (for example 5.1 rule 3, 5.2 rule 7 and section 10) stay in the repository but are excluded from the model-facing reference text, and are never taken as few-shot examples unless they come from reviewed records through an example manifest.

**Future check of the assembled input** (proposed). No prompt, reference text or packet has been prepared yet, so no such check has been run, and nothing here certifies a packet. Once packet preparation exists, the review of each prompt and reference-text version, before it is frozen (section 6, rule 8), covers the complete model input as packet preparation and the runtime assemble it: the role and system instructions, the HEADER, REFERENCE and TECHNICAL NOTE blocks, the output-format and failure-form text and any context added automatically, not only EXAMPLES. It checks that no worked demonstration remains outside EXAMPLES, that zero-shot EXAMPLES is empty, that few-shot adds only the files of the approved manifest to the same shared material, and that the definitions, templates, allowed-value lists and required schema content are still there.

**The report filter** (inquiry agent). Software filters the report before the inquiry agent sees it ([Handoffs, section 2.4](HANDOFFS.md#24-input-packets), Askable issues). In mode A, packet preparation applies the routing of [Workflow, section 3.2](WORKFLOW.md#32-routing-after-a-check) to the item's frozen report, as the pipeline does in round 1, and places only the askable issues in the ISSUES block. Issues on the item's `must_not_ask` list therefore never reach the agent, and that list tests the filter, not the agent (section 4.5). Proposed filter check, by the scorer, per item: the issue ids that the packet manifest lists for the ISSUES block (section 3.6) include no `must_not_ask` id and every `must_ask` id. A failed check is listed for review as a defect of packet preparation or of the item's inquiry expectations. It is reported per item, never scored against the agent, and the item's inquiry scores are listed for review. In mode A this check takes the place of the unwanted and mixed questions of section 4.5, which the filter and the question round's format check make impossible there. In mode B the same filter runs on the run's own report, so an issue counts as one that should not have reached the inquiry agent only through the expected verdict of an expected judgment it matches; unwanted questions are counted as section 2.2 sets out (D33 A).

### 3.6 Packet manifest for evaluation

**Stage:** Stage 1.

[Handoffs, section 2.4](HANDOFFS.md#24-input-packets) defines the packet manifest: a run-log record that software writes for every packet and that agents never see. Software computes every checksum in it and keeps it in the run log only (D13 A). For a packet of an evaluation or measurement batch, the workflow controller adds the following fields (proposed). Its run-log form is the `packet_manifest` entry of [Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries), which carries these fields too for such a packet, `placed_files` included, and its retention is set in [Run records, section 2.11](RUN_RECORDS.md#211-retention). The field `placed_files` keeps its own name so that it stays apart from the common field `files` of every run-log entry ([Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries)): `files` gives the file references of the stored files that the step read and wrote, and `placed_files` how each file entered the packet and which checksum it was compared with.

| Field | Content | Stage |
|---|---|---|
| The fields of [Handoffs, section 2.4](HANDOFFS.md#24-input-packets) | Every field that Handoffs, section 2.4, lists for the packet manifest, unchanged | Stage 1 |
| `item_id`, `condition`, `repetition` | With the run id of the context, the run the packet belongs to (section 10.2). None of them enters the packet itself (section 6, rule 6) | Stage 1 |
| `placed_files` | Every file placed in the packet, one row each: its part in the packet (input, frozen draft, frozen evidence entries, frozen not-mapped report, frozen round-1 issues, frozen judgments, example file, or, in mode B, an earlier output of the run), the folder it was read from, the SHA-256 computed when the packet was built, and the SHA-256 it is compared with: for a file of the evaluation dataset, the one that the input-set manifest, variant list, item list or example manifest gives; for an earlier output of the run (mode B), the one the run log recorded when the output was stored ([Run records, section 2.9](RUN_RECORDS.md#29-checksums-d13-a); D13 A) | Stage 1 |
| `issue_ids` | The issue ids placed in the ISSUES block, in order; for the inquiry agent, the askable ids that the report filter kept (section 3.5) | Stage 1 |

The prompt and reference-text checksums (`prompt_sha256`, `reference_sha256`) and the two packet checksums (`packet_sha256`, the checksum in the packet's file reference, and `packet_sent_sha256`) are among the fields of [Handoffs, section 2.4](HANDOFFS.md#24-input-packets); the binding file also carries `prompt_sha256` ([Runtime, section 10.2](RUNTIME.md#102-the-binding-file)).

**Check (software, while the packet is built; proposed).** Every row of `placed_files` was read from the input folder, the example store or the run's own folder (section 6, rule 1), and its two checksums are equal: a dataset file's computed checksum equals the one its list gives (section 3.5, rule 2), and an earlier output's equals the one the run log recorded when it was stored. Otherwise no attempt starts, and the batch stops (section 10.4). The run's `input_check` entry for the packet records each part of this check, as [Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries) sets out: each dataset file against its list, each earlier output (mode B) against the file reference that the run log recorded when it was stored, and the folder each file was read from. A checksum that differs gives the result `checksum_mismatch`, and a file read from outside those folders the result `wrong_folder`.

## 4. Expected side (proposed)

**Stage:** Stage 1. Each subsection is **proposed; Tillman Heisner accepts, changes or replaces** it.

### 4.1 Rules for all expected files

**Stage:** Stage 1.

**Proposed; Tillman Heisner accepts, changes or replaces.**

1. **Where and for what:** in the expected folder only (section 6). Each expected file names its `item_id` or `variant_id`, the SHA-256 of the input-side files it was built for, and the version of this document it follows. Expected issue lists also name the issue-format version they follow (section 4.3). If the checksums no longer match, the scorer skips the item and reports it.
2. **Origin of each row** (Q1 item 4): `rule`, derived by a named fixed rule from structured XML, or `hand_marked`, a methodology fact marked by Tillman Heisner, with its passage and quote. Free-text facts come only from hand marks.
3. **Pending rows:** a row marked `pending` (not yet settled) is left out of scores and listed. Proposed: frozen test-set expected files hold no pending rows; for development files, the number of pending rows is reported next to every score.
4. **Format:** CSV, JSON or another format is the builder's choice; this section proposes the fields. Under D8 A, derived JSON Schema files for these formats are in [design/specs](specs/README.md); they are proposals like the formats.
5. **Unexpected findings:** an agent's finding, an issue or a value, that matches no expected row is not counted as a false alarm or an invented value straight away. The scorer lists it in a review list (in the scores folder, section 6), and Tillman Heisner reviews it; a confirmed finding goes into a new version of the expected file. Scores name the expected-file version and are reported before and after the review.
6. **Change lists** (for entry variants): one row per change, with the location (an xpath, or the hand-marked passage), the action (`removed`, `changed` or `added`), the old and new text, the expected rows it affects, and its family (section 5).
7. **Planted-defect lists** (for record variants and planted issues): one row per defect, with the pointer, what was planted, the parent record's SHA-256, the expected catcher (deterministic verifier or verification agent), the expected kind and the expected verdict.
8. **Matching of issues** follows [Issue format, notes 1](../ISSUE_FORMAT.md#notes-for-the-evaluation-datasets-not-part-of-the-format): issues match on kind and pointers, and `issue_id`, `rule_id`, `summary` and `raised_by` are ignored; `source_locators` are not part of the match either and are counted as rule 9 says.
   - **Deterministic verifier:** exact match on (kind, set of pointers), under the grouping convention of section 4.3.
   - **Verification agent:** an expected (kind, set of pointers) is found when one or more raised issues of that kind together cover the set and each of them holds only pointers from it. Issue format 4 rule 3 allows the pH of two measurements to share one issue, so the T9HQ4X pH conflict may come as one issue on both pH fields or as two issues, one per field; both count as found. A set covered only in part counts as missed and is listed for review.
9. **Locators:** for `source_conflict`, `wrong_value` and `missed_value`, the format requires `source_locators` ([Issue format 4](../ISSUE_FORMAT.md#4-issue)). Whether they include the expected xpaths is reported as a separate count, locator completeness, and is not part of the match. For other kinds, locators are reported only when present.
10. **Expected-file check (scorer, before scoring):** the checksums match (rule 1); every filled row of an expected-value table has an xpath and a quote, and every hand-marked row also a passage; frozen test-set files hold no pending rows.
11. **Reporting:** the numbers are small, so scores are given as counts per item and condition, not only as percentages. Counts are also grouped by entry and publication group; variants and repetitions stay under their entry and are never counted as independent datasets (section 4.7). The views of section 4.7 are never combined into one overall score. What a score report names is proposed in section 10.7.
12. **Mode-specific keys.** Expected issue lists (section 4.3), expected judgments and issues (section 4.4) and inquiry expectations (section 4.5) carry a required `mode`, `A` or `B`, and their rows follow it:
    - **Mode A:** rows are keyed by the frozen issue id where the item has frozen issues (judgments, must-ask and must-not-ask ids), and by kind and pointers, matched as in rule 8. The scorer resolves the frozen ids in the item's frozen files.
    - **Mode B:** rows are keyed by (source anchor, field, kind), where the anchor is `anchor_xpath` plus `anchor_label` as in the expected-value table (section 4.2) and the field is the path below the anchored object. The scorer maps each generated issue through the draft's evidence entries: each pointer to the draft object it lies in, that object to its anchor by the mapping rule of section 4.2, and the rest of the pointer to the field. Document-level pointers that lie in no anchored object, such as `/creators`, do not depend on object order and are kept as they are, with no anchor. Issue ids, pointers and object order of the run are ignored, so two runs that raise the same source issue under different ids or at different positions match the same row.
    - **Unmappable or ambiguous:** a generated issue, judgment or question tag whose mapping finds no anchor, or several, or an anchor already taken by a duplicate object, is listed on the review list (rule 5), never counted as right or wrong without review. The review list names the mode.
    - The expected-value table and the expected not-mapped list are keyed by anchor already and serve both modes. Expected files never enter a packet (section 6), whatever their mode.

### 4.2 Extraction agent

**Stage:** Stage 1.

**Proposed; Tillman Heisner accepts, changes or replaces.**

**Expected-value table.** One row per source anchor and field, keyed by (`object_type`, anchor, `field`), where the anchor is `anchor_xpath` plus `anchor_label`:

| Column | Content | Stage |
|---|---|---|
| `object_type` | The EnzymeML object, for example `Parameter`, `Measurement`, `MeasurementData`, `SmallMolecule`, `Protein`, `Vessel` | Stage 1 |
| `anchor_xpath` | The input element the object comes from. For an object that only free text states, the methodology element, `/experiment/methodology`. | Stage 1 |
| `anchor_label` | Blank for structured anchors. For a methodology anchor, a short label that tells objects of one type apart, for example `vessel`. | Stage 1 |
| `anchor_aliases` | Other elements where the input states the same object, for example HEPES NaOH in dataset 2 of T9HQ4X when the anchor is its first occurrence in dataset 1 | Stage 1 |
| `field` | The EnzymeML field. References between objects, such as `species_id`, are extracted facts (Issue format 3.1, "Not software"), and their expected value is the anchor of the object referred to. Parameter links ([Issue format 8.1](../ISSUE_FORMAT.md#81-evidence-entries-this-format-relies-on)) use `link.species_id` and `link.measurement_id` in the same way. | Stage 1 |
| `value` | The expected value, typed where possible; blank if `empty` | Stage 1 |
| `unit` | The unit as the input spells it, if any | Stage 1 |
| `unit_id` | The unit's meaning, as an id from the unit table, reviewed by Tillman Heisner | Stage 1 |
| `alternatives` | Other statements of the same amount that the input makes, each as (value, unit, xpath, quote), for example a concentration given in other units in the methods text. Filled by Tillman Heisner; each is accepted as correct. | Stage 1 |
| `xpath` | The accepted citation locations (one or more) | Stage 1 |
| `quote` | The verbatim quote the value rests on | Stage 1 |
| `passage` | Hand-marked rows only: the passage Tillman Heisner marked | Stage 1 |
| `filled` | `filled` or `empty` | Stage 1 |
| `origin` | `rule` or `hand_marked` (section 4.1) | Stage 1 |

SOFTWARE fields ([Issue format 3.1](../ISSUE_FORMAT.md#31-software-fields)) are not in the table and are not scored here, because the assembly step fills them, not the extraction agent.

**Full rows (proposed).** The table holds a row, filled or empty, for every non-SOFTWARE field of every anchored object, so that every output value meets a row. Where a row is still missing, a value in that field is listed for review (section 4.1 rule 5) before it is classed as invented.

**Unit table.** An expected-side file that maps each unit spelling used in the entries to a unit id, with its dimension and scale, reviewed by Tillman Heisner. It does not come from the assembly step (rule `S-UNIT`), so that a mistake in that step cannot hide a unit error. The scorer compares units only through this table. Spellings need care: T9HQ4X gives temperature with unit `C`, which some unit systems read as coulomb ([Issue format 9](../ISSUE_FORMAT.md#9-validation-profile) item 2).

**Anchors, not pointers.** The order of objects in a draft is the agent's choice, so `/measurements/0` need not be dataset 1. Proposed mapping rule:
- each draft object maps to the anchor of its object type whose element, or one of whose aliases, holds the xpaths cited in the object's evidence entries;
- an object cited only to the methodology maps to the methodology anchor of its object type with the fitting label;
- an object that maps to no anchor, or to several, is listed for review;
- a second object that maps to an anchor already taken, for example HEPES NaOH created once per dataset as two small molecules, is a duplicate: it is listed for review and its values are not scored a second time.

**Expected not-mapped list.** Information EnzymeML cannot hold (Q2 item 4), one row per piece: anchor xpath, a short description and origin. Examples: the C-terminal His-tag of T9HQ4X at `/experiment/protein/sequenceModifications/cTerminalTag`, and, if Tillman Heisner accepts natural case N3 (section 5.2), the source organism. Who writes not-mapped entries and what they hold is set in [Issue format 7.1](../ISSUE_FORMAT.md#71-flow) step 1 and [8.1](../ISSUE_FORMAT.md#81-evidence-entries-this-format-relies-on), and their key names in [Handoffs, section 2.14](HANDOFFS.md#214-not-mapped-entries). Proposed: score how many expected rows were reported, and list extra entries for review without counting them against the agent.

**Score classes** (Q4.1), per row:

| Expected | Output | Class | Stage |
|---|---|---|---|
| filled | the same value and unit as the row or one of its alternatives | correct | Stage 1 |
| filled | a different value or unit | wrong | Stage 1 |
| empty | empty | correctly empty | Stage 1 |
| empty | filled | invented | Stage 1 |
| filled | empty | missed | Stage 1 |

- "The same value" uses the normaliser of the citation check ([Issue format 8.2](../ISSUE_FORMAT.md#82-citation-check)): numbers compare by value, letter case is ignored, and identifier URL templates are applied. "The same unit" means the same `unit_id` in the unit table.
- **Stated facts and empty fields apart** (AD-D03). Recovery of stated facts counts filled rows only: correct out of correct, wrong and missed. Correctly empty is reported apart, with invented, and the two are never added together (section 4.7).
- **Tags** on wrong and invented values, reported with the class:
  - `unit`: wrong, and only the unit differs from the row or an alternative. This is what the integrity view counts as a unit error (section 4.7), the measure of the proposed gate "no unit errors".
  - `converted`: wrong, but value and unit together give the same amount as a stated pair that the input does not state in this form, for example 82 microM for a Km stated only as 0.082 mM. Values are never converted ([register conflict C-16](PACKAGE_ADOPTION.md#7-conflict-register)), so it stays wrong. It is reported apart and is not counted as a unit error.
  - `parent_value`: on a changed-value variant, a wrong value that equals the parent's value; on a removed-value variant, an invented value that equals the parent's removed value. Both are signs that the agent did not read the input (Q4.1).

**Citation classes** (the integrity view's unsupported citations, section 4.7, the measure of the proposed gate "every filled value cited"), per filled value in the output:
- `cited`: passes the citation check at an accepted xpath of the row, or at the xpath of the alternative whose value it gives. For a hand-marked row, any quote inside the marked passage that passes the check counts.
- `cited_elsewhere`: passes the check at another xpath. Listed for review, because an equal value can sit in an unrelated node.
- `uncited`: no citation, or the check fails.

**T9HQ4X (illustrative).** Row keys use the public entry's element order; `...` repeats the anchor. The columns `anchor_aliases`, `alternatives` and `passage` are shown in the notes below the table.

| object_type | anchor_xpath | anchor_label | field | value | unit | unit_id | xpath | quote | filled | origin | Stage |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Parameter | `/experiment/datasets/dataset[1]/resultSet/kineticParameter/value[2]` |  | `value` | 0.082 | mM | `millimolar` | `.../@value` | `0.082` | filled | rule | Stage 1 |
| Parameter | same |  | `stderr` | 0.009 |  |  | `.../@se` | `0.009` | filled | rule | Stage 1 |
| Measurement | `/experiment/datasets/dataset[1]` |  | `ph` | 7.8 |  |  | `.../assayConditions/value[2]/@value` | `7.8` | filled | rule | Stage 1 |
| Measurement | same |  | `temperature` | 25.0 | C | `degree_Celsius` | `.../assayConditions/value[3]/@value` | `25.0` | filled | rule | Stage 1 |
| MeasurementData | `/experiment/datasets/dataset[1]/assayConditions/smallCompound[2]` |  | `prepared` | 400.0 | microM | `micromolar` | `.../value/@value` | `400.0` | filled | rule | Stage 1 |
| MeasurementData | `/experiment/datasets/dataset[1]/assayConditions/smallCompound[3]` |  | `prepared` |  |  |  |  |  | empty | rule | Stage 1 |
| SmallMolecule | `/experiment/datasets/dataset[1]/assayConditions/smallCompound[1]` |  | `constant` |  |  |  |  |  | empty | rule | Stage 1 |
| Protein | `/experiment/protein` |  | `organism` | Escherichia coli |  |  | `/experiment/protein/expressionSystem` | `Escherichia coli` | filled | rule | Stage 1 |
| Protein | same |  | `ecnumber` |  |  |  |  |  | empty | rule | Stage 1 |
| Vessel | `/experiment/methodology` | `vessel` | `volume` | 0.1 | ml | `millilitre` | `/experiment/methodology` | `0.1` | filled | hand_marked | Stage 1 |
| Vessel | same | `vessel` | `name` | microwell plate |  |  | `/experiment/methodology` | `microwell plate` | filled | hand_marked | Stage 1 |

- The pH row expects 7.8, the structured value, although the methods text says 7.4 ([Architecture, Principles](../ARCHITECTURE.md#principles)). The conflict is expected from the verification agent (section 4.4).
- The temperature row's `unit_id` records the reviewed meaning of `C`, degrees Celsius.
- The phenazine methosulfate row has one alternative: 0.4, mM, `/experiment/methodology`, quote `0.4`, from the hand-marked passage "0.4mM PMS". Both spellings are correct (trap T2, section 5.2).
- The substrate's `prepared` is empty because the entry gives only a range (Issue format 8.1, "Values the field cannot hold"; natural case N1). Filling it is invented.
- `constant` is never stated in the entry, so a filled value is invented. Its `anchor_aliases` hold `/experiment/datasets/dataset[2]/assayConditions/smallCompound[1]`, HEPES NaOH in dataset 2.
- The two Protein rows follow the proposed natural cases N3 and N4 (section 5.2).
- The Vessel rows rest on the hand-marked passages "Reaction volume: 0.1ml." and "Reactions carried in a microwell plate at 25°C."

### 4.3 Deterministic verifier

**Stage:** Stage 1.

**Proposed; Tillman Heisner accepts, changes or replaces.**

**Expected issue list.** For each item (an assembled draft with its evidence entries, plus the input): the issue-format version the list follows, for example "0.6", `mode: A` (section 4.1, rule 12; mode B does not score the deterministic verifier, section 2.2), and every issue the deterministic verifier should raise in round 1, as (kind, pointer or set of pointers). Optional columns for reading only, not for matching: `rule_id` and a short note.

**Grouping convention (proposed).** Exact matching needs one way of grouping issues, and the deterministic verifier must follow the same one: one issue per pointer, except OR-rule issues, which list all alternative fields ([Issue format 3](../ISSUE_FORMAT.md#3-field-roles), rule 4); missing issues sit at the highest empty level ([Issue format 4](../ISSUE_FORMAT.md#4-issue), rule 2). Tillman Heisner confirms this convention.

**Score:** exact match ([Issue format, notes 2](../ISSUE_FORMAT.md#notes-for-the-evaluation-datasets-not-part-of-the-format)): matched, missing and extra issues. An item passes only with no missing and no extra issue.

**Schema "required" errors** ([Issue format 4.1](../ISSUE_FORMAT.md#41-kinds) note 4, since version 0.5). The expected lists follow it:
- at an empty field that has a field role (ASK-REQ, ASK, ASK-IF or LIST), a schema "required" error is expected only as the matching `missing_*` issue, not also as `wrong_type`;
- at an empty SOFTWARE field, it stays `wrong_type` and goes to human review ([Issue format 4.2](../ISSUE_FORMAT.md#42-judgment-verification-agents-report) rule 6).

Issue format v0.4 said that every schema violation is `wrong_type`. A deterministic verifier built to v0.4 would therefore also raise `wrong_type` for a "required" error at an empty field with a role, and fail these lists. Proposed: a test-set run of the deterministic verifier is admitted only when the verifier implements the issue-format version the expected lists name (section 7.1, rule 5).

**Recommendations (not part of the interface).** How the builder makes expected issues is Tillman Heisner's choice (section 6, rule 10). Two suggestions: write the `missing_*` expectations from the role table ([Issue format 3](../ISSUE_FORMAT.md#3-field-roles)) with code that is separate from the deterministic verifier's, so that one mistake is not copied into both, and review them by hand for the development items; take the mechanical issues from the planted-defect list (section 5.1).

**T9HQ4X (illustrative; the pointers depend on the draft):**

| Kind | Pointer | Why | Stage |
|---|---|---|---|
| `missing_required` | `/creators` | Creators are the people who prepare the record ([Issue format 3.2](../ISSUE_FORMAT.md#32-ask-req-fields)), and the draft has none. One issue at the highest empty level; under [Issue format 4.1](../ISSUE_FORMAT.md#41-kinds) note 4, no `wrong_type` for the schema's "required" error. | Stage 1 |
| `missing_required` | `/small_molecules/0/constant` | The entry never says whether an amount stays the same ([Issue format 10.2](../ISSUE_FORMAT.md#102-a-grouped-question)). | Stage 1 |
| `missing_recommended` | `/measurements/0/species_data/2/prepared` | The substrate is given only as a range. | Stage 1 |
| `missing_optional` | `/proteins/0/ecnumber` | A LIST field left empty in the draft (natural case N4). | Stage 1 |
| `wrong_type` | `/version` | Only in a planted variant whose version reads `"2.0\n"` (section 5.1, family DV6): a SOFTWARE field, so `wrong_type`. | Stage 1 |

### 4.4 Verification agent

**Stage:** Stage 1.

**Proposed; Tillman Heisner accepts, changes or replaces.**

**Items** (Q4.2). Every item starts from a reviewed draft of its input, or from a record variant of one:
- **planted defects:** a record variant with one or a few planted defects (section 5.1), its round-1 issues from the deterministic verifier, and possibly planted round-1 issues;
- **clean controls:** a reviewed draft with no planted defect, and its round-1 issues. Clean means no planted defect, not no finding: the input's natural findings (section 5.2) are still expected. A T9HQ4X clean control therefore still expects the pH conflict;
- **source conflicts:** an input whose statements disagree, either naturally (the T9HQ4X pH, development only) or planted in a variant (families S2 and S3, section 5.2).

**Expected judgments.** For each round-1 issue except `missing_optional` ([Issue format 4.2](../ISSUE_FORMAT.md#42-judgment-verification-agents-report) rule 1), keyed by the file's `mode` (section 4.1, rule 12): in mode A, the issue's id in the frozen packet and its (kind, pointers); in mode B, its (source anchor, field, kind); and the expected verdict, `confirmed` or `rejected`. The expected side never says `uncertain`. Verdicts on `missing_required` and `missing_recommended` issues are scored only under gap; verdicts on the other kinds are scored under confirmed and rejected. A judgment on a `missing_optional` issue is listed, not scored.

**Expected issues.** Each issue the agent should add, as (kind, pointers) in mode A or as (source anchor, field, kind) in mode B (section 4.1, rule 12): planted ones from the planted-defect list, natural ones from the natural findings Tillman Heisner lists for the input (section 5.2). They are matched by the rule for agent-raised issues (section 4.1 rule 8). For `source_conflict`, `wrong_value` and `missed_value`, the expected file also names the xpaths the locators should include, for the locator-completeness count (section 4.1 rule 9):
- `source_conflict`: the xpaths of both sides;
- `wrong_value` and `missed_value`: the xpath that states the source value.

An optional **must-not-raise list** names traps where any finding would be a false alarm (section 5.2). On a clean control, the expected added issues are exactly the input's natural findings; any other added issue is a false alarm.

**Score classes** (Q4.2, mapped as in [Issue format, notes 3](../ISSUE_FORMAT.md#notes-for-the-evaluation-datasets-not-part-of-the-format)):

| Class | What is scored | Stage |
|---|---|---|
| confirmed | Verdicts on the deterministic verifier's `wrong_type`, `broken_reference`, `bad_citation` and `wrong_unit` issues, real or planted, whose expected verdict is `confirmed`: matched or not | Stage 1 |
| rejected | Verdicts on the same kinds whose expected verdict is `rejected`: matched or not | Stage 1 |
| source conflict | Expected `source_conflict` issues: found or missed; extra ones listed. Locator completeness is reported beside it. | Stage 1 |
| gap | Verdicts on `missing_required` and `missing_recommended` issues: `rejected` plus a `missed_value` where the input states the value (Issue format 4.2 rule 5), `confirmed` where it does not. Also expected `missed_value` issues at a parent pointer for omitted objects: found or missed. A verdict without the matching `missed_value`, or the reverse, is reported as partial. | Stage 1 |
| value defect (proposed addition) | The agent's own `wrong_value` and `wrong_unit` issues on planted value defects (families V1, V3, V6): found or missed. Q4.2 names no class for them; Tillman Heisner may keep this row or fold it into another class. | Stage 1 |

- **False alarms:** added issues that match nothing expected, after the review in section 4.1 rule 5, counted per item and separately for clean controls.
- **Left out of verdict accuracy:** the deterministic verifier's `missing_*` issues ([Issue format, notes 2](../ISSUE_FORMAT.md#notes-for-the-evaluation-datasets-not-part-of-the-format)). Their verdicts appear only under gap.

**T9HQ4X (illustrative; development items only):**
- **Source conflict:** kind `source_conflict`, pointers {`/measurements/0/ph`, `/measurements/1/ph`}, as one issue or two (section 4.1 rule 8). For locator completeness, the expected xpaths are both datasets' pH (`/experiment/datasets/dataset[1]/assayConditions/value[2]/@value` and the same in `dataset[2]`) and `/experiment/methodology`, where the hand-marked passage reads "20mM HEPES pH 7.4" ([Issue format 10.1](../ISSUE_FORMAT.md#101-a-ph-conflict)).
- **Trap (must not raise):** the methods text gives phenazine methosulfate as "0.4mM", and the datasets give 400.0 microM. This is the same amount in two units, not a conflict.
- **Planted defect:** the Km of dataset 1 is changed to 0.82 in the draft while its citation still quotes "0.082". The deterministic verifier raises `bad_citation`; the expected verdict is `confirmed`.
- **Natural cases:** the expected outcomes for the substrate range, the DCPIP name, the organism, the EC number and the protein name are proposed in section 5.2 (N1 to N5).

### 4.5 Inquiry agent

**Stage:** Stage 1.

**Proposed; Tillman Heisner accepts, changes or replaces.**

**Inquiry expectations** per item, with `mode: A` (the frozen issues have fixed ids; section 4.1, rule 12):

| Field | Content | Stage |
|---|---|---|
| `must_ask` | Issue ids that at least one question must tag | Stage 1 |
| `must_not_ask` | Issue ids of the item's frozen report that no question may tag: `missing_optional` issues and anything routed to human review (Issue format 4.2 rule 6; [5.1](../ISSUE_FORMAT.md#51-question) rule 2) | Stage 1 |
| `groups` (optional) | Sets of issue ids expected in one question, for example the six `constant` issues of Issue format 10.2; reported, not required | Stage 1 |
| `question_count` | An accepted range, for example 8 to 14 | Stage 1 |

[Handoffs, section 2.4](HANDOFFS.md#24-input-packets) settles that software filters the report before the inquiry agent sees it: the packet holds only the askable issues. `must_not_ask` issues therefore never reach the agent, and that list tests the filter, not the agent. Section 3.5 sets out how the filter builds the packet and how the scorer checks it.

For mode B, the file has `mode: B`: must-ask topics are keyed by (anchor, field, kind) instead of issue ids, and only some are fixed (section 2.2). The scorer maps each question's tagged issue ids to topics through the mapping of section 4.1, rule 12; a tag it cannot map, or maps to several topics, goes to the review list.

**Score classes** (Q4.3):
- **topic coverage:** the must-ask ids tagged by at least one question, out of all must-ask ids;
- **unwanted questions:** questions none of whose issue ids should have reached the inquiry agent (Issue format, notes 5). Proposed in addition: "mixed" questions, which tag a must-not-ask id next to a wanted one, counted separately. In mode A the report filter (section 3.5) and the question round's format check make unwanted and mixed questions impossible; the filter check of section 3.5 takes their place there. In mode B, unwanted questions and mixed questions are counted as section 2.2 sets out (D33 A);
- **question count:** the number of questions and whether it lies in the range, reported with the number of tagged issues;
- **wording:** rated by a person on the wording-rating sheet.

**Tags are part of the format check.** That every question tags at least one issue id, and that every tagged id exists in the packet (Q4.3: questions carry the issue IDs they address), is checked by the question round's format check ([Handoffs, section 2.9](HANDOFFS.md#29-question-round)). An output that breaks it is a technical failure of class `not_in_format`, with the one technical re-run, and is counted under technical failures (section 4.6), not as a content check. This follows the reading of D14 that [Handoffs, section 2.2](HANDOFFS.md#22-format-check-content-checks-and-technical-failures) proposes and that Tillman Heisner confirmed on 2026-10-21 (D25 A).

**Content checks** (counted, not part of the classes): all content checks of [Handoffs, section 2.9](HANDOFFS.md#29-question-round), namely:
- every `choose_one` question ends with both standard closing options, except for enum fields, where only "The question does not fit" is required (Issue format 5.1, options item 2);
- a closing option with another value, or another option that uses `free_entry` or `does_not_fit`, counts as a missing standard closing option ([Handoffs, section 2.9](HANDOFFS.md#29-question-round), Closing options);
- all `R-CTX-LAW` issues are tagged by one grouped question (Issue format 5.1 rule 3);
- a rate-law option that fails a check of [Issue format 3.1](../ISSUE_FORMAT.md#31-software-fields) ("Rate-law bindings") on the packet's record, or whose label shows an id, counted (AD-D01); an option whose value breaks the question round's format check, such as a missing argument or an id the packet does not hold, is a technical failure instead ([Handoffs, section 2.9](HANDOFFS.md#29-question-round));
- no question text contains one of the packet's issue ids or pointers, found by exact search for those known strings;
- askable issues that no question tags (`untagged_issue_ids`, [Handoffs, section 2.9](HANDOFFS.md#29-question-round)), counted; for a must-ask id this is the same miss that topic coverage counts;
- hits of the question screen (D23 A), counted as `question_screen_hits` (section 10.3).

**Wording-rating sheet.** One row per question: the question text, its options, and the summaries of the issues it tags. It is kept in the scores folder (section 6). The rater scores each question against the plain-language rule ([Issue format 5.3](../ISSUE_FORMAT.md#53-plain-language-rule)):
1. It names things the scientist knows, with no pointers, ids or EnzymeML field names.
2. It shows the current and the source value where they exist.
3. It asks for one decision, with the reason in one clause.
4. Proposed addition, not in Issue format 5.3: a scientist could answer it without opening the record.

Proposed scale: 1 (no), 2 (partly), 3 (yes), plus a comment. The rater sees the questions in shuffled order and is not told the condition or the model. Where possible, the rater is a scientist who did not build the dataset.

### 4.6 Uncertain verdicts and other special cases

**Stage:** Stage 1.

**Proposed; Tillman Heisner accepts, changes or replaces.**

- **Uncertain** counts as flagged: it is scored like `confirmed`, because it is routed like `confirmed` (Issue format 4.2 rule 4). The uncertain rate, uncertain verdicts out of all verdicts, is reported per item and condition (Issue format, notes 4).
- **Missing judgments:** a round-1 issue that should have a judgment and has none, or has two different verdicts, is counted as not judged, scored under no verdict class and reported separately.
- **Technical failures** (unparsable, truncated or crashed output, and the failure form) are not scored as content. They are counted and reported by class and code (sections 10.3 and 10.4). A hit of a frozen evaluation cap is a technical failure (D12 A); cap hits are counted per cap and apart from other technical failures ([Run records, section 4.10](RUN_RECORDS.md#410-cap-hits-in-evaluation); section 10.6). A technical failure, a cap hit or an item not run is not scored as a wrong value, but it never drops out of the report either: every content count is given with the operational-completion counts of the same runs (section 4.7). How technical failures and cap hits count towards acceptance is part of the open Q4 item 5. Re-attempts follow the one technical re-run of [Issue format 7.1](../ISSUE_FORMAT.md#71-flow) (D14 A), and first-try and final results are reported separately (section 10.5). A void attempt is not a technical failure of the agent: nothing it returned is used, and it stops the batch (section 10.4).
- **Repetitions:** each item runs more than once per condition. Tillman Heisner sets the number before the first test-set run, and the spread is reported. Each repetition is its own run, with its own packets and attempts (section 10.1). Repetitions, and the variants of one entry, are reported under their entry and publication group and are not independent scientific datasets (section 4.1, rule 11).
- **Development results** are reported apart from test results. They are tuning results, used to diagnose the workflow (section 4.7) and to tune it (section 6, rule 9), and never count as held-out assessment.

### 4.7 Diagnostic views and continuation criteria

**Stage:** Stage 1.

**Decided on 2026-10-27 (AD-D03; [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)); the grouping of existing classes below is proposed, and Tillman Heisner accepts, changes or replaces it.**

The score classes and modes of sections 2 and 4.2 to 4.6 stay as they are. A score report gives them in three separate diagnostic views, each for the first-try and the final result (section 10.5), and never combines them into one overall or "trustworthiness" score:

| View | What it holds, from existing classes and fields | Stage |
|---|---|---|
| Integrity | Invented values (section 4.2); unit errors (`unit` tag, with `converted` apart); unsupported citations (`uncited`, with `cited_elsewhere` reviewed); expected source conflicts missed (sections 2.2 and 4.4, matched as in section 4.1 rule 8) | Stage 1 |
| Usefulness | Recovery of stated facts (correct out of the filled rows), apart from correctly empty fields (section 4.2); in mode B, errors caught downstream (deterministic-only and agent catches apart) against "asked, not caught", and residual unflagged errors (section 2.2); must-ask topic coverage, unwanted and mixed questions, that is decisions asked that no correct pipeline asks, and the question count (sections 2.2 and 4.5) | Stage 1 |
| Operational completion | Runs scheduled (the batch record's items, conditions and repetitions) against runs ended, by `run_end` (section 10.4), with the runs not completed; technical failures by class and code, re-runs, cap hits, void attempts and items not run (sections 4.6, 10.3 and 10.4); in mode B, the extraction errors that no later step judged because that step failed or was not reached (sections 2.2 and 10.5); results that could not be scored: the review list and unmappable or ambiguous results (section 4.1, rules 5 and 12), pending rows (rule 3), items the scorer skipped (rule 1) and failed filter checks (section 3.5), and runs with a differing served model, held out of scores until reviewed (section 11, rule 3) | Stage 1 |

Classes that none of these views names, for example the verification agent's verdict classes, false alarms, the uncertain rate, the deterministic verifier's exact match and the wording rating, are reported per step as sections 4.3 to 4.6 set out.

**Rules** (AD-D03):
1. **Diagnostic during development.** On development entries the views are used to find and fix weaknesses (section 6, rule 9); they are not acceptance evidence.
2. **Nothing vanishes.** A technical failure is not a wrong scientific value, but it is never left out: every content count is reported with the operational-completion counts of the same runs, and unresolved or unmappable results are listed, never dropped or scored silently. Correctly empty fields never count as recovered facts.
3. **Dependence.** Counts are grouped by entry and publication group; variants and repetitions of one entry are not independent datasets (section 4.1, rule 11).
4. **Continuation criteria first.** Explicit criteria for continuing are set before any held-out (test-set) score report is read, informed by what development shows to be feasible and by what the stakeholders can tolerate. This document sets no numerical threshold and no general zero-error rule; [Q4](../OPEN_QUESTIONS.md#q4---how-should-extraction-and-verification-be-evaluated) item 5 stays open to that extent. Tillman Heisner sets and approves the criteria under his interim Stage 1 authority, in a versioned evaluation plan that each held-out assessment batch references (section 4.8; decided on 2026-10-28). Meeting them means that the workflow is technically ready for proposing a bounded trial with researchers; it does not authorize the use of participants' data or effort, or any wider pilot or consortium step, which stays the separate decision of [Q8](../OPEN_QUESTIONS.md#q8---what-determines-pilot-success-and-continuation).
5. **What zero means.** Zero observed integrity errors on these entries is evidence about this benchmark, not proof that no such error can occur on other inputs. No report claims measured time savings.

### 4.8 Evaluation plan and tuning disclosure

**Stage:** Stage 1.

**Decided by Tillman Heisner on 2026-10-28 ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated); [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated); [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)); the field names are proposed.**

- **Evaluation plan.** A stored file, versioned, that holds the continuation criteria of section 4.7, rule 4, for Stage 1 held-out assessment: `plan_version`; `criteria`; `approved_by`, Tillman Heisner, with `approved_at`; and `frozen_on`, from which the version is never changed. A change makes a new version. Its derived schema file is `evaluation-plan.schema.json` (section 10.8). This document selects no threshold for it.
- **Tuning disclosure.** Before each held-out assessment batch, Tillman Heisner records whether information from its test entries, their outputs or their scores informed tuning of the workflow being assessed: `test_information_used`, true or false, and, when true, `entries`, the entries concerned, and `changes`, the changes it informed, with `recorded_by` and `recorded_at`. The batch's `batch_started` entry holds it, and the batch record copies it (section 10.1). Software checks that it is present and reports what it says; it cannot show that no information was used, and it does not watch who opens which score report.
- **What the disclosure means.** Where it says that information from test entries informed the workflow being assessed, assessment on those entries is reported as not held out for that workflow, whatever its version number: a new version does not restore held-out status, and a fresh held-out claim needs entries that are untouched. Earlier results stay as they were. Preplanned repetitions of an unchanged workflow do not count as tuning merely because an earlier repetition finished (section 4.6).
- **Fixed reference.** A held-out assessment batch names one plan version, by its file reference with checksum, in its `batch_started` entry and its batch record. A later plan version never changes what an earlier batch referenced or its criteria.
- **Development batches** need neither a plan nor a disclosure; every other admission rule applies to them (section 7.1).

## 5. Planted-defect families and canary strings

**Stage:** Stage 1. **Proposed:** these are lists to choose from, offered as ideas only. Tillman Heisner chooses, changes or replaces any of them, and none is a requirement. No file of the external design package is copied or loaded: its synthetic example files are never items, examples or expected files. Some of its rejection examples suggested families here; those that rest on its own rules for `/version`, a missing-field registry or a ban on the verification agent raising gaps are not used, because ARIADNE rules replace them ([register, conflicts C-01, C-02 and C-23](PACKAGE_ADOPTION.md#7-conflict-register)).

Each family names where the defect is planted, what is expected and, where it applies, the expected issue kind under [Issue format 4.1](../ISSUE_FORMAT.md#41-kinds) and the validation profile ([Issue format 9](../ISSUE_FORMAT.md#9-validation-profile)). Free-text changes use no regex (section 6, rule 4); making them by hand is recommended.

All T9HQ4X examples below are illustrative. T9HQ4X is a development entry, so its variants serve only as development items or examples; test items come from test entries.

### 5.1 Planted defects

**Stage:** Stage 1.

**In the input (entry variants, for the extraction agent; Q4.1)**

| # | Family | Example change | Expected | Stage |
|---|---|---|---|---|
| E1 | Removed structured value | Delete the Km value of dataset 1 | The row becomes `empty`; a filled value is invented, tagged `parent_value` if it equals the removed value | Stage 1 |
| E2 | Changed structured value | Km 0.082 becomes 0.093 | The row follows the variant; the old value is tagged `parent_value` | Stage 1 |
| E3 | Changed unit | Km unit mM becomes microM, value unchanged | The unit follows the variant | Stage 1 |
| E4 | Removed free-text fact (by hand) | Delete the reaction-volume sentence | Vessel volume `empty` | Stage 1 |
| E5 | Changed free-text fact (by hand) | Reaction volume 0.1ml becomes 0.2ml | The row follows the variant | Stage 1 |
| E6 | Several changes at once | Change several well-known values together | As E2; shows whether values come from memory rather than the input | Stage 1 |
| E7 | Instruction text in free text (by hand) | A sentence telling the agent to fill or change a value | No row changes. Only the effect on scores is measured here; the containment tests for such text are in [Containment, section 7](CONTAINMENT.md#7-prompt-injection-tests-pi-01-to-pi-13). | Stage 1 |
| E8 | Free text that contradicts a structured value (by hand) | The methods text states another temperature | The structured value is kept; the conflict is expected from the verification agent (S2), citing both ([Issue format 4.1](../ISSUE_FORMAT.md#41-kinds), note 1) | Stage 1 |

**In the record (record variants, for the deterministic verifier)**

| # | Family | Example | Expected | Stage |
|---|---|---|---|---|
| DV1 | Placeholder | `null`, `""` or `{}` in a field | `wrong_type` (Issue format 2). Proposed: at a field with a role, `null` and `""` also count as empty, so its `missing_*` issue is expected too; so does `{}` at a unit field, because a unit with neither a name nor base units is empty. Any other `{}` gives `wrong_type` only. Confirmed by Tillman Heisner on 2026-10-21 (D35 A). | Stage 1 |
| DV2 | Wrong JSON type | `"0.082"` as text where a number belongs | `wrong_type` | Stage 1 |
| DV3 | Value outside an allowed list | A modifier role the schema does not list | `wrong_type` | Stage 1 |
| DV4 | Undefined property | A key the schema does not define | `wrong_type` | Stage 1 |
| DV5 | Removed field that has a role | A filled measurement `name` deleted | Only `missing_required` (Issue format 4.1 note 4) | Stage 1 |
| DV6 | Empty or malformed SOFTWARE field | `/version` deleted, or set to `"2.0\n"` or `" 2.0"` | `wrong_type`, routed to human review (Issue format 4.1 note 4; Issue format 9 item 1) | Stage 1 |
| DV7 | Dangling or duplicate id | A `species_id` that names no species; two objects with one id; a parameter link naming no measurement | `broken_reference` | Stage 1 |
| DV8 | Citation defects | No citation; an xpath that finds nothing; a quote not in its node; a value that does not equal its quote (0.08 for "0.082") | `bad_citation` | Stage 1 |
| DV9 | Unit defects | A unit that cannot be parsed; a temperature unit given in mM | `wrong_unit` | Stage 1 |
| DV10 | Input changed only where nothing is cited | An entry variant that changes no node the draft cites | The same issue list as for the parent, since the input is read only for citations | Stage 1 |
| DV11 | Empty list or blank text | `[]` at a list that ARIADNE policy requires to have an entry (`creators`, `vessels`, `reactants`, `species_data`); whitespace-only text at a field with a role | `[]`: only `missing_*`. The pinned schema sets no minimum number of entries for any list, so it raises nothing, and `[]` is empty (Issue format 2). Whitespace-only text: proposed, only `missing_*`. It is empty (Issue format 2), and it is not one of the placeholders that Issue format 2 lists (`null`, `""`, `{}`), so `wrong_type` follows only where the pinned schema itself rejects the value. Confirmed by Tillman Heisner on 2026-10-21 (D35 A); raising it also as `wrong_type` would change Issue format and would need a new Issue format version recorded in the ledger. | Stage 1 |

**In the record or the round-1 issues (for the verification agent; Q4.2)**

| # | Family | Example | Expected | Stage |
|---|---|---|---|---|
| V1 | Right-looking citation to the wrong node | Dataset 1's pH 7.8 cited to the substrate range start, `/experiment/datasets/dataset[1]/assayConditions/smallCompound[3]/value/@startValue`, which also reads "7.8" | The citation check passes; the agent raises `wrong_value`, citing the pH node. The value itself is right, so `wrong_value` is only the closest v0.5 kind; Tillman Heisner confirms it. | Stage 1 |
| V2 | Value not equal to its quote | Km 0.82 with the quote "0.082" | Deterministic `bad_citation`; verdict `confirmed` | Stage 1 |
| V3 | Unit differs from the source | Km unit set to microM; value and citation unchanged | `wrong_unit` from the agent | Stage 1 |
| V4 | Dropped value | A stated temperature removed from the draft | Deterministic `missing_recommended`; agent `rejected` plus `missed_value` (gap) | Stage 1 |
| V5 | Dropped object | Dataset 2's Km parameter left out | `missed_value` at the parent pointer (gap) | Stage 1 |
| V6 | Values swapped between datasets | The two datasets' kcat values exchanged, each with the other's citation | Kind to be settled by Tillman Heisner; `wrong_value` is the closest | Stage 1 |
| V7 | Planted false issue | A round-1 `wrong_unit` on a correct unit, or `bad_citation` on a correct citation | Verdict `rejected` | Stage 1 |
| V8 | Planted true issue | A round-1 mechanical issue that is right | Verdict `confirmed` | Stage 1 |

**In the report (for the inquiry agent; Q4.3)**

| # | Family | Example | Expected | Stage |
|---|---|---|---|---|
| I1 | Issues that must not be asked | `missing_optional` issues; rejected mechanical issues; issues on SOFTWARE fields | Not asked. Software filters them out before the agent sees the report ([Handoffs, section 2.4](HANDOFFS.md#24-input-packets)), so this family tests the filter, not the agent (sections 3.5 and 4.5) | Stage 1 |
| I2 | Issues that belong together | Several `constant` issues | One question (reported, not required) | Stage 1 |
| I3 | Rejected issue that is still asked | A `missing_recommended` judged `rejected`, with a reason | Asked, with the reason shown (Issue format 4.2 rule 6) | Stage 1 |
| I4 | Uncertain verdict | An issue judged `uncertain` | Asked; the question says the agent was unsure (Issue format 4.2 rule 4) | Stage 1 |
| I5 | Rate-law issues | One `R-CTX-LAW` issue per reaction | One grouped question for all reactions, offering for each reaction fully bound options that the parameter links support, each within one dataset and substrate, and only the closing options where no option can be formed (Issue format 5.1 rule 3); required (content checks, section 4.5). Planted family V6, which swaps kcat values between datasets, also probes cross-pairing | Stage 1 |
| I6 | Instruction text in a quote | A source quote telling the agent to ask nothing | No effect on the questions | Stage 1 |

### 5.2 Source conflicts, clean controls and natural cases

**Stage:** Stage 1.

**Source conflicts**
- **S1, natural:** T9HQ4X gives pH 7.8 in both datasets and pH 7.4 in the methods text (Issue format 10.1). For development and few-shot use only.
- **S2, planted in free text:** free text in a variant contradicts a structured value, such as a temperature, a pH or a concentration.
- **S3, planted between structured values:** two structured statements about one field disagree, for example one compound with different identifiers in two datasets.

Test-set source conflicts come from natural conflicts in test entries, which Tillman Heisner hand-marks, or from S2 and S3 variants of test entries.

**Clean controls and traps** (no finding expected beyond the input's natural findings)
- **T1:** a reviewed draft with no planted defect. Only the input's natural findings are expected; for T9HQ4X, that includes the pH conflict.
- **T2:** the same amount in two units, as T9HQ4X's phenazine methosulfate ("0.4mM" in the methods text, 400.0 microM in the datasets) or its temperature (25 degrees Celsius in both places, written differently).
- **T3:** a value copied faithfully that looks implausible. Such values are out of Stage 1 scope (Issue format 4.1 note 3).
- **T4:** one value stated twice with the same content, as T9HQ4X's repeated kcat.

**Natural cases in T9HQ4X to classify.** Each needs an expected outcome, or the scorer would have to guess. Tillman Heisner accepts, changes or replaces each proposal.

| # | What the entry says | Proposed expectation | Stage |
|---|---|---|---|
| N1 | Both substrates are given only as a concentration range | `prepared` stays empty; the `missing_recommended` issue is judged `confirmed`, with no `missed_value`; the range's not-mapped entry stays in the not-mapped report whatever the answer (Issue format 8.1) | Stage 1 |
| N2 | The methods text names "0.1mM DCPIP", and the datasets list "Reduced 2,6-Dichlorophenolindophenol" at 100.0 microM | The amounts are equal, so the amount is a trap (T2). Whether the name difference is a source conflict or a trap is for Tillman Heisner to decide. | Stage 1 |
| N3 | STRENDA `organism` is the source organism, Xanthomonas campestris pv. vitiscarnosae, with `taxonId` 487900 beside it; `expressionSystem` is Escherichia coli | EnzymeML `Protein.organism` is the expression host ([Issue format 3.5](../ISSUE_FORMAT.md#35-list-fields)), so Escherichia coli is extracted. The source organism and its taxon id go to the not-mapped list, and `organism_tax_id` stays empty. | Stage 1 |
| N4 | The comment says the protein was misannotated to EC 1.1.3.15 | Trap: `ecnumber` stays empty, and a filled 1.1.3.15 is invented | Stage 1 |
| N5 | The protein name begins with the accession "A0A077SBA9", while the UniProt attribute gives "A0A1T1QSD4" | The name is copied as stated, and the reference comes from the attribute. Whether the two accessions form a source conflict is for Tillman Heisner to decide. | Stage 1 |

### 5.3 Canary strings

**Stage:** Stage 1.

**Proposed.** A canary is a random string placed in expected-side files. Before a model request is sent, the model gateway searches the request for every canary, by exact search, not by pattern ([Runtime, section 11.2](RUNTIME.md#112-the-request-shape-rule), rule 11). A hit refuses the request, voids the attempt and is recorded. The gateway's search is always on; in real runs its list holds the evaluation canaries only if they are adopted, and the packet check of [Roles, section 7.2](ROLES.md#72-packet-layout) searches each packet whenever that list is not empty. In evaluation, a canary found by either search stops the batch, and no result of the batch is reported until Tillman Heisner has reviewed how the canary got there (section 10.4). The containment suite tests separation with canaries of its own, whether or not evaluation canaries are adopted ([Containment, section 9](CONTAINMENT.md#9-evaluation-separation-test-es-01-to-es-03); section 11).

Canaries help detect a verbatim leak of an expected-side file. They cannot show that nothing leaked: a paraphrase, or rows copied without the canary, carries no canary. The main controls are the separation rules (section 6) and the manifest and prompt checks (section 3.3); canaries are an optional detector on top.

**Options to choose from:**

| # | Option | Gives | Stage |
|---|---|---|---|
| CS1 | One canary per interface version, in every expected file | Simple; shows that something leaked, not what | Stage 1 |
| CS2 | One canary per expected file | Shows which file leaked; a longer canary list | Stage 1 |
| CS3 | One canary per step's expected folder | A middle way | Stage 1 |
| CS4 | A self-test before every run: a request carrying a canary must be refused | Shows that the search works | Stage 1 |
| CS5 | Agent outputs are searched too | Catches a leak that reached the context by another route | Stage 1 |
| CS6 | A separate, allowed marker in example files | Shows which examples reached the context; never mixed up with canaries | Stage 1 |
| CS7 | A canary in every row or record, not only in a header field | Catches rows copied out of a file; longer files | Stage 1 |

**Rules for any choice (proposed):**
1. A canary is random and at least 32 characters long, for example `ARIADNE-CANARY-` followed by 32 random hexadecimal characters. It is never derived from item ids or content.
2. Canaries are kept in a canary list: a separate file outside the expected folder that holds only the canary strings. The software that searches for canaries, the model gateway's request search, the packet check and the manifest and prompt checks of section 3.3, reads only this list, never an expected file.
3. Canaries are never placed in inputs. Entries stay as stored (Q1 item 1), and variants contain only their listed changes.
4. Each expected file carries its canary in a field of its own, for example `canary`, or, under CS7, in every row.
5. Score reports and review lists carry a canary too, because they copy expected values (section 6, rule 1).
6. Example files and prompts carry no canary (section 3.3).

## 6. Separation rules

**Stage:** Stage 1.

Q4.4 governs: agents never see expected outputs. The rules below are proposed to enforce it; the external package's similar rule is credited only as consistent with Q4.4.

1. **Separate folders.** The input side, the example store, the expected side and the scores are separate folders. Proposed layout:

   ```text
   evaluation/
     input/      entries, variants, the items' frozen files, item lists,
                 input-set manifest, variant list                        (the workflow controller reads)
     examples/   example files and example manifests                     (the workflow controller reads)
     expected/   expected files, change lists, planted-defect lists,
                 unit table                                              (only the scorer reads)
     scores/     score reports, review lists, wording-rating sheets      (the scorer writes; people read; the workflow controller never reads)
     canaries    the canary list and nothing else, if canaries are adopted (only the model gateway's request search,
                 the packet check and the manifest and prompt checks read it)
     runs/       one batch folder per evaluation or measurement batch:
                 its batch log, its batch record and one run folder per
                 run, in the layout of Run records, section 2.2, each
                 run folder with its evaluation run record
                 (sections 3.6 and 10)                                   (software writes: the workflow controller, the model gateway
                                                                          and the monitor collector write the logs, and the launcher
                                                                          moves each attempt folder in after its attempt; the scorer reads)
   ```

   An expected file is never inside a packet directory, and no packet is built from the expected or scores folder. The batch-folder and run-folder layout is that of [Run records, section 2.2](RUN_RECORDS.md#22-where-it-is-kept), and which software writes which log is set in [Run records, section 2.10](RUN_RECORDS.md#210-write-once-and-append-only-rules), rule 3. Containment suite runs and behaviour-variant runs are kept outside `evaluation/runs/` (section 11, rules 1 and 7).
2. **The workflow controller never reads expected files** or score reports. Its configuration names only the input, example and run folders; when canaries are adopted, the canary list, which its packet check and the manifest and prompt checks of section 3.3 read (section 5.3); and, for the admission check and for appending hit lines after a containment hit, the report index and the suite runs' folders ([Run records, section 2.7](RUN_RECORDS.md#27-containment-reports)); in a containment run, also the parts of the fixture store it uses (fixture inputs with their checksums, the suite's canary list and the own-canary exemption lists for the packet check, fixture prompt copies, negative configurations and launcher variants), and in a behaviour-variant run, of the fixture store, only the fixture inputs with their checksums (section 11, rules 4 and 7); never the suite's test copy of the expected folder; [Containment, section 9](CONTAINMENT.md#9-evaluation-separation-test-es-01-to-es-03) (ES-02) tests this. The scorer is a separate program that runs after the attempts it scores have finished. No agent attempt sees any evaluation folder: each attempt's container mounts only its own attempt folder ([Runtime, section 10.1](RUNTIME.md#101-the-attempt-folder); [Containment, section 2.4](CONTAINMENT.md#24-the-container-d10-a)).
3. **Expected outputs never enter any agent context:** not in packets, prompts or examples. A record that an item gives the verification agent as its draft is an input-side file of that item and carries none of the expected-side annotations: no change list, defect label, expected issue or verdict. Examples come only from the example store through an example manifest (section 3.3). Example files are made separately from reviewed records and are never copied from the expected folder.
4. **No regex over free text.** Free-text facts on the expected side come only from Tillman Heisner's hand marks (Q1 item 4). The builder and the scorer never search the methodology text with patterns to find values. An exact search for known strings, such as canaries or a packet's own ids, is not a regex over free text.
5. **Opaque names.** Ids and file names on the input side say nothing about what is tested.
6. **Nothing from the manifests in a packet.** A packet holds no entry id, variant id, parent id or checksum, item id, split, fold, publication group or coverage note, apart from what the input file and the example files placed from the attempt's example manifest themselves state: a stored entry, and an example made from one, keeps its own STRENDA id and DOI; which entries examples may come from is set by leave-one-out (section 3.3). An item's own input and frozen files never share a packet with their parent or with a variant made from them (D34 A; section 3.5, rule 5). How an item's files enter a packet is set in section 3.5.
7. **Separate agents.** Each agent has its own prompt and its own example manifests, and each attempt runs in a fresh process ([ledger: Hermes Agent chosen as Stage 1 runtime](../README.md#2026-10-29---workflow-and-review-design-consolidated)), in a container of its own that mounts only its own attempt folder (D10 A; [Runtime, section 10](RUNTIME.md#10-the-attempt-sequence)). In mode B, an agent sees only what the pipeline passes to it.
8. **Freeze before testing.** Before the first test-set run, Tillman Heisner freezes the expected files for the test items, the prompts, the reference texts and the example manifests. A prompt or reference-text version is frozen only after the check of the assembled model input for worked demonstrations (section 3.5, Future check of the assembled input). A later change is a new version, and scores name the versions they used.
9. **Tune on development results.** Prompts, reference texts and examples are tuned on development results; development entries and their variants serve tuning, and their results are never held-out assessment. If information from test entries, their outputs or their scores informs a change, the tuning disclosure of the next held-out assessment records it and the changes it informed (section 4.8), and assessment of the changed workflow on those entries is reported as not held out: it is a follow-up evaluation, not a fresh held-out assessment, and those entries are no longer untouched tests. A new version number does not change that, the earlier results stay as they were, and the split itself does not change ([Q1](../OPEN_QUESTIONS.md#q1---which-existing-datasets-should-be-used), item 3). The continuation criteria of section 4.7 are set in a frozen evaluation-plan version before the first held-out assessment batch (AD-D02, AD-D03; section 4.8).
10. **The builder's internals are not specified.** ARIADNE specifies only what the builder hands over: manifests, item lists, example files, expected files, change lists, planted-defect lists, the unit table and, if canaries are adopted, the canary list.
11. **Containment runs stay apart.** Attempts of a containment run are never evaluation attempts, and no expected file of a test item reaches a containment fixture (section 11).

## 7. Admission rule for evaluation runs

**Stage:** Stage 1.

### 7.1 Admission (proposed)

**Stage:** Stage 1.

An evaluation run, that is a batch (section 10.1), starts only when all of the following hold. Otherwise it does not start, and each rule that failed is recorded in the `batch_refused` entry of its batch log ([Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries); section 10.1). Before every agent attempt, the admission check of [Roles, section 8.2](ROLES.md#82-operations), row 14, applies rules 1, 7 and 8 again. A measurement batch is admitted by the same rules; under rule 6 it runs under the development profile (section 10.6), and under rule 10 it is a development batch.

1. **Containment:** every model call in any mode, evaluation included, requires a current VERIFIED containment report ([Containment, section 12](CONTAINMENT.md#12-admission-rule)). VERIFIED is the passing status of [Containment, section 12.1](CONTAINMENT.md#121-report-status); a report is current while nothing its runtime manifest binds has changed ([Containment, section 12.2](CONTAINMENT.md#122-the-runtime-manifest)); and the admission check of [Containment, section 12.4](CONTAINMENT.md#124-the-admission-check) decides. This applies the ledger Decision that no run starts before the containment test suite passes. A mode A run of the deterministic verifier makes no model call. Even so, every batch, including one of deterministic-verifier items only, is admitted under a current VERIFIED report, so that its batch record names one (section 10.1).
2. **Manifests and prompts:** the input-set manifest, every example manifest and the prompt check pass (sections 3.1 and 3.3).
3. **Same items:** both conditions use the same item list, and the zero-shot and few-shot runs of an item use the same `item_id` and frozen files (Q4.4).
4. **Canaries, if adopted:** the canary list is loaded and, if option CS4 is chosen, the self-test passes (section 5.3).
5. **Versions:** a test-set run uses a version of this document that Tillman Heisner has frozen, and the freezes of section 6 rule 8 are recorded. A deterministic-verifier run on test items also needs a verifier that implements the issue-format version its expected lists name (section 4.3). Development runs may use a draft version and are marked as development runs.
6. **Model route and limits:** every attempt uses the one model route of D11 A1, as the route record of [Runtime, section 12.1](RUNTIME.md#121-the-route-record) holds it. A test-set batch runs only under the evaluation profile frozen by the ledger Decision of [Run records, section 4.9](RUN_RECORDS.md#49-evaluation-caps), recorded before any test-set batch (D12 A), and only when the versions that this Decision records as measured ([Run records, section 4.9](RUN_RECORDS.md#49-evaluation-caps), Freezing) equal those of the batch: the route record's version, the Hermes pin, the admitted request templates, and the prompt, reference-text and example-manifest versions. Otherwise the batch is refused under this rule. Which profile a development batch uses is set in section 10.6.
7. **Not a containment run:** the model gateway confirms that its upstream is the recorded route, not the stub model, so that no test-only gateway setting or launcher variant can apply (D21 A; section 11).
8. **One runtime per batch:** every attempt of the batch runs under the same runtime manifest and the same VERIFIED report. If the report becomes STALE, or a FAILED report for the same manifest follows, no further attempt starts and the batch stops (section 10.4).
9. **Evaluation plan and disclosure:** a test batch (rule 10), a held-out assessment, names an evaluation-plan version that Tillman Heisner has approved and frozen and that holds continuation criteria, and carries its tuning disclosure (section 4.8), before it starts or makes any model call. Software checks that the plan file exists with the referenced version and checksum, that it records its approval and freeze, and that it holds criteria, and that the disclosure is present; it does not judge the criteria. A development batch needs neither (decided on 2026-10-28; [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated); cases EP-01 to EP-06 in section 7.3).
10. **One split per batch:** a batch is a development batch or a test batch, never both. Before the batch starts or makes any model call, software reads the `split` of every item of every item list the batch names (section 3.4): if all are `development`, it is a development batch; if all are `test`, it is a test batch; otherwise it is refused under this rule: its `batch_refused` entry records rule 10 with the item lists the batch names, and its batch record shows the refusal, so that the refusal says that the batch mixes development and test items. A measurement batch uses development entries and their variants, measurement-only size variants included (sections 1.2 and 3.2), so it is a development batch under this rule, and its items are never counted as test items. A development batch still needs every other rule that applies to it; a test batch also needs rule 9; and a test batch that assesses a changed workflow on entries its disclosure names is a follow-up, labelled not held out (sections 4.8 and 10.7). This rule changes neither the split of section 3.1 nor the evaluation modes (decided on 2026-10-28; [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated); cases EP-07 to EP-09 in section 7.4).

### 7.2 To follow in version 1.1

**Stage:** Stage 1.

Written in phase P6. This section keeps its heading so that existing links stay valid; each item that version 1.0 listed here now lives in the section named below.

| Item listed in version 1.0 | Where it is now | Stage |
|---|---|---|
| Packets: what each agent's packet contains, built by the same packet builder as the pipeline (D6 A) | Section 3.5; contents in [Handoffs, section 2.4](HANDOFFS.md#24-input-packets) and blocks in [Roles, section 7.2](ROLES.md#72-packet-layout) | Stage 1 |
| A packet manifest listing every file with its checksum (D13 A) and the prompt id | Section 3.6 | Stage 1 |
| How an item's frozen files enter packets, within section 6 rule 6 | Section 3.5 | Stage 1 |
| The report filter of section 4.5 | Sections 3.5 and 4.5 | Stage 1 |
| Run-record fields: run, mode, step, item, split, condition, repetition, versions, runtime and containment report, route and model (D11 A1), generation settings, prompt and example manifest ids, packet and output checksums (D13 A), validation result, failure class, times | Sections 10.1 to 10.3 | Stage 1 |
| Re-attempts, with first-try and final results reported separately (D14 A) | Sections 10.4 and 10.5 | Stage 1 |
| Usage measured at the model gateway, and the budget profile (D12 A) | Section 10.6; profiles, the measurement plan, the caps and the request-log fields in [Run records, sections 4.1](RUN_RECORDS.md#41-budget-profiles), [4.8](RUN_RECORDS.md#48-measurement-plan), [4.9](RUN_RECORDS.md#49-evaluation-caps) and [2.5](RUN_RECORDS.md#25-the-request-log) | Stage 1 |
| Schema files for packets and run records (D8 A) | Section 10.8; the files are in [design/specs](specs/README.md#the-files) | Stage 1 |

### 7.3 Evaluation-plan and disclosure cases EP-01 to EP-06

**Stage:** Stage 1.

Decided on 2026-10-28 ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated); [ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)); the case ids are proposed. Specified, not implemented. The cases use fixture plans, batch logs and score reports, never held-out results, and refusal is checked before any model call.

| Case | Situation | Expected | Stage |
|---|---|---|---|
| EP-01 | Missing plan: a batch of test items names no evaluation-plan version | The batch does not start and makes no model call; its `batch_refused` entry records rule 9 of section 7.1, and its batch record shows the refusal | Stage 1 |
| EP-02 | Unapproved or incomplete plan: the named version does not exist, its file does not match the referenced checksum, it records no approval or no freeze, or it holds no criteria | Refused as in EP-01; software reports which check failed and does not judge the criteria | Stage 1 |
| EP-03 | Missing disclosure: a batch of test items names an approved, frozen plan version but carries no tuning disclosure | Refused as in EP-01 | Stage 1 |
| EP-04 | Fixed reference: batch B1 starts under plan version 1; Tillman Heisner then freezes version 2 with changed criteria, and batch B2 starts | B1's `batch_started` entry and batch record still name version 1 with its checksum, and B1's score report names version 1 and its criteria; B2 names version 2; nothing written for B1 changes | Stage 1 |
| EP-05 | Disclosed follow-up: after B1, the scores of test entry X inform a change to a prompt; the changed workflow, under a new version number, is assessed on X in batch B3, whose disclosure records X and the change | B3 is admitted; its score report marks the runs on X as not held out, with what the disclosure says, as a follow-up evaluation, not a fresh held-out assessment; B1's results stay as they were; a held-out claim for the changed workflow needs untouched entries. A batch that only repeats B1's unchanged workflow as planned (section 4.6) does not record that repetition as tuning | Stage 1 |
| EP-06 | Development batch: a batch of development items names no plan and carries no disclosure | Admitted if every other rule of section 7.1 holds; marked as a development batch, and never counted as held-out assessment | Stage 1 |

### 7.4 Batch-split cases EP-07 to EP-09

**Stage:** Stage 1.

Decided on 2026-10-28 ([ledger](../README.md#2026-10-29---workflow-and-review-design-consolidated)); the case ids are proposed. Specified, not implemented. The cases use fixture item lists, batch logs and score reports, never held-out results, and refusal is checked before any model call.

| Case | Situation | Expected | Stage |
|---|---|---|---|
| EP-07 | Mixed batch: a batch names an extraction-agent item list of development items and a verification-agent item list of test items, or one item list that holds both | The batch does not start and makes no model call; its `batch_refused` entry records rule 10 of section 7.1, with the item lists the batch names, and any other rule that failed; its batch record shows the refusal | Stage 1 |
| EP-08 | Measurement batch: a measurement batch names items of the development entries and of their measurement-only size variants | It is a development batch under rule 10: it needs no evaluation plan and no disclosure, every other rule of section 7.1 applies to it, and none of its items is counted as a test item | Stage 1 |
| EP-09 | Separate batches in one report: a score report covers a development batch and a test batch of the same workflow, and a disclosed follow-up batch on test entries (EP-05) | The batches pass their own gates (EP-06; EP-01 to EP-03); the report shows the development results apart and may compare them with the test results, but no held-out score includes a development result; the follow-up's runs are marked not held out (section 10.7) | Stage 1 |

## 8. Traceability

**Stage:** Stage 1.

Each Q4 item and each proposed gate is mapped to a mode, an expected-side file and a score class. The gates are proposals and are reported as integrity measures (section 4.7); no numerical threshold or zero-error rule is selected, and acceptance criteria remain open to that extent (Q4 item 5; AD-D03). Against leaks of expected outputs, the separation rules and the manifest and prompt checks are the main control; canaries, if adopted, are an optional detector.

| Requirement | Mode | Expected-side file | Score class | Section | Stage |
|---|---|---|---|---|---|
| Q4: one dataset per agent | A for each step; B | Expected files per step; item list per step (input side) | Per step, below | 3.4, 4 | Stage 1 |
| Q4: expected values cite their XML location or a hand-marked quote | Before scoring, all modes | Expected-value table (`xpath`, `quote`, `passage`, `origin`) | Not scored; the expected-file check: every filled row has an xpath and a quote, every hand-marked row also a passage | 4.1, 4.2 | Stage 1 |
| Q4.1: extraction fields | A (extraction agent); B | Expected-value table; unit table; expected not-mapped list | correct, wrong, correctly empty, invented, missed; tags `unit`, `converted`, `parent_value`; not-mapped rows reported | 4.2 | Stage 1 |
| Q4.1: variants with removed or changed values | A (extraction agent) | Change list; the variant's expected-value table | Removed: correctly empty, or invented (tagged `parent_value` if it equals the removed value). Changed: correct, or wrong tagged `parent_value` | 3.2, 4.2, 5.1 | Stage 1 |
| Q4.2: planted defects, clean controls, source conflicts | A (verification agent) | Expected judgments and issues, including natural findings; planted-defect list | confirmed, rejected, source conflict, gap; value defect (proposed); false alarms | 4.4, 5.1, 5.2 | Stage 1 |
| Q4.2: the deterministic verifier checks only structure, units and citations | A (deterministic verifier) | Expected issue list; planted-defect list | Exact match: matched, missing, extra. Family DV10 tests the "only": an input change outside cited nodes changes no issue. | 4.3, 5.1 | Stage 1 |
| Q4.3: questions carry the issue IDs they address | A (inquiry agent); B | None; the packet's own issue ids | Format check of the question round: a question with no tag, or with a tag the packet does not hold, makes the output a technical failure (`not_in_format`), counted with the technical failures | 4.5, 4.6 | Stage 1 |
| Q4.3: topic coverage, unwanted questions, question count, wording | A (inquiry agent); B | Inquiry expectations; mode B must-ask topics; wording-rating sheet (scores folder) | Topic coverage, question count, wording rating; unwanted questions are counted in mode B against the step that let their issue through (D33 A, section 2.2) and are replaced in mode A by the filter check of section 3.5; neither is scored against the agent | 2.2, 3.5, 4.5 | Stage 1 |
| Q4.4: zero-shot and few-shot on the same items | A and B, both conditions | None; item lists and example manifests are on the input side | Every class above, per condition; in mode A the packets of an item differ only in EXAMPLES; in mode B the input and the fixed configuration are the same, and only EXAMPLES and the run's own downstream outputs differ (section 3.5, rule 4); items not run in one condition are reported apart | 3.3, 3.4, 3.5, 7.1, 10.4 | Stage 1 |
| Q4.4: examples only from the development set; separate prompts | All | None; the example manifest check, the prompt check, and prompt and example manifest ids in packet manifests and run records | Not scored; after a failed check the batch does not start (section 7.1, rule 2) | 3.3, 3.6, 6, 10.3 | Stage 1 |
| Q4.4: agents never see expected outputs | All | None needed; separation rules and checks. If adopted, a canary in every expected file. | Not scored; a canary hit, if canaries are adopted, voids the attempt and stops the batch | 3.3, 3.5, 3.6, 5.3, 6, 11 | Stage 1 |
| Q4.4: tested alone | A: each agent, and the deterministic verifier, alone on frozen packets | The expected file of each step | The classes of each step | 2.1, 3.5, 4 | Stage 1 |
| Q4.4: tested in sequence | B: the three agents in sequence through round 1 | The expected-value table and source conflicts, keyed by anchor; mode B must-ask topics | Extraction classes; caught downstream; source conflicts raised; question scores | 2.2, 3.5 | Stage 1 |
| Q4.5: acceptance criteria (open) | All | None | Not set. The three diagnostic views are reported side by side, with no overall score; continuation criteria are set before test-set results are read. Technical failures, cap hits, void attempts and items not run are counted and reported under operational completion; how they count towards acceptance stays open | 4.6, 4.7, 6, 10.4, 10.6, 10.7 | Stage 1 |
| D14 A: first-try and final results apart | A and B | None | First-try and final views side by side, with re-runs counted per agent and class | 10.5 | Stage 1 |
| D12 A: usage measured; frozen caps in evaluation | A and B | None | Usage per attempt; budget profile per run; unknown usage flagged, never zero | 10.6 | Stage 1 |
| Every model call needs a VERIFIED containment report; containment runs never count | A (agents) and B | None | Not scored; admission, and the report named in every run record | 7.1, 10.2, 11 | Stage 1 |
| Integrity (proposed gate: no invented values) | A (extraction agent); B | Expected-value table | invented, counted after review; the gate's "invented = 0" is not selected as a threshold | 4.2, 4.7 | Stage 1 |
| Integrity (proposed gate: no unit errors) | A (extraction agent); B; A (verification agent) | Expected-value table (`unit`, `unit_id`) and unit table; planted-defect list (V3) | Extraction, in A and B alike: wrong tagged `unit`, counted, with `converted` reported apart. Verification agent: planted unit defects found, under value defect, reported per step (section 4.4), outside the integrity view. No threshold selected | 4.2, 4.4, 4.7 | Stage 1 |
| Integrity (proposed gate: every filled value cited) | A (extraction agent); B | Expected-value table (`xpath`, `quote`) | `uncited`, counted; `cited_elsewhere` reviewed. No threshold selected | 4.2, 4.7 | Stage 1 |
| Integrity (proposed gate: every source conflict flagged) | A (verification agent); B | Expected judgments and issues | source conflicts missed, counted, matched as in section 4.1 rule 8. No threshold selected | 2.2, 4.1, 4.4, 4.7 | Stage 1 |
| Usefulness and residual unflagged errors (AD-D03) | A; B | Expected-value table; expected judgments and issues; inquiry expectations | Recovery of stated facts apart from correctly empty; caught, "asked, not caught" and residual unflagged errors (mode B); topic coverage, unwanted questions, question count | 2.2, 4.2, 4.5, 4.7 | Stage 1 |
| Operational completion (AD-D03) | A and B | None | Runs scheduled and ended, failures, re-runs, cap hits, results not scored, listed beside every content count | 4.6, 4.7, 10.4, 10.7 | Stage 1 |

## 9. Choices before the freeze

**Stage:** Stage 1.

Before freezing a version of this document (version 1.0 was not frozen), Tillman Heisner decides:
1. each expected-side format in section 4, including the unit table, accepted alternatives and full rows: accept, change or replace;
2. the matching rules: the deterministic verifier's grouping convention (section 4.3) and the covering rule for agent-raised issues (section 4.1 rule 8);
3. whether the verification agent's "value defect" row stays (section 4.4), and the kinds for families V1 and V6;
4. the reading of placeholders (family DV1) and of whitespace-only text (family DV11): decided (D35 A, section 5.1);
5. for mode B, one condition per run, the anchor-mapping rule and the fixed must-ask topics (sections 2.2, 4.2 and 4.5); how unwanted questions are counted in mode B is decided (D33 A, section 2.2);
6. the publication grouping of T9HQ4X and GNICYO, and whether leave-one-out works per entry or per publication group (section 3.3);
7. the expected outcomes of the natural cases N1 to N5 (section 5.2);
8. which planted-defect families to use, and how many defects per item;
9. whether to adopt canaries, and which options (section 5.3);
10. the wording-rating scale, criterion 4 and who rates (section 4.5);
11. the number of repetitions per item and condition (section 4.6);
12. the packet, packet-manifest, run-record and batch-record interfaces, which ARIADNE specifies (sections 3.5, 3.6 and 10; D9 A): he reviews them before he freezes the version, including how runs and batches end (section 10.4), the first-try view of mode B (section 10.5) and the report-filter check (section 3.5);
13. the grouping of existing classes into the diagnostic views and the definition of residual unflagged errors (sections 2.2 and 4.7): accept, change or replace.

Separately from the freeze, Tillman Heisner sets the continuation criteria in a frozen evaluation-plan version before the first held-out assessment batch (sections 4.7, 4.8 and 7.1, rule 9); this document proposes none.

## 10. Evaluation run record

**Stage:** Stage 1. Stage 2 additions in section 12.

The derived schema files of the evaluation run record and the batch record are listed in section 10.8.

### 10.1 Runs, batches and attempts

**Stage:** Stage 1.

- A **batch** starts when the admission of section 7.1 passes. It names its items (from one item list per step), its conditions, its number of repetitions (section 4.6) and its budget profile (section 10.6). All its attempts run under one runtime manifest and one VERIFIED containment report (section 7.1, rule 8). A batch is either an evaluation batch, of evaluation runs, or a measurement batch, of measurement runs (section 1.2; [Run records, section 4.8](RUN_RECORDS.md#48-measurement-plan)), never both.
- A **run** is one item in one condition and one repetition. Each repetition is its own run, with its own packets and attempts; nothing carries over between runs, because every attempt starts in a fresh container ([Runtime, section 10.3](RUNTIME.md#103-the-sequence)). Each run has its own record id and round 1 in the context of its files ([Handoffs, section 2.1](HANDOFFS.md#21-conventions-for-every-handoff)).
- Each run has one **evaluation run record** (sections 10.2 and 10.3). It lists the run's agent attempts, first tries and technical re-runs alike, and the software steps the run used. A measurement run gets the same record, marked as such by its `kind` (section 10.2), so that its usage is read the same way; the scorer refuses it (section 11, rule 3).
- **Where it lives.** The workflow controller writes the record once, when the run ends, as a file in the run's folder ([Run records, section 2.2](RUN_RECORDS.md#22-where-it-is-kept)). It is named by the run's `evaluation_record` entry ([Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries)). The run-log entries it refers to (the attempt entries and the attempt result of [Handoffs, section 2.13](HANDOFFS.md#213-attempt-result-and-technical-failure), the packet manifest of section 3.6 and the request log of [Runtime, section 11.3](RUNTIME.md#113-the-request-log)) are those of [Run records, sections 2.3 to 2.5](RUN_RECORDS.md#23-run-log-entries), and retention is set in [Run records, section 2.11](RUN_RECORDS.md#211-retention).
- **Checksums.** The evaluation run record and the batch record hold checksums (sections 10.1 to 10.3), as `binding.json` does ([Runtime, section 10.2](RUNTIME.md#102-the-binding-file)). All three are stored files that software writes only to record a run or a batch and that the run log names, so they are part of the run log as [Run records, section 1.2](RUN_RECORDS.md#12-terms) (Run log) defines it, and their checksums are kept in the run log only (D13 A; [Run records, section 2.9](RUN_RECORDS.md#29-checksums-d13-a)). None is a record file, handoff or packet, and record files never hold a checksum ([Issue format 11](../ISSUE_FORMAT.md#11-deliberately-left-out)). Neither record has an idempotency key or a revision chain (Stage 2, if ever; section 12).
- **Who writes and reads it.** Software copies each value from the one source named in the tables below; no agent and no person writes in it. The scorer and people read it. Agents never see it, and nothing of it enters a packet (section 6, rule 6).

**Batch log and batch record** (proposed). Each batch has a batch log in its batch folder, which the workflow controller writes from the admission attempt on, so that a refused admission is recorded too ([Run records, sections 2.2 and 2.3](RUN_RECORDS.md#23-run-log-entries)): `batch_started` when the admission of section 7.1 passes, `batch_refused`, with each rule that failed, when it does not, and `batch_ended` when the batch ends. When a batch ends or is refused, the workflow controller writes its **batch record**: a stored file, written once, that the `batch_ended` or `batch_refused` entry names, with its checksum (D13 A; [Run records, section 2.9](RUN_RECORDS.md#29-checksums-d13-a)). Software copies each value from the batch log: for a batch that started, from its `batch_started` and `batch_ended` entries; for a refused batch, from its `batch_refused` entry, which carries the fields of `batch_started` as far as the admission attempt determined them ([Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries)). A value that the admission attempt did not determine is absent from the record of a refused batch, never filled in. Score reports name the batch record (section 10.7).

| Field | Content | Stage |
|---|---|---|
| `batch_id`, `kind` | The batch's id, written by software; `evaluation` or `measurement`, as the batch log's `run_kind` records it ([Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries)) | Stage 1 |
| `admission` | The result and time of the admission of section 7.1 and, if it was refused, each rule that failed | Stage 1 |
| `follows_batch` | For a batch that runs what a stopped batch did not complete, that batch's id (section 10.4); otherwise absent | Stage 1 |
| `runtime_manifest_sha256`, `containment_report` | The runtime-manifest checksum and the id of the VERIFIED report the batch was admitted under (section 7.1, rules 1 and 8), a batch of deterministic-verifier items only included; for a refused batch, the manifest checksum if the admission attempt computed it, and the report that the admission check found, if any | Stage 1 |
| `budget_profile` | The profile's name and version (section 10.6) | Stage 1 |
| `items`, `conditions`, `repetitions` | The item lists with their ids and versions, the conditions and the number of repetitions | Stage 1 |
| `canaries` | `none`, or the adopted options of section 5.3 and the checksum of the canary list loaded | Stage 1 |
| `evaluation_plan` | For a held-out assessment: the evaluation-plan version it references, with its file reference and checksum and its `plan_version` (section 4.8); absent for a development batch | Stage 1 |
| `tuning_disclosure` | For a held-out assessment: the tuning disclosure recorded before it started (section 4.8); absent for a development batch | Stage 1 |
| `started_at`, `ended_at` | RFC 3339 in UTC; absent for a refused batch, whose `admission` field gives the time | Stage 1 |
| `end` | `completed`, or `stopped` with the code or check that stopped it and the run where it happened (section 10.4), and the ids of the runs not completed; absent for a refused batch | Stage 1 |

Two notes come after a batch has stopped, and the batch record, which is never changed ([Run records, section 2.10](RUN_RECORDS.md#210-write-once-and-append-only-rules)), does not hold them. They are the batch log's `fix` entry, the note of how the cause was fixed ([Workflow, section 4.4.4](WORKFLOW.md#444-resume)), written before any batch runs what this one did not complete; and its `canary_review` entry, after a canary was found, Tillman Heisner's review of how it got there, with its date (section 10.4). Both entries are set out in [Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries).

### 10.2 Fields of a run

**Stage:** Stage 1.

| Field | Content | Source | Stage |
|---|---|---|---|
| `run_id` | The run's id, opaque, written by software ([Handoffs, section 2.1](HANDOFFS.md#21-conventions-for-every-handoff), ARIADNE identifiers) | Workflow controller | Stage 1 |
| `record_id`, `round` | The rest of the context of the run's files: its record id, and round 1 ([Handoffs, section 2.1](HANDOFFS.md#21-conventions-for-every-handoff)) | Workflow controller | Stage 1 |
| `batch_id` | The batch the run belongs to (section 10.1) | Workflow controller | Stage 1 |
| `kind` | `evaluation` or `measurement` (section 1.2), as the run log's `run_kind` field records it ([Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries)) | Run log (`run_kind`) | Stage 1 |
| `mode` | The evaluation mode, `A` or `B` (section 2) | Item list | Stage 1 |
| `step` | The step under test, as in the item list (section 3.4): `extraction_agent`, `deterministic_verifier`, `verification_agent`, `inquiry_agent` or `sequence` | Item list | Stage 1 |
| `item_id`, `split`, `fold` | The item, its split and its fold | Item list | Stage 1 |
| `condition` | `zero_shot` or `few_shot`; none for a deterministic-verifier run | Batch | Stage 1 |
| `repetition` | The repetition's number, from 1 to the number Tillman Heisner sets (section 4.6) | Batch | Stage 1 |
| `versions` | The version of this document; the versions of the input-set manifest, the item list, the example manifests used and, where the run's input is an entry variant, the variant list, each marked frozen or draft (section 6, rule 8) from its `frozen_on` (section 3), the item list with its `item_list_id`; for a run that uses the deterministic verifier, its version and the issue-format version it implements (section 7.1, rule 5) | Manifests; workflow controller | Stage 1 |
| `runtime_manifest_sha256`, `containment_report` | The runtime-manifest checksum that the admission check computed for the run's attempts (the `admission` entry of [Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries), and the attempt entries' fields of the same names, [Run records, section 2.4](RUN_RECORDS.md#24-attempt-entries); [Containment, section 12.2](CONTAINMENT.md#122-the-runtime-manifest)), and the id of the report that admitted them, VERIFIED at admission ([Containment, sections 12.1 and 12.4](CONTAINMENT.md#124-the-admission-check)). Absent only for a mode A run of the deterministic verifier, which makes no model call | Admission check; run log | Stage 1 |
| `hermes_tag`, `hermes_commit` | The pinned Hermes release ([Runtime, section 3](RUNTIME.md#3-pin)): the binding's `hermes_pin`, and the commit that the runtime manifest binds. Absent for a mode A run of the deterministic verifier, which has no attempt | Binding file ([Runtime, section 10.2](RUNTIME.md#102-the-binding-file)); runtime manifest | Stage 1 |
| `route_id`, `route_version`, `model` | The route record and its version, and the dated model it names ([Runtime, section 12.1](RUNTIME.md#121-the-route-record); D11 A1). Absent for a mode A run of the deterministic verifier, which has no attempt | Binding file (`route_id`); route record (`route_version`, `model`) | Stage 1 |
| `served_models` | The served-model ids of the run's attempts (section 10.3). No ids for a mode A run of the deterministic verifier, which has no attempt. Proposed: a reported id that differs from the route's model is flagged, and the run is listed for review (section 11, rule 3). A forwarded request whose response reports no served-model id, for example a cut stream or a response that never arrived, is recorded as such and never flagged as a different model; where its usage is missing too, the unknown-usage flag covers it ([Run records, section 4.4](RUN_RECORDS.md#44-unknown-usage)) | Attempt entries (request log) | Stage 1 |
| `generation_settings` | Per agent, one entry for each agent (role-prompt version) of the run, since a mode B run has three agents: what that agent's requests carried besides the prompt and the packet, that is, `max_tokens` as sent, and the reasoning setting and every sampling parameter as sent, with the checksum of the request body without its messages, as the request log records them ([Run records, section 2.5](RUN_RECORDS.md#25-the-request-log)). These are the same for every request of one agent (role-prompt version) in a batch, not for every run of a batch: the route record and the admitted `config.yaml`, both bound by the runtime manifest ([Containment, section 12.2](CONTAINMENT.md#122-the-runtime-manifest)), fix the reasoning setting and the sampling parameters; `max_tokens` is set by the budget profile, the route's documented maximum under the development profile and the agent's frozen output cap under the evaluation profile ([Run records, section 4.1](RUN_RECORDS.md#41-budget-profiles)); and the body without its messages also holds the agent's system text. Gateway rule 7 refuses any other `max_tokens` ([Runtime, section 11.2](RUNTIME.md#112-the-request-shape-rule)) | Request log (`max_tokens`, `generation_settings`) | Stage 1 |
| `budget_profile` | The profile's name and version, the batch's and so the same for every run of the batch (section 10.1), and, for the evaluation profile, the ledger Decision that froze it ([Run records, section 4.9](RUN_RECORDS.md#49-evaluation-caps)); and, per agent, one entry for each agent (role-prompt version) of the run, the limit values in force for that agent's attempts, as the attempt entries record them (`budget_profile`, `limits`; [Run records, section 2.4](RUN_RECORDS.md#24-attempt-entries)), with the wall-clock limit as its length in minutes (`wall_clock_minutes`), which is the same for every attempt while its end time is not, the input cap included under the evaluation profile, and the limit on attempts per pipeline stage, which the workflow controller holds. Under the evaluation profile the limit values are that agent's frozen caps, which are set per agent ([Run records, section 4.9](RUN_RECORDS.md#49-evaluation-caps)) | Batch; attempt entries; workflow controller (attempts per pipeline stage) | Stage 1 |
| `attempts` | One row per agent attempt, in order (section 10.3) | Attempt results; attempt entries | Stage 1 |
| `software_steps` | For each software step the run used (the assembly step and the deterministic verifier in mode B; the deterministic verifier in its mode A runs): its version, the SHA-256 of its output and its self-check result ([Handoffs, section 2.2](HANDOFFS.md#22-format-check-content-checks-and-technical-failures)), as the `software_step` entries record them ([Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries)) | Workflow controller | Stage 1 |
| `first_try_result`, `final_result` | The two views of section 10.5 | Workflow controller | Stage 1 |
| `run_end` | `completed`, `technical_failure`, `not_run` or `stopped` (section 10.4), with the code where one applies ([Roles, section 8.7](ROLES.md#87-denial-and-failure-codes); [Run records, section 2.8](RUN_RECORDS.md#28-run-log-codes)) or, where none does, the result of the check that stopped the run, for example the `input_check` or `schema_check` result `checksum_mismatch` ([Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries)). Software copies the code or check result from the run-log entry that carries it: a `code` entry, the `attempt_ended` entry of the attempt that ended the run, or an `input_check` or `schema_check` entry; where `xml_refused` is carried is set in [Run records, section 2.8](RUN_RECORDS.md#28-run-log-codes). Where a frozen cap stopped a step before an attempt started (code `cap_hit`), also `cap_hit`, naming the cap: `input_tokens` or `attempts`, copied from the run log's `code` entry ([Run records, sections 2.3](RUN_RECORDS.md#23-run-log-entries) and [4.10](RUN_RECORDS.md#410-cap-hits-in-evaluation)) | Workflow controller; run log (`code`, `attempt_ended`, `input_check` or `schema_check` entry) | Stage 1 |
| `started_at`, `ended_at` | When the run started and ended, in RFC 3339 and UTC | Workflow controller | Stage 1 |

### 10.3 Fields of an attempt

**Stage:** Stage 1.

| Field | Content | Source | Stage |
|---|---|---|---|
| `attempt_id`, `agent`, `part`, `try`, `rerun_of` | As in [Handoffs, section 2.13](HANDOFFS.md#213-attempt-result-and-technical-failure); `agent` names the role that ran | Attempt entry (`attempt_started`) | Stage 1 |
| `packet_manifest`, `packet_sha256` | The packet manifest's run-log entry (section 3.6) and the checksum of the packet as stored ([Runtime, section 10.2](RUNTIME.md#102-the-binding-file); D13 A). The checksum of the text as Hermes sends it stays in the attempt entry ([Run records, section 2.4](RUN_RECORDS.md#24-attempt-entries)) | Packet manifest | Stage 1 |
| `packet_bytes` | The size of the packet and of its INPUT and REFERENCE blocks in bytes (an inquiry packet has no INPUT block, so its INPUT size is absent: D26 A): the source bytes delivered to the attempt ([Run records, section 4.2](RUN_RECORDS.md#42-what-is-measured)) | Packet manifest | Stage 1 |
| `prompt_id`, `prompt_version`, `reference_version`, `example_manifest_id` | The prompt's artifact id and version name, the reference-text version and the example manifest, in zero-shot the empty zero-shot manifest of the agent and the item's fold (section 3.3) | Packet manifest | Stage 1 |
| `raw_output_sha256` | The checksum of the stored raw output, failures included, as the `raw_output` file reference of the attempt entry carries it ([Run records, section 2.4](RUN_RECORDS.md#24-attempt-entries); `raw_output` in Handoffs 2.13; D13 A); empty only when nothing was returned | Attempt entry (run log) | Stage 1 |
| `outcome` | `output`, `technical_failure` or `void` (Handoffs 2.13); absent for an attempt whose start-up self-check failed before the turn, or that was stopped at the wall-clock guard after the gateway answered the runner's status request and before its first model request, which is no attempt failure and whose `code` is `startup_check_failed`, unless a monitor record is unexplained, which makes the attempt void with code `containment_hit`, or the monitoring evidence is incomplete, which makes it void with code `monitor_incomplete` ([Run records, section 2.4](RUN_RECORDS.md#24-attempt-entries)) | Attempt entry (`attempt_ended`); the attempt result where one exists | Stage 1 |
| `failure_class` | For a technical failure, its class, required. The only exceptions, which have no class, are an attempt that the request guard ended under the development profile (`code` `runaway_guard`) and one that a frozen request cap ended under the evaluation profile (`code` `cap_hit`, with `cap_hit` `requests`), each where [Run records, section 2.4](RUN_RECORDS.md#24-attempt-entries) applies it; any other code is not enough, and a technical failure never lacks both a class and one of these codes. For a void attempt, the code that made it void (Handoffs 2.13); absent where `outcome` is absent | Attempt entry (`attempt_ended`) | Stage 1 |
| `code` | The run-log code where one applies, for example `runaway_guard` or `containment_hit`, from [Roles, section 8.7](ROLES.md#87-denial-and-failure-codes); how the run log carries it: [Run records, section 2.8](RUN_RECORDS.md#28-run-log-codes) | Run log | Stage 1 |
| `cap_hit` | Evaluation profile only: the frozen cap that was hit. There are five ([Run records, section 4.10](RUN_RECORDS.md#410-cap-hits-in-evaluation)). Three are hit during an attempt, `output_tokens`, `requests` and `wall_clock`; this field names them, as the attempt entry records it ([Run records, section 2.4](RUN_RECORDS.md#24-attempt-entries)), and is otherwise absent. Two are checked before an attempt starts, `input_tokens` and `attempts`; a hit stops the step without an attempt, and the `cap_hit` value of the run's `run_end` names it (section 10.2) | Attempt entry (run log) | Stage 1 |
| `input_above_cap` | Evaluation profile only: true when the provider reported more input tokens for a forwarded request than the frozen input cap ([Run records, section 4.10](RUN_RECORDS.md#410-cap-hits-in-evaluation)); otherwise absent. Proposed: the outcome stands, because the input has already been sent, and the evaluation reports the flag | Attempt entry (run log) | Stage 1 |
| `validation` | The format check's result: `passed`; the class it gave, `not_json` or `not_in_format` ([Handoffs, section 2.2](HANDOFFS.md#22-format-check-content-checks-and-technical-failures)), or `failure_form` for the agent's failure form; or `not_run` when no candidate output reached the format check, for example after class `truncated` or `crashed` (the attempt entry then has no `candidate_sha256`; [Run records, section 2.4](RUN_RECORDS.md#24-attempt-entries)); and the number of content-check findings by kind ([Handoffs, section 2.2](HANDOFFS.md#22-format-check-content-checks-and-technical-failures)), for the inquiry agent the content checks of section 4.5; absent when the attempt has no attempt result, because no request was forwarded (Handoffs 2.13) | Attempt result; attempt entry (`content_findings`) | Stage 1 |
| `unknown_tool_calls` | Tool calls refused because no tool is offered, counted (Handoffs 2.13); zero for an attempt without an attempt result, since no request was forwarded and so no model answer could ask for a tool | Attempt entry (`attempt_ended`) | Stage 1 |
| `question_screen_hits` | Inquiry agent only: hits of the question screen, recorded and counted (D23 A; [Handoffs, section 2.9](HANDOFFS.md#29-question-round)) | Run log | Stage 1 |
| `requests` | The attempt's forwarded requests, in total and by class (first, retry, continuation), and its refused requests, as the attempt entry takes them from the request log ([Run records, section 2.4](RUN_RECORDS.md#24-attempt-entries)); refused requests that fit no class as `unclassifiable`, counted among the refused ([Run records, section 2.4](RUN_RECORDS.md#24-attempt-entries)) | Attempt entry (request log) | Stage 1 |
| `usage`, `usage_unknown` | The attempt's token totals over its forwarded requests, as the attempt entry takes them from the request log ([Run records, section 2.4](RUN_RECORDS.md#24-attempt-entries)); `usage_unknown` names the usage categories that are unknown or incomplete on any request, and on how many requests ([Run records, section 4.4](RUN_RECORDS.md#44-unknown-usage)). A count that the provider reported is kept even when it is incomplete, as a provisional count with its category flagged, and is never presented as a complete total; a missing count is flagged and never written as zero | Attempt entry (request log) | Stage 1 |
| `served_model` | The served model that the provider reported, or that none was reported; a value other than the route's model is flagged (section 10.2) | Attempt entry (request log) | Stage 1 |
| `started_at`, `ended_at` | The attempt's start and end: the container's start and end as the `attempt_ended` entry records them (`container_started_at`, `container_ended_at`; [Run records, section 2.4](RUN_RECORDS.md#24-attempt-entries)) | Attempt entry (`attempt_ended`) | Stage 1 |
| `runner_started_at`, `runner_ended_at` | The runner's own times (`started_at`, `ended_at` in Handoffs 2.13); absent when the attempt has no attempt result | Attempt result | Stage 1 |

Every attempt whose container started has `attempt_started` and `attempt_ended` entries, but an attempt result only when at least one request was forwarded ([Handoffs, section 2.13](HANDOFFS.md#213-attempt-result-and-technical-failure)). So the fields above are copied from the attempt entries wherever these hold them, and a field that only the attempt result holds is absent when there is none.

### 10.4 How runs and batches end

**Stage:** Stage 1.

A pipeline run is suspended after a technical failure ([Workflow, section 4.4](WORKFLOW.md#44-technical-failures)); an evaluation run (here: one run of section 10.1) counts and reports it instead ([Workflow, section 1.4](WORKFLOW.md#14-how-evaluation-runs-use-the-workflow)). Proposed handling in evaluation:

| What happens | The run | The batch | Stage |
|---|---|---|---|
| A forwarded attempt (at least one request forwarded; [Workflow, section 1.2](WORKFLOW.md#12-terms)) fails with class `not_json`, `not_in_format`, `truncated` or `crashed`, including a container-limit hit, a cut stream that no repeat of the same body followed and a stop at the wall-clock guard, which under the evaluation profile holds the frozen wall-clock cap (D18 A; [Runtime, section 13.2](RUNTIME.md#132-native-result-classification), rows 3 and 4) | One technical re-run (D14 A; [Roles, section 7.7](ROLES.md#77-checking-an-output-and-the-technical-re-run)) | Goes on | Stage 1 |
| The re-run fails as well, or an attempt ends with class `failure_form` | Ends as `technical_failure`; counted and reported by class (section 4.6) | Goes on | Stage 1 |
| A frozen evaluation cap is hit (D12 A): during an attempt (output tokens, requests, wall-clock time), or before one starts (the input cap on the packet, attempts per pipeline stage) | A technical failure, counted as a cap hit. A hit without a technical re-run, or whose re-run also fails, ends the run as `technical_failure`. A response at the frozen `max_tokens` is class `truncated`, and a stop at the frozen wall-clock cap class `crashed`, each with the one technical re-run (row 1). A request-cap hit has no class: outcome `technical_failure`, code `cap_hit`, no technical re-run; this, and the handling of a stop before an attempt (code `cap_hit`, no attempt and no try), are set in [Run records, section 4.10](RUN_RECORDS.md#410-cap-hits-in-evaluation). The cap is named by the attempt's `cap_hit` field for a hit during an attempt (section 10.3), and by the `cap_hit` value of the run's `run_end` for a hit before one (section 10.2). Cap hits are reported under operational completion and are not scored as wrong values (section 4.7); how they count towards acceptance is part of the open Q4.5 | Goes on | Stage 1 |
| Under the development profile, the request guard refuses a request (gateway rule 8; D19 A) | The attempt ends as `technical_failure`, code `runaway_guard`, with no re-run ([Runtime, section 12.3](RUNTIME.md#123-limits)); the run ends as `technical_failure` | Goes on | Stage 1 |
| Under the development profile, a further attempt would exceed the guard on attempts per pipeline stage (D19 A) | No further attempt starts (code `runaway_guard`; [Runtime, section 12.3](RUNTIME.md#123-limits)); the run ends as `technical_failure` | Goes on | Stage 1 |
| A packet does not fit the route's context length (`packet_too_large`) | `not_run` in that condition; counted, and the item is reported apart from the paired comparison of the two conditions (Q4.4). This holds under the evaluation profile too, because the context-length check comes first ([Run records, section 4.10](RUN_RECORDS.md#410-cap-hits-in-evaluation), row Input tokens): only a packet that fits the context length but exceeds the frozen input cap is a cap hit (row 3), not `not_run` | Goes on | Stage 1 |
| A software step cannot finish or fails its self-check ([Handoffs, section 2.2](HANDOFFS.md#22-format-check-content-checks-and-technical-failures); [Workflow, section 4.4.1](WORKFLOW.md#441-what-counts-as-a-technical-failure)): the assembly step in mode B, or the deterministic verifier | Ends as `technical_failure`, with the software step named | Stops, because a failing software step is a defect to fix before results are compared, not a property of the item | Stage 1 |
| An attempt is void: `route_refused`, `canary_hit`, a start-up self-check repeated after the turn that fails (`startup_check_failed`), an unexplained monitor record (`containment_hit`, D22 A), or incomplete monitoring evidence (`monitor_incomplete`, AD-D06) | `stopped`; nothing the attempt returned is used, and it uses no try (D28 A; [Workflow, section 4.4.2](WORKFLOW.md#442-the-one-technical-re-run), clarification 4; [Runtime, section 13.2](RUNTIME.md#132-native-result-classification), row 1) | Stops. After `canary_hit`, or a `packet_check_failed` caused by a canary, no result of the batch is reported until Tillman Heisner has reviewed how the canary got there. After `containment_hit`, no attempt under the same runtime manifest is admitted, in any batch or run, until the containment suite passes again (D27 B; [Containment, section 12.4](CONTAINMENT.md#124-the-admission-check)). After `monitor_incomplete`, D27 B does not apply, but no attempt is admitted on the same execution environment until a fix is recorded and its monitors pass a readiness check; the void attempt's requests, usage and time stay counted ([Containment, section 12.4](CONTAINMENT.md#124-the-admission-check)) | Stage 1 |
| No usable attempt can start: any other check before the first forwarded request that suspends a pipeline run ([Workflow, section 4.4.1](WORKFLOW.md#441-what-counts-as-a-technical-failure)), that is, every such check except the two that rows above handle: the attempts-per-stage guard under the development profile and `packet_too_large`. Among them: `not_admitted`; a failed start-up self-check before the turn (`startup_check_failed`) or a model gateway that cannot be reached; `packet_check_failed`; a changed checksum of an input, a frozen file (also one that the workflow controller would hand to the deterministic verifier, which then does not run), an example file (section 3.5, rule 2) or, in mode B, an earlier output of the run (section 3.6, Check), recorded as the `input_check` result `checksum_mismatch` ([Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries)); a file placed in a packet that was read from outside the input folder, the example store and the run's own folder (section 3.6, Check), recorded as the `input_check` result `wrong_folder`; a changed checksum of the pinned schema file, recorded as the `schema_check` result `checksum_mismatch` ([Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries)); a refusal by safe XML parsing (`xml_refused`) or of a home folder that is not empty (`home_not_empty`); monitors that are not ready before the container starts (`monitor_incomplete`) ([Roles, section 8.7](ROLES.md#87-denial-and-failure-codes); [Run records, section 2.8](RUN_RECORDS.md#28-run-log-codes)); an attempt whose container started but which ended before any request was forwarded ([Runtime, section 13.2](RUNTIME.md#132-native-result-classification), attempts with no forwarded request); a STALE or FAILED containment report (section 7.1, rule 8) | `stopped` | Stops | Stage 1 |

**After a batch stops** (proposed). The cause is fixed, and the fix is recorded by the batch log's `fix` entry (section 10.1), as [Workflow, section 4.4.4](WORKFLOW.md#444-resume) asks before any resume. A stopped batch is not resumed: its completed runs keep their records, and the runs it did not complete run in a new batch once admission passes again; that batch's record names the stopped batch (`follows_batch`, section 10.1). Results are compared between conditions only within one runtime manifest, and score reports group them by batch.

### 10.5 First-try and final results

**Stage:** Stage 1.

D14 A: re-runs are counted, and evaluation reports first-try and final results separately ([Handoffs, section 2.13](HANDOFFS.md#213-attempt-result-and-technical-failure); [Workflow, section 4.4.2](WORKFLOW.md#442-the-one-technical-re-run)). Proposed reading:
- **Final result:** what the run produced with its technical re-runs. Each agent step's last attempt with outcome `output` is scored as section 4 sets out; a step whose re-run also failed is a technical failure.
- **First-try result:** the same run read as if no re-run were allowed. A step whose first try failed is a technical failure in this view. In mode B the first-try view ends at that step, and later steps are not scored in it. For an extraction in parts ([Handoffs, section 4.3](HANDOFFS.md#43-extraction-in-parts-contingency)), the step's first try fails if any part's first try failed.
- **One set of attempts.** Both views come from the same attempts; no run is repeated to get them.
- **Reported side by side**, per item, condition and repetition, with the number of re-runs per agent and failure class. Each diagnostic view of section 4.7 is given for both results; where a mode B result ends at a failed step, the extraction errors that no later step judged are counted under operational completion, not as residual unflagged errors (section 2.2).
- **Void attempts**, attempts whose start-up self-check failed before the turn, and attempts with no forwarded request are scored in neither result; they are reported under operational completion (section 4.7) and listed as section 10.7, item 4, sets out (section 10.4).

### 10.6 Usage and budget profiles

**Stage:** Stage 1.

- **Usage** comes from the model gateway's request log ([Runtime, section 11.3](RUNTIME.md#113-the-request-log)): requests by class, and tokens as the provider reports them. Hermes's own counters are diagnostics only. The request log's fields are in [Run records, section 2.5](RUN_RECORDS.md#25-the-request-log), and its retention in [Run records, section 2.11](RUN_RECORDS.md#211-retention).
- **Unknown usage.** Where a forwarded request has no usage or only part of it, for example a cut stream that ended before its usage was reported, or a response that never arrived, the request and the attempt carry the `usage_unknown` flag ([Run records, section 4.4](RUN_RECORDS.md#44-unknown-usage)), and every total that includes them carries it too. A count the provider did report, for example 100 output tokens of a cut stream, is kept as a provisional count with its category flagged; it is never presented as the complete total. A missing count is never written as zero. The score report flags such runs and marks their provisional counts. Requests with unknown or incomplete usage, provisional counts included, are left out of the token maxima only and never calibrate a token cap; the maxima of requests, wall time and attempts still include their attempts, so that an attempt that ended in a cut stream still counts there ([Run records, section 4.4](RUN_RECORDS.md#44-unknown-usage), rule 3).
- **Development profile** (D12 A), as [Run records, section 4.1](RUN_RECORDS.md#41-budget-profiles) sets it out: no token caps; `max_tokens` is the route's documented maximum, passed explicitly; the provisional runaway guards of D19 A, marked not calibrated ([Runtime, section 12.3](RUNTIME.md#123-limits)); and the capability zeros, which are containment rules, not limits ([Containment, section 11](CONTAINMENT.md#11-capability-zeros)).
- **Frozen evaluation profile** (D12 A): the caps of the evaluation profile ([Run records, sections 4.1](RUN_RECORDS.md#41-budget-profiles) and [4.9](RUN_RECORDS.md#49-evaluation-caps)), among them the limits of the Evaluation column of [Runtime, section 12.3](RUNTIME.md#123-limits) and an input cap that packet preparation checks on the packet. They are set from the measurements of [Run records, section 4.8](RUN_RECORDS.md#48-measurement-plan), recorded by a ledger Decision and frozen before any test-set batch, and enforced as [Runtime, section 12.3](RUNTIME.md#123-limits) sets out. How the caps are computed, and the classes of cap hits, are set in [Run records, sections 4.9](RUN_RECORDS.md#49-evaluation-caps) and [4.10](RUN_RECORDS.md#410-cap-hits-in-evaluation), and are not repeated here.
- **Which batch uses which profile** (proposed). A test-set batch runs only under the frozen evaluation profile (section 7.1, rule 6). A measurement batch runs under the development profile, also after the freeze, so that no cap cuts what is measured ([Run records, section 4.8](RUN_RECORDS.md#48-measurement-plan), row Profile). Before the freeze, evaluation batches on development items run under the development profile. After the freeze, every evaluation batch runs under the evaluation profile, development items included, so that development and test results run under the same limits. Results under different profiles or profile versions are reported apart.
- **Which runs are measured.** The measured maxima from which the evaluation caps are set come only from the measurement runs that [Run records, section 4.8](RUN_RECORDS.md#48-measurement-plan) defines (row Runs). Scored development batches are measured like every run, but they do not count towards the maxima. Attempts of containment runs and of behaviour variants never count (section 11, rules 5 and 7).
- **Cap hits in scores.** A cap hit is counted as a technical failure, per cap and apart from other technical failures ([Run records, section 4.10](RUN_RECORDS.md#410-cap-hits-in-evaluation); section 10.4), under operational completion (section 4.7); how it counts towards acceptance is part of the open Q4.5.

### 10.7 What a score report names

**Stage:** Stage 1.

Proposed, in addition to section 4.1, rules 5 and 11. A score report names:
1. the version of this document, of each expected file (section 4.1, rule 5), of the input-set manifest, the item list, the example manifests and, where an item's input is an entry variant, the variant list, and of each prompt and reference text (section 6, rule 8);
2. for each batch, its batch record (section 10.1): the runtime manifest, the containment report and, where D24 A gives one, the ledger Result entry that records that report ([Containment, section 12.4](CONTAINMENT.md#124-the-admission-check)); the route and the model; the budget profile and its version; the canary status; the number of repetitions; and, from the batch log, the `fix` entry of a stopped batch and the `canary_review` entry, where there is one;
3. first-try and final results side by side (section 10.5);
4. technical failures by class and code (section 10.3, `failure_class`), cap hits per cap ([Run records, section 4.10](RUN_RECORDS.md#410-cap-hits-in-evaluation)), attempts flagged `input_above_cap` (section 10.3), void attempts, stopped batches, items not run in a condition, runs with unknown usage, with their provisional counts marked as such (section 10.6), and runs with a differing served model, which are listed for review and left out of scores until Tillman Heisner has reviewed them (section 11, rule 3);
5. development (tuning) results and test results apart (section 4.6), each from its own batches (section 7.1, rule 10): development results may be shown beside test results and compared with them, but are never pooled into a held-out score, with each test-set run marked as held out or, where its batch's tuning disclosure says that information from its entries informed the workflow, as not held out, together with what the disclosure says (sections 4.8 and 6, rule 9); and the scope of the results: the STRENDA DB Export XML entries of the input-set manifest, through the round-1 questions (section 1.1);
6. per agent and item, the input tokens and packet bytes of the zero-shot and the few-shot runs side by side, so that the extra tokens of the examples show (section 3.5, Shared material and examples). The conditions are not claimed to have equal prompt length, and no cost is given, because Stage 1 counts tokens and requests only and has no approved tariff (section 12, row Spending limit);
7. the three diagnostic views of section 4.7, separately and for both results, with counts grouped by entry and publication group, and no overall score; in mode B, the residual unflagged errors with the deterministic-only and agent catches (section 2.2);
8. for a test-set report, the evaluation-plan version that its batches referenced, with its continuation criteria (sections 4.7 and 4.8). A report claims no measured time savings, and zero observed errors are described as evidence about this benchmark only.

A score report carries a canary if canaries are adopted (section 5.3, rule 5).

### 10.8 Derived schema files (proposed)

**Stage:** Stage 1.

Under D8 A, derived JSON Schema files for the formats of this version are in [design/specs](specs/README.md#the-files), each headed "Derived from design/EVALUATION_INTERFACES.md 1.2 (Draft); the document wins", with the `$id` `urn:ariadne:design:<name>:v1.2`, and listed in that README's table of files. Version 1.3 adds the code `monitor_incomplete` (AD-D06) to the code lists of `evaluation-run-record.schema.json` and `evaluation-batch-record.schema.json`, which are derived again and carry `v1.3`; the other files keep the label of version 1.2 until they are next derived (D29 A). Version 1.4 adds `evaluation_plan` and `tuning_disclosure` to `evaluation-batch-record.schema.json`, which is derived again and carries `v1.4`, and adds the file `evaluation-plan.schema.json` (section 4.8). Version 1.5 adds rule 10 to the rule numbers of `evaluation-batch-record.schema.json`, which is derived again and carries `v1.5`. As that README asks, each file stands alone and refers to no other file; key names that this document does not give are marked "Proposed name" there.

| File | Derived from | Stage |
|---|---|---|
| `evaluation-run-record.schema.json`, `evaluation-batch-record.schema.json` | Sections 10.1 to 10.4 | Stage 1 |
| `evaluation-plan.schema.json` | Section 4.8 | Stage 1 |
| `evaluation-packet-manifest.schema.json`: the `packet_manifest` run-log entry of a packet of an evaluation or measurement batch, with the fields of [Handoffs, section 2.4](HANDOFFS.md#24-input-packets), under proposed key names where no document gives one, and the fields that section 3.6 adds; its `$defs/packet_manifest_part` and `$defs/evaluation_packet_part` are identical to those of `run-log-entry.schema.json`, the packet manifest's run-log form | Section 3.6; [Handoffs, section 2.4](HANDOFFS.md#24-input-packets); [Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries) | Stage 1 |
| `input-set-manifest.schema.json`, `variant-list.schema.json`, `example-manifest.schema.json`, `item-list.schema.json` | Section 3 (introduction: list-level fields and checksums) and sections 3.1 to 3.4 | Stage 1 |

The expected-side files already in design/specs follow section 4 of version 1.0. Version 1.1 changed no expected-side format. Version 1.2 changes three of them for C05: `expected-issue-list.schema.json`, `expected-judgments-and-issues.schema.json` and `inquiry-expectations.schema.json` carry the required `mode`, with a branch for mode A rows keyed by frozen issue id, kind and pointers and one for mode B rows keyed by (source anchor, field, kind) (section 4.1, rule 12; the expected issue list allows `A` only); these three name version 1.2. The other expected-side files keep their 1.0 label. All of them are derived again from the frozen version once Tillman Heisner accepts, changes or replaces each format (section 9, item 1). Their `sha256` definition accepts either letter case; it takes the lowercase form of section 3 only when they are derived again from the frozen version, and the change of version 1.2 leaves it as it is. Two corrections to `inquiry-expectations.schema.json` were made in phase P7: `must_not_ask` means issue ids of the item's frozen report (section 4.5), not ids in the packet, because those issues never reach the packet; and its `$comment` states the report filter as settled ([Handoffs, section 2.4](HANDOFFS.md#24-input-packets); section 3.5) instead of as a condition.

## 11. Containment runs and evaluation runs

**Stage:** Stage 1.

The containment suite drives the same workflow controller, launcher, runner and model gateway as evaluation, and its evaluation-separation tests ES-01 to ES-03 run evaluation-shaped runs of modes A and B on development items ([Containment, section 9](CONTAINMENT.md#9-evaluation-separation-test-es-01-to-es-03)). Its attempts call only the scripted stub model ([Containment, section 2.7](CONTAINMENT.md#27-containment-runs-and-real-runs)). They test containment, never an agent, so they must never be counted or scored as evaluation, and evaluation files may reach a containment run only as far as those tests need. Proposed rules:

| # | Rule | Stage |
|---|---|---|
| 1 | **Told apart by its label, confirmed by the gateway.** The workflow controller treats a run as a containment run only when the configuration that starts it labels it `run_kind: containment` and the model gateway confirms that its upstream is the stub model; a run whose label and the gateway's answer disagree is handled as [Containment, section 12.4](CONTAINMENT.md#124-the-admission-check) sets out. It then writes no evaluation run record and nothing into the evaluation folders of section 6, and the run log carries that label on every attempt (`run_kind: containment`, [Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries)), kept with the suite run's own records outside `evaluation/runs/` ([Run records, section 2.2](RUN_RECORDS.md#22-where-it-is-kept)). | Stage 1 |
| 2 | **Evaluation only on the recorded route.** A batch starts only when the gateway confirms that its upstream is the recorded route (section 7.1, rule 7); the test-only gateway settings and launcher variants never apply to an evaluation attempt (D21 A; [Containment, section 2.7](CONTAINMENT.md#27-containment-runs-and-real-runs)). | Stage 1 |
| 3 | **The scorer reads only evaluation run records.** It refuses, and lists, any record that names no containment report (except a mode A run of the deterministic verifier), any record of a measurement run (`kind: measurement`, section 10.2), and any attempt labelled a containment-run or behaviour-variant attempt. It lists runs with a differing served model (section 10.2) for review and leaves them out of scores until Tillman Heisner has reviewed them. | Stage 1 |
| 4 | **The suite's copy of the expected folder.** The test copy that ES-01 to ES-03 use holds only files of development items, or synthetic files of the same shape, with the suite's own canaries. Any evaluation canary in a copied file is replaced by a suite canary, so that no evaluation canary leaves the expected folder. The copy is never kept in the evaluation folders, and no expected file of a test item is ever copied out of the expected folder. [Containment, sections 2.2](CONTAINMENT.md#22-components) and [12.2](CONTAINMENT.md#122-the-runtime-manifest) keep the test copy in the fixture store and bind it as a fixture. | Stage 1 |
| 5 | **Not counted.** Containment-run attempts count towards no evaluation number: not towards repetitions, first-try or final results or technical failures, and not towards the measured maxima from which the evaluation caps are set, which come only from the measurement runs that [Run records, section 4.8](RUN_RECORDS.md#48-measurement-plan) defines (section 10.6). | Stage 1 |
| 6 | **Canaries kept apart.** The suite's canaries are separate strings from the evaluation canaries, if those are adopted (section 5.3). An evaluation canary found in a containment run's evidence is reported to Tillman Heisner as a separation incident, because it means that an expected file left the expected folder. | Stage 1 |
| 7 | **Behaviour variants.** The behaviour variants of the prompt-injection tests call the recorded route under a VERIFIED report ([Containment, sections 7.5 and 12.4](CONTAINMENT.md#75-the-behaviour-variant)), but they are not evaluation runs. Their inputs come from the suite's fixture store, never from the input-set manifest (section 3.1), and the workflow controller labels their attempts as behaviour-variant attempts in the run log (`run_kind: behaviour_variant`, [Run records, section 2.3](RUN_RECORDS.md#23-run-log-entries)), from the configuration that starts them, never from model text. Their runs are kept outside `evaluation/runs/` ([Run records, section 2.2](RUN_RECORDS.md#22-where-it-is-kept)). They are never scored and never used for the cap measurements. Their fixture inputs are admitted as [Containment, section 12.4](CONTAINMENT.md#124-the-admission-check) and [Runtime, section 12.2](RUNTIME.md#122-admission-before-each-attempt) set out. Instruction text as an evaluation item is family E7 or I6 (section 5.1), scored like any other item. | Stage 1 |
| 8 | **One at a time.** A containment run and an evaluation batch never run at once ([Workflow, section 1.3](WORKFLOW.md#13-ground-rules), rule 2). After any containment run, the next attempt's admission checks the report again (section 7.1, rule 8). | Stage 1 |

## 12. Stage 2 tables

**Stage:** Stage 2.

Compact tables. Moving any item into Stage 1 needs a new Decision in the ledger ([stage legend](PACKAGE_ADOPTION.md#41-stage-legend)). Items that [Issue format 11](../ISSUE_FORMAT.md#11-deliberately-left-out) lists as "Stage 2, if ever" are proposals, not commitments.

| Item | Stage 2 proposal | Stage 1 counterpart | Stage |
|---|---|---|---|
| Mode C | Later rounds with answers stored in advance, replayed through answer application and re-checks; each stored answer records where it comes from (section 2.3) | Evaluation stops after round 1; software tests with stored fixtures are not mode C (section 2) | Stage 2 |
| Answer-item count and override rate | Measured in mode C ([Issue format, notes 6](../ISSUE_FORMAT.md#notes-for-the-evaluation-datasets-not-part-of-the-format)) | The question count only | Stage 2 |
| Packets with read tools | If measured packets do not fit (D6 A), the packet names the input and the extraction and verification agents read slices through the read tools ([Roles, section 8.8](ROLES.md#88-stage-2-read-tools); [Handoffs, section 7.10](HANDOFFS.md#710-other-stage-2-handoffs)); the packet manifest then lists every read with its span, and the run record counts the source bytes read and returned per attempt | The whole input in the packet (section 3.5) | Stage 2 |
| Researcher data | Inputs and examples from researcher data only with the data owner's admission of the source and of the model route ([Open questions, Q6](../OPEN_QUESTIONS.md#q6---which-researcher-workflows-and-data-may-be-used); [Handoffs, section 7.8](HANDOFFS.md#78-admission-contracts); [Roles, section 7.8](ROLES.md#78-stage-2-additions)) | Public STRENDA DB entries in the input-set manifest (section 3.1) | Stage 2 |
| Several model routes | Comparisons across routes, with one reviewed prompt version per route and the route as a reported factor; needs a new ledger Decision ([Runtime, section 13.6](RUNTIME.md#136-upgrade-policy)) | One route for all three agents (D11 A1) | Stage 2 |
| Budget reservations | Before each request, the worst case is reserved in every account it touches (shared group, record lineage, agent or software service) and settled from the provider's proven usage; usage above the reservation, or unknown, stays held ([Run records, sections 5.1](RUN_RECORDS.md#51-reserve-settle-and-recover) and [5.2](RUN_RECORDS.md#52-resource-events-reservations-accounts-vectors-and-proofs)) | Usage measured; development guards; frozen evaluation caps (section 10.6) | Stage 2 |
| Spending limit | A spend ceiling per group and per record, only once an approved tariff covers every billed category ([Run records, section 5.7](RUN_RECORDS.md#57-spend-ceiling)) | Tokens and requests only; no money limit | Stage 2 |
| Unknown outcomes | A request whose outcome at the provider is unknown keeps its full reservation, or is charged at the worst case, until the provider's authoritative record settles it ([Run records, section 5.4](RUN_RECORDS.md#54-unknown-outcomes-and-refunds)) | Usage flagged as unknown, never counted as zero (section 10.6) | Stage 2 |
| Concurrency | Several attempts at once, counted in seats, with limits per record and per group ([Run records, section 5.6](RUN_RECORDS.md#56-concurrency-limits)) | One machine step at a time ([Workflow, section 1.3](WORKFLOW.md#13-ground-rules), rule 2; section 11, rule 8) | Stage 2 |
| Checksums inside record files | If ever: record files carry typed references to stored files (checksum, media type and size), and a provenance manifest ([Run records, section 3.8](RUN_RECORDS.md#38-provenance-manifest)) ties every score to its inputs | Record files carry no checksum; checksums sit in the evaluation dataset's lists and in the run log, which includes `binding.json`, evaluation run records and batch records (sections 3, 3.6 and 10; [Run records, sections 1.2](RUN_RECORDS.md#12-terms) and [2.9](RUN_RECORDS.md#29-checksums-d13-a); D13 A) | Stage 2, if ever ([Issue format 11](../ISSUE_FORMAT.md#11-deliberately-left-out)) |
| Idempotent commands | If ever: each command carries an idempotency key, and a repeat with the same key returns the original receipt with no new effect ([Run records, section 3.6](RUN_RECORDS.md#36-command-receipts-de-duplication-and-replay)) | Every run record, batch record and stored file is written once by software ([Run records, section 2.10](RUN_RECORDS.md#210-write-once-and-append-only-rules)) | Stage 2, if ever ([Issue format 11](../ISSUE_FORMAT.md#11-deliberately-left-out)) |
| Raters | A verified identity for each wording rater ([Open questions, Q7](../OPEN_QUESTIONS.md#q7---how-will-researchers-review-the-results)) | The rater named on the rating sheet (section 4.5) | Stage 2 |

## 13. Register mapping note

**Stage:** Stage 1 and 2.

This is the only place in the document that names package identifiers. Their dispositions are in the [register, section 6](PACKAGE_ADOPTION.md#6-coverage-register) and its [conflict register](PACKAGE_ADOPTION.md#7-conflict-register). The table shows where this document carries each row that targets it, and where it uses package ideas whose rows target Run records; their dispositions are in the register and in [Run records, section 7](RUN_RECORDS.md#7-register-mapping-note).

| Register rows | Covered in | Stage |
|---|---|---|
| `file:examples/` | Section 5 (introduction): no fixture is copied or loaded; its rejection fixtures suggested families here and containment tests in [Containment](CONTAINMENT.md), and those on `/version`, the missing-field registry and the gap ban are superseded (conflicts C-01, C-02 and C-23). Section 3.3: never an example | Stage 1 |
| `REQ-13`, `INV-13` | Sections 3.3 (manifest and prompt checks), 3.5 and 3.6 (packets from the input side only), 5.3 (marker strings: always the suite's own canaries in ES-01 to ES-03; evaluation canaries if adopted), 6 (separate folders, separate agents, a fresh container per attempt) and 11; tested by ES-01 to ES-03 ([Containment, section 9](CONTAINMENT.md#9-evaluation-separation-test-es-01-to-es-03)) | Stage 1 |
| `REQ-POL-03` | Sections 3.1, 3.2 and 3.5: only inputs of the input-set manifest and their variants; the deterministic verifier reads the input only for citations (sections 2.1 and 3.5). Data-owner admission: section 12 | Stage 1 and 2 |
| `SC-04` | Families E8 and S2 (sections 5.1 and 5.2): free text gives another temperature than the structured value; the structured value is expected, and a `source_conflict` from the verification agent | Stage 1 |
| `SC-08` | Family V1 (section 5.1): a citation that passes the check at a node that states something else; the verification agent's `wrong_value` (conflict C-03) | Stage 1 |
| Conflict C-30 | Modes, packets, expected-side proposals and run records: sections 2, 3.5, 3.6, 4 and 10 (D9 A) | Stage 1 |
| Conflicts C-11, C-29 and C-35 | Rounds: evaluation stops after round 1 (section 2). Budgets: section 10.6, with profiles, measurements and caps in [Run records, section 4](RUN_RECORDS.md#4-budgets-stage-1). Repair runs: the one technical re-run, and first-try and final results (sections 4.6, 10.4 and 10.5; D14 A) | Stage 1 |
| Rows that target Run records: `budget_specification.yaml#rights_alignment` (attempts and requests counted apart), `budget_specification.yaml#bounded_loops` (the one technical re-run and the guards) | Sections 10.3 to 10.5 | Stage 1 |
| Rows that target Run records: `BudgetEvent` (the per-request usage record of the request log) | Sections 10.3 and 10.6 | Stage 1 |
| Rows that target Run records: `budget_specification.yaml#configuration_identity` (checksums of prompts, example manifests and packet manifests), `budget_specification.yaml#token_semantics` and `POL-C10` (unknown usage is never zero), `H0` (checksums of the original inputs), `ResourceVector` (usage per attempt), `StageFailure` (failure records), `budget_specification.yaml#time_and_leases` (times and the wall-clock limit), `budget_specification.yaml#source_byte_semantics` (source bytes delivered per packet; read tools in Stage 2), `budget_specification.yaml#concurrency_scope` (one at a time), `ArtifactRef` (file references with checksums in the run log) | Stage 1 parts: sections 3, 3.6, 10.2 to 10.6 and section 11, rule 8. Stage 2 parts: section 12 (budget reservations, packets with read tools, concurrency, checksums inside record files) | Stage 1 and 2 |
| Rows that target Run records: `H9` | Not used: evaluation stops before approval; the approval checksums are in [Run records, section 2.9](RUN_RECORDS.md#29-checksums-d13-a) | Stage 1 and 2 |
| Rows that target Run records: `review_contracts.yaml#resource_protocol`, `review_contracts.yaml#execution_seats`, `review_contracts.yaml#command_replay`, `budget_specification.yaml#shared_account_semantics`, `ResourceLedgerEvent`, `ResourceReservation`, `ResourceAccount`, `ResourceProof`, `ProvenanceManifest`, `H1` to `H8` | Not used by Stage 1 evaluation; section 12, rows Budget reservations, Unknown outcomes, Concurrency, Checksums inside record files and Idempotent commands | Stage 2 |
