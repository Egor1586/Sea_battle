import pygame
import os
import socket

from .basement import *
from .placement import placement
from .settings_real import settings_real
from .armory import shop

# pygame.mouse.set_cursor(*pygame.cursors.tri_left)
# pygame.mouse.set_cursor()

data = read_json(fd="settings.json")

GOLD = data["main"]["GOLD"]
FPS = data["main"]["FPS"]
MUSIC_NAME = str(data["main"]["MUSIC_NAME"])

play_music(f"{MUSIC_NAME}", volume = 0.1)

def menu():
    run_menu = True

    def get_local_ip():
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    
    data["lan_ip"] = get_local_ip()

    IP_TEXT = Text(x =120, y = 550, text = str(data["lan_ip"]), text_size=45, color="Black")

    im_coin = pygame.image.load(os.path.abspath(__file__ + "/../../../image/coins/coin_silver.png"))
    im_coin = pygame.transform.scale(im_coin, [60, 60])
    im_coin_holder = pygame.image.load(os.path.abspath(__file__ + "/../../../image/coins/coin_holder2.png"))
    im_coin_holder = pygame.transform.scale(im_coin_holder, [375, 75])
    bg = pygame.image.load(os.path.abspath(__file__ + "/../../../image/bg/background.png"))
    bg = pygame.transform.scale(bg, [1400, 800])

    count_gold = Text(x = 1050, y = 50, text = str(GOLD), text_size=25, color="Grey")
    
    while run_menu:
        screen.fill(MAIN_WINDOW_COLOR)

        screen.blit(bg, (0, 0))
        screen.blit(im_coin_holder,(1000, 20))
        screen.blit(im_coin,(1250, 25))

        #Створення кнопок "play" "settings" "quit", задавання їх величини та кординат на головному екрані. Містять у собі рядковий контент.
        
        button_play.button_draw(screen = screen)
        button_settings.button_draw(screen = screen)
        button_Armory.button_draw(screen = screen)
        button_quit.button_draw(screen = screen)

        IP_TEXT.text_draw(screen = screen)

        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()

        count_gold.text_draw(screen = screen)

        # print(clock.get_fps())

        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and press[0]:

                wait_opponent_window = button_play.checkPress(position = position, press = press)
                settigs_window = button_settings.checkPress(position = position, press = press)
                Armory_win = button_Armory.checkPress(position = position, press = press)
                quit = button_quit.checkPress(position = position, press = press)

                if wait_opponent_window:
                    placement()
                if settigs_window:
                    settings_real()
                if Armory_win:
                    shop()
                if quit:
                    run_menu = False

            if event.type == pygame.QUIT:
                run_menu = False
                pygame.quit()
