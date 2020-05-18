# Write your code here
import random


while True:
    option = input()

    if option == "!exit":
        print("Bye!")
        break

    choices = ["rock", "paper", "scissors"]
    random.shuffle(choices)
    r_comp = choices[0]

    if option == r_comp:
        print("There is a draw ({})".format(option))
    elif option == "rock":
        if r_comp == "paper":
            print("Sorry, but computer chose {}".format(r_comp))
        else:
            print("Well done. Computer chose {} and failed".format(r_comp))
    elif option == "paper":
        if r_comp == "rock":
            print("Well done. Computer chose {} and failed".format(r_comp))
        else:
            print("Sorry, but computer chose {}".format(r_comp))
    elif option == "scissors":
        if r_comp == "paper":
            print("Well done. Computer chose {} and failed".format(r_comp))
        else:
            print("Sorry, but computer chose {}".format(r_comp))
    else:
        print("Invalid input")
