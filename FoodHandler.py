import math
import random
from SETTINGS import SETTINGS
from Food import Food

random.seed()


class FoodHandler:

    def __init__(self):
        self.foods = []
        self.generate_food(SETTINGS.FOOD_COUNT)

    def generate_food(self, count):
        for i in range(count):
            dummy = Food(random.randint(1, SETTINGS.GAME_WIDTH / SETTINGS.BLOCK_WIDTH) * SETTINGS.BLOCK_WIDTH - SETTINGS.BLOCK_WIDTH, random.randint(1, SETTINGS.GAME_HEIGHT / SETTINGS.BLOCK_HEIGHT) * SETTINGS.BLOCK_HEIGHT - SETTINGS.BLOCK_HEIGHT)
            self.foods.append(dummy)

    def get_foods(self):
        return self.foods

    def remove_picked(self):
        for food in self.foods:
            if food.is_picked():
                self.foods.remove(food)
                if len(self.get_foods()) == 0:
                    self.generate_food(SETTINGS.FOOD_COUNT)
                break
