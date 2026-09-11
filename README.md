# ARIADNE: Agentic Research Infrastructure for Auditable Data Normalization and Exchange

> Make the FAIR and scientifically trustworthy choice the easiest choice.

ARIADNE is a system designed to make FAIR data practices easier by helping researchers turn familiar scientific files into structured, evidence-linked records. Its proposed architecture would use EnzymeML for enzyme reaction and kinetics data and linked companion schemas for data outside EnzymeML's scope. Few-shot-guided extraction agents would propose records; deterministic validation, independent verifier agents, and human review would assess them before acceptance.

This repository currently serves as ARIADNE's concept and provenance ledger. Development is intended to begin with a small, co-designed ELEGANCE pilot; no scientific-data processing software is implemented yet.

See the proposed [Pilot](PILOT.md), [Architecture](ARCHITECTURE.md), and [Open questions](OPEN_QUESTIONS.md). To contribute, see [Contributing](CONTRIBUTING.md).


## Provenance ledger

Ledger entries are append-only and follow the [ledger entry template](CONTRIBUTING.md#ledger-entry-template).

### 2026-09-01 to 2026-09-04 — Kick-off motivation

**Type:** User-reported  
**Claim:** ELEGANCE kick-off discussions connected centralized data infrastructure, EnzymeML, FAIR principles, and agentic translation. The amount of specialist knowledge involved motivated an approach that would make these concepts easier for ELEGANCE researchers to use. 
**Evidence:** Participant recollection reported by Tillman Heisner.  
**Recorded by:** Tillman Heisner  
**Supersedes:** none

### 2026-09-07 - Repository licensing established

**Type:** Decision  
**Claim:** Documentation and ledger content are licensed under CC BY 4.0, while future source code is licensed under Apache-2.0. Data, third-party materials, and consortium intellectual-property arrangements are outside these defaults.  
**Evidence:** `LICENSE`; `LICENSE-CODE`; [License](README.md#license).  
**Recorded by:** Tillman Heisner  
**Supersedes:** none

### 2026-09-08 - Pilot direction proposed

**Type:** Proposal  
**Claim:** ARIADNE should begin with a two-stage, human-centered ELEGANCE pilot. Existing datasets would first establish and evaluate evidence-linked EnzymeML extraction, deterministic validation, and independent verification before the workflow is applied to data-owner-approved researcher workflows.
**Evidence:** [Pilot](PILOT.md); [Architecture](ARCHITECTURE.md); [Open questions](OPEN_QUESTIONS.md).  
**Recorded by:** Tillman Heisner  
**Supersedes:** none


## License

Documentation and ledger content are licensed under [CC BY 4.0](LICENSE), and source code under [Apache-2.0](LICENSE-CODE). Data and third-party materials retain their own terms.
