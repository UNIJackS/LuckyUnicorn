# ask the user if they have played before
    show_instructions =  input("Have you played before ?").lower()

# If they say yes 'program continues'
    if show_instructions == "yes":
      print("program continues")

    elif show_instructions == "y":
      print("program continues")

    elif show_instructions == "No":
        print("Displys instructions")

    elif show_instructions == "N":
        print("Displys instructions")

# If they say no 'display instructions'
    else:
        print("Please enter yes or No")
