import pygame
import vector_calc as vc

puple = (120, 15, 235)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (23, 187, 1)

light_purple = (189, 137, 247)
light_red = (255, 147, 147)
light_blue = (117, 178, 251)
light_green = (124, 254, 106)

black_3 = (0, 0, 0)
black_2 = (95, 95, 95)
black_1 = (128, 128, 128)

class Settings():
    def __init__(self):
        self.screen_width = 1500
        self.screen_height = 900
        self.bg_color = (51, 51, 51)

        self.star_num = 3
        self.star_radius = 3
        self.star_settings_list = \
        [
            {'init_pos_x': 700, 'init_pos_y': 100, 'init_speed_modulo': 0.08,
             'init_speed_angle': 0, 'mass': 3, 'color': red, 'route_color': light_red},

            {'init_pos_x': 700, 'init_pos_y': 600, 'init_speed_modulo': 0.08,
             'init_speed_angle': 180, 'mass': 3, 'color': blue, 'route_color': light_blue},

            {'init_pos_x': 1200, 'init_pos_y': 300, 'init_speed_modulo': 0,
             'init_speed_angle': -90, 'mass': 3, 'color': green, 'route_color': light_green},
        ]

        self.routh_length = 2000

        self.vz_3_color = (black_1, black_2, black_3)
        self.vz_rad = 120
        self.vz_acc_para = 40000

        self.G = 10