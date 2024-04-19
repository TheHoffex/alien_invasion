class Settings:
    'stores all settings for Alien Invasion'

    def __init__(self):
        'initialize game settings'
        # Bildschirmeinstellungen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (12, 93, 121)

        # Schiffseinstellungen
        self.ship_speed = 1.5

        # Geschosseinstellungen
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3