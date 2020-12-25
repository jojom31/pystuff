import sys

import pygame 

from settings import Settings

from ship import Ship

class AlienInvasion:
    """Overall class to manage game assests and behavior."""

    def __init__(self):
        """Intialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()



        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)


        # Set the background colors
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()    

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()      

            #Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()                    