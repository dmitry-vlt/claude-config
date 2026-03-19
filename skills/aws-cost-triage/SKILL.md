# aws-cost-triage

## Purpose
Use this skill when investigating AWS spend, unexpected cost growth, waste, inefficient architecture, or cost/performance tradeoffs.

This skill identifies the biggest cost drivers first, explains why spend is occurring, and recommends the highest-ROI fixes without sacrificing reliability blindly.

## Goals
- Identify the dominant AWS cost drivers
- Separate one-time spikes from recurring waste
- Find misconfigurations and inefficient patterns
- Recommend practical changes ranked by ROI
- Preserve reliability, performance, and operational sanity
- Provide a measurement plan to validate savings

## When to Use
Use this skill for:
- monthly AWS bill review
- sudden spend spikes
- service-by-service cost diagnosis
- architecture cost optimization
- storage / compute / transfer / observability cost analysis
- deciding between design alternatives on cost grounds
- pre-scale cost modeling
- customer / tenant cost attribution analysis

## Primary Cost Categories to Check
Always consider these major buckets where relevant:
- EC2
- EKS / ECS / Fargate
- Lambda
- S3
- EBS
- RDS / Aurora
- ElastiCache / Redis
- OpenSearch
- CloudFront
- Data transfer / NAT gateways / inter-AZ traffic
- CloudWatch logs / metrics / traces
- Kinesis / Kafka / MSK
- SQS / SNS
- DynamoDB
- GPU instances
- load balancers
- snapshots / backups / orphaned resources

## Triage Workflow
1. Define the time window of concern.
2. Identify whether the issue is:
   - steady-state high cost
   - sudden spike
   - gradual drift
   - cost regression after a change
3. Identify the top 3–5 cost drivers first.
4. For each major driver, determine:
   - what resource is costing money
   - why usage exists
   - whether it is intentional, excessive, or accidental
5. Distinguish:
   - productive spend
   - waste
   - insurance / redundancy spend
   - temporary experimentation spend
6. Recommend fixes ranked by savings vs implementation risk.
7. Define how to verify savings after changes.

## Cost Investigation Heuristics
Check for:
- idle or underutilized instances
- overprovisioned node groups
- wrong instance family or size
- excessive GPU headroom
- always-on resources that should scale down
- cross-AZ or internet egress surprises
- NAT gateway overuse
- chatty internal traffic
- overly frequent polling
- S3 request explosion
- poor storage tiering
- excessive retention windows
- log volume explosion
- duplicate ingestion pipelines
- abandoned snapshots / volumes / load balancers / IPs
- EKS control-plane and daemon overhead
- expensive observability defaults
- bursty workloads on wrong pricing model
- lack of savings plans / reserved capacity where appropriate

## Output Format

# AWS Cost Triage

## Time Window
Specify the period being analyzed.

## Cost Pattern
One of:
- steady-state high
- spike
- drift
- post-change regression

## Top Cost Drivers
Rank the biggest contributors:
1. Service / resource:
   - why it costs money
   - what appears to be driving usage
2. Service / resource:
   - ...
3. Service / resource:
   - ...

## Findings
For each finding provide:

### Finding [N]: [Short Name]
**Category:** compute / storage / transfer / observability / database / queue / other  
**What is happening:**  
**Likely cause:**  
**Evidence to gather / confirm:**  
**Is it waste, necessary spend, or tradeoff?:**  
**Estimated savings potential:** low / medium / high  
**Risk of changing it:** low / medium / high  

## Recommended Actions
Rank in order of ROI.

### Action [N]
**Change:**  
**Why it helps:**  
**Expected impact:**  
- monthly savings
- performance impact
- reliability impact
- implementation complexity

**Validation:**  
What should be measured before and after?

## Quick Wins
List the easiest high-confidence savings.

## Structural Fixes
List deeper architectural changes that require more effort but materially improve long-term economics.

## Do Not Cut Blindly
List spend that may look expensive but should not be reduced without care:
- redundancy
- backup retention
- core observability
- capacity buffers for critical workloads
- customer-facing latency protections

## Measurement Plan
Track:
- cost by service
- cost by environment
- cost by workload / customer / camera / tenant where applicable
- request counts
- GB stored / transferred
- CPU / GPU utilization
- memory utilization
- queue depth / throughput
- p95 / p99 latency
- log ingest volume

## Rules
- Do not optimize minor line items before identifying the biggest spend.
- Do not recommend risky cuts without stating operational tradeoffs.
- Distinguish resource cost from request/transfer cost.
- Quantify where possible; when exact numbers are unavailable, state assumptions clearly.
- Prefer recurring savings over one-time cleanup unless the one-time cleanup is large.
- Consider engineering time as part of ROI.
- Always separate “waste” from “intentional but expensive.”

## Service-Specific Guidance

### EC2 / GPU
Check:
- utilization vs instance size
- Spot vs on-demand fit
- Savings Plans / Reserved Instances fit
- right-sizing
- scale-to-zero opportunities
- packing efficiency
- expensive idle GPU nodes
- mixed-instance pools

### EKS
Check:
- node headroom
- per-cluster overhead
- daemonset tax
- requests/limits mismatch
- autoscaler behavior
- over-segmentation into too many small clusters
- idle system components

### S3
Check:
- storage class mismatch
- retention windows
- duplicate copies
- transition policy quality
- delete lag
- request volume
- LIST/GET/PUT amplification
- multipart upload leftovers
- replication costs

### Data Transfer / NAT
Check:
- inter-AZ traffic
- internet egress
- NAT gateway centralization patterns
- service placement causing unnecessary traversal
- repeated downloads / uploads
- proxy bottlenecks

### CloudWatch / Observability
Check:
- log verbosity
- duplicate logs
- retention too long
- high-cardinality metrics
- over-instrumentation
- trace sampling strategy
- unnecessary dashboards / alarms pulling expensive data

### Databases
Check:
- overprovisioned instances
- storage bloat
- IOPS over-allocation
- bad query patterns causing scale-ups
- backup / snapshot growth
- unnecessary replicas

## Special Guidance
When analyzing systems like video pipelines, media, or high-throughput AI infrastructure, explicitly check:
- ingest bandwidth
- per-object storage overhead
- request amplification
- transcoding / decoding waste
- GPU underutilization
- unnecessary frame processing
- redundant copies across hot/warm/cold tiers
- queue fan-out costs
- retention by incident relevance rather than blanket retention
