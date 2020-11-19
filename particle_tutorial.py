# Setup Python ----------------------------------------------- #
import pygame, sys, random, os

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

# a particle is a thing that exists at a location
# typically moves around, changes over time, 
# and typically disappears after a certain amount of time

# [loc, velocity, timer]
particles = []
KEYPAD = []

KEY_A = pygame.image.load(os.path.join("images", "A.png"))
RECT_A = KEY_A.get_rect()
KEY_B = pygame.image.load(os.path.join("images", "B.png"))
RECT_B = KEY_B.get_rect()
KEY_C = pygame.image.load(os.path.join("images", "C.png"))
KEY_D = pygame.image.load(os.path.join("images", "D.png"))
KEY_E = pygame.image.load(os.path.join("images", "E.png"))
KEY_F = pygame.image.load(os.path.join("images", "F.png"))
KEY_G = pygame.image.load(os.path.join("images", "G.png"))
KEY_H = pygame.image.load(os.path.join("images", "H.png"))
KEY_I = pygame.image.load(os.path.join("images", "I.png"))
KEY_J = pygame.image.load(os.path.join("images", "J.png"))
KEY_K = pygame.image.load(os.path.join("images", "K.png"))
KEY_L = pygame.image.load(os.path.join("images", "L.png"))
KEY_M = pygame.image.load(os.path.join("images", "M.png"))
KEY_N = pygame.image.load(os.path.join("images", "N.png"))

KEYPAD.append(KEY_A)
KEYPAD.append(KEY_B)

# Loop ------------------------------------------------------- #
while True:
    
    # Background --------------------------------------------- #
    screen.fill((0,0,0))  # If commented out, the screen is not updated by itself ending up with full of particle effect.
    mx, my = pygame.mouse.get_pos()
    particles.append([[mx, my], [random.randint(0, 20) / 10 - 1, -2], random.randint(3, 5)])

    for i in range(len(KEYPAD)):
            screen.blit(KEYPAD[i], (48*i, 0))

    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.1
        
        # pygame.draw.circle(Surface, Color, Center, Radius)
        pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)
    
    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Surface objects doesn't have collidepoint method
        # Rect objects have collidepoint method
        # I want to make a couple of keypads shaking at a random interval of 4 - 7 seconds if there is no MOUSEBUTTONDOWN event
        elif event.type == MOUSEBUTTONDOWN:
            if RECT_A.collidepoint(event.pos):
                KEYPAD.remove(KEY_A)

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)

# BG = pygame.transform.scale(pygame.image.load(os.path.join("FOLDERNAME", "FILENAME.EXTENSION"))), (SIZE_OF_WIDTH, SIZE_OF_HEIGHT))