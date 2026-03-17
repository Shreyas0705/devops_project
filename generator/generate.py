import argparse
import logging
import shutil
import subprocess
from pathlib import Path
from typing import Dict

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = ROOT / "templates"


class GenerationError(Exception):
    """Custom exception for generator failures."""


def configure_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def validate_template(template_name: str) -> Path:
    template_path = TEMPLATES_DIR / template_name
    if not template_path.exists() or not template_path.is_dir():
        available = ", ".join(sorted(p.name for p in TEMPLATES_DIR.iterdir() if p.is_dir()))
        raise GenerationError(f"Template '{template_name}' not found. Available: {available}")
    return template_path


def replace_placeholders(file_path: Path, context: Dict[str, str]) -> None:
    try:
        content = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return  # skip binary files
    for key, value in context.items():
        content = content.replace(f"{{{{{key}}}}}", value)
    file_path.write_text(content, encoding="utf-8")


def copy_template(template_path: Path, destination: Path, context: Dict[str, str]) -> None:
    if destination.exists():
        raise GenerationError(f"Destination '{destination}' already exists.")
    logging.info("Copying template from %s to %s", template_path, destination)
    shutil.copytree(template_path, destination)
    for file_path in destination.rglob("*"):
        if file_path.is_file():
            replace_placeholders(file_path, context)


def run_git_commands(destination: Path) -> None:
    cmds = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-m", "Initial commit"],
    ]
    for cmd in cmds:
        logging.debug("Running git command: %s", " ".join(cmd))
        result = subprocess.run(cmd, cwd=destination, capture_output=True, text=True)
        if result.returncode != 0:
            raise GenerationError(
                f"Git command failed: {' '.join(cmd)}\nSTDOUT:{result.stdout}\nSTDERR:{result.stderr}"
            )


def generate_project(project_name: str, template: str, init_git: bool = True) -> Path:
    template_path = validate_template(template)
    destination = Path.cwd() / project_name
    context = {"PROJECT_NAME": project_name}
    copy_template(template_path, destination, context)
    if init_git:
        run_git_commands(destination)
    logging.info("Project '%s' generated at %s", project_name, destination)
    return destination


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a project from a template.")
    parser.add_argument("name", help="Name of the new project.")
    parser.add_argument("--template", "-t", default="nodejs", help="Template to use (nodejs, python).")
    parser.add_argument("--no-git", action="store_true", help="Skip git initialization.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    configure_logging(args.verbose)
    try:
        generate_project(args.name, args.template, init_git=not args.no_git)
    except GenerationError as exc:
        logging.error(str(exc))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
