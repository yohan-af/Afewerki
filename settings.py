class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600


        # Ship settings
        self.hunter_speed = .45

        # Bullet settings
        self.bullet_speed = 1.95
        # Bullet dimensions
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet1_width = 15
        self.bullet1_height = 3
        self.bullet2_width = 3
        self.bullet2_height = 15

        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.bullet1s_allowed = 3
        self.bullet2s_allowed = 3

        # NPC speeds
        self.bear_speed = .1
        self.duckR_speed = .3
        self.duckR_frequency = .0011
        self.duckL_speed = .25
        self.duckL_frequency = .001

        # Hunter settings
        self.hunter_speed = 1.5
        self.hunter_limit = 2

        # How quickly the game speed up
        self.speedup_scale = 1.1
        self.speedup_scale2 = 1.2

        # How quickly the bear point values increase
        self.score_scale = 1.05

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.hunter_speed = 1.5
        self.bullet_speed = 3.0
        self.bullet1_speed = 3.0
        self.bullet2_speed = 3.0
        self.bear_speed = .2

        # fleet_direction of 1 represents right: -1 represents left; -1 represents left
        self.fleet_direction = 1

        # scoring
        self.bear_points = 100
        self.duckL_points= 15
        self.duckR_points = 15

    def increase_speed(self):
        """Increase speed settings and bear/duck point values."""
        self.hunter_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.bullet1_speed *= self.speedup_scale
        self.bullet2_speed *= self.speedup_scale
        self.bear_speed *= self.speedup_scale2
        self.duckL_speed *= self.speedup_scale
        self.duckR_speed *= self.speedup_scale

        self.bear_points = int(self.bear_points * self.score_scale)

        self.duckL_points = int(self.duckL_points * self.score_scale)

        self.duckR_points = int(self.duckR_points * self.score_scale)




