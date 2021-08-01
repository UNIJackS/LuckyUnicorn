def number_checker(question,low,high):
    # sets the error statement for the if statement to follow
    error = "please enter a whole number between 1 and 10\n"

    # keeps the if statement looping until an appropriate answer is entered
    valid = False
    while not valid:

        # This try statment makes it so the program does not crash if a float is entered rather then an interger as the response
        try:
            response = int(input(question))

            # An if statement that checks if the response to the previous statement is between 0 and 10
            if low < response <= high:
                return(response)

            # An if statement that outputs the error statement if the response is not between 0 and 10
            else:
                print(error)
        except ValueError:
            print(error)
how_much = number_checker("How much would you like to play with ? ", 0, 10)
