import pygame
from settings import Settings
import vector_calc as vc
from pygame.sprite import Sprite

class Visualization(Sprite):
    def __init__(self, screen, ai_settings, star):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.star = star

        self.center_x = 150
        self.center_y = self.star.num * 300 + 150

        self.rad = self.ai_settings.vz_rad
        self.num = self.ai_settings.star_num
        self.color = self.star.color

        self.acc_vz_x = 0
        self.acc_vz_y = 0
        self.acc_vz_end_x = self.center_x
        self.acc_vz_end_y = self.center_y

    def update(self):
        self.acc_vz_x = self.star.acc_x_and_y[0] * self.ai_settings.vz_acc_para
        self.acc_vz_y = self.star.acc_x_and_y[1] * self.ai_settings.vz_acc_para

        self.acc_vz_end_x = self.center_x + self.acc_vz_x
        self.acc_vz_end_y = self.center_y + self.acc_vz_y

    def blit_circle(self):
        pygame.draw.circle(self.screen, self.ai_settings.vz_3_color[2],
                           (self.center_x, self.center_y),
                           int(self.rad), 1)
        pygame.draw.circle(self.screen, self.ai_settings.vz_3_color[1],
                           (self.center_x, self.center_y),
                           int(self.rad * 0.667), 1)
        pygame.draw.circle(self.screen, self.ai_settings.vz_3_color[0],
                           (self.center_x, self.center_y),
                           int(self.rad * 0.333), 1)

    def blit_acc_vz_line(self):
        pygame.draw.line(self.screen, self.color,
                         (self.center_x, self.center_y),
                         (self.acc_vz_end_x, self.acc_vz_end_y),
                         3)