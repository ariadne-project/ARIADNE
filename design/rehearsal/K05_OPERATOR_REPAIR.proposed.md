# K05 operator repair card — candidate proposal only

**Candidate-only guidance, not a change to the existing product rules, an instruction to a deployed system, or a new user decision.** I wrote this card for synthetic design rehearsal. It restates existing rules; all people, checks, approvals and permissions in the examples are fictional. No runtime exists here. I do not select monitoring durations, widen pipeline admission or alter the ledger.

## The short route

1. **Name the environment and latest hold.** “ENV-A is held by H-02; RUN-END-02 stays ended.” Another run on ENV-A does not bypass that hold.
2. **Record a named repair, not a release.** “I, SYN-OP-K05-02, restored the collector connection for H-02. No manifest item changed. Please check readiness.” The person supplies environment, outstanding hold, time and explanation. Software records the independent repair and software check result; the person never writes a release.
3. **Wait for software's fresh check.** Software checks M1–M3 and the collector without starting a container. A failed check leaves the environment held. A successful check is not permission to revive old output.
4. **Require software's release of that latest hold.** Reject pass22 for H-OLD if H-NEW arrived at24. Even a later check25 tied to the old repair cannot repair H-NEW: name H-NEW, repair it, and obtain another check/release.
5. **Check a fresh development attempt.** “For RUN-NEW-02-C05 / ATT-NEW-02-C05, recheck the current matching VERIFIED report, pins, recorded source and route, input/packet/schema prechecks and monitoring deadlines. Keep old output discarded.” With all gates satisfied in the synthetic example, the authored verdict is **admitted**, not “maybe development is allowed.” This is not an executed admission or started attempt. A manifest change instead requires a new matching VERIFIED report as well.
6. **Keep incurred usage, including uncertainty.** “REQ-CUT: 120 input, at least 8 output; combined at least 128. Output usage remains unknown for one request. I cannot assert under 100 output tokens.” Carry the unknown flag and affected-request count into every containing total; incomplete token counts do not calibrate token caps. A new run is separately identified and linked; it does not erase old usage. No money total or new Stage-1 spending policy follows.

For this operational-only example I ask **zero scientific questions**. A software readiness receipt is not an assay fact, scientific approval or data-owner permission. Missing readiness goes to the operational checker, not the scientist. This does not waive scientific review later or suppress an independently askable scientific issue.

## Developer rehearsal handoff (no runtime implementation)

| Authored packet | Expected contract reading |
|---|---|
| H-02@10 → named repair@12 → pass@13 → software release@14 → all gates freshly stipulated | New development attempt admitted in the authored fixture; old run ended and old output discarded |
| H-OLD@20 → repair@21 → pass@22 → H-NEW@24 | ENV-A still held |
| Same history, plus pass@25 still linked to H-OLD | Still held; later timestamp alone is insufficient |
| Named repair H-NEW@26 → pass@27 → software release@28 → fresh gates | New development attempt admitted in the authored fixture; no resurrection |
| Repair H-02 → failed check | No release; no new attempt admitted |
| Separate ENV-B with no holds, same provisional profile, all other gates satisfied | Development batch admitted in fixture; test batch/pipeline refused, including pipeline labelled development; ENV-A unaffected |

These are scriptable **static examples**, not an executable controller specification or completed MH suite. Validate isolated draft line shapes if useful, then inspect full chronology/references separately. A stale release can pass the single-line schema; do not turn shape success into a release decision. Do not use the old CSV text stand-in to claim current XML ingestion support. The source/pin/route gates in these examples are explicit fictional assumptions, not checked files or endpoint permissions.

## Authority and source pins

Line references below are to the immutable `baseline/` in the 2026-10-28 rehearsal; corresponding shared-candidate clauses were identical when I authored this proposal.

- **Decided repair route:** `design/CONTAINMENT.md` §12.4, lines 871–873; **specified, not implemented tests:** §5.4, lines 612, 616–618 (MH-08/09/10).
- **All admission checks remain independent:** `design/RUNTIME.md` §12.2, lines 820–828; additional prechecks `design/CONTAINMENT.md` §12.4, line 870.
- **Provisional uses / still-open development-labelled pipeline exception:** `design/CONTAINMENT.md` §12.4, line 866 and §5.4 line 620 (MH-12); `design/PACKAGE_ADOPTION.md` §4.4, lines 122–124. The exception is **open**, not a new decision here.
- **Preliminary-decided Stage 1 record protocol (derived serialization still draft):** `design/RUN_RECORDS.md` §2.7, line 314; accepted names do not accept all other proposed keys. Software alone writes the index. Example payloads are projections/isolated line-shape samples, not complete validated logs.
- **Preliminary-decided Stage 1 accounting rules (explicit proposals retained):** `design/RUN_RECORDS.md` §§4.3–4.4, lines 623–637. Proposed repeat-measurement mechanism in line 636 is not adopted here.
- **No operational inquiry detour:** `design/ROLES.md` §6.4, line 402; inquiry receives only askable issues and does not route.
- **Shape is not cross-file truth:** `design/specs/README.md`, lines 4, 13, 19–22, 96, 100. Documents prevail; run-record schemas are drafts.
- **Controlled current workpiece, varied files later:** `OPEN_QUESTIONS.md` Q1, lines 9–14. The future requirement stays first-class but is not implemented or supplied by present XPath.

This optional card adds no requirement, authority, approval, supported format or product behavior. The task-local `witnesses.json`, `events.jsonl`, `sourcehashes.json` and `affectedtests.json` retain the evidence and exposure qualifications.
