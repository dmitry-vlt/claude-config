# spec-writer

## Purpose
Use this skill when the user has a rough idea and needs a clear, implementation-ready technical or product spec.

## Goals
Turn ambiguous ideas into structured plans that engineering can execute and leadership can review.

## Workflow
1. Restate the problem precisely.
2. Identify business and technical constraints.
3. Define scope and explicitly mark out-of-scope items.
4. Propose a design that matches the existing architecture where practical.
5. Define interfaces, data flow, and failure modes.
6. Define rollout, observability, and validation.

## Output Format
# [Feature / System Name]

## Problem
What problem is being solved and for whom?

## Goals
- Primary goal
- Secondary goals

## Non-Goals
- Explicitly out of scope items

## Requirements
### Functional Requirements
- FR1:
- FR2:
- FR3:

### Non-Functional Requirements
- Performance
- Reliability
- Security
- Cost
- Operability

## Proposed Design
Describe the system in concrete terms.

## Data Model / Contracts
- Inputs
- Outputs
- Schemas
- Events
- APIs

## User / Operator Flow
Describe the happy path and important alternate paths.

## Failure Modes
- What can fail
- How it is detected
- How the system responds

## Observability
- Metrics
- Logs
- Alerts
- Dashboards

## Rollout Plan
- Phase 1
- Phase 2
- Backward compatibility
- Rollback

## Open Questions
- Q1
- Q2

## Validation Plan
- Unit
- Integration
- Load
- UAT / acceptance

## Rules
- Do not leave requirements vague if a concrete assumption can be made safely.
- Keep the design grounded in the repo’s current patterns unless the user is explicitly redesigning.
- Call out tradeoffs instead of pretending there are none.
