"""Bird class for Flappy Bird game."""

import pygame

from app.constants import (
    BLACK,
    GRAVITY,
    JUMP_STRENGTH,
    RED,
    SCREEN_HEIGHT,
    YELLOW,
)


class Bird:
    """Represents the player-controlled bird."""

    def __init__(self) -> None:
        self._x: int = 100
        self._y: float = SCREEN_HEIGHT // 2
        self._velocity: float = 0.0
        self._width: int = 34
        self._height: int = 24

    @property
    def x(self) -> int:
        """Get the bird's x position."""
        return self._x

    @property
    def y(self) -> float:
        """Get the bird's y position."""
        return self._y

    @property
    def velocity(self) -> float:
        """Get the bird's current velocity."""
        return self._velocity

    @property
    def width(self) -> int:
        """Get the bird's width."""
        return self._width

    @property
    def height(self) -> int:
        """Get the bird's height."""
        return self._height

    def jump(self) -> None:
        """Make the bird jump."""
        self._velocity = JUMP_STRENGTH

    def update(self) -> None:
        """Update bird physics."""
        self._velocity += GRAVITY
        self._y += self._velocity

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the bird on the screen."""
        # Draw a simple bird (yellow circle with a beak)
        pygame.draw.circle(
            screen, YELLOW, (int(self._x), int(self._y)), self._height // 2
        )
        # Beak
        pygame.draw.polygon(
            screen,
            RED,
            [
                (int(self._x + self._width // 2), int(self._y)),
                (int(self._x + self._width // 2 + 10), int(self._y - 5)),
                (int(self._x + self._width // 2 + 10), int(self._y + 5)),
            ],
        )
        # Eye
        pygame.draw.circle(screen, BLACK, (int(self._x + 5), int(self._y - 5)), 3)

    def get_rect(self) -> pygame.Rect:
        """Get the bounding rectangle for collision detection."""
        return pygame.Rect(
            self._x - self._width // 2,
            self._y - self._height // 2,
            self._width,
            self._height,
        )
