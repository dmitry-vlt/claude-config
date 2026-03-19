# CLAUDE.md

## Project Purpose
This repository powers [PROJECT NAME]. The primary goals are:
- Reliability in production
- Fast iteration without regressions
- Clear, maintainable code
- Cost-aware infrastructure decisions

## Non-Negotiables
- Do not make speculative architectural changes unless explicitly requested.
- Do not change public APIs, DB schemas, queue contracts, or event formats without calling it out clearly.
- Prefer the smallest safe fix over broad rewrites.
- Preserve backward compatibility unless the task explicitly authorizes breaking changes.
- Never commit secrets, tokens, private keys, or credentials.
- Never suppress errors silently; log with enough context to debug.
- Never remove tests to make a build pass.

## How to Work in This Repo
- First understand the relevant codepath before editing.
- Before changing behavior, identify:
  - entrypoints
  - dependent modules
  - config/env vars
  - test coverage
  - operational impact
- For non-trivial changes, present:
  1. current behavior
  2. proposed change
  3. risk areas
  4. validation plan

## Code Standards
- Prefer simple, explicit code over clever abstractions.
- Keep functions focused and reasonably small.
- Use descriptive names.
- Avoid hidden side effects.
- Add comments only where intent is not obvious from the code.
- Match existing project patterns unless there is a strong reason to improve them.

## Testing Standards
- Add or update tests for behavior changes.
- Prefer regression tests for bug fixes.
- Prefer integration tests when behavior crosses module or service boundaries.
- Call out any meaningful gaps in testability.

## Performance / Cost Standards
- Be mindful of:
  - unnecessary copies
  - repeated serialization
  - unbounded memory growth
  - excessive network calls
  - chatty storage/API access
  - queue backpressure
  - GPU/CPU hotspots
- When relevant, quantify the likely impact.

## Infra / Deployment Standards
- Highlight changes that affect:
  - Docker images
  - CI/CD
  - Kubernetes manifests
  - Terraform / IaC
  - secrets
  - migrations
  - observability
  - autoscaling
- Always mention rollback implications for production-facing changes.

## Security Standards
- Check auth/authz assumptions.
- Check tenant/data isolation assumptions.
- Check logging for sensitive data leakage.
- Check shell, file, or command execution paths for injection risk.
- Check storage and retention changes for unintended exposure.

## Response Format Preferences
For meaningful tasks, prefer this structure:
1. What I found
2. What I changed / recommend
3. Risks
4. Validation
5. Next best step

