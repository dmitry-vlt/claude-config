# perf-cost-auditor

## Purpose
Use this skill to audit code or architecture for latency, throughput, resource usage, and cloud cost efficiency.

## Goals
Identify the most material bottlenecks and wasted spend.

## Audit Areas
Check for:
- redundant I/O
- repeated deserialization / encoding
- unnecessary copies
- excessive API/storage requests
- suboptimal batching
- hot loops
- lock contention
- memory growth / leaks
- queue lag / backpressure
- poor cache strategy
- underutilized hardware acceleration
- overprovisioned infrastructure

## Workflow
1. Define the performance or cost objective.
2. Identify the likely hot path.
3. Estimate cost/latency contributors.
4. Separate obvious waste from speculative optimization.
5. Recommend changes in priority order.

## Output Format
## Objective
What metric matters here?

## Hot Path
What path is likely dominating time or spend?

## Findings
- [F1] ...
- [F2] ...
- [F3] ...

## Expected Impact
For each finding, estimate:
- latency impact
- throughput impact
- infra cost impact
- implementation complexity

## Recommended Changes
Rank by ROI:
1. ...
2. ...
3. ...

## Measurement Plan
Specify what to measure before and after:
- latency
- p95/p99
- CPU/GPU
- memory
- request counts
- storage/API spend

## Rules
- Do not recommend micro-optimizations before fixing dominant waste.
- Quantify where possible.
- Prefer changes that improve both performance and simplicity.
