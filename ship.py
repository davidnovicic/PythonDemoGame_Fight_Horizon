import pygame


class Ship:

    def __init__(self, ev_game):

        self.screen = ev_game.screen
        self.settings = ev_game.settings
        self.screen_rect = ev_game.screen.get_rect()

        self.image = pygame.image.load("images/ship-1.bmp")
        self.rect = self.image.get_rect()

        # Put each new ship at the bottom of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movment flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):

        # Draw the ship at its current location

        self.screen.blit(self.image, self.rect)

    def update(self):

        # Update the ships x and y value not the rect.

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):

        # Center the ship on the right edge.

        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
