# Guess The Number Game 🎲
Welcome to Guess The Number, a simple and fun Python game where you try to guess a randomly selected number between 0 and 10! You have three chances to guess correctly, and the game will give you feedback after each attempt.

## 🎮 How to Play

1. **Run the game** by executing the `Python-guessing-game.py` script in your terminal.
2. **Make your first guess** when prompted. The game will check if it matches the randomly chosen number.
3. **If you guess incorrectly**, you'll be told how many tries you have left. 
4. **Three wrong guesses?** The game will end and reveal the correct number.

## 🔧 Installation

Make sure you have Python installed. To play, simply download or clone this repository, then run the script in your terminal:

```bash
python Python-guessing-game.py
```
## 📝 Code Highlights

Here's a peek at the core logic:

```python
import random

number = random.randint(0, 10)
player_guess = input('Write your first guess here (number from 0 to 10):')
while player_guess.isdigit() == False:
    print("No digits were given. Try again.")
    player_guess = input('Write your first guess here (number from 0 to 10):')

if number == int(player_guess):
    print('Congratulations! You won.')
else:
    print("Oh no, you got it wrong! Don't worry, you can try 2 more times.")
    player_second_guess = input('Write your second guess here:')
    while player_second_guess.isdigit() == False:
        print("No digits were given. Try again.")
        player_second_guess = input('Write your second guess here:')
    if number == int(player_second_guess):
        print('Congratulations! You won!')
    else:
        print("Oh no, you got it wrong! Don't worry, you can try one last time.")
        player_third_guess = input('Write your third and last guess here:')
        while player_third_guess.isdigit() == False:
            print("No digits were given. Try again.")
            player_third_guess = input('Write your third and last guess here:')
        if number == int(player_third_guess):
            print('Congratulations! You won!')
        else:
            print('Sorry, you lost and the game is over!')
            print(f'The number was {number}...')
```
## 📬 Contact
Feel free to reach out if you have questions or ideas to improve the game! You can find me on [LinkedIn](https://www.linkedin.com/in/vanessacunharamos/) or email me at vanessacrramos@gmail.com.
