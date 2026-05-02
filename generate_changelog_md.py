import subprocess
import re
import sys
import os
from collections import defaultdict


def get_repo_root():
    """
    Dynamically find the git repository root.
    """
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError("Not inside a git repository")

    return result.stdout.strip()


PROJECT_ROOT = get_repo_root()

TYPE_MAP = {
    "feat": "Features",
    "refactor": "Refactoring",
    "fix": "Fixes",
    "chore": "Maintenance",
    "docs": "Documentation"
}

CHANGELOG_PATH = os.path.join(PROJECT_ROOT, "CHANGELOG.md")


def get_git_commits():
    """
    Extract commit history from git.
    Supports formats like:
    v0.1.0 feat: message
    feat: message
    """

    result = subprocess.run(
        [
            "git",
            "log",
            "--pretty=format:%ad|%s",
            "--date=short"
        ],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT
    )

    if result.returncode != 0:
        print("Git error:", result.stderr)
        return []

    commits = []

    # Version optional now
    pattern = r"(v\d+\.\d+\.\d+)?\s*(\w+):\s+(.*)"

    for line in result.stdout.split("\n"):
        try:
            date, message = line.split("|", 1)
            match = re.match(pattern, message)

            if not match:
                continue

            version = match.group(1) or "Unreleased"
            ctype = match.group(2)
            desc = match.group(3)

            section = TYPE_MAP.get(ctype, "Other")

            commits.append({
                "date": date,
                "version": version,
                "section": section,
                "desc": desc
            })

        except ValueError:
            continue

    # Ensure chronological order
    commits.sort(key=lambda x: x["date"])

    return commits


def write_changelog(commits):
    """
    Writes grouped markdown changelog.
    """

    grouped = defaultdict(list)

    for c in commits:
        grouped[c["section"]].append(c)

    with open(CHANGELOG_PATH, "w", encoding="utf-8") as f:

        f.write("# Changelog\n\n")
        f.write("All changes are documented here.\n\n---\n\n")

        for section in TYPE_MAP.values():

            if section not in grouped:
                continue

            f.write(f"# {section}\n\n")
            f.write("| Date | Version | Change |\n")
            f.write("|------|---------|--------|\n")

            for c in grouped[section]:
                f.write(
                    f"| {c['date']} | {c['version']} | {c['desc']} |\n"
                )

            f.write("\n---\n\n")


def main():
    try:
        commits = get_git_commits()
    except RuntimeError as e:
        print(e)
        return

    if not commits:
        print("No valid commits found.")
        return

    write_changelog(commits)

    print(f"CHANGELOG updated at: {CHANGELOG_PATH}")


if __name__ == "__main__":
    main()