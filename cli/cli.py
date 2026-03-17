import argparse
import sys
from pathlib import Path

# Ensure project root is on sys.path when executed directly
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from generator.generate import configure_logging, generate_project


def interactive_prompt() -> argparse.Namespace:
    name = input("Project name: ").strip()
    template = input("Template (nodejs/python) [nodejs]: ").strip() or "nodejs"
    git_choice = input("Initialize git? [Y/n]: ").strip().lower()
    no_git = git_choice == "n"
    return argparse.Namespace(name=name, template=template, no_git=no_git, verbose=False)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Git Repository Template Generator CLI")
    parser.add_argument("name", nargs="?", help="Project name.")
    parser.add_argument("--template", "-t", help="Template to use (nodejs, python).")
    parser.add_argument("--no-git", action="store_true", help="Skip git initialization.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging.")
    parser.add_argument("--interactive", "-i", action="store_true", help="Prompt for inputs.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.interactive or not args.name:
        args = interactive_prompt()

    configure_logging(args.verbose)
    destination = generate_project(args.name, args.template or "nodejs", init_git=not args.no_git)
    print(f"Project created at {Path(destination).resolve()}")


if __name__ == "__main__":
    main()
