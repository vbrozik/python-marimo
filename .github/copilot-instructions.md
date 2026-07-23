# GitHub Copilot Instructions for python-marimo

## Project Context
- **Project Name**: python-marimo
- **Python Version**: 3.14+
- **Package Manager**: `uv`
- **Build System**: `uv_build`

## Tools and Libraries
- Use `marimo` for interactive notebooks.
- Use `uv` for package management and running scripts (e.g., `uv run pytest`).
- Use `pyproject.toml` for project configuration.
- Use `mypy` for static type checking.
- Use `ruff`, `flake8` and `pylint` for code linting.
- Use `isort` for sorting imports.
- Use `pytest` for testing.

## Code Style
- Follow **PEP 8** style guidelines.
- Adhere to `flake8` and `pylint` standards.
- Indent with **4 spaces**.
- Use modern Python 3.14+ features.
- Do not use obsolete features.

### Code Structure
- **Single Responsibility**: Do not combine different functionalities in a single function.
- **Testability**: Make functions testable and reusable.
- **Source Directory**:
    - All package source code resides in `src/`.
    - Marimo notebooks reside in `src/notebooks/`.
    - Utility modules reside in `src/utils/`.
- **Tests Directory**: Unit tests reside in `tests/`.

### Identifiers
- Use descriptive variable and function names.
- Avoid abbreviations unless they are widely recognized.

### Type Hints
- **Mandatory**: Use type hints for function signatures, variables, and class attributes.
- **Tests**: Use type hints in test code as well.
- **Future Import**: Always include `from __future__ import annotations` at the top of every file to enable postponed evaluation of type annotations.

### Docstrings
- **Style**: Use **Google style** for docstrings.
- **Coverage**: Document all public modules, classes, class variables, methods, and functions.
- **Format**:
    - Module docstring at the top of the file, immediately after the shebang (if present), separated by a blank line.
    - First line: Short summary starting with a capital letter, ending with a period, in imperative mood (e.g., "Calculate the sum.").

## Testing
- Use `pytest` as the testing framework.
- Structure tests to mirror the source code hierarchy where possible.
- Use test parameterization to reduce code duplication.
- Use fixtures for setup and teardown of test environments.
- Naming Conventions:
    - Test files: Prefix with `test_` (e.g., `test_module.py`).
    - Test functions/methods: Prefix with `test_` (e.g., `test_functionality()`).
    - Fixture functions: Prefix with `fixture_` (e.g., `fixture_sample_data()`) and define name without the prefix (e.g. `name="sample_data"`) to avoid global namespace shadowing.
- Use `conftest.py` for shared test fixtures and configurations.
