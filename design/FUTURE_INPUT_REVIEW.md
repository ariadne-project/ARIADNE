# Future input review: a source-to-question bridge

**Candidate proposal, 2026-10-29 — not adopted product behavior.** I propose this design-only future-input review path, not a Stage 1 change, parser specification, implementation or new user decision. Stage 1 remains the developmental STRENDA workpiece. Every example and all scientist/record-worker speech below are **synthetic**. No scientific approval, data-owner permission or numerical suitability follows from a review topic.

## 1. Why this small bridge

The same goal is to turn familiar scientific sources into understandable review and useful, honest progress. A source fact may be scientifically meaningful without a justified EnzymeML field: “both tubes stood exactly 75 s before substrate addition” must not become reaction-time observations merely to obtain a pointer. A source-only experiment label may also be needed to distinguish two objects both called “Control.”

I propose a short **review topic**, kept separate from a native field issue. It lets a reviewed source region and its uncertainty reach a question or a retained note even when no target is known. It does not claim that the input can already be imported. “Review-ready” would mean ready for this discussion only, not admitted, validated, approval-ready or authorized for exchange.

This responds to verified future requirements F-K03-02/03, not a current lost-data bug. K03-02 already demonstrated successful disambiguation with enriched context. K07's empty downstream packets demonstrate a rehearsal stimulus gap; they do not show that the baseline lacks issue-registration ownership. [B2, B4, V1, V2]

## 2. Minimum information, not a new schema

A topic needs only:
- A local topic label and a plain-language **about** phrase that distinguishes the experiment or source claim.
- The **source member and representation**, with a retrievable **region** and the visible quotation or image-region description. Keep relevant headers, units, caption/footnote and identity context with it, not just an isolated number. Preserve the source member's readable, cropped, unreadable or unavailable status. For an unreadable member, identify the member/status only; do not invent a quote from its contents.
- The **uncertainty and next action**: a scientific choice, an association question, a request for evidence, or simply a retained note with mapping undecided.
- A **linked target only when known**. Name its owning artifact and target type. Link an existing registered native issue if one really exists. A source-only label is not a native object binding, and a review-draft row is not an EnzymeML pointer. When no justified target exists, leave the link absent and retain the topic.

These are content obligations for a proposed handoff, not a schema extension to the Stage 1 verification report or inquiry packet. Do not fabricate XPath paths, issue IDs, child indices or EnzymeML fields. The current verification report remains judgments plus added issues only. Do not recover context by forwarding the untrusted `cannot_use_packet` sentence. [B2–B5]

For example, this is sufficient as a **human-readable topic card**:

> PREP — E41 amber Control and E42 violet Control. Source: M1, assay-table.txt line 6, “Both tubes stood for exactly 75 s before substrate addition; this is preparation, not a sampled reaction time.” Retain as preparation. Target mapping: undecided. No scientific question needed.

A target-known example is deliberately qualified:

> PH — E41 amber Control at 25 deg C. M1 line 4 says 7.2; M2 line 2 says 7.8. Which reading describes the assay? Linked review target: review-draft.before.json, candidate_slices[0].pH. **This fixture target is a review-row link, not a native EnzymeML issue or permission to apply an answer.**

The packet includes the source inventory and reviewed draft/partial view. “No topics” does not mean all contents are accounted for or that the scientist approved anything. Topic accounting covers the inspected regions, not exhaustive source coverage. [B5]

## 3. Proposed producer and consumer responsibilities

