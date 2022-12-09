import pygame
from pygame.sprite import Sprite


class DuckR(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/duckR.png')
        self.image = pygame.transform.scale(self.image, (100, 70))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.topright = self.screen.get_rect().topleft
            ## switch bottom left and bottom right to go left to right
        self.x = float(self.rect.x)

        """Draw the bullet to the screen."""
        # pygame.draw.rect(self.screen, self.image, self.rect)

    def update(self):
        """Move the alien to the right or left."""
        # positive is left to right
        self.x += self.settings.duckR_speed
        self.rect.x = self.x

class DuckL(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/duckL.png')
        self.image = pygame.transform.scale(self.image, (100, 70))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.midleft = self.screen.get_rect().midright
            ## switch bottom left and bottom right to go left to right
        self.x = float(self.rect.x)

        """Draw the bullet to the screen."""
        # pygame.draw.rect(self.screen, self.image, self.rect)

    def update(self):
        """Move the alien to the right or left."""
        # positive is left to right
        self.x -= self.settings.duckL_speed
        self.rect.x = self.x