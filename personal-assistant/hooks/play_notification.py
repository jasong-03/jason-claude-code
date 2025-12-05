#!/usr/bin/env python3
"""
Cross-platform notification sound player for Claude Code hooks.
Plays system sounds - no user-specific paths required.
"""

import json
import platform
import subprocess
import sys
from pathlib import Path


def play_macos_sound() -> None:
    """Play notification sound on macOS."""
    # Try multiple system sounds in order of preference
    sounds = [
        "/System/Library/Sounds/Funk.aiff",
        "/System/Library/Sounds/Ping.aiff",
        "/System/Library/Sounds/Pop.aiff",
        "/System/Library/Sounds/Blow.aiff",
    ]
    for sound in sounds:
        if Path(sound).exists():
            subprocess.run(["afplay", sound], check=False, capture_output=True)
            return
    # Ultimate fallback: system beep
    subprocess.run(["osascript", "-e", "beep"], check=False, capture_output=True)


def play_windows_sound() -> None:
    """Play notification sound on Windows."""
    try:
        import winsound
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
    except Exception:
        # Fallback to PowerShell if winsound fails
        subprocess.run(
            [
                "powershell",
                "-c",
                "(New-Object Media.SoundPlayer 'C:\\Windows\\Media\\chimes.wav').PlaySync()",
            ],
            check=False,
            capture_output=True,
        )


def play_linux_sound() -> None:
    """Play notification sound on Linux."""
    # Try paplay (PulseAudio) first with various FreeDesktop sounds
    sound_files = [
        "/usr/share/sounds/freedesktop/stereo/complete.oga",
        "/usr/share/sounds/freedesktop/stereo/message.oga",
        "/usr/share/sounds/sound-icons/prompt.wav",
    ]
    for sound in sound_files:
        if Path(sound).exists():
            result = subprocess.run(
                ["paplay", sound], check=False, capture_output=True
            )
            if result.returncode == 0:
                return

    # Try aplay (ALSA) as fallback
    for sound in sound_files:
        if Path(sound).exists():
            result = subprocess.run(
                ["aplay", "-q", sound], check=False, capture_output=True
            )
            if result.returncode == 0:
                return


def play_sound() -> None:
    """Play a notification sound appropriate for the current OS."""
    system = platform.system()

    if system == "Darwin":
        play_macos_sound()
    elif system == "Windows":
        play_windows_sound()
    elif system == "Linux":
        play_linux_sound()
    # Silently do nothing on unsupported platforms


def main() -> None:
    # Consume stdin (hooks receive JSON input even if we don't use it)
    try:
        json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        pass  # Input is optional for notification hooks

    play_sound()
    sys.exit(0)


if __name__ == "__main__":
    main()

