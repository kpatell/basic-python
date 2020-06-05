# Krishan Patel

"""Chaper 18: Sprites and Collision Detection
From Hello World! Computer Programming for Kids and Beginners
Copyright Warren and Carter Sande, 2009-2013
"""

# 17.1: Using sprites to put multiple ball images on the screen
# 17.2: A program for moving balls around using sprites
# 17.3: Using a sprite group instead of a list
# 17.4: Using Clock and get_fps() in the beach ball program
import sys
from random import choice
import pygame

# The ball class definition
class Ball(pygame.sprite.Sprite):
    """Creates a ball subclass"""
    def __init__(self, image_file, loc, move_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = loc
        self.move_speed = move_speed

    def move(self):
        """Moves the ball"""
        self.rect = self.rect.move(self.move_speed)

        if self.rect.left < 0 or self.rect.right > width:
            self.move_speed[0] = -self.move_speed[0]

        if self.rect.top < 0 or self.rect.bottom > height:
            self.move_speed[1] = -self.move_speed[1]

def animate(balls):
    """Animates the ball"""
    screen.fill([255, 255, 255])
    for i in balls:
        i.move()
    for i in balls:
        balls.remove(i)
        if pygame.sprite.spritecollide(i, balls, False):
            i.move_speed[0] = -i.move_speed[0]
            i.move_speed[1] = -i.move_speed[1]
        balls.add(i)
        screen.blit(i.image, i.rect)
    pygame.display.flip()
# `time.delay()` has been removed.

# Initializes everything and draws beach balls
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
IMG_FILE = "images/beach_ball.png"
clock = pygame.time.Clock()  # Creates instance of `Clock`
group = pygame.sprite.Group()

for row in range(0, 2):
    for column in range(0, 2):
        location = [column * 180 + 10, row * 180 + 10]
        speed = [choice([-4, 4]), choice([-4, 4])]
        ball = Ball(IMG_FILE, location, speed)
        group.add(ball)   #add the ball to the group

RUNNING = True
while RUNNING:  # The main `while` loop starts here.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            frame_rate = clock.get_fps()  # Checks the frame rate
            sys.exit()
            print("frame rate =", frame_rate)
    animate(group)
    clock.tick(30)
pygame.quit()
