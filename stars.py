import pygame
from settings import Settings
import vector_calc as vc
from pygame.sprite import Sprite

def add_and_restrict_list(route_list, ele, num):
    route_list.insert(0, ele)
    if len(route_list) > num:
        route_list.pop()

class Star(Sprite):
    def __init__(self, screen, stars, ai_settings, num):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.acc_x_and_y = [float(0), float(0)]
        self.stars = stars

        self.num = num

        self.color = ai_settings.star_settings_list[num]['color']
        self.route_color = ai_settings.star_settings_list[num]['route_color']
        # self.image = pygame.image.load('image/star.bmp')
        # self.rect = self.image.get_rect()

        # self.rect = pygame.draw.circle(screen, self.color, [0, 0], 10, 0)

        self.rect_centerx = ai_settings.star_settings_list[num]['init_pos_x']
        self.rect_centery = ai_settings.star_settings_list[num]['init_pos_y']
        self.rect_centerxy = (self.rect_centerx, self.rect_centery)

        self.centerx = float(self.rect_centerx)
        self.centery = float(self.rect_centery)

        self.speed_axis_x = vc.get_x_from_vec(
            ai_settings.star_settings_list[num]['init_speed_modulo'],
            ai_settings.star_settings_list[num]['init_speed_angle'])
        self.speed_axis_y = vc.get_y_from_vec(
            ai_settings.star_settings_list[num]['init_speed_modulo'],
            ai_settings.star_settings_list[num]['init_speed_angle'])

        self.mass = ai_settings.star_settings_list[num]['mass']

        self.x_pos = []
        self.y_pos = []
        self.xy_pos = [self.x_pos, self.y_pos]

        self.route = []

    def update(self):
        self.centerx += self.speed_axis_x
        self.centery += self.speed_axis_y

        self.rect_centerx = int(self.centerx)
        self.rect_centery = int(self.centery)

        self.acc_x_and_y = vc.get_acc_x_and_y(self, self.stars, self.ai_settings)
        print(self.acc_x_and_y)

        self.speed_axis_x += self.acc_x_and_y[0]
        self.speed_axis_y += self.acc_x_and_y[1]

        add_and_restrict_list(self.route,
                              (self.rect_centerx, self.rect_centery),
                              self.ai_settings.routh_length)

    def blitme(self):
        for route_point in self.route:
            pygame.draw.circle(self.screen, self.route_color,
                               (route_point[0], route_point[1]),
                               2)

        pygame.draw.circle(self.screen, self.color,
                           (self.rect_centerx, self.rect_centery),
                           self.ai_settings.star_radius)