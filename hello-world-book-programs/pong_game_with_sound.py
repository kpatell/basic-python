# Krishan Patel

"""Chaper 19: Sound
From Hello World! Computer Programming for Kids and Beginners
Copyright Warren and Carter Sande, 2009-2013

Adding sound to pong
"""

import sys
import pygame

class Ball(pygame.sprite.Sprite):
    """Creates a Ball object"""
    def __init__(self, image_file, speed, location=[0, 0]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        """Moves the ball"""
        global points, score_text
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]

            if self.rect.top < screen.get_height():
                hit_wall.play()  # Plays sound when the ball hits the side wall

        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            points = points + 1
            score_text = font.render(str(points), 1, (0, 0, 0))
            get_point.play()  # Plays sound when the ball hits the top (player gets a point)


class Paddle(pygame.sprite.Sprite):
    """Creates a Paddle object"""
    def __init__(self, location=[0, 0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100, 20])
        image_surface.fill([0, 0, 0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
pygame.init()  # Initializes Pygame’s sound module
pygame.mixer.init()

pygame.mixer.music.load("hello-world-book-programs/sounds/bg_music.mp3")  # Loads music file
pygame.mixer.music.set_volume(0.3)  # Sets volume of the music
pygame.mixer.music.play(-1)  # Starts playing the music; repeats forever

# Creates sound objects, loads sounds, and sets volume for each
hit = pygame.mixer.Sound("hello-world-book-programs/sounds/hit_paddle.wav")
hit.set_volume(0.4)

new_life = pygame.mixer.Sound("hello-world-book-programs/sounds/new_life.wav")
new_life.set_volume(0.5)

splat = pygame.mixer.Sound("hello-world-book-programs/sounds/splat.wav")
splat.set_volume(0.6)

hit_wall = pygame.mixer.Sound("hello-world-book-programs/sounds/hit_wall.wav")
hit_wall.set_volume(0.4)

get_point = pygame.mixer.Sound("hello-world-book-programs/sounds/get_point.wav")
get_point.set_volume(0.2)

bye = pygame.mixer.Sound("hello-world-book-programs/sounds/game_over.wav")
bye.set_volume(0.6)

screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()

myBall = Ball('hello-world-book-programs/images/wackyball.bmp', [12, 6], [50, 50])
ballGroup = pygame.sprite.Group(myBall)
paddle = Paddle([270, 400])
LIVES = 3
POINTS = 0

font = pygame.font.Font(None, 50)
score_text = font.render(str(POINTS), 1, (0, 0, 0))
textpos = [10, 10]
DONE = False

RUNNING = True
while RUNNING:
    clock.tick(30)
    screen.fill([255, 255, 255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]

    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        hit.play()  # Plays sound when the ball hits the paddle
        myBall.speed[1] = -myBall.speed[1]

    myBall.move()

    if not DONE:
        screen.blit(myBall.image, myBall.rect)
        screen.blit(paddle.image, paddle.rect)
        screen.blit(score_text, textpos)
        for i in range(LIVES):
            width = screen.get_width()
            screen.blit(myBall.image, [width - 40 * i, 20])
        pygame.display.flip()

    if myBall.rect.top >= screen.get_rect().bottom:
        if not DONE:
            splat.play()  # Plays sound when the player loses a life
        LIVES = LIVES - 1
        if LIVES <= 0:
            if not DONE:
                # Waits one second and then plays the ending sound
                pygame.time.delay(1000)
                bye.play()
            FINAL_TEXT1 = "Game Over"
            FINAL_TEXT2 = "Your final score is:  " + str(POINTS)
            ft1_font = pygame.font.Font(None, 70)
            ft1_surf = font.render(FINAL_TEXT1, 1, (0, 0, 0))
            ft2_font = pygame.font.Font(None, 50)

            ft2_surf = font.render(FINAL_TEXT2, 1, (0, 0, 0))
            screen.blit(ft1_surf, [screen.get_width()/2 - \
                        ft1_surf.get_width()/2, 100])
            screen.blit(ft2_surf, [screen.get_width()/2 - \
                        ft2_surf.get_width()/2, 200])

            pygame.display.flip()
            DONE = True
            pygame.mixer.music.fadeout(2000)  # Fades out the music
        else:
            # Plays sound when a new life starts
            pygame.time.delay(1000)
            new_life.play()
            myBall.rect.topleft = [50, 50]
            screen.blit(myBall.image, myBall.rect)
            pygame.display.flip()
            pygame.time.delay(1000)
pygame.quit()
