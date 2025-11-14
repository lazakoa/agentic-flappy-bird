"""Tests for the Bird class."""

import unittest

import pygame

from app.bird import Bird
from app.constants import JUMP_STRENGTH, SCREEN_HEIGHT


class TestBird(unittest.TestCase):
    """Test cases for the Bird class."""

    def setUp(self) -> None:
        """Set up test fixtures."""
        pygame.init()
        self.bird = Bird()

    def test_initialization(self) -> None:
        """Test bird initializes with correct values."""
        self.assertEqual(self.bird.x, 100)
        self.assertEqual(self.bird.y, SCREEN_HEIGHT // 2)
        self.assertEqual(self.bird.velocity, 0.0)
        self.assertEqual(self.bird.width, 34)
        self.assertEqual(self.bird.height, 24)

    def test_jump(self) -> None:
        """Test jump changes velocity."""
        self.bird.jump()
        self.assertEqual(self.bird.velocity, JUMP_STRENGTH)

    def test_update(self) -> None:
        """Test update changes position."""
        initial_y = self.bird.y
        self.bird.update()
        self.assertNotEqual(self.bird.y, initial_y)

    def test_draw(self) -> None:
        """Test draw does not raise an exception."""
        screen = pygame.Surface((800, 600))
        self.bird.draw(screen)

    def test_get_rect(self) -> None:
        """Test get_rect returns a pygame Rect."""
        rect = self.bird.get_rect()
        self.assertIsInstance(rect, pygame.Rect)
