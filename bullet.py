import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    'manage bullets fired from ship'

    def __init__(self, ai_game):
        'create bullets at the ships current pos'
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Erstellt Geschoss bei (0, 0) und legt Pos fest
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Speichert pos als Fließkommazahl
        self.y = float(self.rect.y)

    def update(self):
        'move bullet up the screen'
        # Aktualisiere Fließkommapos
        self.y -= self.settings.bullet_speed
        # Aktualisiere Pos des Rechtecks
        self.rect.y = self.y

    def draw_bullet(self):
        'draw bullet to the screen'
        pygame.draw.rect(self.screen, self.color, self.rect)