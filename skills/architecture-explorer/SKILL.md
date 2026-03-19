# architecture-explorer

## Purpose
Use this skill when the task requires understanding an unfamiliar codebase, subsystem, service boundary, or data flow before making changes.

## Goals
Produce a fast, accurate map of the relevant system so work happens with context instead of guesswork.

## Workflow
1. Identify the user’s requested area of change or concern.
2. Locate likely entrypoints:
   - CLI entrypoints
   - HTTP handlers / routers
   - workers / consumers
   - scheduled jobs
   - UI pages / components
3. Trace the execution path through:
   - service layer
   - domain logic
   - persistence
   - queues/events
   - external APIs
4. Identify config and environment dependencies.
5. Identify:
   - key files
   - data models / schemas
   - contracts / interfaces
   - tests covering the path
6. Summarize the architecture in plain English.

## Output Format
### System Map
- Entry points:
- Core modules:
- Data stores:
- Queues/events:
- External dependencies:
- Config/env vars:
- Tests:
- Operational touchpoints:

### Execution Flow
Provide a concise step-by-step flow from trigger to outcome.

### Risk Areas
Call out:
- tightly coupled areas
- missing tests
- surprising side effects
- hidden config
- migration/deployment sensitivity

### Recommended Starting Point
State the best file(s) to modify and why.

## Rules
- Do not propose edits until the relevant path is understood.
- Prefer citing concrete files/functions over vague descriptions.
- If uncertainty remains, state it explicitly.
