import math


def get_x_from_vec(modulo, angle):
    rad = float((angle / 360) * (2 * math.pi))
    x_value = float(modulo * math.cos(rad))
    return x_value

def get_y_from_vec(modulo, angle):
    rad = float((angle / 360) * (2 * math.pi))
    y_value = float(modulo * math.sin(rad))
    return y_value

def get_modulo_from_xy(x, y):
    modulo = (x**2 + y**2)**0.5
    return modulo

def get_angle_from_xy(x, y):
    pass

def get_acc_x_and_y(star, stars, ai_settings):
    acc_x = float(0)
    acc_y = float(0)
    acc_x_temp = float(0)
    acc_y_temp = float(0)
    distance = float(0)
    distance_square = float(0)
    cos_t = float(0)
    sin_t = float(0)
    mark = 0
    for other_star in stars:
        if other_star is not star:
            distance_square = ((other_star.rect_centery - star.rect_centery)**2 +
                               (other_star.rect_centerx - star.rect_centerx)**2)

            if distance_square < 10000.0:
                distance_square = 10000.0

            distance = distance_square**0.5

            sin_t = (other_star.rect_centery - star.rect_centery) / distance
            cos_t = (other_star.rect_centerx - star.rect_centerx) / distance

            acc_y_temp = ((ai_settings.G * other_star.mass) / distance_square) * sin_t
            acc_x_temp = ((ai_settings.G * other_star.mass) / distance_square) * cos_t


            acc_y += acc_y_temp
            acc_x += acc_x_temp

    ret = [acc_x, acc_y]
    return ret