import pygame
import sys
import random

# Ініціалізація Pygame
pygame.init()

# Константи
WIDTH, HEIGHT = 800, 600
FPS = 60

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Розмір блоку
BLOCK_SIZE = 40

# Створення гравця
player = pygame.Rect(50, 50, BLOCK_SIZE, BLOCK_SIZE)

# Створення вихідної точки та вихіду
exit_point = pygame.Rect(700, 500, BLOCK_SIZE, BLOCK_SIZE)
exit_door = pygame.Rect(750, 550, BLOCK_SIZE, BLOCK_SIZE)

# Створення перешкод
obstacles = [pygame.Rect(200, 200, BLOCK_SIZE, BLOCK_SIZE),
             pygame.Rect(400, 300, BLOCK_SIZE, BLOCK_SIZE),
             pygame.Rect(600, 200, BLOCK_SIZE, BLOCK_SIZE)]

# Створення вікна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пригоди у Лабіринті")

clock = pygame.time.Clock()

# Головний цикл гри
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Рух гравця за допомогою стрілок
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.move_ip(-BLOCK_SIZE, 0)
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.move_ip(BLOCK_SIZE, 0)
    if keys[pygame.K_UP] and player.top > 0:
        player.move_ip(0, -BLOCK_SIZE)
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.move_ip(0, BLOCK_SIZE)

    # Перевірка на зіткнення з вихідними точкою та вихідом
    if player.colliderect(exit_point) and player.colliderect(exit_door):
        print("Ви виграли!")
        pygame.quit()
        sys.exit()

    # Перевірка на зіткнення з перешкодами
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            print("Ви врізалися в перешкоду. Гра закінчена!")
            pygame.quit()
            sys.exit()

    # Відображення
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, exit_point)
    pygame.draw.rect(screen, BLACK, exit_door)
    pygame.draw.rect(screen, BLACK, player)
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, obstacle)

    pygame.display.flip()
    clock.tick(FPS)
