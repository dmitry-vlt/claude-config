# debug-investigator

## Purpose
Use this skill when debugging a bug, outage, regression, flaky test, or production incident.

## Goals
Drive toward root cause methodically instead of guessing.

## Workflow
1. Define the observed symptom precisely.
2. Record expected behavior.
3. Identify the narrowest reproducible path.
4. Form multiple hypotheses.
5. Rank hypotheses by probability and blast radius.
6. Inspect:
   - recent changes
   - logs
   - config/env changes
   - dependent systems
   - timing / concurrency issues
7. Propose the smallest safe fix.
8. Define validation steps.

## Output Format
## Symptom
What is happening?

## Expected Behavior
What should happen?

## Reproduction
- Preconditions
- Steps
- Frequency
- Environment

## Most Likely Causes
1. ...
2. ...
3. ...

## Evidence
What in the code/logs/config supports each hypothesis?

## Root Cause
State root cause if supported.
If not proven, state the strongest current hypothesis and what would confirm it.

## Fix Plan
- Minimal code/config change
- Why it should work
- Risk of the fix

## Validation Plan
- Reproduction after fix
- Regression checks
- Monitoring / alerts to watch

## Rules
- Never jump straight from symptom to fix without showing reasoning.
- Distinguish proven facts from hypotheses.
- Prefer the smallest reversible correction first.
