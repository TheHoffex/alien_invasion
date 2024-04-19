import pygame

class Ship:
    'manage the ship'

    def __init__(self, ai_game):
        'initialize and set starting position'
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Lädt Bild und ruft dessen umgebendes Rechteck ab
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Platziert jedes neue Schiff mittig/unten
        self.rect.midbottom = self.screen_rect.midbottom

        # Speichert einen Fließkommawert für den Schiffsmittelpunkt
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        'update ship postition based on movement flag'
        # Aktualisiert Wert für Mittellpunkt nicht des Rechtecks
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Aktualisiere rect auf Grundlage von self.x
        self.rect.x = self.x

    def blitme(self):
        'draw ship at current location'
        self.screen.blit(self.image, self.rect)