import random
def getcomputerchoice():
    return random.choice(["rock","paper","scissors"])

def determinewinner(userchoice,computerchoice):
    if userchoice==computerchoice:
        return "tie"
    elif ((userchoice=="rock" and computerchoice=="scissors")or(userchoice=="scissors" and computerchoice=="paper") or 
         (userchoice=="paper" and computerchoice=="rock")):
        return "user"
    else:
        return "computer"

def playgame():
    userscore=0
    computerscore=0
    print("Welcome to Rock,Paper,Scissors!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.\n")

    while True:
        userchoice=input("Choose 'rock','paper',or'scissors': ").lower().strip()
        if userchoice not in ["rock","paper","scissors"]:
            print("Invalid choice!Please choose again.")
            continue

        computerchoice=getcomputerchoice()
        print(f"\nYou chose:{userchoice}")
        print(f"Computer chose:{computerchoice}")

        winner=determinewinner(userchoice,computerchoice)

        if winner=="tie":
            print("It's a tie!")
        elif winner=="user":
            print("You win")
            userscore+=1
        else:
            print("Computer wins")
            computerscore+=1

        print(f"\nScore: You {userscore}-{computerscore} Computer")

        playagain=input("\nDo you want to play another round? (yes/no): ").lower().strip()
        if playagain!="yes":
            print("\nThanks for playing Rock,Paper,Scissors!")
            print(f"Final Score: You {userscore}-{computerscore} Computer")
            break
playgame()
