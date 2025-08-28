import random
print ("")
playerchoice = input("Enter...\n1 for Rock\n2 for Paper\n3 for scissors\n")
computerchoice = random.randint(1, 3)
#This code anidates a lot of if,else; things that will be solved using operator elif like shown on "pptcorrected.py"
if int(playerchoice) == computerchoice:
    print("Tie!")
else:
    if int(playerchoice) == 1 and computerchoice == 2:
        print("Computer wins")
    else:
        if int(playerchoice) == 2 and computerchoice == 1:
            print("Player wins")
        else:
            if int(playerchoice) == 3 and computerchoice == 1:
                print("Computer wins")
            else:
                if int(playerchoice) == 1 and computerchoice == 3:
                    print("Player wins")
                else:
                    if int(playerchoice) == 3 and computerchoice == 2:
                        print("Player wins")
                    else:
                        if int(playerchoice) == 2 and computerchoice == 3:
                            print("Computer wins")
                        else:
                            print("No funny funny")

print("Computer choice was " + str(computerchoice))