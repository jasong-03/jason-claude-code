---
description: Plan, implement, and verify a feature end-to-end using specialized sub-agents.
allowed-tools: Read, Grep, Glob, Edit, Write, MultiEdit, Bash
---

## Context (auto-included)
- Git Status: !`git status -s || true`
- Node Version: !`node -v || echo "node not found"`
- NPM Version: !`npm -v || echo "npm not found"`

## Your Task
1) **Plan**: Use the **feature-plan** command (or logic) to analyze the request: "$ARGUMENTS". Produce a detailed implementation plan in `/docs/plans/<feature-name>.md` (create directory if needed).
   - Include: User stories, technical requirements, file changes, and verification steps.

2) **Implement**: Use the **fullstack-developer** sub-agent to implement the plan.
   - Instruct the agent to follow the plan strictly.
   - Ensure it updates tests and documentation.

3) **Verify**: Use the **qa-expert** sub-agent to review the implementation.
   - Run tests if applicable.
   - Check for code quality and potential issues.

4) **Summarize**: Provide a summary of what was done, any issues found, and next steps.
