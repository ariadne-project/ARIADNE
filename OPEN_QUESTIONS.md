# Open questions

These questions must be resolved to move ARIADNE from concept to pilot. Detailed discussion and evidence should live in GitHub issues; resolved decisions should be recorded in the provenance ledger.

## Stage 1 - Establish the workflow

### Q1 - Which existing datasets should be used?

1. **Source:** public STRENDA DB entries, as Export XML files stored unchanged with download date and checksum.
2. **Selection:** 15 to 25 entries covering varied enzymes, kinetic parameters, units, compound roles, one or several datasets, and with or without methodology text.
3. **Split:** T9HQ4X and GNICYO form the development set; all others are test entries. Entries from one publication stay in one set.
4. **Expected records:** derived by fixed rules, plus hand-marked methodology facts (see Q4).

Note: these entries are a controlled benchmark for developing a workflow that is intended later to take the varied files researchers use; Stage 1 results describe the workflow on these entries and do not show that it handles arbitrary files. No deterministic extraction comparator is required. The development entries are used for tuning; the test entries are held out for assessment, and an entry used repeatedly for tuning no longer counts as an untouched test ([ledger](README.md#2026-10-29---workflow-and-review-design-consolidated); [Evaluation interfaces, section 1.1](design/EVALUATION_INTERFACES.md#11-purpose)).

### Q2 - What must the EnzymeML records contain?

1. **Draft record:** structurally valid against the schema in Q3: defined fields only, correct types and values, every referenced ID present.
2. **Empty fields:** allowed only where the input lacks the information; each is raised as an issue.
3. **Approved record:** fully valid, with all required fields filled.
4. **Accompanying files:** an evidence file locating every filled value, and a not-mapped report of information EnzymeML cannot hold (for example a His-tag). Links between parameters, substrates, and datasets must be traceable.
5. **Values:** defined per input in the test datasets.

### Q3 - Which EnzymeML target should be tested?
EnzymeML V2.0 at enzymeml-specifications commit bf9321f (`specifications/v2.md`, `schemes/v2/enzymeml-v2.json`). Records declare version `2.0`.

### Q4 - How should extraction and verification be evaluated?

One dataset per agent, built from the Q1 entries. Expected values cite their XML location or a hand-marked methodology quote.

1. **Extraction:** fields scored as correct, wrong, correctly empty, invented, or missed. Variants with removed or changed values test that the agent reads the input.
2. **Verification:** records with planted defects, clean controls, and source conflicts. Issues are classed as confirmed, rejected, source conflict, or gap. The deterministic verifier checks only structure, units, and citations.
3. **Inquiry:** questions carry the issue IDs they address and are scored by topic coverage, unwanted questions, and question count. A person rates the wording.
4. **Zero-shot and few-shot:** same test items, with examples only from the development set. Agents keep separate prompts, never see expected outputs, and are tested alone and in sequence.
5. **Acceptance criteria:** not yet set. Proposed gates: no invented values, no unit errors, every filled value cited, every source conflict flagged.

Note: the proposed interfaces between the dataset builder, the workflow controller and the scorer, which leave this answer unchanged, are in [Evaluation interfaces](design/EVALUATION_INTERFACES.md).

Note: agent evaluation in Stage 1 stops after the first round of questions. Later tests of the whole record lifecycle with stored fixtures are software tests, not agent evaluation, scientific approval, a usability study or evidence of time saved ([ledger](README.md#2026-10-29---workflow-and-review-design-consolidated); [Evaluation interfaces, section 2](design/EVALUATION_INTERFACES.md#2-evaluation-modes)).

Note: results are reported in three separate views, integrity, usefulness and operational completion, not as one overall score, and are used to diagnose the workflow during development. Continuation criteria are to be set explicitly before held-out test results are inspected. No numerical thresholds and no general zero-error rule have been chosen, so item 5 stays open to that extent and its proposed gates remain proposals. Zero critical errors observed on these entries would be evidence about this benchmark, not proof that no such error can occur later ([ledger](README.md#2026-10-29---workflow-and-review-design-consolidated); [Evaluation interfaces, section 4.7](design/EVALUATION_INTERFACES.md#47-diagnostic-views-and-continuation-criteria)). Tillman Heisner sets and approves the criteria in a versioned evaluation plan that every held-out assessment must reference before it starts, and before each held-out assessment he records whether information from its test entries informed tuning; if it did, assessment on those entries is reported as not held out ([ledger](README.md#2026-10-29---workflow-and-review-design-consolidated); [ledger](README.md#2026-10-29---workflow-and-review-design-consolidated); [ledger](README.md#2026-10-29---workflow-and-review-design-consolidated); [Evaluation interfaces, section 4.8](design/EVALUATION_INTERFACES.md#48-evaluation-plan-and-tuning-disclosure)).

## Stage 2 - Apply it with researchers

### Q5 - Who will participate, and what should they gain?
Confirm the participating scientists and technical contributors, their roles and available effort, and what would make the workflow useful enough to use again.

### Q6 - Which researcher workflows and data may be used?
Select representative workflows and record the data owner's conditions for processing, access, model endpoints, storage, retention, sharing, and release.

Note: EnzymeML records name their creators with e-mail addresses, which are personal data released with every shared record; a functional address is allowed (see [Issue format](ISSUE_FORMAT.md#32-ask-req-fields)).

Note: admission of sources and model routes by the data owner is proposed for Stage 2 ([Roles, section 4.3](design/ROLES.md#43-data-owner); [Runtime, section 15](design/RUNTIME.md#15-stage-2)); Stage 1 uses public STRENDA DB entries ([Q1](#q1---which-existing-datasets-should-be-used)).

### Q7 - How will researchers review the results?
Decide how users will inspect evidence, answer clarification questions, correct candidate records, and provide scientific approval.

Note: the review interface (answer forms, evidence views, checked identities and several sign-offs) is proposed for Stage 2 ([Roles, section 4.4](design/ROLES.md#44-stage-2-additions); [Issue format 11](ISSUE_FORMAT.md#11-deliberately-left-out)); for Stage 1 the design proposes that the scientist answers and approves directly, or that another named person enters the scientist's answers and approval when they arrive by another route, such as e-mail, keeping the scientist as author and recording who entered them ([Handoffs, section 1.1](design/HANDOFFS.md#11-purpose)).

## Decision to continue

### Q8 - What determines pilot success and continuation?
Agree how record quality, user experience, time saved, residual risk, maintenance responsibility, and the decision to expand beyond the pilot will be assessed.

Note: for Stage 1, the criteria for continuing are to be set before held-out test results are inspected, informed by what development shows to be feasible and by what the stakeholders can tolerate; no thresholds have been chosen, and Stage 1 measures no time saved ([Q4](#q4---how-should-extraction-and-verification-be-evaluated); [ledger](README.md#2026-10-29---workflow-and-review-design-consolidated)). Tillman Heisner sets and approves these Stage 1 criteria under his interim Stage 1 authority, in a versioned evaluation plan. Meeting them would mean that the workflow is technically ready for proposing a bounded trial with researchers; it would not authorize the use of participants' data or effort, or any wider pilot or consortium step, which this question still has to settle ([ledger](README.md#2026-10-29---workflow-and-review-design-consolidated)).