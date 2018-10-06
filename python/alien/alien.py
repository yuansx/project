import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        if self.rect.right >= self.screen.get_rect().right:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False
    
    def update(self):
        if self.check_edges():
            self.ai_settings.alien_direct = 'right'
        else:
            self.ai_settings.alien_direct = 'left'
        if self.ai_settings.alien_direct == 'right':
            self.x += self.ai_settings.alien_speed
        elif self.ai_settings.alien_direct == 'left':
            self.x -= self.ai_settings.alien_speed
        self.rect.x = int(self.x)

