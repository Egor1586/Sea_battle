import pygame

from .basement import *
from .map import *
from .battle import battle
from ..server import server_thread

data = read_json(fd="settings.json")

MAIN_WINDOW_COLOR = data["main"]["MAIN_WINDOW_COLOR"]
FPS =  data["main"]["FPS"]


def wait_opponent():   
    run_wait_opponent = True
    bg = pygame.image.load(os.path.abspath(os.path.join(__file__ + "..", "..", "..",  ".." ,"image", "bg", "wait_for_opponent_bg.png")))
    bg = pygame.transform.scale(bg, [1400, 800])

    IP = get_local_ip()
    LAN_IP = 0

    IP_TEXT = Text(x =50, y = 50, text = str(IP), text_size=45, color="Black")

    input_box = pygame.Rect(850, 150, 400, 50)
    color_inactive = pygame.Color('white')
    color_active = pygame.Color('blue')
    color = color_inactive
    active = False
    text = ''

    font = pygame.font.Font(None, 36)
    WHITE = (255, 255, 255)

    server = True

    while run_wait_opponent:
        screen.fill(MAIN_WINDOW_COLOR)
        screen.blit(bg, (0, 0))
        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()

        join.button_draw(screen = screen)
        create.button_draw(screen= screen)

        search.text_draw(screen = screen)

        IP_TEXT.text_draw(screen = screen)

        txt_surface = font.render(text, True, WHITE)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
            
        # print(clock.get_fps())
        
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Если пользователь нажимает на текстовое поле
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                
                if active:
                    color = color_active
                else: 
                    color_inactive
                
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        LAN_IP = text  # Вывод текста в консоль
                        text = ''  # Очищаем текстовое поле
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            
            if event.type == pygame.MOUSEBUTTONUP and press[0]:

                join_bool = join.checkPress(position = position, press = press)
                
                create_server = create.checkPress(position = position, press = press)

                if create_server:
                    try:
                        server = True
                        server_thread.start() 
                        print("Работаю одновременно с запуском сервера")
                    except:
                        print("CThd")
                    
                    if server:
                        res = battle(IP)
                        if res == "BACK":
                            # отключить сервер
                            return res

                if join_bool:
                    LAN_IP = text
                    text = ''
                    res = battle(LAN_IP)
                    if res == "BACK":
                        # отключиться от сервера
                        return res
            
            if event.type == pygame.QUIT:
                run_wait_opponent = False
                pygame.quit()