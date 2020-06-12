# Krishan Patel

"""Chaper 19: Sound
From Hello World! Computer Programming for Kids and Beginners
Copyright Warren and Carter Sande, 2009-2013
"""

# 19.1: Trying out sounds in Pygame
# import sys
# import pygame

# pygame.init()  # Initializes Pygame and mixer
# pygame.mixer.init()

# screen = pygame.display.set_mode([640, 480])  # Creates a Pygame window
# pygame.time.delay(1000)

# splat = pygame.mixer.Sound("hello-world-book-programs/sounds/splat.wav")
# splat.play()  # Plays the sound

# RUNNING = True
# while RUNNING:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             RUNNING = False
#             sys.exit()
# pygame.quit()

# 19.2: Playing music
# import sys
# import pygame

# pygame.init()  # Initializes Pygame and mixer
# pygame.mixer.init()

# screen = pygame.display.set_mode([640, 480])  # Creates a Pygame window
# pygame.time.delay(1000)

# pygame.mixer.music.load("hello-world-book-programs/sounds/bg_music.mp3")

# RUNNING = True
# while RUNNING:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             RUNNING = False
#             sys.exit()
# pygame.quit()

# 19.3: Music and sound with volume adjustment
# import sys
# import pygame

# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# pygame.mixer.music.load("hello-world-book-programs/sounds/bg_music.mp3")
# pygame.mixer.music.set_volume(0.30)  # Adjusts the volume of the music
# pygame.mixer.music.play()

# splat = pygame.mixer.Sound("hello-world-book-programs/sounds/splat.wav")
# splat.set_volume(0.50)  # Adjusts the volume of the sound effect
# splat.play()

# RUNNING = True
# while RUNNING:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             RUNNING = False
#             sys.exit()
# pygame.quit()

# 19.4: Waiting for the end of the song to splat
# import sys
# import pygame

# pygame.init()

# screen = pygame.display.set_mode([640, 480])

# pygame.mixer.music.load("hello-world-book-programs/sounds/bg_music.mp3")
# pygame.mixer.music.set_volume(0.3)
# pygame.mixer.music.play()

# splat = pygame.mixer.Sound("hello-world-book-programs/sounds/splat.wav")
# splat.set_volume(0.5)

# RUNNING = True
# while RUNNING:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             RUNNING = False
#             sys.exit()

#     if not pygame.mixer.music.get_busy():  # Checks if the music is done playing
#         splat.play()
#         pygame.time.delay(1000)  # Waits 1 second for the “splat” sound to finish
#         RUNNING = False
#         sys.exit()
# pygame.quit()
