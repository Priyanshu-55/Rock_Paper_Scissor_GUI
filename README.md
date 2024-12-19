# Rock Paper Scissors Game

This project is a simple graphical implementation of the classic "Rock, Paper, Scissors" game using Python's `tkinter` library. The game allows the user to play against a bot in a fun and visually appealing interface.

## Features

- **Graphical User Interface (GUI):** Built with `tkinter`, the game provides an interactive and colorful interface.
- **User vs Bot Gameplay:** The user selects their choice (Rock, Paper, or Scissors), and the bot makes a random choice.
- **Win Counter:** Keeps track of the number of wins for both the user and the bot.
- **Result Display:** Shows the winner of each round or if it’s a tie.
- **Reset Functionality:** The "Refresh" button resets the score counters to zero.

## How to Run the Project

1. **Prerequisites:**
   - Ensure you have Python installed on your system (Python 3.x is recommended).

2. **Run the Script:**
   - Save the code in a file named `rock_paper_scissors.py`.
   - Open a terminal or command prompt, navigate to the directory containing the script, and execute:
     ```bash
     python rock_paper_scissors.py
     ```

3. **Play the Game:**
   - Use the buttons labeled "ROCK," "PAPER," and "SCISSOR" to make your choice.
   - Observe the bot’s choice and the result displayed on the screen.
   - Check the win counters for both the user and the bot.
   - Use the "Refresh" button to reset the scores.

## Code Overview

### Main Components

1. **Labels:**
   - Display user and bot names, results, and scores.
   - Labels are used to create the visual elements of the game.

2. **Buttons:**
   - Buttons allow the user to select their move (Rock, Paper, or Scissors) and reset the game.

3. **Functions:**
   - `userchs(usrtext)`: Updates the user's choice display.
   - `botchs(bottext)`: Updates the bot's choice display.
   - `refresh_win_conter()`: Updates the score labels.
   - `new_counter()`: Resets the win counters to zero.
   - `resultlabel(reslt)`: Displays the result of the round.
   - `rndbot(user)`: Handles bot's choice, determines the result, and updates scores.
   - Button-specific functions (`rckkbtn`, `paprbtn`, `sesrbtn`) trigger gameplay for each choice.

4. **Game Logic:**
   - The bot's choice is randomly selected from a predefined list.
   - The winner is determined based on standard Rock-Paper-Scissors rules.

### GUI Layout

- The game window is set to a fixed size of 800x600 pixels.
- Colors and fonts are chosen to create a vibrant and playful design.
- Elements are placed using the `.place()` method for precise positioning.

## Customization

- **Appearance:**
  - Modify colors, fonts, or sizes to change the look and feel of the game.
- **Rules:**
  - Add more options (e.g., "Lizard" and "Spock") to expand the game.
- **Functionality:**
  - Implement a best-of-three or timed mode for extended gameplay.

## Example Gameplay

1. User clicks "ROCK."
2. The bot randomly selects "SCISSOR."
3. Result displayed: "User Wins."
4. Scores update accordingly.

