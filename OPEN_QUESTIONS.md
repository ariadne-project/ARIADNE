# Open questions

These questions must be resolved to move ARIADNE from concept to pilot. Detailed discussion and evidence should live in GitHub issues; resolved decisions should be recorded in the provenance ledger.

## Stage 1 - Establish the workflow

### Q1 - Which existing datasets should be used?

1. **Source:** public STRENDA DB entries, as Export XML files stored unchanged with download date and checksum.
2. **Selection:** 15 to 25 entries covering varied enzymes, kinetic parameters, units, compound roles, one or several datasets, and with or without methodology text.
3. **Split:** T9HQ4X and GNICYO form the development set; all others are test entries. Entries from one publication stay in one set.
4. **Expected records:** derived by fixed rules, plus hand-marked methodology facts (see Q4).

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

## Stage 2 - Apply it with researchers

### Q5 - Who will participate, and what should they gain?
Confirm the participating scientists and technical contributors, their roles and available effort, and what would make the workflow useful enough to use again.

### Q6 - Which researcher workflows and data may be used?
Select representative workflows and record the data owner's conditions for processing, access, model endpoints, storage, retention, sharing, and release.

### Q7 - How will researchers review the results?
Decide how users will inspect evidence, answer clarification questions, correct candidate records, and provide scientific approval.

## Decision to continue

### Q8 - What determines pilot success and continuation?
Agree how record quality, user experience, time saved, residual risk, maintenance responsibility, and the decision to expand beyond the pilot will be assessed.