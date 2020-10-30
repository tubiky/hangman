import pygame as pg
import random



# 파일을 화면에 끓어다 놓으면 해당 파일을 parameter로 받는 function으로 개선
def check_voca_list():
    DATA = []

    with open ('words.txt', 'r') as words:
        DATA.append(words.readlines())

    print(DATA)

def randomize_answer(words):
    no = random.randint(0, len(words))
    answer = words[no]

    return answer

def main():

    DUMMY_DATA = ["apple", "orange", "lemon", "watermelon"]

    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    
    input_box = pg.Rect(100, 100, 140, 32)
    answer_box = pg.Rect(10, 10, 200, 64)

    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    answer = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                check_voca_list()
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive

            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''

                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]

                    elif event.key == pg.K_F1:
                        answer = randomize_answer(DUMMY_DATA)

                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)

        # Render an answer at random
        txt_answer = font.render(answer, True, color)

        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)
        
        # Blit the answer_box rect.
        pg.draw.rect(screen, color, answer_box, 2)
        screen.blit(txt_answer, (answer_box.x+5, answer_box.y+5))

        pg.display.flip()

        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()