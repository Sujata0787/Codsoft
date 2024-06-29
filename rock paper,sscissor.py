
import random

def winner(userchoice, computerchoice):
    if userchoice == computerchoice:
        return "It's a tie!"
    elif (userchoice == 'rock' and computerchoice == 'scissors') or \
         (userchoice == 'scissors' and computerchoice == 'paper') or \
         (userchoice == 'paper' and computerchoice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def game():
    userscore = 0
    computerscore = 0
    
    while True:
        print("Welcome to Rock, Paper, Scissors!")
        userchoice = input("Enter your choice (rock, paper, or scissors): ").lower()
        computerchoice = random.choice(['rock', 'paper', 'scissors'])
        
        print("You chose:", userchoice)
        print("Computer chose:", computerchoice)
        
        result = winner(userchoice, computerchoice)
        print(result)
        
        if result == "You win!":
            userscore += 1
        elif result == "Computer wins!":
            computerscore += 1
        
        print("Score - You:", userscore, "Computer:", computerscore)
        
        playagain = input("Do you want to play again? (yes/no): ").lower()
        if playagain != 'yes':
            print("Thanks for playing!")
            break

game()