# Krishan Patel

"""Chaper 18: Sprites and Collision Detection
From Hello World! Computer Programming for Kids and Beginners
Copyright Warren and Carter Sande, 2009-2013
"""

# 17.1 Using sprites to put multiple ball images on the screen
import sys
import pygame

# Defines ball subclass
class Ball(pygame.sprite.Sprite):
    """Defines Ball subclass"""
    def __init__(self, image_file, loc):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = loc

# Sets window size
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
IMG_FILE = "images/beach_ball.png"
balls = []
for row in range(0, 3):
    for column in range(0, 3):
        location = [column * 180 + 10, row * 180 + 10]
        ball = Ball(IMG_FILE, location)
        balls.append(ball)  # Adds balls to a list

for ball in balls:
    screen.blit(ball.image, ball.rect)
pygame.display.flip()

RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            sys.exit()
pygame.quit()
