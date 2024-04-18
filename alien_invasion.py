import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self):
        'Initialize the game'
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

        # Hintergrundfarbe
        self.bg_color = (230, 230, 230)

    def run_game(self):
        'start main loop'
        while True:
            # lauscht tastatur und mausergebnisse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Zeichnet Bildschirm bei jedem Schleifendurchlauf neu
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # macht zuletzt gezeichneten Bildschirm sichtbar
            pygame.display.flip()

if __name__ == '__main__':
    # Erstelle und führe Spiel aus
    ai = AlienInvasion()
    ai.run_game()
    