import sys
import pygame
from random import random
from time import sleep
from button import Button



from settings import Settings
from background import Background
from game_stats import GameStats
from scoreboard import Scoreboard
from hunter import Hunter
from bullet import Bullet
from bullet import Bullet1
from bullet import Bullet2
from bear import Bear
from duck import DuckR
from duck import DuckL

# Help from Alexandra Edleman
# Help from ELi
# Help from Peter Lee
# Help from Juon Ortiz
# Help from Eric Lindsey



class FinalProject:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Battle")

        #Create an instance to store game statistics
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.background = pygame.image.load('images/background.bmp')
        self.background = Background(self)
        self.hunter = Hunter(self)

        self.bullets = pygame.sprite.Group()
        self.bullet1s = pygame.sprite.Group()
        self.bullet2s = pygame.sprite.Group()
        self.bears = pygame.sprite.Group()
        self.duckRs = pygame.sprite.Group()
        self.duckLs = pygame.sprite.Group()

        self._createbear_fleet()
        self._createduckL_fleet()
        self._createduckR_fleet()

        # Make the Play button.
        self.play_button = Button(self, "Hunt")

        # Set the background color.
        # Sound effects
        self.bullet_sound = pygame.mixer.Sound('sounds/bullet_sound.mp3')
        self.quack_sound = pygame.mixer.Sound('sounds/duckquacking.mp3')
        self.roar_sound = pygame.mixer.Sound('sounds/rroarr.mp3')
        self.hunterh_sound = pygame.mixer.Sound('sounds/scream.wav')

        pygame.mixer.music.load("sounds/banjo.wav")
        pygame.mixer.music.play(-1)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self._update_bullets()
                self._update_bullet1s()
                self._update_bullet2s()
                self._update_duckRs()
                self._update_duckLs()
                self._update_bears()

                self._update_screen()
                self.hunter.update()
                self.bullets.update()
                self.bullet1s.update()
                self.bullet2s.update()
                self.bears.update()
                self.duckRs.update()
                self.duckLs.update()

                # Get rid of bullets that have disappeared.

                # call function to randomize the fleets

                self._createduckL_fleet()
                self._createduckR_fleet()

            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()


            self.bears.empty()
            self.duckLs.empty()
            self.duckRs.empty()
            self.bullets.empty()
            self.bullet1s.empty()
            self.bullet2s.empty()

            # Create a new fleet and center hunter
            self. _createbear_fleet()
            self._createduckL_fleet()
            self._createduckR_fleet()
            self.settings.increase_speed()
            self.hunter.center_hunter()

            # pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.hunter.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.hunter.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_a:
            # if self.angle == 0:
            #     self.angle = 180
            #     self.hunter.image = pygame.transform.rotate(self.hunter.image, self.angle)
            # elif self.angle == 180:
            #     self.angle == 0
            #     self.hunter.image = pygame.transform.rotate(self.hunter.image, self.angle)

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
            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(self.bullet_sound)
            pygame.mixer.music.unpause()
    def _fire_bullet1(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullet1s) < self.settings.bullets_allowed:
            new_bullet = Bullet1(self)
            self.bullet1s.add(new_bullet)
            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(self.bullet_sound)
            pygame.mixer.music.unpause()

    def _fire_bullet2(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullet2s) < self.settings.bullets_allowed:
            new_bullet = Bullet2(self)
            self.bullet2s.add(new_bullet)
            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(self.bullet_sound)
            pygame.mixer.music.unpause()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.hunter.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.hunter.moving_left = False

    def _createbear_fleet(self):
        """Create the fleet of aliens."""
        # Make a bear
        bear = Bear(self)
        self.bears.add(bear)

    # Duck fleets
    def _createduckR_fleet(self):
        """Create the fleet of aliens."""
        if random() < self.settings.duckR_frequency:
            # Make a duck
            duck = DuckR(self)
            self.duckRs.add(duck)


    def _createduckL_fleet(self):
        """Create the fleet of aliens."""
        if random() < self.settings.duckL_frequency:
        # Make a duck
            duck = DuckL(self)
            self.duckLs.add(duck)

    def _update_bears(self):
        # Look for hunter-bear collisions.
        if pygame.sprite.spritecollideany(self.hunter, self.bears):
            self._hunter_hit()
            print("Hunter attacked!!")

    def _update_duckRs(self):
        self.duckRs.update()
    def _update_duckLs(self):
        self.duckLs.update()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        self.background.blitme()
        self.hunter.blitme()
        self._update_bears()
        self._update_duckRs()
        self._update_duckLs()

        self.bears.draw(self.screen)
        self.duckRs.draw(self.screen)
        self.duckLs.draw(self.screen)

        # Draw the score information
        self.sb.show_score()


        if not self.stats.game_active:
            self.play_button.draw_button()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet1 in self.bullet1s.sprites():
            bullet1.draw_bullet1()
        for bullet2 in self.bullet2s.sprites():
            bullet2.draw_bullet2()

        # # Draw the play button if the game is inactive.
        # if not self.stats.game_active:
        #     self.play_button.draw_button()

        pygame.display.flip()

    # update bullets
    def _update_bullets(self): # LEFT bullet
        """Update position of bullets and get rid of the old bullets."""
        # Update bullet positions.
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left <= 0:
                self.bullets.remove(bullet)




    def _update_bullet1s(self): # Right bullet
        """Update position of bullets and get rid of the old bullets."""
        self.bullet1s.update()
        for bullet1 in self.bullet1s.copy():
            if bullet1.rect.left >= self.screen.get_rect().right:
                self.bullet1s.remove(bullet1)


            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(self.roar_sound)
            pygame.mixer.music.unpause()

        self._check_bullet_bear_collision()

    def _check_bullet_bear_collision(self):
        """Respond to bullet-bear collisions"""
        collisions = pygame.sprite.groupcollide(self.bullet1s, self.bears, True, True)

        if collisions:
            for bears in collisions.values():
                self.stats.score += self.settings.bear_points * len(bears)
                self.sb.prep_score()
                self.sb.check_high_score()
                 # Destroy existing bullets and create new fleet
                self.bullets.empty()
                self._createbear_fleet()
                self.settings.increase_speed()

                # Increase level.
                self.stats.level += 1
                self.sb.prep_level()
                self.stats.score += self.settings.bear_points

    def _update_bullet2s(self): # up BULLET
        """Update position of bullets and get rid of the old bullets."""
        self.bullet2s.update()
        for bullet2 in self.bullet2s.copy():
            if bullet2.rect.top <= 0:
                self.bullet2s.remove(bullet2)
            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(self.quack_sound)
            pygame.mixer.music.unpause()

        self._check_bullet_duckL_collision()
        self._check_bullet_duckR_collision()
    def _check_bullet_duckL_collision(self):
        """Respond to bullet-bear collisions"""
        collisions = pygame.sprite.groupcollide(self.bullet2s, self.duckLs, True, True)

        if collisions:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._createduckL_fleet()
            self.settings.increase_speed()
            self.stats.score += self.settings.duckL_points
            self.sb.prep_score()

    def _check_bullet_duckR_collision(self):
        """Respond to bullet-bear collisions"""
        collisions = pygame.sprite.groupcollide(self.bullet2s, self.duckRs, True, True)

        if collisions:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._createduckR_fleet()
            self.settings.increase_speed()
            self.stats.score += self.settings.duckR_points
            self.sb.prep_score()

    def _hunter_hit(self):
        """Respond to hunter being hit by bear."""
        if self.stats.hunters_left > 0:
            self.stats.hunters_left -= 1
            # Get rid of any remaining bears and bullets.
            self.bears.empty()
            self.duckRs.empty()
            self.duckLs.empty()
            self.bullets.empty()
            self.bullet1s.empty()
            self.bullet2s.empty()
            # Create a new fleet and center the hunter.
            self._createbear_fleet()
            self.hunter.center_hunter()
            # Pause

            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(self.hunterh_sound)
            pygame.mixer.music.unpause()
            sleep(1)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)





if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = FinalProject()
    ai.run_game()