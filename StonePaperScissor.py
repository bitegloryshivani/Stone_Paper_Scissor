# Game-Stone paper scissor
# 10 games and then declare the one who won

import random
list = ['st','p','sc']

chance = 10
no_of_chance = 0
opponent_point = 0
your_point = 0

print(" \t \t \t \t Stone,Paper,Scissor Game\n \n")
print("s for Stone \np for Paper \nsc for Scissor \n")


while no_of_chance < chance:
    input1 = input('Snake,Water,Gun:')
    random1 = random.choice(list)

    if input1 == random1:
        print("Game is tie,0 point to each \n ")

    # if user enter p
    elif input1 == "p" and random1 == "st":
        opponent_point = opponent_point + 1
        print(f"Your guess {input1} and opponent's guess is {random1} \n")
        print("Opponent wins 1 point \n")
        print(f"Opponent point is {opponent_point} and your point is {your_point} \n ")

    elif input1 == "sc" and random1 == "p":
        your_point = your_point + 1
        print(f"Your guess {input1} and Opponent's guess is {random1} \n")
        print("You win 1 point \n")
        print(f"Opponent point is {opponent_point} and your point is {your_point} \n")

    # if user enter st
    elif input1 == "st" and random1 == "p":
        opponent_point = opponent_point + 1
        print(f"your guess {input1} and Opponent guess is {random1} \n")
        print("Opponent wins 1 point \n")
        print(f"Opponent is {opponent_point} and your point is {your_point} \n ")

    elif input1 == "st" and random1 == "sc":
        your_point = your_point + 1
        print(f"your guess {input1} and Opponent guess is {random1} \n")
        print("You wins 1 point \n")
        print(f"Opponent is {opponent_point} and your point is {your_point} \n")

    # if user enter sc

    elif input1 == "sc" and random1 == "p":
        your_point = your_point + 1
        print(f"your guess {input1} and Opponent guess is {random1} \n")
        print("You wins 1 point \n")
        print(f"Opponent is {opponent_point} and your point is {your_point} \n")


    elif input1 == "sc" and random1 == "st":
        opponent_point = opponent_point + 1
        print(f"your guess {input1} and Opponent guess is {random1} \n")
        print("Opponent wins 1 point \n")
        print(f"Opponent is {opponent_point} and your point is {your_point} \n ")

    else:
        print("You have wrote wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if opponent_point==your_point:
    print("Tie")

elif opponent_point > your_point:
    print("Opponent wins and you loose")

else:
    print("You win and computer loose")

print(f"Your point is {your_point} and Opponent point is {opponent_point}")