import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    'represent a single alien'

    def __init__(self, ai_game):
        'int alien and starting pos'
        super().__init__()
        self.screen = ai_game.screen

        # Lädt Bild & rect Attribut
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Platziert jedes neue Schiff oben links auf Bildschirm
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # speichert position
        self.x = float(self.rect.x)