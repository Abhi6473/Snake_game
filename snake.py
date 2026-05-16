# snake.py
SNAKE_COLORS = ["#00FF00","#00DD00","#00BB00","#009900","#007700","#005500"]
SPACE_SIZE = 50
BODY_PARTS = 3

class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.body_size = BODY_PARTS
        self.coordinates = [[300,300],[250,300],[200,300]]
        self.squares = []
        for i, (x, y) in enumerate(self.coordinates):
            color = SNAKE_COLORS[min(i, len(SNAKE_COLORS)-1)]
            
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=color, tag="snake")
            self.squares.append(square)
