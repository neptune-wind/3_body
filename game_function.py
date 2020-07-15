import sys
from time import sleep
import pygame
from stars import Star
from visualization import Visualization

def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def create_star_and_vz(stars, vzs, screen, ai_settings, num):
    star = Star(screen, stars, ai_settings, num)
    vz = Visualization(screen, ai_settings, star)

    stars.add(star)
    vzs.add(vz)

def create_star_fleet(stars, vzs, screen, ai_settings):
    for num in range(ai_settings.star_num):
        create_star_and_vz(stars, vzs, screen, ai_settings, num)

def update_screen(ai_settings, screen, stars, vzs):
    screen.fill(ai_settings.bg_color)

    for star in stars:
        star.update()
        star.blitme()

    for vz in vzs:
        vz.update()
        vz.blit_circle()
        vz.blit_acc_vz_line()

    pygame.display.update()