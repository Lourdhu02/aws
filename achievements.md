# Achievements — AWS ML Study Guide

Track what you've earned as you work through the repo. Each achievement has a name,要求 (what you must do), evidence (how you prove it), and the phase it belongs to.

Use this as a personal scoreboard. Update it as you go; link evidence (lab notes, summary files, diagrams, screenshots). The goal is visible progress, not perfection.

---

## How to use this file

1. Pick a phase from the study plan.
2. Work through the topics and labs.
3. When you meet an achievement's要求, fill in the **Date** and **Evidence** columns.
4. Keep evidence somewhere durable — a `logs/` folder, a separate notes repo, or linked files in this repo.

---

## Achievements

### Phase 00 — Foundations

| # | Achievement | 要求 | Evidence | Status | Date | Evidence link |
|---|------------|------|----------|--------|------|----------------|
| 00.1 | IAM narrator | Explain IAM users, groups, roles, policies, and evaluation logic without notes | Written or recorded explanation | ☐ | | |
| 00.2 | EC2 hands-on | Launch an EC2 instance, SSH in, and clean it up | Screenshot or CLI log | ☐ | | |
| 00.3 | S3 workflow | Upload, version, and access an object in S3; then delete it | CLI or console log | ☐ | | |
| 00.4 | VPC builder | Design and deploy a VPC with public/private subnets | Architecture diagram or stack | ☐ | | |
| 00.5 | Foundations complete | All 00 topics marked Complete in progress.md | progress.md | ☐ | | |

### Phase 01 — ML Infrastructure

| # | Achievement | 要求 | Evidence | Status | Date | Evidence link |
|---|------------|------|----------|--------|------|----------------|
| 01.1 | ECR push | Build a Docker image and push it to ECR | CLI log | ☐ | | |
| 01.2 | ECS run | Run that image in ECS (or Fargate) | Task/service description | ☐ | | |
| 01.3 | SageMaker training | Run a training job on SageMaker | Job config + output | ☐ | | |
| 01.4 | SageMaker deploy | Deploy a model to a SageMaker endpoint | Endpoint config + invocation | ☐ | | |
| 01.5 | ML infra complete | 01 topics marked Complete | progress.md | ☐ | | |

### Phase 02 — MLOps Pipelines

| # | Achievement | 要求 | Evidence | Status | Date | Evidence link |
|---|------------|------|----------|--------|------|----------------|
| 02.1 | CodePipeline model flow | Create a CodePipeline that moves a model artifact | Pipeline diagram or ARN | ☐ | | |
| 02.2 | GitHub Actions on AWS | Create one GitHub Actions workflow that touches AWS | Workflow file + run log | ☐ | | |
| 02.3 | MLflow on AWS | Track a run with MLflow somewhere on AWS | Run record | ☐ | | |
| 02.4 | SageMaker Pipelines | Build a SageMaker Pipeline for training or processing | Pipeline definition | ☐ | | |
| 02.5 | MLOps complete | 02 topics marked Complete | progress.md | ☐ | | |

### Phase 03 — Serverless

| # | Achievement | 要求 | Evidence | Status | Date | Evidence link |
|---|------------|------|----------|--------|------|----------------|
| 03.1 | API Gateway + Lambda | Build a Lambda behind API Gateway that returns a response | Endpoint URL + response | ☐ | | |
| 03.2 | Serverless complete | 03 topics marked Complete | progress.md | ☐ | | |

### Phase 04 — Data Engineering

| # | Achievement | 要求 | Evidence | Status | Date | Evidence link |
|---|------------|------|----------|--------|------|----------------|
| 04.1 | Glue job | Run a Glue ETL job over sample data | Job run + output | ☐ | | |
| 04.2 | Athena query | Query data in S3 with Athena | Query + result | ☐ | | |
| 04.3 | DynamoDB write/read | Put and get items in DynamoDB | CLI or code | ☐ | | |
| 04.4 | Data engineering complete | 04 topics marked Complete | progress.md | ☐ | | |

### Phase 05 — Monitoring

| # | Achievement | 要求 | Evidence | Status | Date | Evidence link |
|---|------------|------|----------|--------|------|----------------|
| 05.1 | CloudWatch alarm | Create an alarm that fires on a metric | Alarm config + invocation | ☐ | | |
| 05.2 | CloudTrail inspection | Find an API call in CloudTrail | Event record | ☐ | | |
| 05.3 | Monitoring complete | 05 topics marked Complete | progress.md | ☐ | | |

