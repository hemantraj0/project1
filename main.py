import random

# Snake-Water-Gun Game
print("Welcome to the Snake, Water, Gun game!")
print("Choose 's' for Snake, 'w' for Water, or 'g' for Gun.")

# Computer's random choice
computer = random.choice([1, 0, -1])

# Dictionaries for mapping
youDict = {"s": 1, "w": 0, "g": -1}
reverseDict = {1: "Snake", 0: "Water", -1: "Gun"}

# User input validation
youStr = input("Enter your choice (s/w/g): ").lower()

if youStr not in youDict:
    print("Invalid input! Please choose 's' for Snake, 'w' for Water, or 'g' for Gun.")
else:
    you = youDict[youStr]
    print(f"Computer choice: {reverseDict[computer]}")
    print(f"Your choice: {reverseDict[you]}")

    # Determine the winner
    if you == computer:
        print("It's a Draw!")
    else:
        if computer == 1 and you == 0:
            print("You lose the game 😓")
        elif computer == 1 and you == -1:
            print("You win the game! 😍")
        elif computer == 0 and you == 1:
            print("You win the game! 😍")
        elif computer == 0 and you == -1:
            print("You lose the game 😓")
        elif computer == -1 and you == 1:
            print("You lose the game 😓")
        elif computer == -1 and you == 0:
            print("You win the game! 😍")
