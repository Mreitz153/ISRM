# ISRM v1.0 Architecture

Canonical publication: https://doi.org/10.5281/zenodo.23115842

## Formal model

`S = { I, P, C, R, D, E ; G, T, A }`

where:

- **I — Intent**
- **P — Perception**
- **C — Context**
- **R — Cognition**
- **D — Decision**
- **E — Execution**
- **G — Control Plane**
- **T — Trust Plane**
- **A — Adaptation Plane**

`W` denotes the external environment.

## Functional responsibilities

### L6 — Intent
Represents desired outcomes, objectives, tasks, constraints, priorities and event-derived goals.

### L5 — Perception
Transforms signals and events into observations usable by the system.

### L4 — Context
Maintains task-relevant state assembled from observations, knowledge, memory and system state.

### L3 — Cognition
Generates, evaluates and refines interpretations, plans and candidate actions.

### L2 — Decision
Selects, rejects, defers or escalates candidate actions under authority, policy and risk constraints.

### L1 — Execution
Translates authorized actions into concrete attempted operations and reports execution outcome.

## External environment

The environment is not an ISRM layer. Effects pass outward through Execution and observations return through Perception.

## Cross-layer planes

**Control Plane (G):** authority, governance, policy and safety.

**Trust Plane (T):** identity, authentication, integrity, security, provenance, accountability and audit.

**Adaptation Plane (A):** evaluation, learning, optimization and controlled behavior-changing updates.

## Operational loop

`Perception → Context → Cognition → Decision → Execution → Environment → Perception`

Intent constrains or initiates processing. Event-driven activation may enter through Perception and create, refine, suspend or terminate Intent subject to Control.

## Recursive composition

An ISRM system may be part of another system's environment while remaining a complete ISRM system itself. This permits recursive composition of agents, robots and systems-of-systems without adding architecture-specific layers.

## Conformance classes

- **C0 — Mappable**
- **C1 — Traceable**
- **C2 — Controlled**
- **C3 — Adaptive-Controlled**

For normative detail, cite and consult the canonical v1.0 Zenodo specification.
