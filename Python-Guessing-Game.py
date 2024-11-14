import random

number = random.randint(0,10)
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