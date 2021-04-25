class GameStats:

    def __init__(self, oa_game):
        self.settings = oa_game.settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        self.octopi_left = self.settings.octopus_limit
        self.score = 0