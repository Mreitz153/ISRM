# ISRM — Intelligent Systems Reference Model

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23115842.svg)](https://doi.org/10.5281/zenodo.23115842)
![Version](https://img.shields.io/badge/version-1.0-blue)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-green)

**An open, technology-neutral reference model for intelligent and goal-directed systems.**

**Originator:** Marcel Reitz — Altenbuch, Germany  
**Initial development:** 2026  
**Public release:** 3 October 2026  
**Canonical v1.0 DOI:** [10.5281/zenodo.23115842](https://doi.org/10.5281/zenodo.23115842)

## ISRM v1.0 documents

The complete public v1.0 document set is available directly in this repository. These PDFs are synchronized from the canonical Zenodo release.

| Document | PDF |
|---|---|
| **ISRM v1.0 Public Specification** | [Open PDF](docs/publications/01_ISRM_v1.0_Public_Specification.pdf) |
| **ISRM Whitepaper** | [Open PDF](docs/publications/02_ISRM_Whitepaper.pdf) |
| **Validation and Falsification Report** | [Open PDF](docs/publications/03_ISRM_Validation_and_Falsification_Report.pdf) |
| **Prior Art and Standards Crosswalk** | [Open PDF](docs/publications/04_ISRM_Prior_Art_and_Standards_Crosswalk.pdf) |
| **Reference Implementation Validation Report** | [Open PDF](docs/publications/10_ISRM_Reference_Implementation_Validation_Report.pdf) |
| **Final Internal Validation Addendum** | [Open PDF](docs/publications/16_ISRM_Final_Internal_Validation_Addendum.pdf) |

**Canonical archived release:** [Zenodo record 23115842](https://zenodo.org/records/23115842) · **DOI:** [10.5281/zenodo.23115842](https://doi.org/10.5281/zenodo.23115842)

> For citation and provenance, use the DOI. The copies in this repository are provided for convenient reading and project discovery.

### German translation / Deutsche Übersetzung

The official German translation and the complete German PDF documentation package are available under **[docs/de/](docs/de/README.md)**.

Direct links:
- [German ISRM v1.0 specification (PDF)](docs/de/02_ISRM_v1.0_Spezifikation_DE.pdf)
- [German validation and falsification report (PDF)](docs/de/03_ISRM_Validierung_Falsifikation_DE.pdf)
- [Complete German documentation index](docs/de/README.md)

The DOI-published English v1.0 remains the authoritative reference in case of discrepancies.

zation work:

**[ISRM v1.0 — Offizielle deutsche Übersetzung](docs/de/ISRM_v1.0_DE.md)**

The DOI-published English v1.0 remains the authoritative reference in case of discrepancies.

## What is ISRM?

The **Intelligent Systems Reference Model (ISRM)** describes how intelligent and goal-directed systems transform intent or events, perceived information and contextual state into decisions, authorized actions and observable effects.

ISRM is intended to provide a common architectural language across:

- AI agents and agentic AI
- autonomous systems
- robotics
- multi-agent systems
- cyber-physical systems
- human-in-the-loop systems
- deterministic automation

ISRM is implementation-independent. It does not prescribe a particular AI model, programming language, protocol, vendor, or physical architecture.

## Reference model

ISRM defines six functional responsibilities:

| Layer | Responsibility |
|---|---|
| **L6 — Intent** | Desired outcomes, objectives, tasks, constraints and priorities |
| **L5 — Perception** | Transforms signals and events into usable observations |
| **L4 — Context** | Maintains task-relevant state, knowledge, memory and assumptions |
| **L3 — Cognition** | Generates and evaluates interpretations, plans and candidate actions |
| **L2 — Decision** | Selects, rejects, defers or escalates actions under authority and policy |
| **L1 — Execution** | Translates authorized actions into concrete attempted operations |

The **Environment** is explicitly outside the functional stack.

Three orthogonal cross-layer planes apply throughout the model:

- **Control Plane** — authority, governance, policy and safety
- **Trust Plane** — identity, authentication, integrity, security, provenance, accountability and audit
- **Adaptation Plane** — evaluation, learning, optimization and controlled behavior-changing updates

### Operational loop

```text
Intent / Event
      ↓
  Perception
      ↓
   Context
      ↓
  Cognition
      ↓
  Decision
      ↓
  Execution
      ↓
 Environment
      └────────────→ Perception
```

A processing episode may begin through **Intent** or **Perception**. ISRM therefore supports both goal-driven and event-driven systems.

## Core characteristics

ISRM v1.0 defines:

- recursive composition of intelligent systems and systems-of-systems
- Processing Episodes for traceable activity
- canonical information objects
- bounded authority and delegation
- uncertainty preservation
- explicit separation of candidate actions from authorized actions
- controlled adaptation and version transitions
- failure categories
- four conformance classes (C0–C3)
- normative invariants and conformance tests

## Recursive composition

Every ISRM system may simultaneously be a complete ISRM system and part of another system's environment. This supports coordinator/worker agents, robot fleets, nested autonomous systems and other systems-of-systems without requiring a special multi-agent layer.

## Reproducible validation assets

The executable ISRM v1.0 internal validation harnesses and result summaries are published in [`validation/`](validation/README.md).

- [Reference implementation validation harness](validation/reference_validation.py)
- [Edge-case and randomized invariant harness](validation/edge_case_validation.py)
- [Conformance test matrix](validation/conformance_test_matrix.csv)
- [Reference results summary](validation/reference_results_summary.csv)
- [Edge-case results summary](validation/edge_case_results_summary.csv)
- [Property-test results](validation/property_results.json)

The harnesses use only the Python standard library and can be executed independently. These are internal validation/falsification assets, not independent certification.

## Validation

The v1.0 development package was exercised against deterministic control, tool-using software agents and recursive multi-agent reference implementations.

Reported internal validation results:

- **69 / 69** applicable reference-implementation test executions passed
- **60 / 60** edge-case executions passed
- **50,000 randomized iterations per tested invariant family** with zero observed violations

These results support internal consistency and implementability of the tested model. They are **not independent certification** and do not prove completeness, safety, legal compliance or suitability as an international standard.

## Canonical publication

The immutable public release of **ISRM v1.0** is archived on Zenodo:

**Reitz, Marcel (2026). _ISRM v1.0 — Intelligent Systems Reference Model: A Technology-Neutral Reference Model for Intelligent and Goal-Directed Systems_. Zenodo.**  
https://doi.org/10.5281/zenodo.23115842

The Zenodo record is the canonical citation target for ISRM v1.0. This GitHub repository is the public development and collaboration home of the project.

## Standardization status

ISRM v1.0 is an **open pre-standard reference model**, not a DIN, EN, ISO/IEC or IEEE standard.

A standardization proposal based on ISRM v1.0 was submitted to **DIN Deutsches Institut für Normung e. V.** in Germany in October 2026. Any future formal standard would be developed through the applicable consensus-based standardization process.

## Prior art and positioning

ISRM does **not** claim invention of feedback control, perception-action loops, cognitive architectures, delegation, layered architectures, governance, provenance or learning.

Relevant bodies of prior work include Sense–Plan–Act architectures, OODA, BDI, MAPE-K, NIST RCS/4D-RCS and existing AI governance, lifecycle, risk and terminology standards. ISRM's proposed contribution is the integrated reference structure combining six functional responsibilities, an explicit environment boundary, three cross-layer planes, recursive composition, Processing Episodes, canonical information objects, authority-preserving transitions and conformance classes.

## Citation

If you use, discuss or build upon ISRM, please cite the Zenodo release:

```text
Reitz, Marcel (2026).
ISRM v1.0 — Intelligent Systems Reference Model:
A Technology-Neutral Reference Model for Intelligent and Goal-Directed Systems.
Zenodo. https://doi.org/10.5281/zenodo.23115842
```

See [CITATION.cff](CITATION.cff) for machine-readable citation metadata.

## Contributing

Independent critique, mappings, implementations, falsification attempts and conformance-test results are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

The ISRM documentation in this repository is made available under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

When referring specifically to the origin of the model, the preferred attribution is:

> **Originator: Marcel Reitz — Altenbuch, Germany. Initial development: 2026.**

---

**ISRM v1.0 · DOI 10.5281/zenodo.23115842 · Marcel Reitz · 2026**
