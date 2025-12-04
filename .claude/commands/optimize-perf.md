---
description: Profile and optimize system performance.
allowed-tools: Read, Grep, Glob, Edit, Write, MultiEdit, Bash
---

## Context (auto-included)
- Git Status: !`git status -s || true`

## Your Task
1) **Measure**: Use the **performance-monitor** agent to gather current metrics/baselines for: "$ARGUMENTS".

2) **Profile**: Use the **performance-engineer** agent to analyze the code and identify bottlenecks.

3) **Optimize**: Use the **refactoring-expert** agent to implement optimizations.
   - Focus on critical paths and high-impact changes.

4) **Verify**: Compare new metrics against the baseline to confirm improvement.
