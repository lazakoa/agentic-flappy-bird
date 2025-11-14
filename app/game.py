"""Game class for Flappy Bird game."""

import sys

import pygame

from app.bird import Bird
from app.constants import (
    BLACK,
    DARK_GREEN,
    FPS,
    GREEN,
    PIPE_FREQUENCY,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SKY_BLUE,
    WHITE,
)
from app.pipe import Pipe


class Game:
    """Main game controller."""

    def __init__(self) -> None:
        self.screen: pygame.Surface = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        pygame.display.set_caption("Flappy Bird")
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.font: pygame.font.Font = pygame.font.Font(None, 50)
        self.small_font: pygame.font.Font = pygame.font.Font(None, 30)
        self._bird: Bird
        self._pipes: list[Pipe]
        self._score: int
        self._game_over: bool
        self._paused: bool
        self._last_pipe_time: int
        self.reset()

    @property
    def bird(self) -> Bird:
        """Get the bird instance."""
        return self._bird

    @property
    def score(self) -> int:
        """Get the current score."""
        return self._score

    @property
    def game_over(self) -> bool:
        """Get the game over state."""
        return self._game_over

    @property
    def paused(self) -> bool:
        """Get the paused state."""
        return self._paused

    def reset(self) -> None:
        """Reset the game to initial state."""
        self._bird = Bird()
        self._pipes = []
        self._score = 0
        self._game_over = False
        self._paused = False
        self._last_pipe_time = pygame.time.get_ticks()

    def handle_events(self) -> bool:
        """Handle user input events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self._game_over:
                        self.reset()
                    elif not self._paused:
                        self._bird.jump()
                elif event.key == pygame.K_ESCAPE:
                    if not self._game_over:
                        self._paused = not self._paused
                elif event.key == pygame.K_q:
                    if self._game_over or self._paused:
                        return False
        return True

    def update(self) -> None:
        """Update game state."""
        if self._game_over or self._paused:
            return

        # Update bird
        self._bird.update()

        # Check if bird hits ground or ceiling
        if self._bird.y > SCREEN_HEIGHT or self._bird.y < 0:
            self._game_over = True

        # Add new pipes
        current_time: int = pygame.time.get_ticks()
        if current_time - self._last_pipe_time > PIPE_FREQUENCY:
            self._pipes.append(Pipe(SCREEN_WIDTH))
            self._last_pipe_time = current_time

        # Update pipes
        for pipe in self._pipes[:]:
            pipe.update()

            # Check collision
            if pipe.collides_with(self._bird):
                self._game_over = True

            # Check if pipe passed
            if not pipe.passed and pipe.x + pipe.width < self._bird.x:
                pipe.passed = True
                self._score += 1

            # Remove off-screen pipes
            if pipe.is_off_screen():
                self._pipes.remove(pipe)

    def draw(self) -> None:
        """Draw all game elements."""
        # Draw background
        self.screen.fill(SKY_BLUE)

        # Draw ground
        pygame.draw.rect(self.screen, GREEN, (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))
        pygame.draw.rect(
            self.screen, DARK_GREEN, (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50), 3
        )

        # Draw pipes
        for pipe in self._pipes:
            pipe.draw(self.screen)

        # Draw bird
        self._bird.draw(self.screen)

        # Draw score
        score_text = self.font.render(str(self._score), True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        # Draw shadow for better visibility
        shadow_text = self.font.render(str(self._score), True, BLACK)
        shadow_rect = shadow_text.get_rect(center=(SCREEN_WIDTH // 2 + 2, 52))
        self.screen.blit(shadow_text, shadow_rect)
        self.screen.blit(score_text, score_rect)

        # Draw pause screen
        if self._paused:
            # Semi-transparent overlay
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))

            # Pause text
            pause_text = self.font.render("PAUSED", True, WHITE)
            pause_rect = pause_text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)
            )
            self.screen.blit(pause_text, pause_rect)

            # Resume instruction
            resume_text = self.small_font.render("Press ESC to resume", True, WHITE)
            resume_rect = resume_text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)
            )
            self.screen.blit(resume_text, resume_rect)

            # Quit instruction
            quit_text = self.small_font.render("Press Q to quit", True, WHITE)
            quit_rect = quit_text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)
            )
            self.screen.blit(quit_text, quit_rect)

        # Draw game over screen
        if self._game_over:
            # Semi-transparent overlay
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))

            # Game over text
            game_over_text = self.font.render("Game Over!", True, WHITE)
            game_over_rect = game_over_text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
            )
            self.screen.blit(game_over_text, game_over_rect)

            # Final score
            final_score_text = self.small_font.render(
                f"Score: {self._score}", True, WHITE
            )
            final_score_rect = final_score_text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            )
            self.screen.blit(final_score_text, final_score_rect)

            # Restart instruction
            restart_text = self.small_font.render("Press SPACE to restart", True, WHITE)
            restart_rect = restart_text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            )
            self.screen.blit(restart_text, restart_rect)

            # Quit instruction
            quit_text = self.small_font.render("Press Q to quit", True, WHITE)
            quit_rect = quit_text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)
            )
            self.screen.blit(quit_text, quit_rect)

        pygame.display.flip()

    def run(self) -> None:
        """Run the main game loop."""
        running: bool = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()
