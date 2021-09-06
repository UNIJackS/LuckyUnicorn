import random


# functions bellow
# yes or no function
def yes_no(question):
    valid = False
    while not valid:
        # coverts the question of yes or no into the variable of response
        response = input(question).lower().strip()

        # An if statement that checks if they said yes or y and if so it returns with a yes no matter the input
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # An elif statement that checks if they said no or n and if so it returns with a no no matter the input
        elif response == "no" or response == "n":
            response = "no"
            return response

        # An else statement that asks them to please enter yes or no
        else:
            print("Please enter yes or No")


# function that prints the instructions when called
def instructions():
    print()
    print("******instructions******")
    print()
    print("An initial amount of money is required this amount should be within $1-10 eg 5,8 and be")
    print("be a whole number no floats/decimals eg 5.6 or 8.4.")
    print("A random token of either a unicorn, zebra, horse or donkey. These tokens are worth")
    print("$5,$1, $1 and $0 respectively.")
    print()
    return ""


# function that checks numbers are within a range
def number_checker(question, low, high):
    # sets the error statement for the if statement to follow
    error = "please enter a whole number between 1 and 10\n"

    # keeps the if statement looping until an appropriate answer is entered
    valid = False
    while not valid:

        # This try statement makes it so the program does not crash if a float is entered rather then...
        # -an integer as the response
        try:
            response = int(input(question))

            # An if statement that checks if the response to the previous statement is between 0 and 10
            if low < response <= high:
                return response

            # An if statement that outputs the error statement if the response is not between 0 and 10
            else:
                print(error)
        except ValueError:
            print(error)


# Token generator function
def token_generator():
    chosen_number = random.randint(1, 100)
    # An if statement that checks if the chosen number is between a range then adds or subtracts the appropriate...
    # -amount from the balance variable
    # checks if the chosen is between 1 and 5 then adds 4 to the balance if it is
    if 1 <= chosen_number <= 5:
        token_chosen = "unicorn"
        response = 4
        token_deco_type = "!"
        return [response, token_chosen, token_deco_type]
        # checks if the chosen is between 6 and 36 then minuses 0.5 to the balance if it is
    elif 6 <= chosen_number <= 36:
        token_chosen = "Horse"
        response = 0.5
        token_deco_type = "H"
        return [response, token_chosen, token_deco_type]
        # checks if the chosen is between 36 and 66 then minuses 0.5 to the balance if it is
    elif 36 <= chosen_number <= 66:
        token_chosen = "Zebra"
        response = -0.5
        token_deco_type = "Z"
        return [response, token_chosen, token_deco_type]
        # checks if the chosen is between 66 and 100 then minuses 1 to the balance if it is
    elif 66 <= chosen_number <= 100:
        token_chosen = "Donkey"
        response = -1
        token_deco_type = "D"
        return [response, token_chosen, token_deco_type]
        # prints an error to the user if one of the previous options were not selected
    else:
        return "Error with token choosing and or generating"
        # prints the token, starting balance and balance


def decoration(deco, text, deco_type):
    print(deco_type * deco * 2 + deco_type * len(text))
    print(deco_type * deco + text + deco_type * deco)
    print(deco_type * deco * 2 + deco_type * len(text))
    print()


# main routine

# Asks the user if they have played before then uses the yes_no function to determine what they said
show_instructions = yes_no("Have you played before ?")

# Shows instructions if no was the answer to the above question
if show_instructions == "no":
    instructions()

balance = number_checker("How much would you like to play with ? ", 0, 10)

rounds_played = 0

still_play = "yes"
# Loops the gambling until the user says to stop or they run out of money
while still_play == "yes":
    while balance >= 1 and still_play == "yes":
        rounds_played += 1
        tokens = token_generator()
        decoration(4, " Round {} ".format(rounds_played), "#")
        balance += tokens[0]
        decoration(4, " You got a {},Your balance is now ${:.2f} ".format(tokens[1], balance), tokens[2])
        still_play = yes_no("Would you like to play again ? ")
    # checks if they still have more than $1 so they can keep gamble
    if balance <= 1 and still_play == "yes":
        print("sorry your out of money")
        still_play = "no"
# prints the amount left after they have finished gambling if they haven't run out of money
if balance > 1:
    print()
    print("You are left with ${}".format(balance))
