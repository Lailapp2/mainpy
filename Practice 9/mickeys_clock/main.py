import pygame
import sys
from clock import rotate_center, get_time_angles

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

# Загрузка картинок
bg = pygame.image.load('images/main_clock.png')
hand = pygame.image.load('images/mickey_hand.png')
bg = pygame.transform.scale(bg, (800, 800))
center = (400, 400)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    sec_angle, min_angle = get_time_angles()

    screen.blit(bg, (0, 0))

    # Рисуем минутную руку
    min_hand, min_rect = rotate_center(hand, min_angle, center)
    screen.blit(min_hand, min_rect)

    # Рисуем секундную руку
    sec_hand, sec_rect = rotate_center(hand, sec_angle, center)
    screen.blit(sec_hand, sec_rect)

    pygame.display.flip()
    clock.tick(60)