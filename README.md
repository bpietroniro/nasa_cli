> "Here's what you do, *you fold it in.*"
> — Moira Rose

Whimsical project to practice building CLIs via Click and familiarize with Jinja2 templating.

Fetches the "Astronomy Pic of the Day" from the NASA public API, renders an HTML template using the response data, and displays it in the default browser.

## Installation

**Prerequisites:** Python 3.11+

```bash
# Clone the repository
git clone <repo-url>
cd nasa_cli
```

### With `uv`

```bash
# Install dependencies (uv creates and manages the virtual environment automatically)
uv sync
```

### With `pip`

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install .
```

## Usage

```bash
python main.py
```