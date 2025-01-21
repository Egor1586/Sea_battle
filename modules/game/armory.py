import pygame
import os

from .basement import *
from .map import *

data = read_json(fd="settings.json")

MAIN_WINDOW_COLOR = data["main"]["MAIN_WINDOW_COLOR"]
HEAD_COLOR = data["color"]["HEAD_COLOR"]
FPS = data["main"]["FPS"]

def shop():
    run_shop = True

    PAGE1 = True
    PAGE2 = False

    card = pygame.image.load(os.path.abspath(__file__ + "/../../../image/skills/card.png"))
    card = pygame.transform.scale(card, [240, 380])

    image_point = pygame.image.load(os.path.abspath(__file__ + "/../../../image/achievements/point.png"))
    image_point = pygame.transform.scale(image_point, [50, 30])

    point_list = [image_point, image_point, image_point, image_point, image_point]

    image_torpedo = skills_list[5].image
    
    card_list= [card, card, card, card, card]

    while run_shop:
        screen.fill(MAIN_WINDOW_COLOR)
        
        if PAGE1:     
            gap = 20
            for card in card_list:
                screen.blit(card, (gap, 230))
                gap += 270


            gap = 32
            for skill in skills_list:
                if skill.id != 6:
                    screen.blit(skill.image, (gap, 243))
                    gap += 270
            
            text_dynamite.text_draw(screen= screen)
            text_radar.text_draw(screen= screen) 
            text_missile.text_draw(screen= screen) 
            text_shield.text_draw(screen= screen) 
            text_bomb.text_draw(screen= screen)
            text_missile2.text_draw(screen= screen)
            text_radar2.text_draw(screen= screen)
            
            title_dynamite.text_draw(screen= screen)
            title_radar.text_draw(screen= screen) 
            title_missile.text_draw(screen= screen) 
            title_shield.text_draw(screen= screen) 
            title_bomb.text_draw(screen= screen)

            price_dynamite.text_draw(screen= screen)
            price_radar.text_draw(screen= screen)
            price_missile.text_draw(screen= screen)
            price_shield.text_draw(screen= screen)
            price_bomb.text_draw(screen= screen)
            
            gap = 160
            for item in point_list:
                screen.blit(item,  (gap, 558))
                gap += 265

        if PAGE2:
            screen.blit(card, (20, 230))
            screen.blit(image_torpedo, (32, 243))
            
            text_torpedo.text_draw(screen= screen)
            title_torpedo.text_draw(screen= screen)
        
            price_torpedo.text_draw(screen= screen)

            screen.blit(image_point, (160, 560))

        
        position = pygame.mouse.get_pos()
       
        press = pygame.mouse.get_pressed()

        pygame.draw.rect(screen, HEAD_COLOR, (0, 0, 1400, 150), 0)
        Armory_text.text_draw(screen = screen)
           

        button_back_menu.button_draw(screen = screen)
        
        armory_page1.button_draw(screen = screen)
        armory_page2.button_draw(screen = screen)

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and press[0]:

                back_to_menu = button_back_menu.checkPress(position = position, press = press)

                page1 = armory_page1.checkPress(position = position, press = press)
                page2 = armory_page2.checkPress(position = position, press = press)
                
                if back_to_menu:
                    return "HOME"
                    
                if page1:
                    PAGE1 = True
                    PAGE2 = False
                elif page2:
                    PAGE1 = False
                    PAGE2 = True

                
            if event.type == pygame.QUIT:
                run_shop = False
                pygame.quit()