### Phase 06 — GenAI

| # | Achievement | 要求 | Evidence | Status | Date | Evidence link |
|---|------------|------|----------|--------|------|----------------|
| 06.1 | Bedrock call | Invoke a Bedrock model | Prompt + response | ☐ | | |
| 06.2 | JumpStart model | Deploy or test a JumpStart model | Model + invocation | ☐ | | |
| 06.3 | GenAI complete | 06 topics marked Complete | progress.md | ☐ | | |

### Phase 07 — Projects

| # | Achievement | 要求 | Evidence | Status | Date | Evidence link |
|---|------------|------|----------|--------|------|----------------|
| 07.1 | Batch inference on S3 | Complete the batch inference project from notes | Project output | ☐ | | |
| 07.2 | Model deployment pipeline | Complete the deployment pipeline project | Pipeline + deploy | ☐ | | |
| 07.3 | Real-time CV pipeline | Complete the real-time CV project | Project output | ☐ | | |
| 07.4 | Serverless ML API | Complete the serverless ML API project | Endpoint + response | ☐ | | |
| 07.5 | Two projects done | At least two of the above marked complete with evidence | progress.md + evidence | ☐ | | |

### Phase 08 — Tooling

| # | Achievement | 要求 | Evidence | Status | Date | Evidence link |
|---|------------|------|----------|--------|------|----------------|
| 08.1 | Dockerized ML workload | Containerize a simple ML script | Dockerfile + run | ☐ | | |
| 08.2 | Terraform infra | Provision an AWS resource with Terraform | TF config + apply | ☐ | | |
| 08.3 | Tooling complete | docker + terraform marked Complete | progress.md | ☐ | | |

### Phase 09 — Certifications

| # | Achievement | 要求 | Evidence | Status | Date | Evidence link |
|---|------------|------|----------|--------|------|----------------|
| 09.1 | ML Specialty revision | Pass the ML Specialty revision checklist unaided | Self-test notes | ☐ | | |
| 09.2 | ML Specialty scenarios | Answer all 5 scenario questions without peeking | Answers file | ☐ | | |
| 09.3 | Solutions Architect revision | Pass the SA revision checklist unaided | Self-test notes | ☐ | | |
| 09.4 | Cert prep complete | Both cert tracks' revision + scenarios done | progress.md + evidence | ☐ | | |

### Cross-phase achievements

| # | Achievement | 要求 | Evidence | Status | Date | Evidence link |
|---|------------|------|----------|--------|------|----------------|
| X.1 | End-to-end story | Draw from memory the full AWS ML flow: data → train → register → deploy → monitor | Diagram | ☐ | | |
| X.2 | Tradeoff explainer | Compare SageMaker, ECS, Lambda, and Bedrock for a given use case without guessing | Written answer | ☐ | | |
| X.3 | Secure workflow design | Design a secure ML workflow with IAM, networking, and logging controls | Design doc | ☐ | | |
| X.4 | Rollback story | Explain batch inference, real-time inference, and deployment rollback paths | Written answer | ☐ | | |
| X.5 | Job-ready | All phase folders at least Revised, two projects complete, exit criteria met | progress.md + evidence | ☐ | | |

---

## Scoring (optional, personal)

If you want a number:

- **Phase completion**: 1 point per phase where all topics are `Complete` and the phase's own achievement (e.g. 00.5) is checked.
- **Project points**: 2 points per completed project in phase 07.
- **Cross-phase points**: 3 points each for X.1–X.4; 5 points for X.5.
- **Cert points**: 2 points per passed revision checklist; 1 point per 5 scenario questions answered.

Max theoretical here: 9 phase points + 8 project points + 17 cross-phase points + 6 cert points = **40 points**.

Your score is a personal signal, not a grade. Treat it as "what have I actually done" rather than "how good am I."

---

## Logs folder

Create a `logs/` folder in this repo for evidence if you want it versioned alongside the notes:

```
logs/
├── 00-iam-explanation.md
├── 01-ecr-push.log
├── 07-batch-inference-output.md
└── ...
```

If you prefer not to version evidence, link to external notes or screenshots instead.
