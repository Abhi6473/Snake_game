# Snake game 
# gradient snake , multiple food types , speed levels , pause 
from tkinter import *
from snake import Snake, SNAKE_COLORS
from blockade import Blockade
from food import Food
from score_manager import update_user_score, get_top_scores
import random

gw = 700
gh = 700
GAME_BG = "#121221"
SPEED = 350
SPACE_SIZE = 50
CANVAS_W = 700
CANVAS_H = 700

paused    = False

def next_turn(snake, food, blockades):
    global direction, score, SPEED
    if paused:
        window.after(SPEED, next_turn, snake, food, blockades)
        return
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLORS[0],outline="black",tag = "snake")
    snake.squares.insert(0, square)
    # Apply gradient colors
    for i, sq in enumerate(snake.squares):
        color = SNAKE_COLORS[min(i, len(SNAKE_COLORS)-1)]
        canvas.itemconfig(sq, fill=color)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        SPEED = max(50, SPEED - 5)
        label.config(text=f"Score: {score}")
        canvas.delete("food")
        food = Food(canvas, snake, blockades)
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake, blockades):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food, blockades)

def check_collisions(snake, blockades):
    x, y = snake.coordinates[0]

    if x < 0 or x >= CANVAS_W or y < 0 or y >= CANVAS_H:
        return True

    for part in snake.coordinates[1:]:
        if part == [x, y]:
            return True

    for bx, by in blockades.coordinates:
        if [x, y] == [bx, by]:
            return True

    return False

def change_direction(new_direction):
    global direction
    opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
    if direction != opposites.get(new_direction):
        direction = new_direction

def start_game():
    global snake, food, blockades, score, direction, SPEED
    SPEED = 350
    window.unbind("<Return>")
    score = 0
    direction = 'down'
    label.config(text=f"Score: {score}")
    canvas.delete("all")

    snake = Snake(canvas)
    blockades = Blockade(canvas, count=5)
    food = Food(canvas, snake, blockades)
    next_turn(snake, food, blockades)

def restart_game():
    start_game()

def game_over():
    canvas.delete("all")
    canvas.create_text(gw / 2, gh / 2 - 100, font=('consolas', 70), text="GAME OVER", fill="red")

    personal_best, global_best = update_user_score(username, score)
    canvas.create_text(gw / 2, gh / 2 - 30, font=('consolas', 28), fill="white", text=f"Your Score: {score}")
    canvas.create_text(gw / 2, gh / 2 + 10, font=('consolas', 24), fill="yellow", text=f"Your Best: {personal_best}  |  Global Best: {global_best}")

    top_scores = get_top_scores()
    scoreboard_text = "Top Players:\n" + "\n".join([f"{i+1}. {name} - {scr}" for i, (name, scr) in enumerate(top_scores)])
    canvas.create_text(gw / 2, gh / 2 + 90, font=('consolas', 20), fill='lightblue', text=scoreboard_text)

    btn = Button(window, text="Restart", font=('consolas', 16), command=restart_game)
    canvas.create_window(gw / 2, gh / 2 + 200, window=btn)
    window.bind("<Return>", lambda e: restart_game())
    
def toggle_pause(event=None):
    global paused
    paused = not paused
    pause_label.config(text="⏸  PAUSED — press P to resume" if paused else "")
    
def ask_username():
    canvas.delete("all")
    canvas.create_text(gw / 2, gh / 2 - 60, font=("Courier New", 30), text="Enter Your Name:", fill="#00FFAA")
    
    entry = Entry(window, font=("consolas", 20))
    canvas.create_window(gw / 2, gh / 2, window=entry)

    def submit():
        global username
        username = entry.get().strip()
        if username:
            canvas.delete("all")
            start_game()
        else:
            canvas.create_text(gw / 2, gh / 2 + 50, text="Please enter a valid name", fill="red", font=("consolas", 16), tag="error")

    btn = Button(window, text="Start", font=("consolas", 15), command=submit)
    canvas.create_window(gw / 2, gh / 2 + 50, window=btn)
    window.bind("<Return>", lambda e: submit())

# Window Setup: 
window=Tk()
window.title("Snake Survival")
window.attributes("-fullscreen",True)
window.configure(bg="black")

#screen dimensions
sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()

direction= "down"
#space background
space_canvas = Canvas(
    window,
    width=sw,
    height=sh,
    bg="black",
    highlightthickness=0
)
space_canvas.pack(fill="both", expand=True)

# Center position calculations
game_x = (sw - gw) // 2
game_y = (sh - gh) // 2 -50

game_x2 = game_x + gw
game_y2 = game_y + gh

#creating space experience
STAR_COUNT = 500
for _ in range(STAR_COUNT):
    while True:
        x = random.randint(0, sw)
        y = random.randint(0, sh)
        # Prevent stars inside game frame
        if not (game_x < x < game_x2 and game_y < y < game_y2):
            break
    # Random tiny star sizes
    size = random.randint(1, 3)
    # Slightly varied white shades
    colors = ["white", "#DDDDDD", "#BBBBBB", "#EEEEFF"]
    space_canvas.create_oval(
        x,
        y,
        x + size,
        y + size,
        fill=random.choice(colors),
        outline=""
    )

#centering the game frame
game_frame = Frame(
    window,
    width=gw,
    height=gh,
    bg=GAME_BG,
    highlightthickness=0,
    highlightbackground="#222244"
)
game_frame.place(
    x=game_x,
    y=game_y
)
# SCORE LABEL
SCORE_BG = GAME_BG
SCORE_FG = "white"
label = Label(
    game_frame,
    text="Score: 0",
    font=("Consolas", 40, "bold"),
    bg="white",
    fg="darkgreen",
    pady=10
)

label.pack(fill=X)

#Pause_ Label
pause_label = Label(
    game_frame, text="",
    font=("Consolas", 16), bg="white", fg="orange"
)
pause_label.pack(fill=X)

# GAME CANVAS

canvas = Canvas(
    game_frame,
    width=700,
    height=700,
    bg=GAME_BG,
    highlightthickness=0
)

canvas.pack(pady=0)
#border walls 
canvas.create_rectangle(
    0,
    0,
    CANVAS_W,
    CANVAS_H,
    outline="white",
    width=4
)

#keyboard bindings
window.bind("<Left>",  lambda e: change_direction("left"))
window.bind("<Right>", lambda e: change_direction("right"))
window.bind("<Up>",    lambda e: change_direction("up"))
window.bind("<Down>",  lambda e: change_direction("down"))
window.bind("<w>", lambda e: change_direction("up"))
window.bind("<a>",  lambda e: change_direction("left"))
window.bind("<s>",  lambda e: change_direction("down"))
window.bind("<d>", lambda e: change_direction("right"))
window.bind("<p>",     toggle_pause)
window.bind("<P>",     toggle_pause)
# ESC KEY TO EXIT
window.bind(
    "<Escape>",
    lambda event: window.destroy()
)

#launch the game
ask_username()
window.mainloop()