# Write your code here
import random

users_file = open("rating.txt")

name = input("Enter your name: ")
print("Hello,", name)

rating = 0
for line in users_file:
    user, rate = line.split()
    if user == name:
        rating = rate
        break

while True:
    option = input()

    if option == "!exit":
        print("Bye!")
        break
    if option == "!rating":
        print("Your rating:", rating)
        break

    choices = ["rock", "paper", "scissors"]
    random.shuffle(choices)
    r_comp = choices[0]

    if option == r_comp:
        print("There is a draw ({})".format(option))
        rating += 50
    elif option == "rock":
        if r_comp == "paper":
            print("Sorry, but computer chose {}".format(r_comp))
        else:
            print("Well done. Computer chose {} and failed".format(r_comp))
            rating += 100
    elif option == "paper":
        if r_comp == "rock":
            print("Well done. Computer chose {} and failed".format(r_comp))
            rating += 100
        else:
            print("Sorry, but computer chose {}".format(r_comp))
    elif option == "scissors":
        if r_comp == "paper":
            print("Well done. Computer chose {} and failed".format(r_comp))
            rating += 100
        else:
            print("Sorry, but computer chose {}".format(r_comp))
    else:
        print("Invalid input")

users_file.close()
