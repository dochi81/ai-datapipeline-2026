# Repository Guidelines

## Project Structure & Module Organization

This repository contains Korean-language data pipeline lessons built around Jupyter notebooks, rather than a packaged application.

- `Chapt 01/`: NumPy and introductory Pandas notebooks.
- `chapt 02/`: Pandas data cleaning, transformation, and aggregation.
- `chapt 03/`: Matplotlib and Seaborn visualization lessons.
- `chapt 04/`: HTML examples and Selenium scraping notebooks, including dynamic pages.
- `data/`: shared CSV, Excel, and text datasets, including saved exercise results.
- `README.md` and `image.png`: course overview, lesson links, and illustration.
- `requirements.txt`: pinned Python dependencies; `.vscode/`: editor settings.

Preserve existing chapter capitalization and Korean filenames. Add lessons to the relevant chapter and update README links. No dedicated source package or test directory currently exists.

## Build, Test, and Development Commands

Run these commands from the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m jupyter lab
```

These create an isolated environment, install dependencies, and launch the notebook editor. Select that environment's kernel. Check each notebook's relative file paths before running; chapter-local execution commonly requires `../data/`. Selenium exercises require Chrome and may require network access. There is no build command or configured test runner.

## Coding Style & Naming Conventions

Use four-space indentation, descriptive `snake_case` Python names, and conventional aliases such as `np`, `pd`, and `plt`. Keep cells focused and explain lesson steps with Markdown or Korean comments. Use descriptive notebook names such as `판다스집계.ipynb`. Prefer relative dataset paths over machine-specific absolute paths. No formatter or linter is configured; avoid unrelated notebook metadata or output changes.

## Testing Guidelines

Restart the kernel and run modified notebooks from top to bottom. Check dataframe columns, row counts, missing values, aggregates, and rendered charts against the exercise expectations. For scraping changes, verify selectors and wait conditions, inspect collected records, and close the driver. Review any generated dataset changes before committing. No automated test framework, test naming convention, or coverage threshold is established.

## Commit & Pull Request Guidelines

History uses short Korean lesson summaries and occasional English `Update ...` messages; no strict prefix convention is established. Write concise, descriptive commits scoped to one lesson or change. Pull requests should identify affected notebooks, explain the change, and describe validation and browser/network prerequisites. Link relevant issues when available and include screenshots for meaningful chart or HTML changes. Exclude credentials, virtual environments, and incidental generated files.
