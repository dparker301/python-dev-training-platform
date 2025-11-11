#!/usr/bin/env python3
import json, os, argparse, subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).parent
CATALOG = json.loads((ROOT / "modules" / "catalog.json").read_text())
PROGRESS_FILE = ROOT / "progress.json"

def load_progress():
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text())
    return {"completed": [], "started": []}

def save_progress(p):
    PROGRESS_FILE.write_text(json.dumps(p, indent=2))

def list_items():
    print("Tracks:")
    for t in CATALOG["tracks"]:
        print(f"  - {t['id']:22} {t['title']} — {t['desc']}")
    print("\nLabs:")
    for l in CATALOG["labs"]:
        print(f"  - {l['id']:28} [{l['track']}] {l['title']} ({l['level']})")

def open_lab(lab_id):
    lab_path = ROOT / "projects" / lab_id
    if not lab_path.exists():
        print(f"Lab not found at {lab_path}")
        sys.exit(1)
    readme = lab_path / "README.md"
    if readme.exists():
        if sys.platform.startswith("win"):
            os.startfile(readme)  # type: ignore
        else:
            subprocess.run(["xdg-open" if sys.platform.startswith("linux") else "open", str(readme)], check=False)
    else:
        print(str(lab_path))

def start_lab(lab_id):
    p = load_progress()
    if lab_id not in p["started"]:
        p["started"].append(lab_id)
        save_progress(p)
        print(f"Marked as started: {lab_id}")
    else:
        print(f"Already started: {lab_id}")
    open_lab(lab_id)

def complete_lab(lab_id):
    p = load_progress()
    if lab_id not in p["completed"]:
        p["completed"].append(lab_id)
        save_progress(p)
        print(f"Marked as completed: {lab_id}")
    else:
        print(f"Already completed: {lab_id}")

def main():
    ap = argparse.ArgumentParser(description="Python Dev Training Platform")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("list", help="List tracks and labs")
    sp = sub.add_parser("open", help="Open a lab README"); sp.add_argument("lab_id")
    sp2 = sub.add_parser("start", help="Mark started + open README"); sp2.add_argument("lab_id")
    sp3 = sub.add_parser("complete", help="Mark a lab complete"); sp3.add_argument("lab_id")
    args = ap.parse_args()
    if args.cmd == "list": list_items()
    elif args.cmd == "open": open_lab(args.lab_id)
    elif args.cmd == "start": start_lab(args.lab_id)
    elif args.cmd == "complete": complete_lab(args.lab_id)
    else: ap.print_help()

if __name__ == "__main__":
    main()
