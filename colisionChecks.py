from SETTINGS import SETTINGS


def check_death(snake_rects):
    first = True

    for snake_rect in snake_rects:
        if first:
            first = False
            continue

        if snake_rects[0].x == snake_rect.x and snake_rects[0].y == snake_rect.y:
            return True

    return False


def check_bounds(snake):
    snake_pos = snake.get_pos()

    if SETTINGS.NO_BOUNDS:
        # Infinite
        if snake_pos[0] > SETTINGS.GAME_WIDTH - SETTINGS.BLOCK_WIDTH:
            snake.set_pos(0, snake_pos[1])
        if snake_pos[0] < 0:
            snake.set_pos(SETTINGS.GAME_WIDTH - SETTINGS.BLOCK_WIDTH, snake_pos[1])
        if snake_pos[1] > SETTINGS.GAME_HEIGHT - SETTINGS.BLOCK_HEIGHT:
            snake.set_pos(snake_pos[0], 0)
        if snake_pos[1] < 0:
            snake.set_pos(snake_pos[0], SETTINGS.GAME_HEIGHT - SETTINGS.BLOCK_HEIGHT)
    else:
        # Blocked
        if snake_pos[0] > SETTINGS.GAME_WIDTH - SETTINGS.BLOCK_WIDTH \
                or snake_pos[0] < 0 \
                or snake_pos[1] > SETTINGS.GAME_HEIGHT - SETTINGS.BLOCK_HEIGHT \
                or snake_pos[1] < 0:
            return True

    return False


def check_food_pickup(snake_head, foods):
    for food in foods:
        food_pos = food.get_pos()
        if food_pos[0] == snake_head.x and food_pos[1] == snake_head.y:
            food.set_picked()
            return True

    return False
