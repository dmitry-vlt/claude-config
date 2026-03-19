# multi-agent-task-breakdown

## Purpose
Use this skill when a task is too broad, too cross-functional, or too parallelizable for one agent to handle efficiently.

This skill decomposes work into clear sub-tasks that can be delegated to specialized agents while preserving shared context, ordering constraints, dependencies, and integration checkpoints.

## Goals
- Break large initiatives into tractable workstreams
- Identify what can run in parallel vs what must be sequential
- Assign work to the right agent type
- Prevent duplicate or conflicting work
- Preserve enough context so delegated agents can execute well
- Define integration, validation, and closure criteria

## When to Use
Use this skill for:
- large feature builds
- multi-step debugging efforts
- system migrations
- product launches
- refactors spanning multiple services
- infra + app + UI changes
- incident response involving several tracks
- research / build / validation loops
- roadmap items that need coordinated execution

## Agent Types
Use the following conceptual agent roles unless the repository defines others:
- Coordinator
- Engineer
- Reviewer
- Debugger
- Infra
- Security
- Product / Spec
- QA / Test
- Docs / Release
- Data / Analytics

If the repo has custom agents, map work to them instead.

## Workflow
1. Restate the objective clearly.
2. Identify the real deliverable.
3. Separate discovery, implementation, validation, and rollout work.
4. Identify dependencies and ordering constraints.
5. Split work into agent-sized tasks with explicit outputs.
6. Mark tasks as:
   - parallel
   - sequential
   - blocked
   - optional
7. Define handoff contracts between agents.
8. Define checkpoints where work must be merged or reviewed.
9. Define final acceptance criteria.

## Decomposition Principles
- Split by ownership boundary, not arbitrary file count.
- Prefer tasks that one agent can complete without constant interruption.
- Avoid creating tasks that require two agents to edit the same thing simultaneously unless explicitly coordinated.
- Isolate high-risk workstreams.
- Keep one coordinator-level view of dependencies and status.
- Ensure each task has a clear done condition.
- Preserve shared assumptions in every handoff.

## Output Format

# Task Breakdown

## Objective
State the end goal in one paragraph.

## Final Deliverable
What must exist when this initiative is done?

## Key Constraints
- technical constraints
- product constraints
- time / risk constraints
- compatibility constraints
- operational constraints

## Workstreams
For each workstream provide:

### Workstream: [Name]
**Owner Agent:** [Agent Type]  
**Purpose:**  
**Inputs / Context Needed:**  
**Tasks:**  
1. ...
2. ...
3. ...

**Outputs:**  
- ...
- ...

**Dependencies:**  
- depends on:
- blocks:

**Parallelization:**  
- parallel / sequential / partially parallel

**Done When:**  
- ...

## Recommended Execution Order
1. ...
2. ...
3. ...

## Handoff Contracts
Specify exactly what one agent must provide before the next agent starts:
- spec handoff
- code handoff
- infra handoff
- QA handoff
- release handoff

## Risks
- overlapping ownership
- inconsistent assumptions
- merge conflicts
- missing validation
- rollout coordination failures

## Checkpoints
Define review points where the coordinator should reassess:
- after discovery
- before implementation
- before merge
- before rollout
- after validation

## Acceptance Criteria
- AC1:
- AC2:
- AC3:

## Rules
- Do not merely create a to-do list; create an execution plan.
- Do not split work so finely that coordination overhead dominates.
- Do not assign tasks without specifying inputs and outputs.
- Surface blockers and dependency chains explicitly.
- Highlight the critical path.
- Prefer a small number of strong workstreams over many weak ones.
- Make the plan executable by real agents without additional interpretation.

## Special Guidance
When decomposing engineering-heavy work, usually separate into:
1. discovery / system understanding
2. design / spec
3. implementation
4. verification / testing
5. deployment / rollout
6. documentation / communication

When decomposing incident/debugging work, usually separate into:
1. symptom capture
2. reproduction
3. root-cause investigation
4. candidate fix
5. verification
6. postmortem / prevention

When decomposing product builds across stack layers, usually separate into:
1. backend / API
2. infra / data
3. frontend / UX
4. test / validation
5. docs / release readiness
