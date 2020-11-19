import pygame, sys
import app
from pygame.locals import *

pygame.init()

mainClock = pygame.time.Clock()
pygame.display.set_caption('game base')
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)

background_color = pygame.Color(26,83,92)
button_color1 = pygame.Color(51, 96, 103)
button_color2 = pygame.Color(255, 50, 100)
 
title_font = pygame.font.SysFont(None, 60)
normal_font = pygame.font.SysFont(None, 20)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color) # return Surface object
    textrect = textobj.get_rect() # return Rect object
    #print(textrect)
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect) # surface.blit(Surface, Rect)
 
 
def main_menu():
    while True:
        screen.fill((26,83,92))

        draw_text('HANGMAN for Everyone', title_font, (255, 255, 255), screen, WIDTH/2 - (493/2), 50)
 
        mx, my = pygame.mouse.get_pos()

        addWordsButton = pygame.Rect(500, 200, 260, 80)
        optionButton = pygame.Rect(500, 300, 150, 80)
        quitButton = pygame.Rect(500, 400, 150, 80)
        hangmanRect = pygame.Rect(50, 130, 340, 430)

        pygame.draw.rect(screen, (51, 96, 103), addWordsButton)
        pygame.draw.rect(screen, (255, 50, 100), optionButton)
        pygame.draw.rect(screen, (255, 50, 100), quitButton)
        pygame.draw.rect(screen, button_color2, hangmanRect)

        draw_text("Add Words", title_font, (255, 255, 255), screen, 500, 200)
        draw_text("Option", title_font, (255, 255, 255), screen, 510, 320)
        draw_text("Quit", title_font, (255, 255, 255), screen, 515, 420)


        if addWordsButton.collidepoint((mx, my)):
            if click:
                game()
        if optionButton.collidepoint((mx, my)):
            if click:
                app.main()

        if quitButton.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('Add Words', title_font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Option', title_font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()