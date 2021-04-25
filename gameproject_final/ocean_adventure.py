import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from octopus import Octopus
from bullet import Bullet
from fish import Fish

pygame.mixer.init()

hitSound = pygame.mixer.Sound('gameproject_final/hit.wav')

class OceanAdventure:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Ocean Adventure")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.octopus = Octopus(self)
        self.bullets = pygame.sprite.Group()
        self.fishes = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, "Play")

        self.bg_color = (187, 230, 247)

    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.octopus.update()
                self._update_bullets()
                self._update_fishes()

            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()

            self.fishes.empty()
            self.bullets.empty()

            self._create_fleet()
            self.octopus.center_octopus()
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.octopus.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.octopus.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.octopus.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.octopus.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.fishes, True, True)
        
        if collisions:
            for fishes in collisions.values():
                self.stats.score += self.settings.fish_points * len(fishes)
            self.sb.prep_score()
            hitSound.play()

        if not self.fishes:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _update_fishes(self):
        self._check_fleet_edges()
        self.fishes.update()

        if pygame.sprite.spritecollideany(self.octopus, self.fishes):
            self._octopus_hit()

        self._check_fishes_bottom()

    def _create_fleet(self):
        fish = Fish(self)
        fish_width, fish_height = fish.rect.size
        available_space_x = self.settings.screen_width - (2 * fish_width)
        number_fishes_x = available_space_x // (2 * fish_width)

        octopus_height = self.octopus.rect.height
        available_space_y = (self.settings.screen_height -
                                (3 * fish_height) - octopus_height)
        number_rows = available_space_y // (2 * fish_height)

        for row_number in range(number_rows):
            for fish_number in range(number_fishes_x):
                self._create_fish(fish_number, row_number)
            
    def _create_fish(self, fish_number, row_number):
        fish = Fish(self)
        fish_width, fish_height = fish.rect.size
        fish.x = fish_width + 2 * fish_width * fish_number
        fish.rect.x = fish.x
        fish.rect.y = fish.rect.height + 2 * fish.rect.height * row_number
        self.fishes.add(fish)

    def _check_fleet_edges(self):
        for fish in self.fishes.sprites():
            if fish.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for fish in self.fishes.sprites():
            fish.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_fishes_bottom(self):
        screen_rect = self.screen.get_rect()
        for fish in self.fishes.sprites():
            if fish.rect.bottom >= screen_rect.bottom:
                self._octopus_hit()
                break

    def _octopus_hit(self):
        if self.stats.octopi_left > 0:
            self.fishes.empty()
            self.bullets.empty()
            self._create_fleet()
            self.octopus.center_octopus()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.octopus.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.fishes.draw(self.screen)

        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    oa = OceanAdventure()
    oa.run_game()