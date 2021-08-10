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
def number_checker(question,low,high):
    # sets the error statement for the if statement to follow
    error = "please enter a whole number between 1 and 10\n"

    # keeps the if statement looping until an appropriate answer is entered
    valid = False
    while not valid:

        # This try statement makes it so the program does not crash if a float is entered rather then an interger as the response
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


# main routine

# Asks the user if they have played before then uses the yes_no function to determine what they said
show_instructions = yes_no("Have you played before ?")

# Shows instructions if no was the answer to the above question
if show_instructions == "no":
    instructions()

starting_balacnce = number_checker("How much would you like to play with ? ", 0, 10)

print("You have asked to play with ${}".format(starting_balacnce))

import random
balance = 5
tokens = ["unicorn","Zebra","Zebra","Zebra","Horse","Horse","Horse","Donkey","Donkey","Donkey",]

starting_balacnce = balance

for i in range(0,1,1):
    chosen = random.choice(tokens)
    if chosen == "unicorn":
        balance += 4
    elif chosen == "Zebra":
        balance -= 1
    elif chosen == "Horse":
        balance -= 1
    elif chosen == "Donkey":
        balance -= 0.5
    else:
        print("Error with token chosing and or generating")
print("You got a {},  Your balance is now {}".format(chosen,balance))
