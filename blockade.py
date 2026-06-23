# blockade.py
import random

SPACE_SIZE = 50
BLOCKADE_COLOR = "#888888"
CANVAS_W = 700
CANVAS_H = 700

# How many grid cells of buffer to keep clear around the snake
SAFE_RADIUS_CELLS = 3

class Blockade:
    def __init__(self, canvas, count=5, snake=None, safe_cells=None):
        """
        canvas: the tkinter canvas to draw on
        count: number of blockades to place
        snake: optional Snake instance, used to avoid spawning on/near it
        safe_cells: optional explicit set of (x, y) cells to avoid (e.g. a
                    starting safe-zone), in addition to any snake buffer
        """
        self.canvas = canvas
        self.count = count
        self.coordinates = []
        self._draw_ids = []
        self._place_all(snake=snake, safe_cells=safe_cells)

    def _forbidden_cells(self, snake=None, safe_cells=None):
        """Build the set of grid cells blockades must not occupy."""
        forbidden = set()

        if safe_cells:
            forbidden.update(tuple(c) for c in safe_cells)

        if snake is not None:
            # Keep a buffer of cells clear around every current snake segment
            for (sx, sy) in snake.coordinates:
                scx, scy = sx // SPACE_SIZE, sy // SPACE_SIZE
                for dx in range(-SAFE_RADIUS_CELLS, SAFE_RADIUS_CELLS + 1):
                    for dy in range(-SAFE_RADIUS_CELLS, SAFE_RADIUS_CELLS + 1):
                        forbidden.add((scx + dx, scy + dy))

        return forbidden

    def _random_free_cell(self, forbidden, taken):
        """Find a grid cell that isn't forbidden and isn't already taken."""
        max_attempts = 500
        cols = CANVAS_W // SPACE_SIZE
        rows = CANVAS_H // SPACE_SIZE

        for _ in range(max_attempts):
            cx = random.randint(0, cols - 1)
            cy = random.randint(0, rows - 1)
            if (cx, cy) in forbidden:
                continue
            if (cx, cy) in taken:
                continue
            return cx, cy

        # Fallback: scan deterministically for any free cell at all
        for cx in range(cols):
            for cy in range(rows):
                if (cx, cy) not in forbidden and (cx, cy) not in taken:
                    return cx, cy

        return None  # Grid is completely full (shouldn't realistically happen)

    def _place_all(self, snake=None, safe_cells=None):
        forbidden = self._forbidden_cells(snake=snake, safe_cells=safe_cells)
        taken = set()
        new_coords = []

        for _ in range(self.count):
            cell = self._random_free_cell(forbidden, taken)
            if cell is None:
                break
            cx, cy = cell
            taken.add((cx, cy))
            new_coords.append([cx * SPACE_SIZE, cy * SPACE_SIZE])

        self.coordinates = new_coords
        self._redraw()

    def _redraw(self):
        # Remove old blockade shapes and draw fresh ones at current coordinates
        self.canvas.delete("blockade")
        self._draw_ids = []
        for x, y in self.coordinates:
            shape = self.canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=BLOCKADE_COLOR, tag="blockade"
            )
            self._draw_ids.append(shape)

    def reposition(self, snake=None, safe_cells=None):
        """Move all blockades to new random safe positions instantly."""
        self._place_all(snake=snake, safe_cells=safe_cells)
