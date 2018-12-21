import pygame

class Ship():
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.screen_rect.centerx)
        self.ship_speed = ai_settings.ship_speed
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_right:
            self.centerx += self.ship_speed
            if self.centerx > self.screen_rect.right:
                self.centerx = self.screen_rect.right
        if self.moving_left:
            self.centerx -= self.ship_speed
            if self.centerx < self.screen_rect.left:
                self.centerx = self.screen_rect.left
        self.rect.centerx = int(self.centerx)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self, screen):
        self.centerx = screen.get_rect().centerx
