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
pygame.display.set_caption("Racer Practice 11")

# Настройки времени и FPS
clock = pygame.time.Clock()
FPS = 60

# Переменная для игрового цикла
a = True

# Загружаем фон
try:
    fon = pygame.image.load("AnimatedStreet.png")
    fon = pygame.transform.scale(fon, (width, height))

    player_img = pygame.image.load("Player.png")
    player_img = pygame.transform.scale(player_img, (50, 100))

    enemy_img = pygame.image.load("Enemy.png")
    enemy_img = pygame.transform.scale(enemy_img, (50, 100))

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
enemy_shag = 5 

coin_x = random.randint(40, width-40)
coin_y = -40
coin_shag = 3

# --- NEW VARIABLES FOR PRACTICE 11 ---
score = 0
point = 0
coin_weight = 1  # Вес текущей монеты
N = 10           # Порог монет для ускорения врага
# -------------------------------------

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

while a:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False

    # Движение объектов
    enemy_y += enemy_shag
    coin_y += coin_shag

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < width - 50:
        player_x += 5

    # Области для коллизий
    player_rect = player_img.get_rect(topleft=(player_x, player_y))
    enemy_rect = enemy_img.get_rect(topleft=(enemy_x, enemy_y))
    coin_rect = coin_img.get_rect(topleft=(coin_x, coin_y))
    
    # Респавн врага
    if enemy_y > height:
        score += 1
        enemy_y = -100
        enemy_x = random.randint(50, width-50)

    # Респавн монеты (если пролетела мимо)
    if coin_y > height:
        coin_y = -40
        coin_x = random.randint(40, width-40)
        # Randomly generating coins with different weights (Task 1)
        coin_weight = random.randint(1, 5) 

    # Столкновение с врагом
    if player_rect.colliderect(enemy_rect):
        ecran.fill((255, 0, 0))
        game_over_text = font.render("GAME OVER", True, (0, 0, 0))
        ecran.blit(game_over_text, (20, 250))
        pygame.display.update()
        pygame.time.delay(2000)
        a = False

    # --- TASK 1 & 2: COIN COLLECTION AND ENEMY SPEED UP ---
    if player_rect.colliderect(coin_rect):
        point += coin_weight # Earn points based on weight
        
        # Increase the speed of Enemy when the player earns N coins (Task 2)
        if point >= N:
            enemy_shag += 2
            N += 10 # Increase the next threshold
            
        # Reset coin position and generate new weight
        coin_y = -40
        coin_x = random.randint(40, width-40)
        coin_weight = random.randint(1, 5) # New weight for next coin
    # -------------------------------------------------------

    # ОТРИСОВКА
    ecran.blit(fon, (0, 0)) 

    text_score = font_small.render(f"SCORE: {score}", True, (0, 0, 0))
    # Показываем текущее количество монет и вес следующей монеты
    text_point = font_small.render(f"COINS: {point} (Next: {coin_weight})", True, (0, 0, 0))
    
    ecran.blit(text_score, (5, 5))
    ecran.blit(text_point, (180, 5))

    ecran.blit(player_img, (player_x, player_y))
    ecran.blit(enemy_img, (enemy_x, enemy_y))
    
    # Визуально выделяем монету, если она "тяжелая" (увеличиваем размер)
    current_coin_img = pygame.transform.scale(coin_img, (30 + coin_weight*5, 30 + coin_weight*5))
    ecran.blit(current_coin_img, (coin_x, coin_y))
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()