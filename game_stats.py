class GameStats:

    def __init__(self, fh_game):

        self.settings = fh_game.settings
        self.reset_stats()

    def reset_stats(self):

        self.ships_left = self.settings.ships_left
