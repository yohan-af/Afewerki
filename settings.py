class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1500
        self.screen_height = 740


        # Ship settings
        self.hunter_speed = .35

        # Bullet settings
        self.bullet_speed = 1.95
        # Bullet dimensions
        self.bullet_width = 15
        self.bullet_height = 5
        self.bullet1_width = 15
        self.bullet1_height = 5
        self.bullet2_width = 5
        self.bullet2_height = 15

        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.bullet1s_allowed = 3
        self.bullet2s_allowed = 3
