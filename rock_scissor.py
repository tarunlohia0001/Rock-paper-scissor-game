"""
1.input from the user(rock,paper,scissor)
2.computer will choice randomly
3.result print

cases:
A.Rock
Rock-Rock= tie
Rock-paper= paper Win
Rock-Scissor = Rock Win 

B.Paper
Paper-Rock= Raper wins
Paper-paper= tie
Paper-Scissor = scissor Win 

C.Scissor
Scissor-Rock= Rock wins
Scissor-paper= scissor wins
Scissor-Scissor = tie 
"""
import random
item_list=["Rock","Paper","Scissor"]

user_choice = input("Enter your move = Rock, Paper,scissor=")
comp_choice = random.choice(item_list)

print(f"User choice={user_choice}, Computer choice={comp_choice}")

if user_choice==comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice=="Rock":
    if comp_choice=="Paper":
        print("Paper covers Rock = Computer")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice=="Paper":
    if comp_choice=="Scissor":
        print("Scissor cuts Paper = Computer win") 
    else:
        print("Paper covers rock , You win")

elif user_choice=="Scissor":
    if comp_choice=="Paper":
        print("Scissor cuts paper,You win")
    else:
        print("Rock smashes scissor, Computer")

