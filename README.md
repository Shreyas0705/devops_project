# Git Repository Template Generator

Generate standardized repositories with a single command.

## Architecture
- `generator/generate.py`: core logic to copy templates, replace `{{PROJECT_NAME}}`, and optionally initialize git.
- `cli/cli.py`: argparse/interactive CLI wrapper calling generator.
- `templates/`: ready-to-use Node.js and Python templates with Docker and GitHub Actions CI.
- `tests/`: unit tests for the generator.
- `Dockerfile`: containerizes the generator tool.

## Usage
```bash
pip install -r requirements.txt
python cli/cli.py myproject --template nodejs
python cli/cli.py --interactive  # guided mode
```

## Run in Docker
```bash
docker build -t repo-template-generator .
docker run --rm -v ${PWD}:/workspace -w /workspace repo-template-generator myproject --template python
```

## Development
- Run tests: `pytest`
- Add templates under `templates/<name>` with placeholders `{{PROJECT_NAME}}`.
