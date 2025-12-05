# Personal Assistant

This plugin turns Claude Code into your personal assistant. It contains a context system, memory management, and hooks to play notification sounds.

## Requirements

**[NOTE]** You must already have uv installed and the AI Launchpad marketplace added, see [main README](../README.md) if you haven't already.

No additional requirements.

## Installation

1. Start Claude Code anywhere.

```bash
claude
```

2. Install the plugin

```bash
/plugin install personal-assistant@ai-launchpad-marketplace
```

You can also do this interactively by running `/plugin`.

3. Restart Claude Code for the changes to take effect.

## Plugin Structure

```
personal-assistant/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── README.md                # Plugin documentation
├── context/                 # Context system
│   ├── CLAUDE.md            # Root context file
│   └── memory/              # Memory system
│       ├── memories.md      # Memories file
│       └── CLAUDE.md        # Memory system context file
└── hooks/                   # Hooks system
    ├── hooks.json           # Hooks configuration
    ├── load_context_system.py # Hook to load context system
    └── play_notification.py # Hook to play notification sound
```