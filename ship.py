import pygame

class Ship:
    'manage the ship'

    def __init__(self, ai_game):
        'initialize and set starting position'
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Lädt Bild und ruft dessen umgebendes Rechteck ab
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Platziert jedes neue Schiff mittig/unten
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        'draw ship at current location'
        self.screen.blit(self.image, self.rect)