# Krishan Patel

"""Chaper 18: A New Kind of Input - Events
From Hello World! Computer Programming for Kids and Beginners
Copyright Warren and Carter Sande, 2009-2013
"""

# 18.1: Bouncing ball program, with sprites and Clock.tick()
# import sys
# import pygame

# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# background = pygame.Surface(screen.get_size())
# background.fill([255, 255, 255])
# clock = pygame.time.Clock()

# # The `Ball` class, including the `move()` method
# class Ball(pygame.sprite.Sprite):
#     """Creates a Ball object"""
#     def __init__(self, image_file, speed, location):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location
#         self.speed = speed

#     def move(self):
#         """Moves the balL"""
#         if self.rect.left <= screen.get_rect().left or \
#                 self.rect.right >= screen.get_rect().right:
#             self.speed[0] = - self.speed[0]
#         newpos = self.rect.move(self.speed)
#         self.rect = newpos

# my_ball = Ball('beach_ball.png', [10, 0], [20, 20])

# RUNNING = True
# while RUNNING:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             RUNNING = False
#             sys.exit()
#     clock.tick(30)  # This is the clock.
#     # Redraws everything
#     screen.blit(background, (0, 0))
#     my_ball.move()
#     screen.blit(my_ball.image, my_ball.rect)
#     pygame.display.flip()
# pygame.quit()

# 18.2: Bouncing ball with up and down arrow keys
# import sys
# import pygame

# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# background = pygame.Surface(screen.get_size())
# background.fill([255, 255, 255])
# clock = pygame.time.Clock()

# # The `Ball` class definition, including the `move()` method
# class Ball(pygame.sprite.Sprite):
#     """Creates a Ball object"""
#     def __init__(self, image_file, speed, location):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location
#         self.speed = speed

#     def move(self):
#         """Moves the Ball"""
#         if self.rect.left <= screen.get_rect().left or \
#                 self.rect.right >= screen.get_rect().right:
#             self.speed[0] = - self.speed[0]
#         newpos = self.rect.move(self.speed)
#         self.rect = newpos

# my_ball = Ball('images/beach_ball.png', [10, 0], [20, 20])
#
# RUNNING = True
# while RUNNING:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             RUNNING = False
#             sys.exit()
#         # Checks for key presses and moves ball up or down
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 my_ball.rect.top = my_ball.rect.top - 10
#             elif event.key == pygame.K_DOWN:
#                 my_ball.rect.top = my_ball.rect.top + 10

#     clock.tick(30)

#     # Redraws everything
#     screen.blit(background, (0, 0))
#     my_ball.move()
#     screen.blit(my_ball.image, my_ball.rect)
#     pygame.display.flip()
# pygame.quit()

# 18.3: Using a timer event to move the ball up and down
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode([640, 480])
background = pygame.Surface(screen.get_size())
background.fill([255, 255, 255])
clock = pygame.time.Clock()

# The `Ball` class definition, including the `move()` method
class Ball(pygame.sprite.Sprite):
    """Creates a Ball object"""
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        """Moves the Ball"""
        if self.rect.left <= screen.get_rect().left or \
                self.rect.right >= screen.get_rect().right:
            self.speed[0] = - self.speed[0]
        newpos = self.rect.move(self.speed)
        self.rect = newpos

my_ball = Ball('images/beach_ball.png', [10, 0], [20, 20])
pygame.time.set_timer(pygame.USEREVENT, 1000)
DIRECTION = 1

RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            sys.exit()
        # Checks for key presses and moves ball up or down
        elif event.type == pygame.USEREVENT:
            my_ball.rect.centery = my_ball.rect.centery + (30*DIRECTION)

            if my_ball.rect.top <= 0 or \
                my_ball.rect.bottom >= screen.get_rect().bottom:
                DIRECTION = -DIRECTION
    clock.tick(20)

    # Redraws everything
    screen.blit(background, (0, 0))
    my_ball.move()
    screen.blit(my_ball.image, my_ball.rect)
    pygame.display.flip()
pygame.quit()
