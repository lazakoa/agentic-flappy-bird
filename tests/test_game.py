"""Tests for the Game class."""

import unittest
from unittest.mock import patch

import pygame

from app.game import Game


class TestGame(unittest.TestCase):
    """Test cases for the Game class."""

    def setUp(self) -> None:
        """Set up test fixtures."""
        pygame.init()
        with patch("pygame.display.set_mode"):
            self.game = Game()

    def test_initialization(self) -> None:
        """Test game initializes with correct values."""
        self.assertIsNotNone(self.game.bird)
        self.assertEqual(self.game.score, 0)
        self.assertFalse(self.game.game_over)
        self.assertFalse(self.game.paused)

    def test_reset(self) -> None:
        """Test reset resets game state."""
        # Modify game state
        self.game._score = 10
        self.game._game_over = True
        self.game._paused = True

        # Reset
        self.game.reset()

        # Verify reset
        self.assertEqual(self.game.score, 0)
        self.assertFalse(self.game.game_over)
        self.assertFalse(self.game.paused)

    def test_handle_events_quit(self) -> None:
        """Test handling quit event returns False."""
        quit_event = pygame.event.Event(pygame.QUIT)
        with patch("pygame.event.get", return_value=[quit_event]):
            result = self.game.handle_events()
            self.assertFalse(result)

    def test_handle_events_space_restarts(self) -> None:
        """Test space key restarts game when game over."""
        self.game._game_over = True
        self.game._score = 5

        space_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
        with patch("pygame.event.get", return_value=[space_event]):
            self.game.handle_events()
            self.assertEqual(self.game.score, 0)

    def test_handle_events_escape_toggles_pause(self) -> None:
        """Test escape key toggles pause."""
        self.game._game_over = False
        initial_paused = self.game.paused

        escape_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)
        with patch("pygame.event.get", return_value=[escape_event]):
            self.game.handle_events()
            self.assertNotEqual(self.game.paused, initial_paused)

    def test_handle_events_q_quits_when_paused(self) -> None:
        """Test q key quits game when paused."""
        self.game._paused = True

        q_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_q)
        with patch("pygame.event.get", return_value=[q_event]):
            result = self.game.handle_events()
            self.assertFalse(result)

    def test_handle_events_q_quits_when_game_over(self) -> None:
        """Test q key quits game when game over."""
        self.game._game_over = True

        q_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_q)
        with patch("pygame.event.get", return_value=[q_event]):
            result = self.game.handle_events()
            self.assertFalse(result)

    def test_update_when_game_over(self) -> None:
        """Test update does nothing when game is over."""
        self.game._game_over = True
        initial_bird_y = self.game.bird.y
        self.game.update()
        self.assertEqual(self.game.bird.y, initial_bird_y)

    def test_update_when_paused(self) -> None:
        """Test update does nothing when paused."""
        self.game._paused = True
        initial_bird_y = self.game.bird.y
        self.game.update()
        self.assertEqual(self.game.bird.y, initial_bird_y)

    def test_update_changes_game_state(self) -> None:
        """Test update changes game state."""
        self.game._game_over = False
        self.game._paused = False
        initial_bird_y = self.game.bird.y
        self.game.update()
        # Bird should have moved
        self.assertNotEqual(self.game.bird.y, initial_bird_y)

    @patch("pygame.display.flip")
    def test_draw(self, mock_flip: unittest.mock.MagicMock) -> None:
        """Test draw completes without error."""
        self.game.screen = pygame.Surface((800, 600))
        self.game.draw()
        mock_flip.assert_called_once()
