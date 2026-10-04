#!/usr/bin/env python3
"""
LYN_0 Academy - Mission 01 installer.

Installs SOUL.md and USER.md into your Hermes home.

    python install.py            install the templates (backs up existing files)
    python install.py --check    verify the files are in place, change nothing
    python install.py --force    overwrite without asking

Works on Windows, macOS and Linux. No dependencies.
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

SOUL_DST = "SOUL.md"
USER_REL = Path("memories") / "USER.md"

BANNER = r"""
  LYN_0 Academy - Mission 01
  Your AI learns who it's working for
"""


def hermes_home() -> Path:
    """Resolve $HERMES_HOME, falling back to the per-OS default."""
    env = os.environ.get("HERMES_HOME") or os.environ.get("HERMES_AGENT_HOME")
    if env:
        return Path(env).expanduser()

    if sys.platform == "win32":
        base = os.environ.get("LOCALAPPDATA") or (Path.home() / "AppData" / "Local")
        return Path(base) / "hermes"
    return Path.home() / ".hermes"


def report(label: str, path: Path, note: str = "") -> None:
    mark = "OK " if path.exists() else "-- "
    extra = f"  ({note})" if note else ""
    print(f"  [{mark}] {label:<9} {path}{extra}")


def do_check(home: Path) -> bool:
    soul = home / SOUL_DST
    user = home / USER_REL
    print("\nChecking installation\n")
    report("SOUL.md", soul, "who your AI is" if soul.exists() else "not found")
    report("USER.md", user, "who it works for" if user.exists() else "not found")

    templates = Path(__file__).parent / "files"
    empty_soul = soul.exists() and "___" in soul.read_text(encoding="utf-8", errors="ignore")
    empty_user = user.exists() and "___" in user.read_text(encoding="utf-8", errors="ignore")

    print()
    if empty_soul:
        print("  SOUL.md still has ___ blanks in it. Edit it, then rerun --check.")
    if empty_user:
        print("  USER.md still has ___ blanks in it. Edit it, then rerun --check.")
    if not templates.is_dir():
        print(f"  Template folder missing: {templates}")

    ok = soul.exists() and user.exists() and not empty_soul and not empty_user
    print("\n" + ("All set. Run the six checks in test.md." if ok
                  else "Not done yet. Finish the blanks and rerun this."))
    return ok


def backup(path: Path, home: Path) -> Path | None:
    if not path.exists():
        return None
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    dest = home / "backups" / f"{path.name}.{stamp}.bak"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, dest)
    return dest


def do_install(home: Path, force: bool) -> None:
    files = Path(__file__).parent / "files"
    src_soul = files / "SOUL_TEMPLATE.md"
    src_user = files / "USER_TEMPLATE.md"

    for src in (src_soul, src_user):
        if not src.exists():
            print(f"  Missing template: {src}")
            sys.exit(1)

    home.mkdir(parents=True, exist_ok=True)
    (home / "memories").mkdir(parents=True, exist_ok=True)

    for src, dst in ((src_soul, home / SOUL_DST), (src_user, home / USER_REL)):
        if dst.exists() and not force:
            print(f"\n  {dst.name} already exists.")
            ans = input("  Back it up and overwrite? [y/N] ").strip().lower()
            if ans not in ("y", "yes"):
                print(f"  Kept your {dst.name}. Skipped.")
                continue
        bak = backup(dst, home)
        if bak:
            print(f"\n  Backed up to {bak}")
        shutil.copy2(src, dst)
        print(f"  Installed {dst}")

    print("\n  Next: open both files, replace every ___ with your own answers,")
    print("  then run: python install.py --check")


def main() -> None:
    ap = argparse.ArgumentParser(description="LYN_0 Academy - Mission 01 installer")
    ap.add_argument("--check", action="store_true", help="verify only, change nothing")
    ap.add_argument("--force", action="store_true", help="overwrite without asking")
    ap.add_argument("--home", type=Path, help="override the Hermes home path")
    args = ap.parse_args()

    home = args.home.expanduser() if args.home else hermes_home()
    print(BANNER)
    print(f"Hermes home: {home}")

    if args.check:
        sys.exit(0 if do_check(home) else 1)
    do_install(home, args.force)
    print()


if __name__ == "__main__":
    main()