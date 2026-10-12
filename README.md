# ARIADNE: Agentic Research Infrastructure for Auditable Data Normalization and Exchange

> Make the FAIR and scientifically trustworthy choice the easiest choice.

ARIADNE is a system designed to make FAIR data practices easier by helping researchers turn familiar scientific files into structured, evidence-linked records. Its proposed architecture would use EnzymeML for enzyme reaction and kinetics data and linked companion schemas for data outside EnzymeML's scope. Few-shot-guided extraction agents would propose records; deterministic validation, independent verifier agents, and human review would assess them before acceptance.

This repository currently serves as ARIADNE's concept and provenance ledger. Development is intended to begin with a small, co-designed ELEGANCE pilot; no scientific-data processing software is implemented yet.

See the proposed [Pilot](PILOT.md), [Architecture](ARCHITECTURE.md), and [Open questions](OPEN_QUESTIONS.md). To contribute, see [Contributing](CONTRIBUTING.md).


## Provenance ledger

Ledger entries are append-only and follow the [ledger entry template](CONTRIBUTING.md#ledger-entry-template).

### 2026-09-01 to 2026-09-04 - Kick-off motivation

**Type:** User-reported\
**Claim:** ELEGANCE kick-off discussions connected centralized data infrastructure, EnzymeML, FAIR principles, and agentic translation. The amount of specialist knowledge involved motivated an approach that would make these concepts easier for ELEGANCE researchers to use.\
**Evidence:** Participant recollection reported by Tillman Heisner.\
**Recorded by:** Tillman Heisner\
**Supersedes:** none

### 2026-09-07 - Repository licensing established

**Type:** Decision\
**Claim:** Documentation and ledger content are licensed under CC BY 4.0, while future source code is licensed under Apache-2.0. Data, third-party materials, and consortium intellectual-property arrangements are outside these defaults.\
**Evidence:** `LICENSE`; `LICENSE-CODE`; [License](README.md#license).\
**Recorded by:** Tillman Heisner\
**Supersedes:** none

### 2026-09-08 - Pilot direction proposed

**Type:** Proposal\
**Claim:** ARIADNE should begin with a two-stage, human-centered ELEGANCE pilot. Existing datasets would first establish and evaluate evidence-linked EnzymeML extraction, deterministic validation, and independent verification before the workflow is applied to data-owner-approved researcher workflows.\
**Evidence:** [Pilot](PILOT.md); [Architecture](ARCHITECTURE.md); [Open questions](OPEN_QUESTIONS.md).\
**Recorded by:** Tillman Heisner\
**Supersedes:** none

### 2026-10-12 - Interim decision authority for Stage 1

**Type:** User-reported\
**Claim:** Tillman Heisner holds interim decision authority for the Stage 1 design until the pilot's decision authority is confirmed.\
**Evidence:** Statement by Tillman Heisner; [Pilot](PILOT.md#proposed-participants).\
**Recorded by:** Tillman Heisner\
**Supersedes:** none

### 2026-10-12 - Stage 1 benchmark datasets decided

**Type:** Decision\
**Claim:** Under interim authority, Tillman Heisner decided that Stage 1 will use 15 to 25 public STRENDA DB entries as Export XML input, with T9HQ4X and GNICYO as the development set and expected records derived by fixed rules plus hand-marked methodology facts.\
**Evidence:** [Open questions, Q1](OPEN_QUESTIONS.md#q1---which-existing-datasets-should-be-used); [Interim decision authority](README.md#2026-10-12---interim-decision-authority-for-stage-1).\
**Recorded by:** Tillman Heisner\
**Supersedes:** none

### 2026-10-12 - EnzymeML record requirements decided

**Type:** Decision\
**Claim:** Under interim authority, Tillman Heisner decided that draft EnzymeML records must be structurally valid, may leave required fields empty only where the input lacks the information, and must come with an evidence file and a not-mapped report; approved records must be fully valid.\
**Evidence:** [Open questions, Q2](OPEN_QUESTIONS.md#q2---what-must-the-enzymeml-records-contain); [Interim decision authority](README.md#2026-10-12---interim-decision-authority-for-stage-1).\
**Recorded by:** Tillman Heisner\
**Supersedes:** none

### 2026-10-12 - EnzymeML V2.0 target decided

**Type:** Decision\
**Claim:** Under interim authority, Tillman Heisner decided that the pilot will target EnzymeML V2.0 as defined at enzymeml-specifications commit bf9321f.\
**Evidence:** [Open questions, Q3](OPEN_QUESTIONS.md#q3---which-enzymeml-target-should-be-tested); https://github.com/EnzymeML/enzymeml-specifications/tree/bf9321f720eaff48d315bad52aebc1765cf42188; [Interim decision authority](README.md#2026-10-12---interim-decision-authority-for-stage-1).\
**Recorded by:** Tillman Heisner\
**Supersedes:** none

### 2026-10-12 - Stage 1 evaluation design decided

**Type:** Decision\
**Claim:** Under interim authority, Tillman Heisner decided that the extraction, verification, and inquiry agents will each be evaluated on a dataset built from the Q1 entries, with zero-shot and few-shot compared on the same test items; acceptance criteria remain open.\
**Evidence:** [Open questions, Q4](OPEN_QUESTIONS.md#q4---how-should-extraction-and-verification-be-evaluated); [Interim decision authority](README.md#2026-10-12---interim-decision-authority-for-stage-1).\
**Recorded by:** Tillman Heisner\
**Supersedes:** none

### 2026-10-12 - Pipeline architecture decided

**Type:** Decision\
**Claim:** Under interim authority, Tillman Heisner decided that ARIADNE's proposed pipeline will consist of an extraction agent, a deterministic verifier, a verification agent, and an inquiry agent sharing one issue format, with the scientist answering the questions and approving the final record.\
**Evidence:** [Architecture](ARCHITECTURE.md#proposed-flow); [Interim decision authority](README.md#2026-10-12---interim-decision-authority-for-stage-1).\
**Recorded by:** Tillman Heisner\
**Supersedes:** none


## License

Documentation and ledger content are licensed under [CC BY 4.0](LICENSE), and source code under [Apache-2.0](LICENSE-CODE). Data and third-party materials retain their own terms.
