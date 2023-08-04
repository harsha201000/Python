import pygame 
import sys
import time
from pygame.locals import *

# Set up pygame
pygame.init()

# Set up the window
WIDTH = 400
HEIGHT = 400
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Pygame Rectangle Animation')

# Set up direction variable
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# Set up the colors.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up box data struture.
b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 90, 60), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

# Run the game loop.
while True:
    # Check for Quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw the white background on the surface.
    windowSurface.fill(WHITE)
    
    for box in boxes:
        # Move the box data structure.
        if box['dir'] == DOWNLEFT:
            box['rect'].left -= MOVESPEED
            box['rect'].top += MOVESPEED
        if box['dir'] == DOWNRIGHT:
            box['rect'].left += MOVESPEED
            box['rect'].top += MOVESPEED
        if box['dir'] == UPLEFT:
            box['rect'].left -= MOVESPEED
            box['rect'].top -= MOVESPEED
        if box['dir'] == UPRIGHT:
            box['rect'].left += MOVESPEED
            box['rect'].top -= MOVESPEED
                
        # Check whether the box has moved out of the window.
        if box['rect'].top < 0:
        # The box has moved past the top
            if box['dir'] == UPLEFT:
                box['dir'] = DOWNLEFT
            if box['dir'] == UPRIGHT:
                box['dir'] = DOWNRIGHT
        if box['rect'].bottom > HEIGHT:
        # The box has moved past the bottom
            if box['dir'] == DOWNLEFT:
                box['dir'] = UPLEFT
            if box['dir'] == DOWNRIGHT:
                box['dir'] = UPRIGHT
        if box['rect'].left < 0:
        # The box has moved past the left side
            if box['dir'] == DOWNLEFT:
                box['dir'] = DOWNRIGHT
            if box['dir'] == UPLEFT:
                box['dir'] = UPRIGHT
        if box['rect'].right > WIDTH:
        # The box has moved past the right side
            if box['dir'] == DOWNRIGHT:
                box['dir'] = DOWNLEFT
            if box['dir'] == UPRIGHT:
                box['dir'] = UPLEFT
                
        # Draw the box onto the surface.
        pygame.draw.rect(windowSurface, box['color'], box['rect'])

    # Draw the winow onto the screen.
    pygame.display.update()
    time.sleep(0.02)