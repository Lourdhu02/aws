# AWS Service Catalog

A quick-reference map of the AWS services covered in this repo, grouped by domain.

## Compute

| Service | What it is | Where it appears in this repo |
|---------|-----------|-------------------------------|
| EC2 | Virtual servers; base compute unit for many workloads | Phase 00 (foundations), Phase 01 (ML infra) |
| Lambda | Serverless functions; event-driven, scale-to-zero | Phase 03 (serverless), Phase 07 (serverless ML API) |
| ECS | Container orchestration on AWS | Phase 01 (ML infrastructure) |
| SageMaker | Managed ML platform: training, deployment, pipelines, JumpStart | Phase 01, Phase 02, Phase 06 |

## Storage

| Service | What it is | Where it appears |
|---------|-----------|-----------------|
| S3 | Object storage; data, model artifacts, logs | Phase 00, everywhere in ML workflows |
| ECR | Container image registry | Phase 01 |

## Database

| Service | What it is | Where it appears |
|---------|-----------|-----------------|
| RDS | Managed relational databases | Phase 04 (data engineering) |
| DynamoDB | Managed NoSQL | Phase 04 |

## Data engineering

| Service | What it is | Where it appears |
|---------|-----------|-----------------|
| Glue | Managed ETL | Phase 04 |
| Athena | Serverless SQL over S3 | Phase 04 |

## Pipelines and automation

| Service | What it is | Where it appears |
|---------|-----------|-----------------|
| CodePipeline | AWS-native CI/CD pipeline | Phase 02 |
| GitHub Actions | CI/CD integrated with GitHub repos | Phase 02 |
| SageMaker Pipelines | ML training/deployment pipeline | Phase 02 |

## Monitoring and governance

| Service | What it is | Where it appears |
|---------|-----------|-----------------|
| CloudWatch | Metrics, logs, alarms, dashboards | Phase 05 |
| CloudTrail | API audit trail | Phase 05 |
| IAM | Identity and access management | Phase 00, foundational throughout |

## GenAI

| Service | What it is | Where it appears |
|---------|-----------|-----------------|
| Bedrock | Managed foundation model access | Phase 06 |
| SageMaker JumpStart | Pre-built models and solutions | Phase 06 |

## Infrastructure as code

| Tool | What it is | Where it appears |
|------|-----------|-----------------|
| CloudFormation | AWS-native IaC | deployment.md, Phase 09 |
| Terraform | Multi-cloud IaC | terraform/, Phase 08, deployment.md |

## Container tooling

| Tool | What it is | Where it appears |
|------|-----------|-----------------|
| Docker | Container build and runtime | docker/, Phase 08 |

## Foundational services

These appear across every phase rather than in one folder:

- **IAM** — access control for everything
- **S3** — data and artifact storage for everything ML
- **CloudWatch** — observability for everything deployed
- **CloudTrail** — audit trail for everything

## How to use this catalog

- Use it to locate where a service is covered in the notes.
- Use it to check whether you can explain the service and where it fits in an ML architecture.
- Use it as a checklist when reviewing a design: have you accounted for compute, storage, data, pipeline, monitoring, and access control?
