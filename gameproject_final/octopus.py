import pygame

class Octopus:

    def __init__(self, oa_game):
        self.screen = oa_game.screen
        self.settings = oa_game.settings
        self.screen_rect = oa_game.screen.get_rect()

        self.image = pygame.image.load('gameproject_final/images/octopus.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.octopus_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.octopus_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_octopus(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)