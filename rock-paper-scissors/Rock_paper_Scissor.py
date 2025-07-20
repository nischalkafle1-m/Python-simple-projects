''' 🪨📄✂️ Rock Paper Scissors Game  
**My first Python project** '''

import random

def play_game():
    dict={1:"Rock", 2:"Paper",3:"Scissor"}
    while True: #Repeat if the Game is tie
           
        computer= random.randint(1,3)
        
        print("Welcome to Rock, Paper, Scissor Game!")
        user=input("Choose r for Rock, p for Paper, s for Scissor: ").lower()
        
        if user not in ["r", "p", "s"]:
            print("Invalid input! Please choose r, p, or s.")
            return  # Stop the game if input is invalid
        
        
        n={"r":1, "p":2, "s":3}
        revdict={1:"Rock", 2:"Paper", 3:"Scissor"}
        if user in n:
            user_choice=n[user]
            computer_choice=computer
            print(f"Computer chose: {revdict[computer_choice]}")
            print(f"You chose: {revdict[user_choice]}")
            if user_choice == computer_choice:
                print("It's a tie!")
                
            elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
                print("You win!") #End the game after one round
                break
            else:
                print("You lose!")
                break # End the game after one round
            
play_game()