# Security Policy

## Supported versions

Only the current `main` branch is supported. Issues reported against outdated forks or branches may not be addressed.

## Reporting a vulnerability

If you discover a security issue in this repository — for example, exposed secrets, broadly-scoped IAM policies that would be unsafe in production, or a deployment guide that encourages risky defaults — please report it responsibly.

### How to report

- Open a private security advisory on GitHub, or
- Email the maintainer directly if a private channel is preferred.

Please do **not** open a public issue for an unpatched security vulnerability.

### What to include

- Description of the issue
- Location (file, line, or configuration)
- Impact you expect
- A suggested fix, if you have one

### What to expect

- Acknowledgement within a reasonable time
- A fix or mitigation plan before public disclosure
- Credit for the report in the release notes, if you want it

## Security notes for learners

This repo contains learning materials, not production audit. When you apply these patterns:

- Rotate or delete any real credentials used during labs.
- Never paste real secrets into notes, scripts, or issues.
- Treat lab IAM roles as temporary; clean them up when the lab ends.
- Review any CloudFormation or Terraform before applying it to a real account.
- Watch your bill — undeleted endpoints, unattached volumes, and old model artifacts are the most common surprise costs.
