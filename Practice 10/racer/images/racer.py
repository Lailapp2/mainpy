import pygame
import sys 
import random

# Запускаем pygame
pygame.init() 

# Размеры окна
height = 600
width = 400

# Создаем окно
ecran = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer Practice 10")

# Настройки времени и FPS
clock = pygame.time.Clock()
FPS = 60

# Переменная для игрового цикла
a = True

# Загружаем фон (убедись, что файл лежит в той же папке)
try:
    fon = pygame.image.load("AnimatedStreet.png")
    fon = pygame.transform.scale(fon, (width, height))

    # Загружаем машину игрока
    player_img = pygame.image.load("Player.png")
    player_img = pygame.transform.scale(player_img, (50, 100))

    # Загружаем машину врага
    enemy_img = pygame.image.load("Enemy.png")
    enemy_img = pygame.transform.scale(enemy_img, (50, 100))

    # Загружаем монету
    coin_img = pygame.image.load("Coin.png")
    coin_img = pygame.transform.scale(coin_img, (40, 40))
except pygame.error as e:
    print(f"Ошибка загрузки картинок: {e}")
    pygame.quit()
    sys.exit()

# Начальные позиции
player_x = 200
player_y = 480

enemy_x = random.randint(50, width-50)
enemy_y = -100
enemy_shag = 5 # Увеличили скорость для плавности при 60 FPS

coin_x = random.randint(40, width-40)
coin_y = -40
coin_shag = 3

score = 0
point = 0

# Создаем шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

# ГЛАВНЫЙ ЦИКЛ ИГРЫ
while a:
    # 1. Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False

    # 2. Движение объектов
    enemy_y += enemy_shag
    coin_y += coin_shag

    # 3. Управление игроком (Клавиши)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < width - 50:
        player_x += 5

    # 4. Области для коллизий (обновляем каждый кадр)
    player_rect = player_img.get_rect(topleft=(player_x, player_y))
    enemy_rect = enemy_img.get_rect(topleft=(enemy_x, enemy_y))
    coin_rect = coin_img.get_rect(topleft=(coin_x, coin_y))
    
    # 5. Логика появления новых объектов
    if enemy_y > height:
        score += 1
        enemy_y = -100
        enemy_x = random.randint(50, width-50)
        # Немного ускоряем врага каждые 5 очков
        if score % 5 == 0:
            enemy_shag += 1

    if coin_y > height:
        coin_y = -40
        coin_x = random.randint(40, width-40)

    # 6. Проверка столкновений
    # Столкновение с врагом
    if player_rect.colliderect(enemy_rect):
        ecran.fill((255, 0, 0)) # Красный экран смерти
        game_over_text = font.render("GAME OVER", True, (0, 0, 0))
        ecran.blit(game_over_text, (20, 250))
        pygame.display.update()
        pygame.time.delay(2000)
        a = False

    # Сбор монеты
    if player_rect.colliderect(coin_rect):
        point += 1
        coin_y = -40
        coin_x = random.randint(40, width-40)

    # 7. ОТРИСОВКА
    ecran.blit(fon, (0, 0)) # Фон первым

    # Тексты очков
    text_score = font_small.render(f"SCORE: {score}", True, (0, 0, 0))
    text_point = font_small.render(f"COINS: {point}", True, (0, 0, 0))
    ecran.blit(text_score, (5, 5))
    ecran.blit(text_point, (275, 5))

    # Объекты
    ecran.blit(player_img, (player_x, player_y))
    ecran.blit(enemy_img, (enemy_x, enemy_y))
    ecran.blit(coin_img, (coin_x, coin_y))
    
    # Обновляем экран
    pygame.display.update()
    
    # Ограничение частоты кадров
    clock.tick(FPS)

pygame.quit()
sys.exit()