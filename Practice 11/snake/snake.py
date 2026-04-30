import pygame
import sys
import random

pygame.init()

width = 400
height = 600
shag = 20

ecran = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Practice 11")

clock = pygame.time.Clock()
speed = 4

a = True

snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"

# --- NEW VARIABLES FOR PRACTICE 11 ---
food = (200, 200)
food_weight = 1             # Вес еды (Task 1)
food_timer = 5000           # Время жизни еды в миллисекундах (Task 2)
last_food_spawn = pygame.time.get_ticks() # Время появления текущей еды
# -------------------------------------

score = 0
level = 0
font = pygame.font.SysFont("Verdana", 20)

while a:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            if event.key == pygame.K_DOWN and direction != "UP":
                direction = "UP" # Ошибка в исходнике была, исправил на DOWN
                direction = "DOWN"
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # --- TASK 2: FOOD DISAPPEARING AFTER SOME TIME (TIMER) ---
    current_time = pygame.time.get_ticks()
    if current_time - last_food_spawn > food_timer:
        # Перегенерация еды, если время вышло
        food = (random.randrange(0, width, shag), random.randrange(0, height, shag))
        food_weight = random.randint(1, 3) # Случайный вес для новой еды
        last_food_spawn = current_time
    # ---------------------------------------------------------

    head_x, head_y = snake[0]

    if direction == "RIGHT":
        head_x += shag
    if direction == "LEFT":
        head_x -= shag
    if direction == "UP":
        head_y -= shag
    if direction == "DOWN":
        head_y += shag

    new_head = (head_x, head_y)

    # Проверка стен и столкновения с собой
    if head_x < 0 or head_x >= width or head_y < 0 or head_y >= height or new_head in snake[1:]:
        ecran.fill((255, 0, 0))
        text = font.render("Game Over", True, (0, 0, 0))
        ecran.blit(text, (130, 280))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)

    # --- TASK 1: RANDOMLY GENERATING FOOD WITH DIFFERENT WEIGHTS ---
    if new_head == food:
        score += food_weight # Добавляем вес еды к счету
        
        # Генерируем новую еду и её характеристики
        food = (random.randrange(0, width, shag), random.randrange(0, height, shag))
        food_weight = random.randint(1, 3) # Вес от 1 до 3
        last_food_spawn = current_time     # Сброс таймера
        
        if score // 5 > level: # Повышаем уровень каждые 5 очков
            level += 1
            speed += 1
    else:
        # Если еда не съедена, удаляем хвост (движение)
        snake.pop()

    # Рисуем фон
    ecran.fill((0, 0, 0))

    # Рисуем змейку
    for part in snake:
        pygame.draw.rect(ecran, (0, 255, 0), (part[0], part[1], shag, shag))

    # Рисуем еду (Размер зависит от веса)
    # Больше вес — больше визуальный размер (но в пределах клетки shag)
    padding = 10 - (food_weight * 3) 
    pygame.draw.rect(ecran, (255, 255, 0), (food[0]+padding, food[1]+padding, shag-padding*2, shag-padding*2))

    # Рисуем интерфейс
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    weight_text = font.render(f"Food Weight: {food_weight}", True, (255, 255, 0))
    
    ecran.blit(text, (10, 10))
    ecran.blit(level_text, (10, 35))
    ecran.blit(weight_text, (200, 10))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()