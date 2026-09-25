# Contributing to AWS ML Study Guide

Thanks for your interest. This repo is a learning system — notes, labs, and certification prep — and contributions that strengthen any of those three layers are welcome.

## What we accept

### Topic notes
- New AWS service or feature notes in the same LaTeX style as existing topics.
- Corrections or expansions to existing `.tex` files.
- When adding a topic, place it in the phase folder that matches its domain (see [README.md](README.md) table). If the phase doesn't exist yet, create it.

### Lab guides
- Hands-on lab write-ups for each topic. A lab guide lives in the topic folder under `labs/` and should let someone reproduce a real AWS interaction end-to-end.
- Minimum: what you build, what you need (IAM permissions, services), steps, and how to clean up.
- See the [lab template](.github/lab-template.md) below.

### Certification material
- Additional scenario questions, revision notes, or answers for the ML Specialty or Solutions Architect tracks.
- Answers should be clearly marked as spoiler content.

### Documentation
- README improvements, progress tracker enhancements, study plan updates, deployment guide expansions.

## What we don't accept

- Generated or copied content without attribution.
- Topic notes that don't follow the existing LaTeX structure.
- Anything that requires paid AWS credits without a clear cost warning.

## How to contribute

1. Fork the repo.
2. Create a branch from `main`.
3. Make your change. If you touch a `.tex` file, recompile the PDF and include both.
4. Open a PR using the [PR template](.github/PULL_REQUEST_TEMPLATE.md).
5. Label the PR appropriately (bug, enhancement, documentation).

## Lab guide template

Copy this into `<topic-folder>/labs/<lab-name>.md`:

```markdown
# <Lab Name>

## Goal

<!-- One sentence: what you will build or demonstrate. -->

## Prerequisites

- AWS account with permissions for <services>
- <any CLI tools, roles, or resources to create first>
- Estimated cost: <free tier / approximate cost / clean-up note>

## Steps

1. <step>
2. <step>

## What you should see

<!-- Expected output, console state, or behavior. -->

## Cleanup

<!-- Resources to delete so you don't keep paying. -->

## Notes

<!-- Gotchas, alternatives, or what to try next. -->
```

## Style

- LaTeX notes use 10pt two-column article, Helvetica/sans-serif, 0.7in margins.
- Keep notes concise and operational — explain what a service does, when to use it, and what to watch for.
- Use clear section headers: Overview, Core Concepts, How It Works, AI/ML Relevance, Operational Notes.

## Questions

Open an issue with the `[Feature]` or `[Bug]` prefix as appropriate.
