#!/usr/bin/env python3
"""
UserPromptSubmit hook to load context system into Claude's context.
"""

import json
import sys
from pathlib import Path


def get_hook_root() -> Path:
    """
    Get the root directory for the hook's context system.
    Uses the hook file's location to find the sibling 'context' folder.

    Structure expected:
        <hook_root>/
            hooks/
                load_context_system.py  (this file)
            context/
                CLAUDE.md
    """
    hook_dir = Path(__file__).resolve().parent  # hooks/
    hook_root = hook_dir.parent  # personal-assistant/ (or whatever it's named)
    return hook_root


def ensure_file(path: Path, default: str = "") -> None:
    """Create file with default content if it doesn't exist."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(default, encoding="utf-8")


def main() -> None:
    # Parse hook input from stdin (required even if unused, to consume the input)
    try:
        json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
        sys.exit(1)

    # Get the context file path relative to this hook's location
    hook_root = get_hook_root()
    context_path = hook_root / "context" / "CLAUDE.md"

    # Read the context file, creating it if it doesn't exist
    try:
        ensure_file(context_path, "# Context\n\nAdd your context instructions here.\n")
        context = context_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"Warning: Unable to read context file: {e}", file=sys.stderr)
        context = ""

    # Output the context to be injected into Claude's session
    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": context,
        }
    }
    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
