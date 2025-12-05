---
description: Analyze, fix, and verify bugs based on error logs or descriptions.
allowed-tools: Read, Grep, Glob, Edit, Write, MultiEdit, Bash
---

## Context (auto-included)
- Git Status: !`git status -s || true`

## Your Task
1) **Analyze**: Use the **error-coordinator** agent to analyze the bug description: "$ARGUMENTS".
   - Identify potential root causes and error patterns.

2) **Fix**: Use the **code-reviewer** agent to propose and implement a safe fix.
   - Ensure the fix addresses the root cause without introducing regressions.

3) **Verify**: Use the **qa-expert** agent to verify the fix.
   - Run relevant tests or suggest manual verification steps.

4) **Summarize**: Report the fix applied and any verification results.
