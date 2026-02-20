
# functions go here

def yes_no(question):

    """Cheks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check your user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "no":
            return"no"
        else:
            print("please enter yes / no")

# main routine

# testing loop...
while True:
    want_instructions = yes_no("do you want to do the instructions? ")
    print(f"you chose {want_instructions}")

print ("we done")
