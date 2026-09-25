# AWS ML Study Guide

> Structured, hands-on AWS learning path for machine learning infrastructure, MLOps, serverless, data engineering, monitoring, GenAI, and production projects — with LaTeX notes, mind maps, labs, and certification prep.

![GitHub repo size](https://img.shields.io/github/repo-size/Lourdhu02/aws.svg)
![GitHub commits](https://img.shields.io/github/commits/Lourdhu02/aws/main.svg)
![GitHub issues](https://img.shields.io/github/issues/Lourdhu02/aws.svg)
![License](https://img.shields.io/github/license/Lourdhu02/aws.svg)

---

## What this repo is

A complete AWS ML study system — not just notes. You get concept coverage (LaTeX topics + PDFs), execution discipline (hands-on labs, progress tracking, exit criteria), and certification readiness (revision checklists, scenario questions). The goal is to take you from "I've read about SageMaker" to "I can design and defend a production AWS ML architecture."

## What's inside

| Phase | Folder | Topics | Format |
|-------|--------|--------|--------|
| 00 | [`00-foundations/`](00-foundations) | IAM, EC2, S3, VPC | LaTeX + PDF |
| 01 | [`01-ml-infrastructure/`](01-ml-infrastructure) | ECR, ECS, SageMaker (core, training, deployment) | LaTeX + PDF |
| 02 | [`02-mlops-pipelines/`](02-mlops-pipelines) | CodePipeline, GitHub Actions, MLflow, SageMaker Pipelines | LaTeX + PDF |
| 03 | [`03-serverless/`](03-serverless) | API Gateway, Lambda | LaTeX + PDF |
| 04 | [`04-data-engineering/`](04-data-engineering) | RDS, Glue, Athena, DynamoDB | LaTeX + PDF |
| 05 | [`05-monitoring/`](05-monitoring) | CloudWatch, CloudTrail | LaTeX + PDF |
| 06 | [`06-genai/`](06-genai) | Bedrock, SageMaker JumpStart | LaTeX + PDF |
| 07 | [`07-projects/`](07-projects) | Batch inference, deployment pipeline, real-time CV, serverless ML API | LaTeX + PDF |
| 08 | [`docker/`](docker), [`terraform/`](terraform) | Docker for ML, Terraform for AWS ML infra | LaTeX + PDF |
| 09 | [`certifications/`](certifications) | AWS ML Specialty, AWS Solutions Architect | LaTeX + PDF + checklists + scenarios |

- **Master PDF**: [`AWS_ML_Study_Guide.pdf`](AWS_ML_Study_Guide.pdf) — compiled view of all topics.
- **Certification support**: revision checklists and scenario questions under each cert folder.

## Quick start

```bash
# 1. Clone
git clone https://github.com/Lourdhu02/aws.git
cd aws

# 2. Read one phase
cat 00-foundations/iam/iam_core.tex      # or open the .pdf

# 3. Do the lab (see study-plan.md for the sequence)
# 4. Track progress
cat progress.md                          # update your row

# 5. Recompile LaTeX (if you edit notes)
cd 00-foundations/iam
pdflatex iam_core.tex
```

## Learning path

| Phase | Scope | Exit goal |
|-------|-------|-----------|
| 00 | Foundations: IAM, EC2, S3, VPC | Explain all four without notes; build a private subnet layout |
| 01 | ML infrastructure: ECR, ECS, SageMaker | Build a Docker image, push to ECR, run in ECS or SageMaker |
| 02 | MLOps pipelines: CodePipeline, GitHub Actions, MLflow, SageMaker Pipelines | Create one GitHub Actions workflow and one pipeline-driven model release |
| 03 | Serverless: API Gateway, Lambda | Build a Lambda + API Gateway flow |
| 04 | Data engineering: RDS, Glue, Athena, DynamoDB | Build an S3-to-Athena or Glue data flow |
| 05 | Monitoring: CloudWatch, CloudTrail | Create CloudWatch alarms; inspect CloudTrail activity |
| 06 | GenAI: Bedrock, SageMaker JumpStart | Call one Bedrock or JumpStart flow |
| 07 | Projects: batch inference, deployment pipeline, real-time CV, serverless ML API | Complete at least two end-to-end projects |
| 08 | Tooling: Docker, Terraform | Containerize an ML workload; provision infra with Terraform |
| 09 | Certifications: AWS ML Specialty, AWS Solutions Architect | Pass revision checklist; answer scenario questions unaided |

## How to use this repo

1. Read the topic note (`.tex` or `.pdf`).
2. Review the matching mind map or architecture diagram (where available).
3. Do **one hands-on AWS lab** for that topic. Lab guides are in each topic folder's `labs/` subdirectory (coming soon — see [CONTRIBUTING.md](CONTRIBUTING.md) to help build them).
4. Update [`progress.md`](progress.md) with status, date, and evidence link.
5. Write a short summary in your own words before moving on.
6. Use [`study-plan.md`](study-plan.md) as the execution plan; use [`progress.md`](progress.md) as your tracker.

## Progress tracking

See [`progress.md`](progress.md). Each topic row has:

- **Status**: `Not Started` → `Reading` → `Hands-On` → `Revised` → `Complete`
- **Date**: when you last touched it
- **Evidence**: link to lab output, diagram you drew, or summary note

The [confidence rubric](study-plan.md#confidence-rubric) tells you when you're ready to move on.

## Certification prep

- **AWS ML Specialty**: [`certifications/aws-ml-specialty/`](certifications/aws-ml-specialty) — core notes, [revision checklist](certifications/aws-ml-specialty/notes/revision_checklist.md), [scenario questions](certifications/aws-ml-specialty/practice-tests/scenario_questions.md)
- **AWS Solutions Architect**: [`certifications/aws-solutions-architect/`](certifications/aws-solutions-architect) — core notes, [revision checklist](certifications/aws-solutions-architect/notes/revision_checklist.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version: lab guides, scenario answers, corrections, and new topic notes are all welcome. If you're building lab guides, follow the template in each topic folder's `labs/` directory.

## Repository structure

```
aws/
├── 00-foundations/          # IAM, EC2, S3, VPC
├── 01-ml-infrastructure/   # ECR, ECS, SageMaker
├── 02-mlops-pipelines/     # CodePipeline, GitHub Actions, MLflow, SageMaker Pipelines
├── 03-serverless/          # API Gateway, Lambda
├── 04-data-engineering/    # RDS, Glue, Athena, DynamoDB
├── 05-monitoring/          # CloudWatch, CloudTrail
├── 06-genai/               # Bedrock, SageMaker JumpStart
├── 07-projects/            # 4 end-to-end project notes
├── certifications/          # ML Specialty + Solutions Architect
├── docker/                 # Docker for ML workloads
├── terraform/              # Terraform for AWS ML infra
├── scripts/                 # Build/validation scripts
├── AWS_ML_Study_Guide.pdf   # Master compiled PDF
├── README.md               # This file
├── study-plan.md           # Execution plan
├── progress.md             # Tracker
├── deployment.md           # IaC deployment guide
├── services.md             # AWS service catalog
├── CHANGELOG.md            # Release history
├── LICENSE                 # MIT
├── .gitignore              # Ignored files
└── .github/                # Issue templates, PR template, CI
```

## License

MIT — see [LICENSE](LICENSE).

---

*Built for structured AWS ML learning. If this repo helps you, star it — it helps others find it.*
