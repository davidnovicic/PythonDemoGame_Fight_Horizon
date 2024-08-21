import sys
import math

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button


class EventHorizon:

    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Fight Horizon")

        self.screen_rect = self.screen.get_rect()

        self.ship = Ship(self)
        self.alien = Alien(self)

        self.stats = GameStats(self)

        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self.aliens_2 = pygame.sprite.Group()

        self._create_fleet()

        self.scroll = 0

        # Start Alien Invasion in an active state.
        #
        self.game_active = False

        # Make the play Button

        self.play_button = Button(self, "Play")

    def run_game(self):

        while True:

            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self.update_screen()

            self.clock.tick(60)

    def draw_bg(self):

        bg_image = pygame.image.load("images/bg_space_seamless_1.bmp").convert()
        bg_rect = bg_image.get_rect()

        bg_width = bg_rect.width

        titles = math.ceil(bg_width)

        for i in range(0, titles):
            self.screen.blit(bg_image, (i * bg_width + self.scroll, 0))

        self.scroll -= 3

    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # We pilot ship from here

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.
                    self.ship.moving_right = True

                elif event.key == pygame.K_LEFT:
                    # Move the ship to the right.
                    self.ship.moving_left = True

                elif event.key == pygame.K_UP:
                    # Move the ship to the right.
                    self.ship.moving_up = True

                elif event.key == pygame.K_DOWN:
                    # Move the ship to the right.
                    self.ship.moving_down = True

                ### Fire bullet

                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()

            ### KEY UP

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

                elif event.key == pygame.K_UP:
                    self.ship.moving_up = False

                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start new game when player clicks Play."""

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.game_active:

            self.stats.reset_stats()

            self.game_active = True

            # Get rid of the remaining bullets and aliens.

            self.bullets.empty()
            self.aliens.empty()

            # Creat a new fleet and center the ship.

            self._create_fleet()
            self.ship.center_ship()

    def update_screen(self):

        # DRAW BACKROUND
        self.draw_bg()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()

        self.aliens.draw(self.screen)
        self.aliens_2.draw(self.screen)

        # Draw the play button if the game is inactive.

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _fire_bullet(self):

        # if len(self.bullets) < self.settings.bullets_allowed:

        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):

        # Update bullet position.
        self.bullets.update()

        # # Get rid of the of bullets that have disappered.
        for bullet in self.bullets.copy():
            if bullet.rect.right > self.ship.screen_rect.right:
                self.bullets.remove(bullet)

            # print(len(self.bullets))

        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _create_fleet(self):

        alien = Alien(self)
        alien_height, alien_width = alien.rect.size

        current_y, current_x = alien_width, 8 * alien_height

        while current_y < (self.settings.screen_height - alien_width):
            while current_x < (self.settings.screen_width - alien_height):
                self.create_alien(current_x, current_y)
                current_x += 2 * alien_height

            current_x = 8 * alien_height
            current_y += 2 * alien_width

    def create_alien(self, x_position, y_position=0):

        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.y = y_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def create_second_alien(self, x_position, y_position):

        second_alien = Alien(self)
        second_alien.x = x_position
        second_alien.y = y_position
        second_alien.rect.x = x_position
        second_alien.rect.y = y_position
        self.aliens_2.add(second_alien)

    def _update_aliens(self):

        self.aliens.update()
        self.aliens_2.update()
        self.left_edge_update()
        self.x_right_left()
        self.y_left_edge_to_top()

        self.x_right_edge_to_bottom()
        self.y_right_edge_to_bottom()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _ship_hit(self):

        # Respond to the ship being hit by an alien

        if self.stats.ships_left > 0:

            self.stats.ships_left -= 1

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)

        else:
            self.game_active = False

    def left_edge_update(self):

        for alien in self.aliens.sprites():

            if alien.check_top_bottom_edge():
                self._move_alien_left()
            break

    def x_right_left(self):

        for alien in self.aliens.sprites():
            if alien.check_left_edge():
                self.x_left_edge_to_top()
            break

    def y_left_edge_to_top(self):

        for alien in self.aliens.sprites():
            if alien.check_left_edge():
                self.y_left_top()
            break

    def x_right_edge_to_bottom(self):

        for alien in self.aliens.sprites():
            if alien.check_right_edge():
                self.x_right_bottom()
                break

    def y_right_edge_to_bottom(self):

        for alien in self.aliens.sprites():
            if alien.check_right_edge():
                self.y_right_bottom()
                break

    ##
    ##  DONT PUT CODE BELLOW INTO LOOP
    ##
    def _move_alien_left(self):

        self.settings.y_alien_speed = 0

    def x_left_edge_to_top(self):

        self.settings.x_alien_speed = -3

    def y_left_top(self):

        self.settings.y_alien_speed = -3

    def y_right_bottom(self):

        self.settings.y_alien_speed = 3

    def x_right_bottom(self):

        self.settings.x_alien_speed *= -1


if __name__ == "__main__":
    # Make a game instance, and run the game.

    ev = EventHorizon()
    ev.run_game()
