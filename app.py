import pygame
import random

# 파일을 화면에 끓어다 놓으면 해당 파일을 parameter로 받는 function으로 개선
def check_voca_list():
    
    VOCA = []

    with open ('words.txt', 'r') as words:
        DATA = words.readlines()
    
    for d in DATA:
        VOCA.append(d.strip())

    print(VOCA)
    return VOCA

def randomize_answer(words):
    answer = ''

    if words != False:
        random.shuffle(words)
        answer = words.pop(0)

    return answer

def main():

    DUMMY_DATA = ["apple", "orange", "lemon", "watermelon"]
    WIDTH, HEIGHT = 640, 480
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    
    answer_box = pygame.Rect(WIDTH * 0.1, HEIGHT * 0.1, WIDTH * 0.8, HEIGHT / 4)
    input_box = pygame.Rect(WIDTH * 0.1, HEIGHT * 0.4, WIDTH * 0.8, HEIGHT / 6)

    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    answer = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                check_voca_list()
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text == answer:
                            print("Correct!")
                            text = ''
                        else:
                            print("Wrong!")
                            text = ''

                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]

                    elif event.key == pygame.K_F1:
                        answer = randomize_answer(check_voca_list())

                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)

        # Render an answer at random
        txt_answer = font.render(answer, True, color)

        # Resize the box if the text is too long.
        width = max(400, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)
        
        # Blit the answer_box rect.
        pygame.draw.rect(screen, color, answer_box, 2)
        screen.blit(txt_answer, (answer_box.x+5, answer_box.y+5))

        pygame.display.flip()

        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()