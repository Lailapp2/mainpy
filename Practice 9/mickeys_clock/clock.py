import pygame
import datetime

def rotate_center(image, angle, center):
    # Вращаем исходную картинку
    rotated_image = pygame.transform.rotate(image, angle)
    # Определяем новый прямоугольник с сохранением центра
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

def get_time_angles():
    now = datetime.datetime.now()
    # Секунды: 360 градусов / 60 сек = 6 градусов на 1 сек
    # Минус ставим, так как в pygame вращение идет против часовой стрелки
    sec_angle = -(now.second * 6)
    # Минуты: чтобы стрелка двигалась плавно, добавляем долю секунд
    min_angle = -(now.minute * 6 + now.second * 0.1)
    return sec_angle, min_angle