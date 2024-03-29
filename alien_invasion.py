import sys
import pygame

from settings import Settings
from ship import Ship
from pygame.event import Event

class AlienInvasion:
    def __init__(self) -> None:
        # Initialize the game, and create game resources.
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
    

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
            
    

    def _check_events(self) -> None:
            #Respond to keypresses and mouse events from the player.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                         self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                         self.ship.moving_left = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False  
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False        
                         #Move the ship to the right.
                        self.ship.rect.x += 1

    def _check_keydown_events(self, event: pygame.event.Event) -> None:
            #Responding to player keypresses.
            if event.key == pygame.K_RIGHT:
                 self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                 self.ship.moving_left = True
            elif event.key == pygame.K_q:
                 sys.exit()

    def _check_keyup_events(self, event: pygame.event.Event) -> None:
        pass

    def _update_screen(self) -> None:
         #Updating screen images and flipping to the new screen.
         self.screen.fill(self.settings.bg_color)
         self.ship.blitme()

         pygame.display.flip()




            
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


    