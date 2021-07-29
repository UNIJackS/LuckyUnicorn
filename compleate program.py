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

# function that prints the instructions
def instructions():
    print("******instructions******")
    print()
    print("Rules of the game")
    print()
    return ""

# main routine

# Asks the user if they have played before then uses the yes_no function to determine what they said
show_instructions = yes_no("Have you played before ?")
# Shows instructions if no was the answer to the above question
if show_instructions == "no":
    instructions()

print("program continues")