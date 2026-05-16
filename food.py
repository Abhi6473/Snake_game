# food.py
import random

SPACE_SIZE = 50
FOOD_COLOR = "#FF0000"
CANVAS_W = 700
CANVAS_H = 700

class Food:
    def __init__(self, canvas, snake, blockades):
        while True:
            x = random.randint(0, (CANVAS_W // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (CANVAS_H // SPACE_SIZE) - 1) * SPACE_SIZE
            # avoid food to respawn on blockade or snake
            if [x, y] in blockades.coordinates:
                continue
            if [x, y] in snake.coordinates:
                continue

            break

        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
