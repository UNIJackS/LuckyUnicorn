


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




