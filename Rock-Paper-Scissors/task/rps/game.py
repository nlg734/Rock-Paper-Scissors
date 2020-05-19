# Write your code here
import random


def will_win(choice, comp, options):
    if choice not in options:
        return -1
    i = options.index(choice)
    if i == 0:
        reordered = options[1:]
    else:
        reordered = options[i+1:]
        for op in options[:i]:
            reordered.append(op)
    j = reordered.index(comp)
    if j >= len(reordered) / 2:
        return True
    return False


users_file = open("rating.txt")

name = input("Enter your name: ")
print("Hello,", name)

rating = 0
for line in users_file:
    user, rate = line.split()
    if user == name:
        rating = int(rate)
        break

choices = input().split(",")
if len(choices) == 1:
    choices = ["rock", "paper", "scissors"]
shuffled = []
for item in choices:
    shuffled.append(item)

print("Okay, let's start")

while True:
    option = input()

    if option == "!exit":
        print("Bye!")
        break
    if option == "!rating":
        print("Your rating:", rating)
        continue
    random.shuffle(shuffled)
    r_comp = shuffled[0]

    if option == r_comp:
        print("There is a draw ({})".format(option))
        rating += 50
    else:
        win = will_win(option, r_comp, choices)
        if win == -1:
            print("Invalid input")
        elif win:
            print("Well done. Computer chose {} and failed".format(r_comp))
            rating += 100
        else:
            print("Sorry, but computer chose {}".format(r_comp))

users_file.close()
