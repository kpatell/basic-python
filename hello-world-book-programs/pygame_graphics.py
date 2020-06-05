# Krishan Patel

"""Chaper 16: Graphics
From Hello World! Computer Programming for Kids and Beginners
Copyright Warren and Carter Sande, 2009-2013
"""

# Beach ball bouncing
import sys
import math
import pygame

# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load('images/beach_ball.png')
# X_COOR = 50
# Y_COOR = 50
# X_SPEED = 5
# RUNNING = True
# while RUNNING:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             RUNNING = False
#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255, 255, 255], [X_COOR, Y_COOR, 90, 90], 0)
#     X_COOR = X_COOR + X_SPEED
#     if X_COOR > screen.get_width():  # If the ball is at the far right …
#         X_COOR = 0  # … start over at the left side.
#     screen.blit(my_ball, [X_COOR, Y_COOR])
#     pygame.display.flip()
# pygame.quit()

# Well connected sine wave
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
plotPoints = []
for x in range(0, 640):
    y = int(math.sin(x/640 * 4 * math.pi) * 200 + 240)  # Calculates y-position for each point
    plotPoints.append([x, y])  # Adds each point to the list
pygame.draw.lines(screen, [0, 0, 0], False, plotPoints, 1)
pygame.display.flip()
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            sys.exit()
pygame.quit()
