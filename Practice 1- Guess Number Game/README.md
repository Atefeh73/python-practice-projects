# 🎯 Guess the Number Game (Python Practice Project)

A beginner-friendly Python console game where the computer randomly selects a number and the player tries to guess it within limited attempts. The game includes difficulty levels, dynamic range selection, and a replay system.

---

## 📌 Features

- 🎲 Random number generation within user-defined range
- 🎚️ Difficulty levels (Easy / Medium / Hard)
- 📏 Dynamic attempt system based on range size
- 🔁 Replay option without restarting the program
- 📊 Best score tracking (persistent during session)
- 🚫 Duplicate guess prevention
- ⚠️ Input error handling

---

## 🧠 Concepts Practiced

This project helped me practice and understand:

- Variables and data types
- Loops (`while`, `for`)
- Conditional statements (`if/elif/else`)
- Sets (to track previous guesses)
- Exception handling (`try/except`)
- Random module usage
- Game loop design
- Basic game logic structure

---

## 🎮 How the Game Works

1. The player selects a minimum and maximum range.
2. The game calculates the range size.
3. The player selects a difficulty level:
   - Easy
   - Medium
   - Hard
4. The program generates a random number within the range.
5. The player tries to guess the number within limited attempts.
6. After each guess, the game gives hints:
   - Too high 📈
   - Too low 📉
7. The game continues until:
   - The number is guessed correctly 🎉
   - Attempts run out ❌
8. The player can choose to replay the game.

---

## 🏆 Difficulty System

Difficulty is based on both **range size** and **attempt limits**:

| Difficulty | Range Size | Attempts |
|------------|-----------|----------|
| Easy       | Small     | More attempts |
| Medium     | Medium    | Balanced |
| Hard       | Large     | Fewer attempts |

---

## 🧾 Example Gameplay

Enter range: 1 - 50
Choose difficulty: medium

Guess a number between 1 to 50
Attempt times: 6
👉 Too low!

Attempt times: 5
👉 Too high!

🎉 Congrats! You won in 3 attempts!
New best score!


---

## 🔁 Replay Feature

After each game, the player can choose:
play again? yes/no


If "yes", the game restarts with new settings.

---

## 🚀 How to Run

Make sure you have Python installed, then run:

```bash
python main.py
