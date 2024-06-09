import pygame
import random
import os

from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT, MOUSEBUTTONDOWN

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 750
WIDTH = 1200

FONT = pygame.font.SysFont('Verdana', 20)
GAME_OVER_FONT = pygame.font.SysFont('Verdana', 50)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (255, 0, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = background_image.get_width()
bg_move = 3

IMAGE_PATH = "Goose"
PLAYER_IMG = os.listdir(IMAGE_PATH)

player_image = pygame.image.load('player.png')
player_image = pygame.transform.scale(player_image, (80, 30))
player_rect = player_image.get_rect(center=(0, HEIGHT // 2))

enemy_image = pygame.image.load('enemy.png')
enemy_image = pygame.transform.scale(enemy_image, (40, 40))

bonus_image = pygame.image.load('bonus.png')
bonus_image = pygame.transform.scale(bonus_image, (60, 60))

player_move_down = [0, 5]
player_move_top = [0, -5]
player_move_right = [5, 0]
player_move_left = [-5, 0]

def create_enemy():
    enemy_size = enemy_image.get_size()
    enemy_rect = pygame.Rect(WIDTH, random.randint(HEIGHT // 4, 3 * HEIGHT // 4 - enemy_size[1]), *enemy_size)
    enemy_move = [random.randint(-8, -4), 0]
    return [enemy_image, enemy_rect, enemy_move]

def create_bonus():
    bonus_size = bonus_image.get_size()
    bonus_rect = pygame.Rect(random.randint(WIDTH // 4, 3 * WIDTH // 4 - bonus_size[0]), 0, *bonus_size)
    bonus_move = [0, random.randint(4, 8)]
    return [bonus_image, bonus_rect, bonus_move]

def draw_button(display, text, font, color, rect):
    pygame.draw.rect(display, color, rect)
    text_surface = font.render(text, True, COLOR_BLACK)
    text_rect = text_surface.get_rect(center=rect.center)
    display.blit(text_surface, text_rect)

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 2000)

CHANGE_IMG = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMG, 200)

enemies = []
bonuses = []

score = 0

img_index = 0

playing = True
game_over = False

button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
button_rect_exit = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 120, 200, 50)

while playing:
    FPS.tick(500)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY and not game_over:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS and not game_over:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMG:
            player_image = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMG[img_index]))
            player_image = pygame.transform.scale(player_image, (80, 30))
            img_index += 1
            if img_index >= len(PLAYER_IMG):
                img_index = 0
        if event.type == MOUSEBUTTONDOWN and game_over:
            if button_rect.collidepoint(event.pos):
                game_over = False
                score = 0
                player_rect.center = (0, HEIGHT // 2)
                enemies = []
                bonuses = []
            if button_rect_exit.collidepoint(event.pos):
                playing = False

    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X1 < -background_image.get_width():
        bg_X1 = background_image.get_width()

    if bg_X2 < -background_image.get_width():
        bg_X2 = background_image.get_width()

    main_display.blit(background_image, (bg_X1, 0))
    main_display.blit(background_image, (bg_X2, 0))

    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[K_DOWN] and player_rect.bottom < HEIGHT:
            player_rect = player_rect.move(player_move_down)
            
        if keys[K_RIGHT] and player_rect.right < WIDTH:
            player_rect = player_rect.move(player_move_right)

        if keys[K_UP] and player_rect.top > 0:
            player_rect = player_rect.move(player_move_top)

        if keys[K_LEFT] and player_rect.left > 0:
            player_rect = player_rect.move(player_move_left)

        for enemy in enemies:
            enemy[1] = enemy[1].move(enemy[2])
            main_display.blit(enemy[0], enemy[1])

            if player_rect.colliderect(enemy[1]):
                game_over = True

        for bonus in bonuses:
            bonus[1] = bonus[1].move(bonus[2])
            main_display.blit(bonus[0], bonus[1])

            if player_rect.colliderect(bonus[1]):
                score += 1
                bonuses.pop(bonuses.index(bonus))

        main_display.blit(FONT.render(str(score), True, COLOR_BLACK), (WIDTH - 50, 20))
        main_display.blit(player_image, player_rect)

        pygame.display.flip()

        for enemy in enemies:
            if enemy[1].left < 0:
                enemies.pop(enemies.index(enemy))

        for bonus in bonuses:
            if bonus[1].top > HEIGHT:
                bonuses.pop(bonuses.index(bonus))
        

    else:
        main_display.blit(GAME_OVER_FONT.render(f"SCORE: {score}", True, COLOR_BLACK), (WIDTH // 2 - 100, HEIGHT // 2 - 25))
        draw_button(main_display, "Play Again", FONT, COLOR_GREEN, button_rect)
        draw_button(main_display, "Exit", FONT, COLOR_RED, button_rect_exit)
        pygame.display.flip()

pygame.quit()
