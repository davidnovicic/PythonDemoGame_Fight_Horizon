class Settings:

    def __init__(self):

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 7
        self.ships_left = 3

        # Bullet settings
        self.bullet_speed = 7
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        # self.bullets_allowed = 3

        # Alien Settings

        self.x_alien_speed = 1
        self.y_alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_up_speed = 1

        # fleet_ direction of 1 represents right; -1 left.
        self.fleet_direction = 1
