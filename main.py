# Draw Lines in Pygame / No Functions

# Pygame game template

import pygame
import sys
import config  # Import the config module
import random

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False  # Return False to indicate quitting
    return True  # Continue running if no quit event

class Player(pygame.sprite.Sprite):
    """Represents the player's paddle"""

    def __init__(self, color):
        super().__init__()
        self.color = color
        self.image = pygame.surface((config.PLAYER_WIDTH, config.PLAYER_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        # Position (x, y)
        self.x = config.PLAYER_START_X
        self.y = config.PLAYER_START_Y
        self.rect.center = (self.x, self.y)

    def update(self):
        """Moves the player based on keyboard input"""
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.x <= config.WINDOW_WIDTH - config.PLAYER_WIDTH // 2 and self.y > config.WINDOW_HEIGHT - 100:
            self.x += config.PLAYER_MOVEMENT_SPEED
        if keys[pygame.K_LEFT] and self.x >= config.PLAYER_WIDTH // 2 and self.y > config.WINDOW_HEIGHT - 100:
            self.x -= config.PLAYER_MOVEMENT_SPEED

        self.rect.center = (self.x, self.y)

class Ball(pygame.sprite.Sprite):
        def __init__(self):
        def __init__(self):

def main():

    screen = init_game()  # Initialize the game and get the screen
    clock = pygame.time.Clock() # Initialize the clock objecct
    

 
    # Main game loop
    running = True
    while running:
        running = handle_events()  # Handle events and check if we should continue running

        # Fill the screen with a background color 
        screen.fill(config.WHITE) 

        pygame.display.flip()  # Update the display

        clock.tick(config.FPS) # Limit frame rate to specified number of frames per second (FPS)

    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    main()  































