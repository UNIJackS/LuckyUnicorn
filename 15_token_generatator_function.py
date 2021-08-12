import random
# sets the balance
balance = 100
# sets the list of tokens and there probability
tokens = ["unicorn","Zebra","Zebra","Zebra","Horse","Horse","Horse","Donkey","Donkey","Donkey",]
chosen = "test"
starting_balacnce = balance
# A loop that loops the if statement 20 times
for i in range(1,100):
    chosen_number = random.randint(1,500)
    # An if statement that checks what the chosen token is then adds or subtracts the appropriate amount from the balance varable
    # checks if the chosen is a unicorn then adds 4 to the balance if it is
    if 1 <= chosen_number <= 5:
        chosen = "unicorn"
        balance += 4
    # checks if the chosen is a horse or zebra then subtracts 0.5 from the balance if it is
    elif 6 <= chosen_number <= 36:
        chosen = "Horse"
        balance -= 0.5

    elif 36 <= chosen_number <= 66:
        chosen = "Zebra"
        balance -= 0.5
    # checks if the chosen is a unicorn then subtracts 1 from the balance if it is
    elif 66 <= chosen_number <= 100:
        chosen = "Donkey"
        balance -= 1
    # prints an error to the user if one of the previous options was not selected
    else:
        print("Error with token chosing and or generating")
    # prints the token, starting balance and balance
    print("You got a {}, Your balance was {:.2f} now its {:.2f}".format(chosen,starting_balacnce,balance))
