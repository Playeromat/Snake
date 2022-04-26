import pygame
from SETTINGS import SETTINGS


def get_snake_rects(snake):
    snake_rects = []
    pos_history = snake.get_pos_history()
    snake_pos = snake.get_pos()

    snake_rects.append(pygame.Rect(snake_pos[0], snake_pos[1], SETTINGS.BLOCK_WIDTH, SETTINGS.BLOCK_HEIGHT))

    for i in range(snake.get_tail_length()):
        snake_rects.append(pygame.Rect(pos_history[i][0], pos_history[i][1], SETTINGS.BLOCK_WIDTH, SETTINGS.BLOCK_HEIGHT))

    return snake_rects


def get_food_rects(foods):
    food_rects = []
    for food in foods:
        food_pos = food.get_pos()
        food_rects.append(pygame.Rect(food_pos[0], food_pos[1], SETTINGS.BLOCK_WIDTH, SETTINGS.BLOCK_HEIGHT))

    return food_rects
