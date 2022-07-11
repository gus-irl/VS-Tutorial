from logging import PercentStyle
import random


def say_hello(name):
    print("Hello " + name)

def coin_flip():
    return random.choice(["Heads", "Tails"])

def is10(num):
    if (num == 10):
        print("This number is 10!")
    elif (num > 10):
        print("This number is greater than 10")
    elif (num < 10):
        print("This number is less than 10")


def count(num):
    tails_count = 0
    heads_count = 0
    print("\n\n\n\n\n\n")
    for x in range(num):
        result = coin_flip()
        if (result == "Tails"):
            tails_count += 1
        else:
            heads_count += 1
        print("Flipped " + result + "...")
    print("Done! \n\nResults:")
    print("Heads Count: " + str(heads_count) + " (" + str(heads_count / 10 * 100) + "%)")
    print("Tails Count: " + str(tails_count) + " (" + str(tails_count / 10 * 100) + "%)")
    if (tails_count == heads_count):
        print("You flipped Tails & Heads an even amount of times!")
    elif (tails_count > heads_count):
        print("You flipped Tails more than Heads!")
    else:
        print("You flipped Heads more than Tails!")
        
        