# ARIADNE architecture

## Status

This document describes a proposed system, not implemented software, an approved ELEGANCE architecture, or a production deployment. See the proposed [Pilot](PILOT.md) and [Open questions](OPEN_QUESTIONS.md).

## Proposed flow

```text
researchers provide the scientific files they already use
  -> ARIADNE preserves the original files and records their origin
  -> deterministic software extracts their contents and source locations
  -> reviewed examples guide extraction and clarification agents
  -> the agents propose evidence-linked EnzymeML records
  -> deterministic checks test structure, units, and source links
  -> separate verifier agents compare the proposals with the evidence
  -> scientists review and correct the candidate records
  -> ARIADNE generates and checks EnzymeML outputs
  -> data owners approve any exchange
  -> approved records are shared with an authorized destination
```

## Principles

- **Human-centered:** Researchers begin with familiar files and receive useful guidance without first mastering EnzymeML.
- **Evidence-linked:** Deterministic parsing records what is present and where; agents propose what it means. Accepted values remain linked to exact source evidence.
- **Agent-assisted:** Few-shot-guided extraction agents propose records and clarification questions. Separate verifier agents independently check the candidates.
- **Controlled:** Agents cannot approve their own outputs or bypass deterministic checks, scientific review, or data-owner authority.
- **Standards-aware:** EnzymeML represents enzyme reaction and kinetics data. Linked companion schemas cover data outside its scope; the initial pilot itself is limited to EnzymeML.