| Boundary | Proposed responsibility | What is not delegated |
|---|---|---|
| Source material → source review | The source reviewer drafts topics from preserved members/representations. It records source association evidence separately from interpretation and marks unreadability/cropping. It retains the stated 75 s preparation even with no target. | No inferred contents of locked/cropped members; no file-name authority, new scientific truth or implicit permission. |
| Source review → discussion-ready view | The named record worker reviews that source-region references, experiment discriminators, uncertainty and any existing target association are justified. It records the reason if a topic is retained but not asked. A targetless topic is not rejected merely for being targetless. Ambiguous source-to-object associations remain explicit questions. | This review is not scientific record approval or owner admission. The worker does not silently decide whether two exports are revisions or separate experiments. |
| Discussion-ready view → inquiry | A future packet assembler, analogous to the existing controller, supplies only the reviewed topics, relevant source context, draft view and any earlier replies. It names this **future source-review mode** explicitly; it does not invoke the baseline inquiry contract with `issues: []` and call the result a product failure. | No separate new actual role, parser, runtime or automatic target creation is specified. Existing Stage 1 controller/registration ownership is not erased. [B2, V2] |
| Inquiry → scientist | Ask concise questions with supported names/discriminators and alternatives, including another value, “the question does not fit,” or “unsure.” Request missing evidence in ordinary words. Do not ask the scientist for XPath, schema fields, topic IDs or JSON. Retained source notes need not become questions. | Questions do not alter the record, settle source authority or imply approval. |
| Scientist reply → partial review | Retain the original claims and the reply as distinct evidence. Update the **review aid** only as explicitly scripted/recorded; keep unresolved topics and every member's status visible. If a native target is later established, its owning process must separately register/apply/check under its contract. | No automatic native answer application, issue closure, scientific approval, permission to share or numerical-use claim. [B6, B7] |

These responsibilities are my candidate design proposal for this future branch. They are not claimed to have already run or to be new decisions by the user. Admission/security mechanisms, actual source readers and cross-format locator profiles remain separate future work. Current Stage 1 source checks are unchanged. [B1, B8]

## 4. Concrete dialogue: same scientific goal, useful partial result

**Source fixture:** M1 is a readable text table; M2 a readable lab note. Both distinguish E41 amber Control at 25 deg C and E42 violet Control at 30 deg C as separate preparations. M3 is named `assay_final_v9.txt` but has only export ID export-6. M4 is a cropped scan-region stand-in. M5 is an unreadable-member marker with no scientific contents. All five text stand-ins remain retained; no native scan, workbook or instrument binary was decoded.

**Source reviewer → reviewed topics:**
- E41 table pH 7.2 conflicts with note pH 7.8; link the known review row only.
- E42 pH 8.1 is stated by the note; the table's blank pH is not a conflicting value.
- Preserve the 75 s preparation as a cited source note; native mapping undecided.
- Ask the relationship of export-6 to E42; matching conditions and `v9` do not establish it.
- Keep E43 cropped and the instrument member unreadable; request fuller/readable evidence without discarding M1–M3.

**Inquiry → scientist:** “For amber Control E41 at 25 deg C, should this review draft use pH 7.2 from the table or 7.8 from the lab note? You can give another value or say the question does not fit.”

**Scientist, synthetic:** “Use 7.8 in the review draft. I state that the earlier table entry was before recalibration. Keep both quotations and my explanation.”

**Inquiry → scientist:** “Is export-6 the violet Control E42 again, a different experiment, or are you unsure? The filename does not decide this.”

**Scientist, synthetic:** “I am unsure. Keep it unassociated; do not count it as another replicate or call it a revision.”

**Inquiry → scientist:** “Can you provide the full E43 scan, including the complete Km value, unit and assay conditions? If not, I will keep it incomplete.” Separately: “Can you supply a readable instrument export, or should I leave this attachment pending?”

**Scientist, synthetic:** “Not today. Keep E43 unresolved and the instrument attachment pending.”

**Partial review → scientist/reuser:** “E41 is proposed pH 7.8 on your statement; E42 remains candidate pH 8.1 on the note. The 75 s preparation is visible with mapping undecided. export-6 remains unassociated. E43 has no complete Km, unit or conditions; the instrument member has no readable contents. This is not an imported, checked or approved record. Would this source-linked partial help compare setup now, or do you need the complete record first?”

**Scientist/reuser, synthetic:** “It helps compare the two preparations. I cannot use E43 for a Km fit or count export-6 as another experiment. This is not approval of a final record or permission to share.”

This is an authored same-author dialogue, **not independent role-play, an implemented transition or measured usefulness**. Task-local `partial-review.md`/`.json` retain these concrete claims and limits; `counterexamples.json` contrasts target-required, name-only, filename-wins and crop-as-complete failures with the proposed transitions.

## 5. Limits and cheaper alternatives

**No change:** retain the honest current unsupported-input stop and local source notes. That is correct for current Stage 1; it does not demonstrate a future scientist-facing partial review.

**Simpler:** a named person can manually prepare one source-linked review note and the four questions above. No extra schema is needed. I use that as the first rehearsal vehicle; the topic obligations only make the source/uncertainty/target distinction reproducible across that handoff. If no source-only topic exists, use the ordinary native issue/question route rather than duplicating it.

