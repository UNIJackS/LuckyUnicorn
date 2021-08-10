import random
balance = 15
tokens = ["unicorn","Zebra","Zebra","Zebra","Horse","Horse","Horse","Donkey","Donkey","Donkey",]

starting_balacnce = balance

for i in range(0,20,1):
    chosen = random.choice(tokens)
    if chosen == "unicorn":
        balance += 4
    elif chosen == "Zebra":
        balance -= 0.5
    elif chosen == "Horse":
        balance -= 0.5
    elif chosen == "Donkey":
        balance -= 1
    else:
        print("Error with token chosing and or generating")
    print("You got a {},  Your balance was {:.2f} now its {:.2f}".format(chosen,starting_balacnce,balance))
