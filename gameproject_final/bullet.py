import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, oa_game):
        super().__init__()
        self.screen = oa_game.screen
        self.settings = oa_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = oa_game.octopus.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)