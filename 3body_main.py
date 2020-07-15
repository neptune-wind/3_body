import pygame
from pygame.sprite import Group
import sys
from settings import Settings
from stars import Star
import game_function as gf
from visualization import Visualization

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Three body problem")

    stars = Group()
    vzs = Group()

    gf.create_star_fleet(stars, vzs, screen, ai_settings)

    while True:
        gf.check_event()

        gf.update_screen(ai_settings, screen, stars, vzs)

run_game()