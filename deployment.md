# Deployment Guide

## Infrastructure as Code

This repo's production-style projects should be deployable through code, not console clicks. Two IaC paths are supported: **CloudFormation** for AWS-native stacks and **Terraform** for multi-cloud or team-standardized infra.

## When to use which

| Approach | Best for | Notes |
|----------|----------|-------|
| CloudFormation | AWS-only stacks, quick prototyping, AWS-native integration | YAML or JSON; AWS SAM extends it for serverless |
| Terraform | Teams standardizing across clouds, state-managed infra, reusable modules | HCL; state file is the source of truth — manage it carefully |

## General deployment principles

1. **Never deploy production infra from a laptop session alone.** Use a pipeline (GitHub Actions, CodePipeline) so deployments are reviewed, repeatable, and auditable.
2. **Separate environments.** Dev, staging, and production should be different accounts or at minimum different stacks with different parameters.
3. **Parameterize everything that changes per environment** — instance sizes, bucket names, model artifact paths, endpoint names.
4. **Drift happens.** Check for drift periodically; reconcile before it accumulates.
5. **Delete what you build.** Every lab and project should have a cleanup path. Unused endpoints, unattached EBS volumes, and old model artifacts are the most common surprise bills.

## Deployment flow for ML workloads

A typical ML deployment path through IaC:

1. **Data and artifacts**
   - S3 buckets for raw data, processed data, model artifacts, and logs.
   - Bucket policies and encryption configured as part of the stack.
2. **Compute**
   - ECR repository for the container image, or a SageMaker model / endpoint configuration.
   - ECS task definition and service, or Lambda function and configuration.
   - IAM roles scoped to only the S3 paths, logs, and secrets the workload needs.
3. **Networking**
   - VPC layout if the workload needs private subnets, NAT, or VPC endpoints.
   - Security groups that allow only the traffic the service actually uses.
4. **Observability**
   - CloudWatch log groups, alarms, and dashboards as part of the same deploy.
   - CloudTrail enabled account-wide (usually not per-stack).
5. **Release control**
   - Pipeline that builds the image, runs validation, and promotes the model or service only after checks pass.
   - Rollback path: previous image tag, previous model version, or previous endpoint configuration.

## Clean up after every lab

Before you close a lab or project:

- Delete endpoint configurations and endpoints.
- Delete or empty S3 buckets created for the lab.
- Delete ECR images if they are lab-only.
- Delete CloudFormation stacks or run `terraform destroy` for the lab's resource set.
- Remove IAM roles and policies created for the lab if they are not reused.

If cost is a concern, prefer serverless and on-demand options during learning, and run destruction commands immediately after verifying the lab worked.

## Related notes

- [`terraform/terraform_core.tex`](terraform/terraform_core.tex) — Terraform fundamentals for AWS ML infra.
- [`docker/docker_core.tex`](docker/docker_core.tex) — containerizing ML workloads before deployment.
- Phase 07 project notes — end-to-end deployment scenarios (batch inference, real-time CV, serverless ML API).
