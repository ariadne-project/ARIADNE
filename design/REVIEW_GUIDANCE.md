# Researcher review guidance — candidate proposal

**Status:** Proposed, non-normative rehearsal guidance. Not a new user decision, product interface, state, or implemented behavior. The existing scientific/approval rules and document precedence remain unchanged ([Workflow, opening status and precedence](WORKFLOW.md), baseline lines 4–5). Stage 1 remains the developmental STRENDA workpiece, not general input support ([Handoffs §2.3](HANDOFFS.md#23-input-file-record), baseline lines 139–149).

## Stop for now is not the same as ending this run

For a temporary break while a question remains unanswered, the existing **Awaiting answers** state has no deadline. A separately recorded withdrawal by a named person ends this run: **Withdrawn** has no outgoing transition. Withdrawal is an existing **design rule, not part of Issue format** ([Workflow §2](WORKFLOW.md#2-stage-1-states), baseline lines 91, 99; [§3.1](WORKFLOW.md#31-transition-table), line 176). This guidance recommends wording, not automatic interpretation of an ambiguous message or a new default transition.

When someone says “stop for now,” a useful receipt identifies what is already in the draft, which replies are only collected, what remains unknown, and whether the run is waiting or has actually been withdrawn. It need not ask another lab question or demand approval. Do not describe a withdrawn run as resumable.

### Example: known pH, required volume absent, temperature unit unknown

**SYNTHETIC scripted dialogue; not a software trace.** Start with an incomplete snapshot: Blank A pH absent; Blank cuvette volume absent; temperature number 298.15 present without a unit. The current round asks those three facts. For this illustration only, the pH and volume replies pass their answer checks; no accepted unit answer is submitted. The original statement about the unknown unit remains available for review, not a unit value.

**Scientist:** “Blank A was pH 7.0. The cuvette volume wasn't recorded and I can't recover it; don't use a typical volume. I can't identify the unit for 298.15. Stop for now—I want to come back, not end this run.”

**Example receipt:** “I have your pH 7.0 reply and your explanation that the Blank cuvette volume is unavailable. They are collected replies, not yet changes to the saved draft: the temperature unit question is still unanswered. I will leave this round waiting, without a deadline, and ask nothing further now. I will not guess a volume or Kelvin. Your existing partial draft, evidence and not-mapped report remain local review material alongside your replies. This is not final EnzymeML approval or permission to share. You can return to the outstanding question later; ending this run instead would be a separate withdrawal, not a resumable pause.”

All-or-nothing round preparation matters: every question needs an accepted answer before a working copy is prepared; omitted items stay open. A receipt must not claim that a newly supplied pH is already committed or has an applied evidence entry when it is only collected ([Issue format §5.2](../ISSUE_FORMAT.md#52-answer), baseline lines 282–283; [Workflow §4.2](WORKFLOW.md#42-applying-answers), lines 277–280).

A required volume declared unavailable still blocks and, once applied, is not asked again. A unit closes only with a value, not “not available.” After a check, an open askable unit takes priority over the not-approvable ending; the unavailable volume alone cannot bypass it ([Issue format §3](../ISSUE_FORMAT.md#3-field-roles), baseline line 58; [§5.4](../ISSUE_FORMAT.md#54-closure), lines 296–299; [Workflow §3.2](WORKFLOW.md#32-routing-after-a-check), lines 182–189).

## Useful partial work is not final approval

Stored snapshots, evidence, not-mapped reports and replies can support local review and later reconciliation; retention is not a promise of a new export, a resume transition, or external access ([Run records §2.1](RUN_RECORDS.md#21-what-is-kept-for-each-run), baseline lines 108–117; [§2.11](RUN_RECORDS.md#211-retention), lines 385–391). An uncommitted reply and its original are distinct from the snapshot and its evidence. Keep that distinction visible rather than filling gaps to make the result look complete.

Before scientific approval, present the actual current review material and the decision sought, not just an old approval utterance. The existing approval summary is a human-readable view, not a new value source or proof it was understood ([Handoffs §2.12](HANDOFFS.md#212-approval), baseline line 437). A synthetic fixture must show its **already supplied** review material, with its seeded-check limitations, or omit a redundant approval turn; that is fixture routing, not a new product field. Never borrow another case's complete volume or unit to repair an incomplete case.

Scientific approval has existing conditions; sharing still needs the data owner's separate approval. Neither a temporary break nor local retention grants either ([Issue format §7.2](../ISSUE_FORMAT.md#72-approval), baseline lines 386–403). No scientist approval or owner permission in this example is real.
