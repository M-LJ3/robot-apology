"""A tiny apology note from a robot that messed up.

This program drops one funny robot apology into /output/entry.txt.
"""

from pathlib import Path

APOLOGY_PATH = Path("/output/entry.txt")


def robot_sorry():
    """Return one humorous apology line from a robot."""
    return (
        "Sorry I deleted your files: my circuits crossed, "
        "and my backup had a backup plan to fail."
    )


def confirm_apology_saved(expected):
    """Make sure the saved apology is the one we intended."""
    saved = APOLOGY_PATH.read_text(encoding="utf-8")
    assert saved == expected


def main():
    note = robot_sorry()
    APOLOGY_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Leave the apology exactly as worded, no newline at the end.
    APOLOGY_PATH.write_text(note, encoding="utf-8")
    # Check the note on disk matches the apology, character for character.
    confirm_apology_saved(note)


if __name__ == "__main__":
    main()
