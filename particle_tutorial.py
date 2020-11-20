# Setup Python ----------------------------------------------- #
import pygame, sys, random, os

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((1000, 1000),0,32)

# a particle is a thing that exists at a location
# typically moves around, changes over time, 
# and typically disappears after a certain amount of time

# [loc, velocity, timer]
particles = []


class Keypad(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, x_pos, y_pos, path, filename):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.image.load(os.path.join(str(path), str(filename) + ".png"))

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect(top=x_pos, left=y_pos)

A = Keypad(40, 40, "images", "A")
B = Keypad(100, 200, "images", "B")

keypad_group = pygame.sprite.Group()
keypad_group.add(A)
keypad_group.add(B)

"""
OFFSET = 10
KEYPAD = []
ALPHABET = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]

for i, j in enumerate(ALPHABET):
    i = pygame.image.load(os.path.join("images", j + ".png"))
    KEYPAD.append(i)
"""
# Loop ------------------------------------------------------- #
while True:
    
    # Make mouse cursor invisible
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    
    # Background --------------------------------------------- #
    screen.fill((0,0,0))  # If commented out, the screen is not updated by itself ending up with full of particle effect.
    mx, my = pygame.mouse.get_pos()

    # Particle --------------------------------------------- #
    particles.append([[mx, my], [random.randint(0, 20) / 10 - 1, -2], random.randint(3, 5)])

    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.1
        
        # pygame.draw.circle(Surface, Color, Center, Radius)
        pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))

        if particle[2] <= 0:
            particles.remove(particle)

    keypad_group.draw(screen)
    """
    for i in range(len(KEYPAD)):
        if i <= 12:
            screen.blit(KEYPAD[i], (48*i + OFFSET*i, 0))

        else:
            screen.blit(KEYPAD[i], (48*(i-13) + OFFSET*(i-13), 60))
    """
    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Surface objects doesn't have collidepoint method
        # Rect objects do have collidepoint method
        # If I remove KEY_A element in KEYPAD list, all the other KEY buttons are rearranged since the number of elements is change.
        # What if I just append an empty rect element, whenever I remove KEY surface? and do some exceptions...
        # I want to make a couple of keypads shaking at a random interval of 4 - 7 seconds if there is no MOUSEBUTTONDOWN event
        # What type of parameters are needed to make shaking square?
        # -> Shaking Duration, Interval, Twisted Angle(Is there something like this?), Type of shaking or motion I would say, 
        elif event.type == MOUSEBUTTONDOWN:
            for i in keypad_group:
                if i.rect.collidepoint(event.pos):
                    i.kill()

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)

# BG = pygame.transform.scale(pygame.image.load(os.path.join("FOLDERNAME", "FILENAME.EXTENSION"))), (SIZE_OF_WIDTH, SIZE_OF_HEIGHT))