import random
import os
def ConsoleClear():
    os.system('cls' if os.name == 'nt' else 'clear')
ConsoleClear()


# Title Statement
print("Welcome to Rock Paper Scissors")

playGame = int(input("1. Play\n2. Exit\n"))
ConsoleClear()
while playGame != 2:

    # Get user choice and computer choice
    userChoice =  int(input("1. Rock\n2. Paper\n3. Scissors\n"))
    compChoice = random.randint(1, 3)

    rock = """
        ______
    ----'   ___)
        (_____)
        (_____)
        (____)
    ----.__(___)
    """

    paper = """
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """

    scissors = """
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """
    userImage = "Fail"
    compImage = "Fail"
    # Set Image
    if userChoice == 1:
        userImage = rock
    elif userChoice == 2:
        userImage = paper
    elif userChoice == 3:
        userImage = scissors


    if compChoice == 1:
        compImage = rock
    elif compChoice == 2:
        compImage = paper
    elif compChoice == 3:
        compImage = scissors

    # If-Else to decide outcomes
    ConsoleClear()
    print(f"You Chose\n{userImage}")
    print(f"Computer Chose\n{compImage}")

    if userChoice == compChoice:
        print("You tied")
    elif (userChoice == 1 and compChoice == 2) or (userChoice == 2 and compChoice == 3) or (userChoice == 3 and compChoice == 1):
        print("You Lose")
    else:
        print("You Win!")

    playGame = int(input("\n1. Play Again\n2. Exit\n"))
    ConsoleClear()