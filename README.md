# Snake-game
A classic Snake game implementation using Python's turtle graphics library.

# 🐍 Snake Game (Python Turtle Graphics)

This is a fully functional **Snake Game** where the player controls a snake to eat food and grow longer while avoiding collisions with walls and the snake's own tail. The game features a scoring system with **persistent high score tracking**.

---

## ✨ Features
- 🎮 Classic Snake gameplay with arrow key controls  
- 🍎 Food collection system that grows the snake  
- 🧱 Collision detection for walls and snake tail  
- 🏆 Score tracking with current and high score display  
- 💾 Persistent high score storage between game sessions  

---

## ⚙️ Installation

### 📋 Prerequisites
- Python 3.x  
- No additional packages required (uses built-in `turtle` graphics)


 ### 🎮 How to Play

Use the arrow keys to control the snake:

⬆️ Up Arrow → Move up

⬇️ Down Arrow → Move down

⬅️ Left Arrow → Move left

➡️ Right Arrow → Move right

Eat the red food to grow your snake and increase your score. Avoid hitting the walls or your own tail!

### 📂 File Structure

snake-game/
├── main.py          # Main game loop and event handling
├── snake.py         # Snake class with movement logic
├── food.py          # Food class for random food generation
├── scoreboard.py    # Score tracking and display
├── data.txt         # High score storage
└── README.md        # Project documentation

### 🧩 Game Components

#### 🐍 Snake (snake.py)

Handles snake creation and initialization

Manages movement in four directions

Controls snake growth when food is consumed

Prevents invalid direction changes (e.g., up → down directly)

#### 🍎 Food (food.py)

Creates food pellets at random screen locations

Refreshes food position after consumption

Uses turtle graphics for visual representation

#### 🏆 Scoreboard (scoreboard.py)

Tracks current game score

Loads and saves high score to file

Displays score information on screen

Handles score reset functionality

#### 🎮 Main Game (main.py)

Coordinates all game components

Handles collision detection

Manages game loop and timing

Processes keyboard input

### 🚧 Future Enhancements

Multiple difficulty levels

Sound effects

Different food types with bonus points

Pause/resume functionality

Game menu system

Custom themes and colors

