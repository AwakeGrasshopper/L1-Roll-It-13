# functions go here

def yes_no(question):

    """Cheks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check your user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return"no"
        else:
            print("please enter yes / no")


def instructions():
    """prints instructions"""

    print("""
*** instructions ****

Roll the dice and try to win!    
    """)


# main routine

# ask the user if they want instructions (check they say yes / np)
want_instructions = yes_no("do you want to do the instructions? ")

# display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("Program continues")
