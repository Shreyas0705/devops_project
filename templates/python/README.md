# {{PROJECT_NAME}} (Python)

## Getting Started
- Create venv: `python -m venv .venv && source .venv/bin/activate` (or `Scripts\\activate` on Windows)
- Install dependencies: `pip install -r requirements.txt`
- Run tests: `pytest`

## Docker
- Build: `docker build -t {{PROJECT_NAME}} .`
- Run: `docker run -p 8000:8000 {{PROJECT_NAME}}`

## CI
GitHub Actions workflow is in `.github/workflows/ci.yml`.
