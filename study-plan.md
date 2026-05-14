# Study Plan

This repo is now strong on concept coverage. What was still missing was execution discipline: labs, revision, and project exit criteria. Use this plan to close that gap.

## How to use the repo

1. Read the topic note.
2. Review the matching PDF.
3. Open the related mind map or architecture diagram.
4. Do one hands-on AWS lab for that topic.
5. Update [progress.md](progress.md).
6. Write a short summary in your own words before moving on.

## Recommended sequence

### Phase 1

- Finish `00-foundations`.
- Goal: explain IAM, EC2, S3, and VPC without notes.
- Hands-on: create IAM roles, launch EC2, upload to S3, build a private subnet layout.

### Phase 2

- Finish `01-ml-infrastructure`.
- Goal: understand how SageMaker, ECR, and ECS fit together.
- Hands-on: build one Docker image, push it to ECR, and run it in ECS or SageMaker.

### Phase 3

- Finish `02-mlops-pipelines`.
- Goal: understand repeatable training and deployment automation.
- Hands-on: create one GitHub Actions workflow and one pipeline-driven model release path.

### Phase 4

- Finish `03-serverless` and `04-data-engineering`.
- Goal: know when to use serverless APIs versus containerized or managed inference.
- Hands-on: build one Lambda plus API Gateway flow and one S3 to Athena or Glue data flow.

### Phase 5

- Finish `05-monitoring` and `06-genai`.
- Goal: monitor systems correctly and understand where Bedrock fits.
- Hands-on: create CloudWatch alarms, inspect CloudTrail activity, and call one Bedrock or JumpStart flow.

### Phase 6

- Finish `07-projects`, `docker`, `terraform`, and the certification folders.
- Goal: connect isolated services into production-style architecture thinking.
- Hands-on: complete at least two end-to-end projects from the repo.

## Exit criteria

You should not mark the repo complete until all of these are true:

- You can explain each service in plain English and in architecture terms.
- You can draw the end-to-end AWS ML flow from memory.
- You have built at least two real AWS mini-projects yourself.
- You can compare SageMaker, ECS, Lambda, and Bedrock without guessing.
- You can secure an ML workflow with IAM, networking, and logging controls.
- You can explain batch inference, real-time inference, and deployment rollback paths.

## Confidence rubric

### Not enough yet

- You only read the notes.
- You can define services but cannot build with them.

### Good foundation

- You read the notes, reviewed the PDFs and diagrams, and completed labs for each phase.
- You can make reasonable service choices for common AWS ML problems.

### Job-ready direction

- You completed the notes, labs, and at least two projects.
- You can explain tradeoffs, cost, security, and observability in a real design discussion.

## Best next improvement

The next missing layer after this repo is practice under constraint:

- timed design questions
- troubleshooting broken IAM and networking setups
- deploying and fixing one real inference service
- explaining architecture decisions out loud