**Not proposed:** Stage 1 heterogeneous admission, OCR/parsers, a new database or giant topic schema, exhaustive coverage checks, automatic experiment/revision arbitration, fragment approval, companion-schema implementation or exchange authorization. A cropped or unreadable member limits what can be said about that member, not whether independently supported readable material may be inspected. No partial view substitutes for whole-record scientific approval and separate owner sharing permission. Numerical suitability is a further question. [B5–B8]

## 6. Exact source and verification anchors

Paths/lines below refer to the immutable baseline or accepted verifier artifacts; hashes accompany the task proposal. Status is preserved, not upgraded by this document.

- **B1 — Stage 1 design-rule:** `baseline/design/HANDOFFS.md` §2.3, lines 139–149: one manifest-admitted public STRENDA entry, `strenda_export_xml`; attachments/parser profiles/several inputs deferred. The **decided** XPath locator definition is `baseline/ISSUE_FORMAT.md` §2, line 30; its citation check is §8.2, lines 440–453.
- **B2 — decided/design-rule respectively:** `baseline/ISSUE_FORMAT.md` §4.2, line 208: registration checks and human-review note route already exist. `baseline/design/HANDOFFS.md` §2.4, line 170: the controller supplies native issue context to inquiry. This proposal adds a future discussion envelope, not an allegation of missing current ownership.
- **B3 — Stage 1 design-rule:** `baseline/design/HANDOFFS.md` §2.8, lines 315–319: report contains judgments/added issues only. §2.13, line 483: failure-form sentence is untrusted, log-only and not forwarded.
- **B4 — decided:** `baseline/ISSUE_FORMAT.md` §4.1, lines 185–192: source conflicts, missed-value target requirement, no invented child indices. A source-only preparation note is not proof of an existing native field.
- **B5 — decided/design-rule respectively:** `baseline/ISSUE_FORMAT.md` §8.1, line 434: extraction drafts not-mapped entries, no mandatory issue link and no exhaustive mapped/not-mapped coverage check. `baseline/design/HANDOFFS.md` §2.14, lines 508–521: extraction ownership and existing target-specific report behavior.
- **B6 — decided:** `baseline/ISSUE_FORMAT.md` §6.2, lines 327–338: structural edits require a basis; a person's explanation alone is a statement, never source evidence; re-checks and approval remain required. This bridge does not execute those edits.
- **B7 — decided:** `baseline/ISSUE_FORMAT.md` §7.2, lines 383–403: approval conditions, later-change invalidation, separate owner sharing permission, approved deliverable and numerical-use limit. Final presentation already has an owner in the **design-rule** `baseline/design/WORKFLOW.md` §4.3, lines 300–305; this does not repair an observed missing final-stage producer.
- **B8 — future/design-rule, with precedence preserved:** `baseline/design/HANDOFFS.md` §7, lines 738–742; §7.3, lines 768–778; §7.10, lines 850–858: future member identities/locators/parser profiles, not current heterogeneous checking. `baseline/design/PACKAGE_ADOPTION.md` §3, lines 25–35 and §4.1, lines 44–54: ledger precedence and a new Decision for Stage 1 promotion. `baseline/README.md` lines 12–14 preserves the append-only ledger. `baseline/ARCHITECTURE.md` Status, line 5, and Principles, lines 35–40, bound the proposed human-centered, evidence-linked, standards-aware system.
- **V1 — accepted verification, not product authority:** `execution/tasks/V-K03/1/assessment.md` lines 35–49 and `findings.json`, entries F-K03-02 and F-K03-03: reviewed partial source notes and source-only disambiguation; K03-02 succeeded, and existing record context can sometimes suffice.
- **V2 — accepted verification, not product authority:** `execution/tasks/V-K07/1/assessment.md` lines 25–42 and 65–77; `findings.json`, F-K07-01/02: empty-stage fixture bridge and unreleased partial-use probe; neither a missing current producer nor demonstrated partial-use behavior.

## Discretionary design decisions
- I keep review topics separate from native issues so source evidence can be retained without fabricated targets or weakened registration.
- I reuse existing role responsibilities by analogy rather than proposing a new agent or parser, and choose a manually reviewed note as the simplest rehearsal vehicle.
- I preserve unknown experiment/revision relationships and incomplete members rather than choosing a filename winner or rejecting the whole bundle.
