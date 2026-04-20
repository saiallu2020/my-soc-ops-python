# Agent Instructions

## Development Checklist (mandatory before every commit)

1. `uv run ruff check .` — lint passes
2. `uv run pytest` — all tests pass
3. No unused imports or variables

## Project

**Soc Ops** — Social Bingo game (Python 3.13 / FastAPI / Jinja2 / HTMX). Players match prompts on a 5×5 board to get bingo.

## Architecture

- `app/main.py` — Routes & HTMX endpoints
- `app/models.py` — Pydantic models (`frozen=True`): `GameState`, `BingoSquareData`, `BingoLine`
- `app/game_logic.py` — Board generation, toggling, bingo detection
- `app/game_service.py` — `GameSession` dataclass, in-memory session store
- `app/data.py` — 24 prompts + FREE SPACE
- `app/templates/` — Jinja2 + HTMX partials (`components/`)
- `app/static/css/app.css` — Custom utilities (see `.github/instructions/css-utilities.instructions.md`)
- `tests/` — `test_api.py` (TestClient), `test_game_logic.py`

## Conventions

- snake_case, type hints on all functions, Ruff (E/F/I/N/W, line-length 88)
- Routes return partial HTML via `TemplateResponse` for HTMX swap — never full pages
- Immutable models: use `model_copy(update=...)` instead of mutation
- Sessions: cookie-based via `SessionMiddleware`, stored in-memory dict
- Never use VS Code Simple Browser — HTMX requires a full browser

## Docs

[README.md](README.md) · [workshop/](workshop/) · [CONTRIBUTING.md](CONTRIBUTING.md)
