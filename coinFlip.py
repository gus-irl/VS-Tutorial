import random
import string
import time

def is10(num):
    if (num == 10):
        print("This number is 10!")
    elif (num > 10):
        print("This number is greater than 10")
    elif (num < 10):
        print("This number is less than 10")

def coin_flip():
    return random.choice(["Heads", "Tails"])

def multi_flip(num): # Flips a coin num times and returns the results
    # Data Declaration
    tails_count = 0
    heads_count = 0

    print("\n\n\n\n\n\n")

    for x in range(num):
        result = coin_flip() # Stores the result of the flip into a variable for later use
        if (result == "Tails"):
            tails_count += 1
        else:
            heads_count += 1
        print("Flipped " + result + "...")
    print("Done! \n\nResults:")
    print("Heads Count: " + str(heads_count) + " (" + str(heads_count / num * 100) + "%)")
    print("Tails Count: " + str(tails_count) + " (" + str(tails_count / num * 100) + "%)")
    if (tails_count == heads_count):
        print("You flipped Tails & Heads an even amount of times!")
    elif (tails_count > heads_count):
        print("You flipped Tails more than Heads!")
    else:
        print("You flipped Heads more than Tails!")



def predict():
    guesses = 0
    while True:
        prediction = input("Do you think the coin will flip heads or tails").lower()
        result = coin_flip().lower()
        if (prediction == result):
            print("You were right! The coin flipped " + result)
            guesses += 1
        else:
            print("You were wrong!! The coin flipped " + result)
            break
    print("You guessed right " + str(guesses) + " times!")


def coin_game():
    points = 10
    rounds = 0
    while(points > 0):
        rounds += 1
        print("** ROUND " + str(rounds) + " **")
        bet_amount = int(input("How many points do you want to bet?\nAnswer 0 to end the game.\n"))
        answer = input("Do you think it will be Heads or Tails?\n").lower()
        result = coin_flip().lower()
        print("\n" * 100)
        if (answer == result):
            print("You guessed right!")
            points += bet_amount
            print("Your Points: " + str(points) + " (+" + str(bet_amount) + ")")
        else:
            print("Oh no! You guessed wrong!")
            points -= bet_amount
            print("Your points: " + str(points) + " (-" + str(bet_amount) + ")")
        print("\n--------------------\n")
    time.sleep(1)
    # print("You've finished the game with", end="")
    # animate(1, [".",".",".\n"])
    print("You've finished the game with...")
    time.sleep(.5)
    print(str(points) + " Points", end="")
    time.sleep(1)
    print(" in")
    time.sleep(.5)
    print(str(rounds) + " Rounds!")


# def animate(delay, words):
#     for x in range(len(words)):
#         print(words[x], end="")
#         time.sleep(delay)