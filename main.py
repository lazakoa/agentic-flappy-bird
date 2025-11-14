"""Main entry point for Flappy Bird game."""

import pygame

from app.game import Game

# Initialize Pygame
pygame.init()


def main() -> None:
    """Run the Flappy Bird game."""
    game: Game = Game()
    game.run()


if __name__ == "__main__":
    main()
