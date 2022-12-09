import pygame

class Background(pygame.sprite.Sprite):
    """A class to manage the hunter"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the hunter image and get it to rect.
        self.image = pygame.image.load('images/background.bmp')
        self.rect = self.image.get_rect()

        # Start each new hunter at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

        # Store a decimal value for the hunter's horizontal position.
        self.x = float(self.rect.x)


