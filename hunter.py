import pygame


class Hunter:
    """A class to manage the hunter"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the hunter image and get it to rect.
        self.image = pygame.image.load('images/hunter.png')
        self.rect = self.image.get_rect()

        # Start each new hunter at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the hunter's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update the hunter's position based on the movement flags."""
        # Update the hunter's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.hunter_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.hunter_speed

        # Update rect object from self.x.
        self.rect.x = self.x


    def blitme(self):
        """Draw the hunter at its current location."""
        self.screen.blit(self.image, self.rect)
