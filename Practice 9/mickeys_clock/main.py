import pygame
import sys
from clock import rotate_center, get_time_angles

pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")
clock = pygame.time.Clock()

# Загрузка ресурсов с учетом твоих названий файлов
# Проверь, чтобы в папке images названия были именно такими!
try:
    bg = pygame.image.load('images/main-clock.png')
    # Используем разные руки для минут и секунд
    min_hand_img = pygame.image.load('images/left-hand.PNG')
    sec_hand_img = pygame.image.load('images/right-hand.PNG')
except FileNotFoundError as e:
    print(f"Ошибка: Не найден файл изображения! {e}")
    pygame.quit()
    sys.exit()

# --- ЗАГРУЗКА ИЗОБРАЖЕНИЙ (Найди этот блок в своем main.py) ---
try:
    bg = pygame.image.load('images/main-clock.png')
    # Используем разные руки для минут и секунд
    min_hand_img_raw = pygame.image.load('images/left-hand.PNG') # Исходная большая
    sec_hand_img_raw = pygame.image.load('images/right-hand.PNG') # Исходная большая
except FileNotFoundError as e:
    print(f"Ошибка: Не найден файл изображения! {e}")
    pygame.quit()
    sys.exit()

# --- МАСШТАБИРОВАНИЕ (ДОБАВЬ ЭТИ СТРОКИ) ---
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

# Уменьшаем минутную руку. Попробуй размер (200, 100)
# (Ширина 200 - от центра, Высота 100 - толщина руки)
min_hand_img = pygame.transform.scale(min_hand_img_raw, (300, 500))

# Уменьшаем секундную руку. Сделай её тоньше и длиннее, например (250, 50)
sec_hand_img = pygame.transform.scale(sec_hand_img_raw, (300, 500))

# Точка вращения (центр экрана)
center = (WIDTH // 2, HEIGHT // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Получаем углы на основе текущего времени
    sec_angle, min_angle = get_time_angles()

    # Отрисовка
    screen.blit(bg, (0, 0))

    # Рисуем минутную руку (левая)
    min_hand, min_rect = rotate_center(min_hand_img, min_angle, center)
    screen.blit(min_hand, min_rect)

    # Рисуем секундную руку (правая)
    sec_hand, sec_rect = rotate_center(sec_hand_img, sec_angle, center)
    screen.blit(sec_hand, sec_rect)

    pygame.display.flip()
    clock.tick(60)