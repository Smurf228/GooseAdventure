# GooseAdventure

GooseAdventure is a fast-paced 2D arcade game built with Python and Pygame.
You control an animated goose, dodge incoming rockets, collect falling bonuses, and survive as long as possible to increase your score.

## Why This Project

This project demonstrates practical game development fundamentals:

- real-time game loop and event handling
- keyboard movement with collision constraints
- spawning enemies and bonuses with timer-based events
- collision detection and score tracking
- animated sprite switching
- restart and exit flow on game over

## Gameplay

### Objective

- Avoid enemy rockets.
- Collect bonus items to increase your score.
- Keep going as long as possible.

### Controls

- Arrow Up: move up
- Arrow Down: move down
- Arrow Left: move left
- Arrow Right: move right

### Game Over Menu

- `Play Again` resets score and restarts gameplay.
- `Exit` closes the game.

## Tech Stack

- Python 3
- Pygame

## Project Structure

```text
GooseAdventure/
|-- Goose/                  # Goose animation frames
|   |-- 1-1.png
|   |-- 1-2.png
|   |-- 1-3.png
|   |-- 1-4.png
|   `-- 1-5.png
|-- background.png
|-- bonus.png
|-- enemy.png
|-- player.png
|-- main.py
`-- README.md
```

## Run Locally

1. Clone the repository:

```bash
git clone https://github.com/Smurf228/GooseAdventure.git
cd GooseAdventure
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
```

Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install pygame
```

4. Start the game:

```bash
python main.py
```

## Current Features

- Scrolling background for motion feel
- Enemy spawn with variable horizontal speed
- Bonus spawn with variable falling speed
- Real-time score rendering
- Collision-based game over state
- Button-based restart/exit menu

## Possible Improvements

- Add sound effects and background music
- Add difficulty scaling over time
- Add pause menu and settings
- Add high score persistence to file
- Add start screen and instructions overlay

## Author

GitHub: https://github.com/Smurf228
