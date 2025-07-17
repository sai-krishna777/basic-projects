import random 

options = ["rock","paper","scissors"]
print("let's play rock-paper-scissors")
print("type rock, paper and scissors to play. exit to leave")

while True :
    user = input("enter your choice : ").lower()

    if user == "exit":
       print("thanks for playing!")
       break
    if user not in options:
       print("invalid input, try again")
       continue
    computer = random.choice(options)
    print(f"computer chooses:{computer}")

    if user == computer: 
       print("it's a tie")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer =="paper"):
         print("you win")
    else:
        print("computer wins")