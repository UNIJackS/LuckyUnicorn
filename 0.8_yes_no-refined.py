# loops the code till yes or no is entered
show_instructions = "***"
while show_instructions != "xxx":

# ask the user if they have played before
    show_instructions = input("Have you played before ?").lower().strip()

# If they say yes 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continues")

    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("Displys instructions")
# If they say no 'display instructions'
    else:
        print("Please enter yes or No")



