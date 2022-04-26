import random
import pygame
import RectGenerator
import colisionChecks
from Snake import Snake
from FoodHandler import FoodHandler
from SETTINGS import SETTINGS
from ScoreHandler import ScoreHandler

random.seed()

WINDOW = pygame.display.set_mode((SETTINGS.GAME_WIDTH, SETTINGS.GAME_HEIGHT))

pygame.display.set_caption("Bruno")


def draw_window(snake_rects, food_rects):
    WINDOW.fill(SETTINGS.BG_COLOUR)

    for food_rect in food_rects:
        pygame.draw.rect(WINDOW, SETTINGS.FOOD_COLOUR, food_rect)

    for snake_rect in snake_rects:
        pygame.draw.rect(WINDOW, SETTINGS.SNAKE_COLOUR, snake_rect)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    keepRunning = True
    last_input = None
    fps = SETTINGS.FPS

    snake = Snake()
    food_handler = FoodHandler()
    score_handler = ScoreHandler()

    while keepRunning:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepRunning = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and last_input != pygame.K_DOWN:
                    snake.set_vel([0, -SETTINGS.BLOCK_HEIGHT])
                    last_input = event.key
                if event.key == pygame.K_DOWN and last_input != pygame.K_UP:
                    snake.set_vel([0, SETTINGS.BLOCK_HEIGHT])
                    last_input = event.key
                if event.key == pygame.K_LEFT and last_input != pygame.K_RIGHT:
                    snake.set_vel([-SETTINGS.BLOCK_WIDTH, 0])
                    last_input = event.key
                if event.key == pygame.K_RIGHT and last_input != pygame.K_LEFT:
                    snake.set_vel([SETTINGS.BLOCK_WIDTH, 0])
                    last_input = event.key

        snake.move()

        snake_rects = RectGenerator.get_snake_rects(snake)
        food_rects = RectGenerator.get_food_rects(FoodHandler.get_foods(food_handler))

        if colisionChecks.check_death(snake_rects) or colisionChecks.check_bounds(snake):
            snake.reset()
            score_handler.reset_score()
            last_input = None
            fps = SETTINGS.FPS

        if colisionChecks.check_food_pickup(snake_rects[0], FoodHandler.get_foods(food_handler)):
            snake.set_tail_length(snake.get_tail_length() + 1)
            score_handler.add_score(1)
            food_handler.remove_picked()

            if SETTINGS.INCREASE_SPEED:
                fps *= SETTINGS.SPEED_MULTIPLIER

        draw_window(snake_rects, food_rects)

    pygame.quit()


if __name__ == "__main__":
    main()
