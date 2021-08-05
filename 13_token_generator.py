import random
balance = 0
tokens = ["unicorn","Zebra","Horse","Donkey"]
for i in range(0,20,1):
    chosen =  random.choice(tokens)
    if chosen == "unicorn":
        balance += 4
    elif chosen == "Zebra":
        balance += 1
    elif chosen == "Horse":
        balance += 1
    elif chosen == "Donkey":
        balance += 0
    else:
        print("Error with token chosing and or generating")
print("You got a {}, Your balance is now {}".format(chosen,balance))


