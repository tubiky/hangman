import pygame
import random

# 파일을 화면에 끓어다 놓으면 해당 파일을 parameter로 받는 function으로 개선
def check_voca_list():
    
    VOCA = []

    with open ('words.txt', 'r') as words:
        DATA = words.readlines() # text file을 읽어 각각의 라인을 element로 갖는 리스트를 리턴해준다.
    
    for d in DATA:
        VOCA.append(d.strip())

    return VOCA

# 정답을 랜덤하게 정해주는 function
def randomize_answer(words):
    
    answer = ''

    if len(words) != False:
        random.shuffle(words)
        answer = words.pop(0)
        print("randomize_answer is executed", words)

    else:
        print("You've Finished Today's Warm-Up Activity!")

    return answer

# 키보드 Input이 입력될 때 마다(if event.type == KEYDOWN: spell_check(spell, answer)), 
# 정답의 스펠링과 입력값을 비교하여 
# 입력값이 있다면: 입력된 스펠링만 display 
# 입력값이 없다면: 입력된 철자에 해당하는 keypad 사라지게 만들기 - 클릭불능상태로 상태 변화
def spell_check(spell, answer):
    pass




def main():
    DATA = check_voca_list()
    WIDTH, HEIGHT = 1000, 1000
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    small_font = pygame.font.Font(None, int(HEIGHT/15))
    medium_font = pygame.font.Font(None, int(HEIGHT/7))
    large_font = pygame.font.Font(None, int(HEIGHT/3.5))

    clock = pygame.time.Clock()
    
    answer_box = pygame.Rect(WIDTH * 0.05, HEIGHT * 0.1, WIDTH * 0.95, HEIGHT / 4)
    input_box = pygame.Rect(WIDTH * 0.1, HEIGHT * 0.4, WIDTH * 0.9, HEIGHT / 6)

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
                            answer = randomize_answer(check_voca_list())

                        else:
                            print("Wrong!")
                            text = ''

                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]

                    elif event.key == pygame.K_F1:
                        answer = randomize_answer(DATA)

                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = medium_font.render(text, True, color)

        # Render an answer at random
        txt_answer = large_font.render(answer, True, color)

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