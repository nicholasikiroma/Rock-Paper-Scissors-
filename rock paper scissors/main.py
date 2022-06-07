#Instructions:

#Create a new Python file and call it main.py. Inside it you'll create your game.

#Create a list to store all possible options:

#"R" for "rock", 

#"P" for "paper", 

#"S" for "scissors".

#When the program is run, ask the user to pick an option between "R", "P" or "S"

#If player input is invalid (not amongst our options), print an error, and ask for their input again (should be a loop)

#Use the `choice` function from the inbuilt Python `random` module to make a choice for CPU player(computer).

#Print both player's moves in the format: `Player (Rock) : CPU (Paper)`

#Check both player's moves: 

#If there is a winner, print the winner, and the program ends. 

#If it's a tie (the computer and player pick the same move), restart the game from step 3

import random


options = ["R", "P", "S"]


print('''Welcome to Rock Paper Scissors!

The following terms will be adopted:

"R" stands for "Rock"

"P" stands for "Paper"

"S" stands for "Scissors"

''')

player_name = input('What is your name? ')

print(f'''Hi {player_name}, Here are the rules of the game:

Rock wins Scissors

Paper wins Rock

Scissors wins Paper

    ''')

#main game loop
while True: 

    cpu_option = random.choice(options)

    #loop for for wrong player option
    while True:

        player_option = input("What option do you choose? ")

        

        if player_option.upper()=="P" or player_option.upper()=="R" or player_option.upper() =="S":
            break
            
        else:
            print("Oosps! you have entered the wrong option. Please try again.")
        continue

    
# Conditions for declaring winners

    if player_option.upper() == cpu_option:

        print(f"Player ({player_option.upper()}) : Computer ({cpu_option})")
       
        print("It's a tie")
       
        continue

    elif (cpu_option=="R" and player_option.upper()=="S") or (cpu_option=="S" and player_option.upper()=="P") or (cpu_option=="P" and player_option.upper()=="R"):
        print(f"Player ({player_option.upper()}) : Computer ({cpu_option})")
        print("Computer Wins!")    

    else:
        (player_option.upper()=="R" and cpu_option=="S") or (player_option.upper()=="S" and cpu_option=="P") or (player_option.upper()=="P" and cpu_option=="R")
        print(f"Player ({player_option.upper()}) : Computer ({cpu_option})")
        print(f"{player_name} Wins!")

        break

    break

print("Thank you for playing!")

            


