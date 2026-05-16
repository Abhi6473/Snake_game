# blockade.py
from tkinter import *
import random

SPACE_SIZE = 50
BLOCKADE_COLOR = "#888888"
CANVAS_W = 700
CANVAS_H = 700

class Blockade:
    def __init__(self, canvas, count=5):
        self.coordinates = []
        for _ in range(count):
            while True:
                x = random.randint(0, (CANVAS_W // SPACE_SIZE) - 1) * SPACE_SIZE
                y = random.randint(0, (CANVAS_H // SPACE_SIZE) - 1) * SPACE_SIZE
                if [x, y] in self.coordinates:
                    continue
                # No need to check for overlap with food or snake here
                break
            self.coordinates.append([x, y])
            canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=BLOCKADE_COLOR, tag="blockade")
