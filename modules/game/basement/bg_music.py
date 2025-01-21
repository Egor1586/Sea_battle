'''
Цей модуль відтворює музику 
'''
import pygame 
import os

pygame.mixer.init()

def play_music(name_music: str, volume: int):
    '''
    Ця функція програє музику та змінює гучність нуя
    '''
    path_to_music = os.path.abspath(os.path.join(__file__, "..", "..", "..", "..", "sound", "music"))
    music = (path_to_music + f"/{name_music}.mp3")
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(loops=0, start=2.0, fade_ms=0)
    pygame.mixer.music.set_volume(volume)

def sound_path(name):
    path = os.path.abspath(__file__ + f"/../../../../sound/sounds/{name}.mp3")
    return path


sound_hit_path = sound_path("sound_hit")
sound_miss_path = sound_path("sound_miss")
sound_radar_path = sound_path("sound_radar")
sound_shield_path = sound_path("sound_shield")
sound_put_shield_path = sound_path("sound_put_shield")

swich_path = sound_path("swich")

sound_hit = pygame.mixer.Sound(sound_hit_path)
sound_miss = pygame.mixer.Sound(sound_miss_path)
sound_radar = pygame.mixer.Sound(sound_radar_path)
sound_shield = pygame.mixer.Sound(sound_shield_path)
sound_put_shield = pygame.mixer.Sound(sound_put_shield_path)

swich = pygame.mixer.Sound(swich_path)

sound_hit.set_volume(0.02)
sound_miss.set_volume(0.02)
sound_radar.set_volume(0.02)
sound_shield.set_volume(0.02)
sound_put_shield.set_volume(0.02)
swich.set_volume(0.02)




