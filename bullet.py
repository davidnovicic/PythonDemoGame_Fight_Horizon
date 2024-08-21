import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ev_game):

        super().__init__()
        self.screen = ev_game.screen
        self.settings = ev_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) at the ship's
        # current position

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )

        self.rect.midright = ev_game.ship.rect.midright

        # Store the bullet's position as a float.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):

        # Update the exact position of the bullet.

        # Fire bullets
        self.x += self.settings.bullet_speed
        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):

        # Draw bullet to the screen.
        pygame.draw.rect(self.screen, self.color, self.rect)
