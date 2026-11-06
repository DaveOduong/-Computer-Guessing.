# Number Guessing Game (Python)

## Description
A Python number guessing game featuring two modes: **Player Guessing** and **Computer Guessing**.

In the first mode, the computer generates a random number, and the player attempts to guess it. In the second mode, the computer tries to guess a number chosen by the player using feedback.

## Features

- **Player Guessing:** The computer randomly selects a number, and the player keeps guessing until correct.
- **Computer Guessing:** The computer generates guesses within a specified range based on the player's feedback.
- Provides feedback when a guess is too high or too low.
- Uses random number generation to make guesses.
- Continues until the correct number is found.

## How It Works

### 1. Player Guessing – `guess(x)`
- Generates a random number between 1 and the specified maximum.
- Requests the player's guess.
- Displays "Too low" or "Too High" depending on the input.
- Repeats until the player guesses correctly.

### 2. Computer Guessing – `computer_guess(x)`
- Starts with a minimum value of 1 and a maximum value of `x`.
- The computer randomly selects a number within the current range.
- The player provides feedback:
  - `L` – The computer's guess is lower than the chosen number.
  - `H` – The computer's guess is higher than the chosen number.
  - `C` – The computer guessed correctly.
- Adjusts the guessing range based on the feedback.
- Continues until the player confirms the correct guess.

## Technologies Used
- Python
- Random Module
- Functions
- While Loops
- If-Else Statements
- User Input

## How to Run
1. Install Python.
2. Save the code as `guessing_game.py`.
3. Open a terminal in the project folder.
4. Run:

```bash
python guessing_game.py
```

## Learning Objectives
This project demonstrates functions, random number generation, loops, conditional statements, user input, and basic search-range adjustment.

## Note
To run the player guessing mode, replace the last line with:

```python
guess(10)
```

To run the computer guessing mode:

```python
computer_guess(10)
```
