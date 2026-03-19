# pr-reviewer

## Purpose
Use this skill to review a branch, diff, or pull request with high signal and low fluff.

## Goals
Find correctness, reliability, performance, security, and maintainability issues before merge.

## Review Checklist
Inspect for:
- logical correctness
- edge cases
- error handling
- data races / concurrency hazards
- API/schema compatibility
- test coverage gaps
- performance regressions
- cloud cost regressions
- security risks
- observability impact
- rollback risk

## Workflow
1. Understand the stated intent of the change.
2. Compare implementation to intent.
3. Identify high-risk files and contracts.
4. Check whether tests prove the new behavior.
5. Check for production-readiness concerns.
6. Prioritize findings by severity.

## Output Format
## Summary
One paragraph: what the change does and whether it is merge-ready.

## Blocking Issues
- [B1] ...
- [B2] ...

## Non-Blocking Issues
- [N1] ...
- [N2] ...

## Tests Missing or Weak
- ...

## Performance / Cost Concerns
- ...

## Security / Reliability Concerns
- ...

## Suggested Fixes
Provide concrete recommendations, ideally file-level.

## Approval Recommendation
One of:
- Approve
- Approve with minor follow-ups
- Request changes

## Rules
- Do not invent issues without evidence from the diff.
- Be direct and specific.
- Prefer “here is the exact failure mode” over vague style criticism.
- Flag missing rollback or migration considerations when relevant.
