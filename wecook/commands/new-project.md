---
description: Kick off a new feature or project with proper planning and architecture.
allowed-tools: Read, Grep, Glob, Bash
---

## Context (auto-included)
- Git Status: !`git status -s || true`

## Your Task
1) **Requirements**: Use the **requirements-analyst** agent to clarify scope and user stories for: "$ARGUMENTS".
   - Create a PRD or requirements doc.

2) **Tech Stack**: Use the **tech-stack-researcher** agent to recommend tools and libraries.
   - Evaluate options based on the requirements.

3) **Architecture**: Use the **system-architect** agent to design the high-level structure.
   - Define component boundaries and data flow.

4) **Plan**: Output a comprehensive project initiation document in `/docs/plans/<project>-init.md`.
