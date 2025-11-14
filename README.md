# Flappy Bird

A Python implementation of the classic Flappy Bird game using pygame with a modular, class-based architecture.

## Features

- Classic Flappy Bird gameplay mechanics
- Physics-based bird movement with gravity and jump impulse
- Procedurally generated pipes with randomized gaps
- Score tracking system
- Pause functionality
- Game over and restart mechanics
- Comprehensive test suite
- Type-safe code with strict mypy checking
- Code quality enforcement via pre-commit hooks

## Requirements

- Python >= 3.13
- [uv](https://docs.astral.sh/uv/) package manager

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd agentic-flappy-bird
```

2. Install dependencies:
```bash
uv sync
```

This will create a local virtual environment (`.venv`) and install all required packages.

## Running the Game

```bash
uv run python main.py
```

## Game Controls

| Key | Action |
|-----|--------|
| `SPACE` | Jump (during gameplay) / Restart (when game over) |
| `ESC` | Pause/Unpause |
| Close window | Exit game |

## Development

### Adding Dependencies

```bash
uv add <package-name>
```

**Important**: Never install packages globally. Always use `uv add` which installs to the local `.venv`.

### Code Quality

This project enforces code quality through pre-commit hooks:

**Run on all files:**
```bash
uv run pre-commit run --all-files
```

**Run on staged files:**
```bash
uv run pre-commit run
```

**Configured hooks:**
- **ruff**: Fast Python linter with auto-fix
- **ruff-format**: Code formatter
- **mypy**: Static type checker in strict mode

Pre-commit hooks run automatically on `git commit`. If hooks modify files, review and re-stage them before committing again.

**Code standards:**
- All functions, methods, and variables must have type hints
- Code must pass mypy strict mode checks
- Follow PEP 8 style guidelines (enforced by ruff)

### Testing

The project uses Python's built-in `unittest` framework.

**Run all tests:**
```bash
uv run python -m unittest discover -s tests
```

**Run with verbose output:**
```bash
uv run python -m unittest discover -s tests -v
```

**Run specific test file:**
```bash
uv run python -m unittest tests.test_bird
```

**Run specific test class:**
```bash
uv run python -m unittest tests.test_bird.TestBird
```

**Run specific test method:**
```bash
uv run python -m unittest tests.test_bird.TestBird.test_initialization
```

**Test coverage:**
- `tests/test_bird.py` - Bird class tests (physics, rendering, collision)
- `tests/test_pipe.py` - Pipe class tests (movement, collision, scoring)
- `tests/test_game.py` - Game class tests (state management, game loop)

## Architecture

### Bird Class (`app/bird.py`)
- Handles bird physics (gravity, jump mechanics)
- Manages rendering with rotation based on velocity
- Implements collision detection via bounding rectangles

### Pipe Class (`app/pipe.py`)
- Manages pipe position and movement
- Renders pipes with decorative caps
- Handles collision detection with bird
- Tracks scoring logic (when bird passes pipe)

### Game Class (`app/game.py`)
- Orchestrates the main game loop
- Manages game state (running, paused, game over)
- Handles event processing (keyboard input, window events)
- Controls update cycle for all game objects
- Manages rendering pipeline with layered drawing:
  - Background
  - Pipes
  - Bird
  - UI overlays (score, pause/game over messages)

**Design principles:**
- Encapsulation: No direct access to object attributes; use getter methods
- Separation of concerns: Each class has a single, well-defined responsibility
- Type safety: Comprehensive type hints for all code

## Game Mechanics

- **Gravity**: Constant downward acceleration applied to bird
- **Jumping**: Impulse-based upward velocity on spacebar press
- **Pipe spawning**: Fixed interval (`PIPE_FREQUENCY`) with randomized gap positions
- **Collision detection**: Rectangle-based collision system using pygame
- **Scoring**: Increment when bird's x-position passes pipe's right edge
- **Game over**: Triggered by collision with pipes, ceiling, or floor
- **Pause**: Freezes updates while maintaining rendering

## License

Don't care, do whatever you want.


## Contributing

Don't care, do whatever you want.


## Acknowledgments

Inspired by the original Flappy Bird game by Dong Nguyen.
