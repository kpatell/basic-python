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
# pygame.time.set_timer(pygame.USEREVENT, 1000)
# DIRECTION = 1

# RUNNING = True
# while RUNNING:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             RUNNING = False
#             sys.exit()
#         # Checks for key presses and moves ball up or down
#         elif event.type == pygame.USEREVENT:
#             my_ball.rect.centery = my_ball.rect.centery + (30*DIRECTION)

#             if my_ball.rect.top <= 0 or \
#                 my_ball.rect.bottom >= screen.get_rect().bottom:
#                 DIRECTION = -DIRECTION
#     clock.tick(20)

#     # Redraws everything
#     screen.blit(background, (0, 0))
#     my_ball.move()
#     screen.blit(my_ball.image, my_ball.rect)
#     pygame.display.flip()
# pygame.quit()

# 18.4: First version of PyPong
# import sys
# import pygame
# from pygame.locals import *

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
#         self.rect = self.rect.move(self.speed)

#         if self.rect.left < 0 or self.rect.right > screen.get_width():
#             self.speed[0] = -self.speed[0]

#         if self.rect.top <= 0:
#             self.speed[1] = -self.speed[1]

# # The paddle class definition
# class Paddle(pygame.sprite.Sprite):
#     """Creates the paddle"""
#     def __init__(self, location=[0, 0]):
#         pygame.sprite.Sprite.__init__(self)
#         image_surface = pygame.surface.Surface([100, 20])
#         image_surface.fill([0, 0, 0])
#         self.image = image_surface.convert()
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location

# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# clock = pygame.time.Clock()
# ball_speed = [10, 5]

# my_ball = Ball('images/wackyball.bmp', ball_speed, [50, 50])
# ballGroup = pygame.sprite.Group(my_ball)
# paddle = Paddle([270, 400])

# RUNNING = True
# while RUNNING:
#     clock.tick(30)
#     screen.fill([255, 255, 255])

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             RUNNING = False
#             sys.exit()
#         # Move paddle if mouse moves
#         elif event.type == pygame.MOUSEMOTION:
#             paddle.rect.centerx = event.pos[0]

#     if pygame.sprite.spritecollide(paddle, ballGroup, False):
#         my_ball.speed[1] = -my_ball.speed[1]

#     # Redraws everything
#     my_ball.move()
#     screen.blit(my_ball.image, my_ball.rect)
#     screen.blit(paddle.image, paddle.rect)
#     pygame.display.flip()

# pygame.quit()

# 18.5: Final PyPong code
import sys
import pygame

# Defines the ball class
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
        global POINTS, SCORE_TEXT
        self.rect = self.rect.move(self.speed)

        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]

        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            POINTS = POINTS + 1
            SCORE_TEXT = font.render(str(POINTS), 1, (0, 0, 0))

# Defines the paddle class
class Paddle(pygame.sprite.Sprite):
    """Defines paddle class"""
    def __init__(self, location=[0, 0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100, 20])
        image_surface.fill([0, 0, 0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

pygame.init()

# Initializes everything
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()
myBall = Ball('images/wackyball.bmp', [10, 5], [50, 50])
ballGroup = pygame.sprite.Group(myBall)
paddle = Paddle([270, 400])
LIVES = 3
POINTS = 0

# Creates the font object
font = pygame.font.Font(None, 50)
score_surf = font.render(str(POINTS), 1, (0, 0, 0))
textpos = [10, 10]

DONE = False
RUNNING = True
while RUNNING:  # The start of the main program (`while` loop)
    clock.tick(30)
    screen.fill([255, 255, 255])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            sys.exit()
        # Detects mouse motion to move the paddle
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]

    # Detects collisions between the ball and paddle
    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        myBall.speed[1] = -myBall.speed[1]

    # Moves the ball
    myBall.move()

    # Redraws everything
    if not DONE:
        screen.blit(myBall.image, myBall.rect)
        screen.blit(paddle.image, paddle.rect)
        screen.blit(SCORE_TEXT, textpos)

        for i in range(LIVES):
            width = screen.get_width()
            screen.blit(myBall.image, [width - 40 * i, 20])
        pygame.display.flip()

    # Decreases life counter if ball hits bottom
    if myBall.rect.top >= screen.get_rect().bottom:
        LIVES = LIVES - 1
        # Creates and draws the final score text
        if LIVES == 0:
            FINAL_TEXT1 = "Game Over"
            FINAL_TEXT2 = "Your final score is:  " + str(POINTS)
            ft1_font = pygame.font.Font(None, 70)
            ft1_surf = ft1_font.render(FINAL_TEXT1, 1, (0, 0, 0))
            ft2_font = pygame.font.Font(None, 50)
            ft2_surf = ft2_font.render(FINAL_TEXT2, 1, (0, 0, 0))

            screen.blit(ft1_surf, [screen.get_width()//2 - \
                        ft1_surf.get_width()//2, 100])
            screen.blit(ft2_surf, [screen.get_width()//2 - \
                        ft2_surf.get_width()//2, 200])

            pygame.display.flip()
            DONE = True
        # Starts a new life, after a 2-second delay
        else:
            pygame.time.delay(2000)
            myBall.rect.topleft = [50, 50]
pygame.quit()
