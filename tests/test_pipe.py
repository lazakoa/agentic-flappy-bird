"""Tests for the Pipe class."""

import unittest

import pygame

from app.bird import Bird
from app.constants import PIPE_GAP, SCREEN_HEIGHT, SCREEN_WIDTH
from app.pipe import Pipe


class TestPipe(unittest.TestCase):
    """Test cases for the Pipe class."""

    def setUp(self) -> None:
        """Set up test fixtures."""
        pygame.init()
        self.pipe = Pipe(SCREEN_WIDTH)

    def test_initialization(self) -> None:
        """Test pipe initializes with correct values."""
        self.assertEqual(self.pipe.x, SCREEN_WIDTH)
        self.assertEqual(self.pipe.width, 70)
        self.assertEqual(self.pipe.gap, PIPE_GAP)
        self.assertFalse(self.pipe.passed)
        # Verify top_height is within valid range
        self.assertGreaterEqual(self.pipe.top_height, 100)
        self.assertLessEqual(self.pipe.top_height, SCREEN_HEIGHT - self.pipe.gap - 100)

    def test_update(self) -> None:
        """Test update moves pipe left."""
        initial_x = self.pipe.x
        self.pipe.update()
        self.assertLess(self.pipe.x, initial_x)

    def test_draw(self) -> None:
        """Test draw does not raise an exception."""
        screen = pygame.Surface((800, 600))
        self.pipe.draw(screen)

    def test_collides_with(self) -> None:
        """Test collides_with returns boolean."""
        bird = Bird()
        result = self.pipe.collides_with(bird)
        self.assertIsInstance(result, bool)

    def test_is_off_screen_when_visible(self) -> None:
        """Test pipe is not off screen when visible."""
        self.pipe._x = 100
        self.assertFalse(self.pipe.is_off_screen())

    def test_is_off_screen_when_off(self) -> None:
        """Test pipe is off screen when past left edge."""
        self.pipe._x = -self.pipe.width - 1
        self.assertTrue(self.pipe.is_off_screen())
