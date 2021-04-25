import pygame
from pygame.sprite import Sprite

class Fish(Sprite):

    def __init__(self, oa_game):
        super().__init__()
        self.screen = oa_game.screen
        self.settings = oa_game.settings

        self.image = pygame.image.load('gameproject_final/images/fish.png')
        self.image = pygame.transform.scale(self.image,(75,75))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.settings.fish_speed *
                        self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True