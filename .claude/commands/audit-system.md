---
description: Perform a comprehensive system audit covering architecture, security, and performance.
allowed-tools: Read, Grep, Glob, Bash
---

## Context (auto-included)
- Git Status: !`git status -s || true`

## Your Task
1) **Architecture Review**: Use the **system-architect** agent to review the specified component/module: "$ARGUMENTS".
   - Evaluate component boundaries, dependencies, and scalability.

2) **Security Check**: Use the **security-engineer** agent to scan for vulnerabilities.
   - Check for common security issues and compliance gaps.

3) **Performance Analysis**: Use the **performance-engineer** agent to identify bottlenecks.
   - Analyze critical paths and resource usage.

4) **Report**: Compile findings into a consolidated audit report in `/docs/audits/<component>-audit.md`.
