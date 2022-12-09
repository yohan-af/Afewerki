import pygame
from pygame.sprite import Sprite


class Bear(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/bear.png')
        self.image = pygame.transform.scale(self.image, (250, 170))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.bottomleft = self.screen.get_rect().bottomright
            ## switch bottom left and bottom right to go left to right
        self.x = float(self.rect.x)

        """Draw the bullet to the screen."""
        # pygame.draw.rect(self.screen, self.image, self.rect)

    def update(self):
        """Move the alien to the right or left."""
        # positive is left to right
        self.x -= self.settings.bear_speed
        self.rect.x = self.x

