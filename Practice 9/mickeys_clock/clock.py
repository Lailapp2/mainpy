import pygame
import datetime

def rotate_center(image, angle, center):
    # Вращаем картинку
    rotated_image = pygame.transform.rotate(image, angle)
    # Находим новый прямоугольник и центрируем его по нужной точке
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

def get_time_angles():
    now = datetime.datetime.now()
    # Углы для Pygame (минус нужен для движения по часовой стрелке)
    sec_angle = -(now.second * 6) 
    min_angle = -(now.minute * 6 + now.second * 0.1)
    return sec_angle, min_angle