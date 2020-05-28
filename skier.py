# Krishan Patel
# Skier game created to assist with learning python
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   https://opensource.org/licenses/mit-license.php

"""Skier game created to assist with learning python
Copyright Warren & Carter Sande, 2013"""

import os
import random
import pygame

def load_images():
    """Loads the images needed"""
    folder = 'images/'
    image_names = []

    for filename in os.listdir(folder):
        if any([filename.endswith(x) for x in ['.png']]):
            img_name = os.path.join(filename)
            if not filename.startswith(('skier_crash.png', 'skier_flag.png', 'skier_tree.png')):
                image_names.append(img_name)

    return image_names


def sort_images():
    """Sorts the images in order"""
    image_order = ["skier_down.png", "skier_right1.png", "skier_right2.png",
                   "skier_left2.png", "skier_left1.png"]
    unsorted_images = load_images()
    order_map = {}

    for pos, item in enumerate(image_order):
        order_map[item] = pos

    sorted_images = sorted(unsorted_images, key=order_map.get)

    return sorted_images


skier_images = sort_images()

"""
class GetImages(object):
    def __init__(self):
        self.folder = 'images/'
        self.image_order = ["skier_down.png", "skier_right1.png",
                            "skier_right2.png", "skier_left2.png", "skier_left1.png"]
        self.order_map = {}


    def load_images(self):
        self.image_names = []
        for filename in os.listdir(self.folder):
            if any([filename.endswith(x) for x in ['.png']]):
                img_name = os.path.join(filename)
                if not filename.startswith(('skier_crash.png', 'skier_flag.png', 'skier_tree.png')):
                    self.image_names.append(img_name)
        return self.image_names
    def sort_images(self):
        #self.sorted_images = self.load_images()

        for pos, item in enumerate(self.image_order):
            self.order_map[item] = pos
        #self.sorted_images = self.load_images(), self.sorted_images.sort(key=self.order_map.get)
        self.loaded_images = self.load_images()
        self.sorted_images = sorted(self.loaded_images, key=self.order_map.get)

        return self.sorted_images
#Sorted skier_images
#Simages = GetImages()
print(GetImages().load_images())
print(GetImages().sort_images())
skier_images1 = GetImages().sort_images()
print(skier_images1)
end = time. time()
print(end - start)
"""


# class for the Skier sprite
class SkierClass(pygame.sprite.Sprite):
    """Creates the skier"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.angle = 0

    def turn(self, direction):
        """Turns the skier"""
        # load new image and change speed when the skier turns
        self.angle = self.angle + direction

        if self.angle < -2:
            self.angle = -2
        if self.angle > 2:
            self.angle = 2

        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        turn_speed = [self.angle, 6 - abs(self.angle) * 2]
        return turn_speed

    def move(self, move_speed):
        """Moves the skier right and left"""
        self.rect.centerx = self.rect.centerx + move_speed[0]
        if self.rect.centerx < 20:
            self.rect.centerx = 20
        if self.rect.centerx > 620:
            self.rect.centerx = 620

class ObstacleClass(pygame.sprite.Sprite):
    """Creates trees and flags"""
    def __init__(self, image_file, location, obstacle_type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.obstacle_type = obstacle_type
        self.passed = False

    def update(self):
        """Updates the map"""
        global speed
        self.rect.centery -= speed[1]
        if self.rect.centery < -32:
            self.kill()


# create one "screen" of obstacles: 640 x 640
# use "blocks" of 64 x 64 pixels, so objects aren't too close together
def create_map():
    """Creates one window of random trees and flags"""
    global OBSTACLES
    locations = []
    for _i in range(10):  # 10 obstacles per screen
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        location = [col * 64 + 32, row * 64 + 32 + 640]  # center x, y for obstacle
        if location not in locations:  # prevent 2 obstacles in the same place
            locations.append(location)
            obstacle_type = random.choice(["tree", "flag"])

            if obstacle_type == "tree":
                img = "skier_tree.png"
            elif obstacle_type == "flag":
                img = "skier_flag.png"
            obstacle = ObstacleClass(img, location, obstacle_type)
            OBSTACLES.add(obstacle)

def animate():
    """Redraw the screen, including all sprites"""
    screen.fill([255, 255, 255])
    OBSTACLES.draw(screen)
    screen.blit(skier.image, skier.rect)
    screen.blit(score_text, [10, 10])
    pygame.display.flip()

# initialize everything
pygame.init()
screen = pygame.display.set_mode([640, 640])
clock = pygame.time.Clock()
speed = [0, 6]
OBSTACLES = pygame.sprite.Group()  # group of obstacle objects
skier = SkierClass()
MAP_POSITION = 0
POINTS = 0
create_map()  # create one screen full of obstacles
font = pygame.font.Font(None, 50)

# main Pygame event loop
RUNNING = True
while RUNNING:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        if event.type == pygame.KEYDOWN:  # check for key presses
            if event.key == pygame.K_LEFT:  # left arrow turns left
                speed = skier.turn(-1)
            elif event.key == pygame.K_RIGHT:  # right arrow turns right
                speed = skier.turn(1)
    skier.move(speed)  # move the skier (left or right)
    MAP_POSITION += speed[1]  # scroll the obstacles

    # create a new block of obstacles at the bottom
    if MAP_POSITION >= 640:
        create_map()
        MAP_POSITION = 0

    # check for hitting trees or getting flags
    hit = pygame.sprite.spritecollide(skier, OBSTACLES, False)
    if hit:
        if hit[0].type == "tree" and not hit[0].passed:  # crashed into tree
            POINTS = POINTS - 100
            skier.image = pygame.image.load("skier_crash.png")  # crash image
            animate()
            pygame.time.delay(1000)
            skier.image = pygame.image.load("skier_down.png")  # resume skiing
            skier.angle = 0
            speed = [0, 6]
            hit[0].passed = True
        elif hit[0].type == "flag" and not hit[0].passed:  # got a flag
            POINTS += 10
            hit[0].kill()  # remove the flag

    OBSTACLES.update()
    score_text = font.render("Score: " + str(POINTS), 1, (0, 0, 0))
    animate()

pygame.quit()
