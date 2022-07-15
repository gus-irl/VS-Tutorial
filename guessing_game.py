import random

def guessing_game():
    print("\n" * 100 + "** Setup **")
    lower_range = int(input("What is the lowest number you want to guess?\n"))
    highest_range = int(input("What is the highest number you want to guess?\n"))

    random_number = random.randint(lower_range, highest_range)
    guess = 0
    guesses = 0

    print("\n" * 100)
    while(random_number != guess):
        print("I'm guessing of a number between " + str(lower_range) + " and " + str(highest_range) + "...")
        guess = int(input("\nWhat is your guess?\n"))
        print("\n" * 100)
        if (guess > random_number):
            print("Too High!")
            guesses += 1
        elif (guess < random_number):
            print("Too Low!")
            guesses += 1
        else:
            print(str(random_number) + "!\nYou guessed my number in " + str(guesses) + " attempts!\n")
            break

        print("\nYour last guess: " + str(guess))

    again = input("Would you like to play again? (Y/n)").lower()
    if (again == 'y'):
        guessing_game()
    
guessing_game() # Run the game immedietely when pressing run python file (play button)