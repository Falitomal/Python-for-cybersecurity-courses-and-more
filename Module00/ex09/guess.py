# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jledesma <jledesma@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/14 07:10:49 by jledesma          #+#    #+#              #
#    Updated: 2023/04/15 19:25:19 by jledesma         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import random

def guess():
    """Guess a number between 1 and 99"""
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Good luck!")
    print("Type exit to quit.")
    number = random.randint(1, 99)
    tries = 0
    while True:
        print("What's your guess between 1 and 99?")
        guess = input()
        if guess == 'exit':
            print('Goodbye')
            exit()
        try:
            guess = int(guess)
        except ValueError:
            print("Not is integer")
            continue
        guess = int(guess)
        if (int(guess) == 42 and guess == number and tries == 0):
            print("The answer to the ultimate question of life, the universe and everything is 42.")
            print("Congratulations! You got it on your first try!")
            break
        elif (int(guess) == number and tries == 0):
            print("Congratulations! You got it on your first try!")
            break
        elif (int(guess) == 42 and guess == number):
            print("The answer to the ultimate question of life, the universe and everything is 42.")
            print("You won in", tries, "attempts!")
            break
        elif int(guess) < 1:
            print("The number is out of range")
        elif int(guess) > 99:
            print("The number is out of range")
        elif int(guess) < number:
            print("Too low!")
            tries += 1
        elif int(guess) > number:
            print("Too high!")
            tries += 1
        elif int(guess) == number:
            tries += 1
            print("Congratulations, you've got it!")
            print("You won in", tries, "attempts!")
            break

guess()