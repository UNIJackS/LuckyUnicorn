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

balance = 5

rounds_played = 0

still_play = "yes"
while still_play == "yes":
    while balance >= 1 and still_play == "yes":
        rounds_played += 1
        print("Round {}".format(rounds_played))
        balance -= 1
        print("you have ${} left".format(balance))
        still_play = yes_no("Would you like to play again ? ")
    if balance <= 1 and still_play == "yes":
        print("sorry your out of money")
        still_play = "no"
print("You are left with ${}".format(balance))

