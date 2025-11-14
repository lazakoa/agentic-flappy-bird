# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flappy Bird game implementation using pygame. The game is organized into modules under the `app/` directory with a comprehensive test suite in `tests/`.

## Development Commands

**Run the game:**
```bash
uv run python main.py
```

**Add dependencies:**
```bash
uv add <package-name>
```

**Sync dependencies:**
```bash
uv sync
```

**Important**: Never install packages globally with uv. All installations should be local to the project using `uv add` which automatically installs to the local `.venv`.

## Code Quality Tools

This project uses pre-commit hooks for code quality:

**Run pre-commit on all files:**
```bash
uv run pre-commit run --all-files
```

**Run pre-commit on staged files:**
```bash
uv run pre-commit run
```

**Hooks configured:**
- **ruff**: Linter with auto-fix
- **ruff-format**: Code formatter
- **mypy**: Static type checker (configured in strict mode)

Pre-commit hooks run automatically on `git commit`. If hooks modify files, review the changes and re-stage them.

**Code standards:**
- All functions, methods, and variables should have type hints
- Code must pass mypy strict mode checks (configured in pyproject.toml)

## Testing

This project uses Python's built-in `unittest` framework for testing.

**Run all tests:**
```bash
uv run python -m unittest discover -s tests
```

**Run all tests with verbose output:**
```bash
uv run python -m unittest discover -s tests -v
```

**Run a specific test file:**
```bash
uv run python -m unittest tests.test_bird
```

**Run a specific test class:**
```bash
uv run python -m unittest tests.test_bird.TestBird
```

**Run a specific test method:**
```bash
uv run python -m unittest tests.test_bird.TestBird.test_initialization
```

**Test structure:**
- `tests/test_bird.py` - Tests for Bird class
- `tests/test_pipe.py` - Tests for Pipe class
- `tests/test_game.py` - Tests for Game class

## Project Structure

The game follows a modular class-based architecture:

**Main modules:**
- `main.py` - Entry point for the game
- `app/constants.py` - Game constants and configuration
- `app/bird.py` - Bird class: physics, rendering, collision detection
- `app/pipe.py` - Pipe class: obstacle management, collision detection
- `app/game.py` - Game class: main game loop, state management, rendering

**Architecture:**
- **Bird class** (`app/bird.py`): Handles bird physics (gravity, jump mechanics), rendering, and collision detection via bounding rectangles
- **Pipe class** (`app/pipe.py`): Manages pipe position, movement, rendering (with decorative caps), collision detection, and scoring logic
- **Game class** (`app/game.py`): Main game loop that orchestrates:
  - Event handling (jump, pause, restart, quit)
  - Game state management (running, paused, game over)
  - Update cycle for all game objects
  - Rendering pipeline with layered drawing (background, pipes, bird, UI overlays)
  - There should be no direct access to an instatiated object's attributes, go through a getter method.

## Game Controls

- **SPACE**: Jump when playing; restart when game over
- **ESC**: Pause and unpause during gameplay
- **Window close**: Exit the game

## Key Implementation Details

- Physics system uses constant gravity with impulse-based jumping
- Pipes spawn at fixed intervals (PIPE_FREQUENCY) with randomized gap positions
- Collision detection uses pygame's rect-based collision system
- Pause state freezes all game updates but maintains rendering
- Score increments when bird's x-position passes pipe's right edge (tracked via `passed` flag)
- Game over triggers on ceiling/floor collision or pipe collision

## Known Issues

- 2025-11-14: Nuitka doesn't work with uv right now, don't bother trying to run in through uv.
