
import random
import sys
from enum import Enum
class RPS(Enum):
  ROCK = 1
  PAPER = 2
  SCISSORS = 3
print ("")
playerchoice = input("Enter...\n1 for Rock\n2 for Paper\n3 for scissors\n")
computerchoice = random.randint(1, 3)
#This code solves the problem of annidating lots of if,else conditionals
if int(playerchoice) < 1 or int(playerchoice) > 3:
 sys.exit("You can only choose 1, 2 or 3") #Ends program till here
elif int(playerchoice) == computerchoice:
    print("Tie!")
elif int(playerchoice) == 2 and computerchoice == 1:
 print("Player wins")
elif int(playerchoice) == 1 and computerchoice == 3:
 print("Player wins")
elif int(playerchoice) == 3 and computerchoice == 2:
 print("Player wins")
else:
 print("Computer wins")
print ("Player choice was " + str(RPS(int(playerchoice))).replace('RPS.', ''))
print ("Computer choice was " + str(RPS(computerchoice)).replace('RPS.', ''))