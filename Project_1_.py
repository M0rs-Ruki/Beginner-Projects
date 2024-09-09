# rock paper scissors game in python project

import random

while True:
    ran = ["rock","paper","scissors"]
    com_random = random.choice(ran)
    user_input = input("Enter you ch (rock,paper,scissors): ").lower()
    
    while user_input not in ran:
         user_input = input("Enter you ch (rock,paper,scissors): ").lower()
    
    print(f"computer ch {com_random}")
    print(f"user input is {user_input}")
    
    
    if user_input == com_random:
        print("T")
    elif user_input == "rock" and com_random == "paper":
        print("you lose")
    elif user_input == "scissors" and com_random == "paper":
        print("you win")
    elif user_input == "rock" and com_random == "paper" :
        print("you lose")
    elif user_input == "rock" and com_random == "scissors" :
        print("you win")
    elif user_input == "scissors" and com_random == "rock" :
        print("you lose")
    elif user_input == "paper" and com_random == "rock" :
        print("you win")
    elif user_input == "paper" and com_random == "scissors" :
        print("you win")
    else:
        print("Try agin, i don't knowe")
    exit_game = input("enter 'q' for exit ")
    if exit_game.lower() == "q":
        break