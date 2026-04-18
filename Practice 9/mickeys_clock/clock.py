import pygame
import datetime

def rotate_center(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

def get_time_angles():
    now = datetime.datetime.now()
    # 360 градусов / 60 секунд = 6 градусов на одну секунду
    # Вычитаем из 90, так как 0 градусов в pygame — это направление вправо
    sec_angle = 90 - (now.second * 6)
    min_angle = 90 - (now.minute * 6)
    return sec_angle, min_angle