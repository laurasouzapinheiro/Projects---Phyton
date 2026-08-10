import sys # imports the sys module, which provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. In this case, it is used to exit the program if the player's choice is invalid.
import random # imports the random module, which implements pseudo-random number generators for various distributions. In this case, it is used to generate a random choice for the computer.   
from enum import Enum # imports the Enum class from the enum module, which is used to create enumerations, which are a set of symbolic names (members) bound to unique, constant values. In this case, it is used to create an enumeration for the choices in the game.

class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")
playerchoice = input('Please enter your choice... \n1 for Rock 🪨 \n2 for Paper 📄 \n3 for Scissors ✂️:\n\n ')

player = Choice(int(playerchoice))

choices = {
    Choice.ROCK: "Rock 🪨",
    Choice.PAPER: "Paper 📄",
    Choice.SCISSORS: "Scissors ✂️"
}

if player not in Choice:
    sys.exit("Invalid choice. Please enter 1, 2 or 3.") # exits the program if the player's choice is not between 1 and 3

computerchoice = random.randint(1, 3) # chooses a random number between 1 and 3 for the computer's choice   
# random.choice("123") could also be used here to select from a list of choices, but randint() is used in this case to generate a random integer.
# computer = int(computerchoice), would needed if random.choice() was used instead of random.randint() to convert the string to an integer.

print(f"\nYou chose: {player} ({choices[player]})") # prints the player's choice
print(f"Python chose: {computerchoice} ({choices[computerchoice]})") # prints the computer's choice
if player == computerchoice: # checks if the player's choice is the same as the computer's choice
    print("It's a tie! 🤝") # prints "It's a tie!" if the player's choice is the same as the computer's choice
elif (player == Choice.ROCK and computerchoice == Choice.SCISSORS) or (player == Choice.PAPER and computerchoice == Choice.ROCK) or (player == Choice.SCISSORS and computerchoice == Choice.PAPER): # checks if the player wins
    print("You win! 🎉") # prints "You win!" if the player wins    
else: # if the player does not win and it is not a tie, then the computer wins
    print("Python wins! 🐍") # prints "Python wins!" if the computer wins
