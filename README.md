---
# Snake Game (Tkinter Edition)

A classic Snake Game built using Python's `tkinter` GUI framework. This version includes dynamic food placement, moving snake, blockades, restart capability, user tracking, and persistent score management.

---
## Prerequisites

Before running the game, ensure that the following are installed on your system:

Python 3.8 or higher
Tkinter library (usually comes pre-installed with Python)

To verify Python installation, open a terminal/command prompt and run:

python --version

or

python3 --version

To verify Tkinter installation:

python -m tkinter

A small Tkinter window should appear if Tkinter is installed correctly.

---

## Project Structure

```bash
├── game.py              # Main game logic and UI
├── snake.py             # Snake class (movement, rendering)
├── food.py              # Food class with collision-aware placement
├── blockade.py          # Blockade class with random placement
├── score_manager.py     # Handles user scores and JSON I/O
├── scores.json          # Auto-generated file storing player high scores
└── README.md            # You are here!
```

---
## Running the Game
# Windows

* Make sure all `.py` files are in the same directory.
* Open Command Prompt or VS code.
* Navigate to the project directory:
* cd path\to\SnakeGame
# Windows :
* Run the program:
```bash
python game.py
```

# Linux/macOS
* Run the program:
```bash
python3 game.py
```
A window will open where you can enter your name and start playing.

---
## How to Play
After launching the game, enter your name and click Start.
Control the snake using the keyboard arrow keys:
Key	Action
↑	Move Up
↓	Move Down
←	Move Left
→	Move Right

Eat the food blocks to increase your score.
Avoid:
Hitting the walls
Hitting your own body
Colliding with blockades (obstacles)
The game ends when a collision occurs.
Features
User name input before starting the game.
Score tracking during gameplay.
Personal best score tracking.
Global high score tracking.
Top players leaderboard.
Random food generation.
Random blockade generation.
Restart option after Game Over.

## Troubleshooting
## ModuleNotFoundError

If you encounter errors such as:

ModuleNotFoundError: No module named 'snake'

Ensure that:

snake.py
food.py
blockade.py
score_manager.py

are present in the same folder as main.py.

## Tkinter Not Found

Install Tkinter if it is missing.

## Ubuntu/Debian:

sudo apt install python3-tk

## Fedora:

sudo dnf install python3-tkinter

## Windows:

Reinstall Python and ensure that Tcl/Tk and IDLE are selected during installation.

Exit

Close the game window at any time to terminate the application.
