"""Pipe class for Flappy Bird game."""

import random
from typing import TYPE_CHECKING

import pygame

from app.constants import (
    DARK_GREEN,
    GREEN,
    PIPE_GAP,
    PIPE_SPEED,
    SCREEN_HEIGHT,
)

if TYPE_CHECKING:
    from app.bird import Bird


class Pipe:
    """Represents a pipe obstacle."""

    def __init__(self, x: int) -> None:
        self._x: int = x
        self._width: int = 70
        self._gap: int = PIPE_GAP
        self._top_height: int = random.randint(100, SCREEN_HEIGHT - self._gap - 100)
        self._bottom_y: int = self._top_height + self._gap
        self._passed: bool = False

    @property
    def x(self) -> int:
        """Get the pipe's x position."""
        return self._x

    @property
    def width(self) -> int:
        """Get the pipe's width."""
        return self._width

    @property
    def gap(self) -> int:
        """Get the pipe's gap size."""
        return self._gap

    @property
    def top_height(self) -> int:
        """Get the top pipe's height."""
        return self._top_height

    @property
    def bottom_y(self) -> int:
        """Get the bottom pipe's y position."""
        return self._bottom_y

    @property
    def passed(self) -> bool:
        """Get whether the bird has passed this pipe."""
        return self._passed

    @passed.setter
    def passed(self, value: bool) -> None:
        """Set whether the bird has passed this pipe."""
        self._passed = value

    def update(self) -> None:
        """Update pipe position."""
        self._x -= PIPE_SPEED

    def draw(self, screen: pygame.Surface) -> None:
        """Draw the pipe on the screen."""
        # Top pipe
        pygame.draw.rect(screen, GREEN, (self._x, 0, self._width, self._top_height))
        pygame.draw.rect(
            screen, DARK_GREEN, (self._x, 0, self._width, self._top_height), 3
        )
        # Top pipe cap
        pygame.draw.rect(
            screen, GREEN, (self._x - 5, self._top_height - 20, self._width + 10, 20)
        )
        pygame.draw.rect(
            screen,
            DARK_GREEN,
            (self._x - 5, self._top_height - 20, self._width + 10, 20),
            3,
        )

        # Bottom pipe
        pygame.draw.rect(
            screen,
            GREEN,
            (self._x, self._bottom_y, self._width, SCREEN_HEIGHT - self._bottom_y),
        )
        pygame.draw.rect(
            screen,
            DARK_GREEN,
            (self._x, self._bottom_y, self._width, SCREEN_HEIGHT - self._bottom_y),
            3,
        )
        # Bottom pipe cap
        pygame.draw.rect(
            screen, GREEN, (self._x - 5, self._bottom_y, self._width + 10, 20)
        )
        pygame.draw.rect(
            screen, DARK_GREEN, (self._x - 5, self._bottom_y, self._width + 10, 20), 3
        )

    def collides_with(self, bird: "Bird") -> bool:
        """Check if the pipe collides with the bird."""
        bird_rect = bird.get_rect()
        top_pipe_rect = pygame.Rect(self._x, 0, self._width, self._top_height)
        bottom_pipe_rect = pygame.Rect(
            self._x, self._bottom_y, self._width, SCREEN_HEIGHT - self._bottom_y
        )
        return bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(
            bottom_pipe_rect
        )

    def is_off_screen(self) -> bool:
        """Check if the pipe is off screen."""
        return self._x + self._width < 0
