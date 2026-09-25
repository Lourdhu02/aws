# CHANGELOG

All notable changes to this repository are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2025-08-06

### Added
- 27 LaTeX topic notes with compiled PDFs covering AWS ML learning path (phases 00–09)
- Master study guide PDF: `AWS_ML_Study_Guide.pdf`
- Certification support: AWS ML Specialty and AWS Solutions Architect notes, revision checklists, scenario questions
- Study plan with phased execution sequence and exit criteria
- Progress tracker template
- Deployment guide (IaC with CloudFormation and Terraform)
- AWS service catalog overview
- OpenCode developer agent configuration

### Organization
- Topic folders: each service has its own directory with `.tex` source and `.pdf` output
- Certification folders: notes + revision checklist + practice scenarios
- Phase-numbered top-level folders for sequential learning

### Coming soon
- Hands-on lab guides for each topic
- Architecture diagrams and mind maps
- Build/validation scripts in `scripts/`
- GitHub Actions CI for PDF rebuild verification
- Completed progress tracking with evidence links
