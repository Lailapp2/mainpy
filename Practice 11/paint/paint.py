import pygame

pygame.init()

w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Paint Practice 11")

clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 180, 0)
blue = (0, 100, 255)

screen.fill(white)

font = pygame.font.SysFont("Arial", 18)

current_color = black
tool = "brush"
drawing = False
start_pos = None

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b: tool = "brush"
            elif event.key == pygame.K_r: tool = "rectangle"
            elif event.key == pygame.K_c: tool = "circle"
            elif event.key == pygame.K_e: tool = "eraser"
            # Новые клавиши для Practice 11
            elif event.key == pygame.K_s: tool = "square"
            elif event.key == pygame.K_t: tool = "right_triangle"
            elif event.key == pygame.K_a: tool = "equilateral_triangle"
            elif event.key == pygame.K_d: tool = "rhombus"
            
            elif event.key == pygame.K_1: current_color = black
            elif event.key == pygame.K_2: current_color = red
            elif event.key == pygame.K_3: current_color = green
            elif event.key == pygame.K_4: current_color = blue
            elif event.key == pygame.K_SPACE: screen.fill(white)

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            x1, y1 = start_pos
            x2, y2 = end_pos

            # 1. Draw square (Task 1)
            if tool == "square":
                side = abs(x2 - x1)
                # Рисуем квадрат, используя side для ширины и высоты
                pygame.draw.rect(screen, current_color, (min(x1, x2), min(y1, y2), side, side), 3)

            # 2. Draw right triangle (Task 2)
            elif tool == "right_triangle":
                points = [(x1, y1), (x1, y2), (x2, y2)]
                pygame.draw.polygon(screen, current_color, points, 3)

            # 3. Draw equilateral triangle (Task 3)
            elif tool == "equilateral_triangle":
                side = x2 - x1
                height_tri = int(side * 0.866) # Формула высоты равностороннего треугольника
                points = [(x1, y1), (x2, y1), ((x1 + x2) // 2, y1 - height_tri)]
                pygame.draw.polygon(screen, current_color, points, 3)

            # 4. Draw rhombus (Task 4)
            elif tool == "rhombus":
                mid_x = (x1 + x2) // 2
                mid_y = (y1 + y2) // 2
                # Точки: верх, право, низ, лево
                points = [(mid_x, y1), (x2, mid_y), (mid_x, y2), (x1, mid_y)]
                pygame.draw.polygon(screen, current_color, points, 3)

            # Старые фигуры
            elif tool == "rectangle":
                x = min(x1, x2)
                y = min(y1, y2)
                width = abs(x1 - x2)
                height = abs(y1 - y2)
                pygame.draw.rect(screen, current_color, (x, y, width, height), 3)

            elif tool == "circle":
                radius = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 3)

    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        if tool == "brush":
            pygame.draw.line(screen, current_color, start_pos, mouse_pos, 5)
            start_pos = mouse_pos
        elif tool == "eraser":
            pygame.draw.line(screen, white, start_pos, mouse_pos, 20)
            start_pos = mouse_pos

    # Панель управления
    pygame.draw.rect(screen, white, (0, 0, w, 50))
    info_line1 = "B:Brush|R:Rect|C:Circle|E:Eraser|S:Square|T:RightTri|A:EquiTri|D:Rhombus"
    info_line2 = "1:Black 2:Red 3:Green 4:Blue | Space: Clear"
    
    screen.blit(font.render(info_line1, True, black), (10, 5))
    screen.blit(font.render(info_line2, True, black), (10, 25))

    pygame.display.update()
    clock.tick(60)

pygame.quit()