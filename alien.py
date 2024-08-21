import pygame

from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ev_game):

        super().__init__()
        self.screen = ev_game.screen
        self.screen_rect = ev_game.screen.get_rect()
        self.settings = ev_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("images/alien-1.bmp")
        self.rect = self.image.get_rect()

        alien_height, alien_width = self.rect.size

        # Start each new alien near the top right screen.

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):

        if self.rect.bottom <= self.settings.screen_height // 2:
            self.x -= self.settings.x_alien_speed
            self.rect.x = self.x
            self.y += self.settings.y_alien_speed
            self.rect.y = self.y

        if self.rect.bottom >= self.settings.screen_height // 2:
            self.x -= self.settings.x_alien_speed
            self.rect.x = self.x
            self.y -= self.settings.y_alien_speed
            self.rect.y = self.y

    def update_second_fleet(self):

        self.x -= self.settings.x_alien_speed
        self.rect.x = self.x

    def check_left_edge(self):

        screen_rect = self.screen.get_rect()

        return self.rect.left <= 0

    def check_top_bottom_edge(self):

        screen_rect = self.screen.get_rect()

        alien_height, alien_width = self.rect.size

        return (self.rect.top <= screen_rect.top) or (
            self.rect.bottom >= screen_rect.bottom - (11 * alien_width)
        )

    def check_right_edge(self):

        screen_rect = self.screen.get_rect()

        return self.rect.right >= screen_rect.right
