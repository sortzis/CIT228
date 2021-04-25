class Settings:

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (187, 230, 247)

        self.octopus_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1

        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.octopus_speed = 1.5
        self.bullet_speed = 3.0
        self.fish_speed = 1.0
        self.fleet_direction = 1
        self.fish_points = 50

    def increase_speed(self):
        self.octopus_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.fish_speed *= self.speedup_scale

        self.fish_points = int(self.fish_points * self.score_scale)
        print(self.fish_points)