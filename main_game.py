import sys
import pygame


from settings import Settings
from background import Background
from hunter import Hunter
from bullet import Bullet
from bullet import Bullet1
from bullet import Bullet2


class FinalProject:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Battle")

        self.background = Background(self)
        self.hunter = Hunter(self)
        self.bullets = pygame.sprite.Group()
        self.bullet1s = pygame.sprite.Group()
        self.bullet2s = pygame.sprite.Group()

        # Set the background color.
        # Sound effects
        self.bullet_sound = pygame.mixer.Sound('sounds/bullet_sound.mp3')

        # Background




    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_bullets()
            self._update_bullet1s()
            self._update_bullet2s()
            self._update_screen()
            self.hunter.update()
            self.bullets.update()
            self.bullet1s.update()
            self.bullet2s.update()

            # Get rid of bullets that have disappeared.


    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.hunter.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.hunter.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_a:
            self._fire_bullet()
        elif event.key == pygame.K_d:
            self._fire_bullet1()
        elif event.key == pygame.K_w:
            self._fire_bullet2()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            pygame.mixer.Sound.play(self.bullet_sound)

    def _fire_bullet1(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullet1s) < self.settings.bullets_allowed:
            new_bullet = Bullet1(self)
            self.bullet1s.add(new_bullet)
            pygame.mixer.Sound.play(self.bullet_sound)

    def _fire_bullet2(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullet2s) < self.settings.bullets_allowed:
            new_bullet = Bullet2(self)
            self.bullet2s.add(new_bullet)
            pygame.mixer.Sound.play(self.bullet_sound)

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.hunter.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.hunter.moving_left = False



    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.background.blitme()
        self.hunter.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet1 in self.bullet1s.sprites():
            bullet1.draw_bullet1()
        for bullet2 in self.bullet2s.sprites():
            bullet2.draw_bullet2()

        pygame.display.flip()

    def _update_bullets(self):
        """Update position of bullets and get rid of the old bullets."""
        # Update bullet positions.
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left <= 0:
                self.bullets.remove(bullet)


    def _update_bullet1s(self):
        """Update position of bullets and get rid of the old bullets."""
        self.bullet1s.update()
        for bullet1 in self.bullet1s.copy():
            if bullet1.rect.left >= self.screen.get_rect().right:
                self.bullet1s.remove(bullet1)

    def _update_bullet2s(self):
        """Update position of bullets and get rid of the old bullets."""
        self.bullet2s.update()
        for bullet2 in self.bullet2s.copy():
            if bullet2.rect.top <= 0:
                self.bullet2s.remove(bullet2)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = FinalProject()
    ai.run_game()