import shutil
import uuid

import pytest

from generator.generate import GenerationError, generate_project, validate_template


def test_validate_template_invalid():
    with pytest.raises(GenerationError):
        validate_template("unknown")


def test_generate_project_creates_files():
    project_name = f"sample_{uuid.uuid4().hex[:8]}"
    dest = generate_project(project_name, "python", init_git=False)
    try:
        assert (dest / "README.md").exists()
        assert "{{PROJECT_NAME}}" not in (dest / "README.md").read_text()
        assert (dest / ".github" / "workflows" / "ci.yml").exists()
    finally:
        shutil.rmtree(dest, ignore_errors=True)
