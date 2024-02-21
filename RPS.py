def string_checker(question, valid_ans):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        # print error when error
        print(error)
        print()


def num_check(question):
    valid = False
    while not valid:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        if question == "":
            return "infinite"

        try:

            # ask user to enter a number
            response = int(to_check)

            # checks number is more than one
            if response < 1:
                print(error)
            # Outputs error if input is invalid
            else:
                return response

        except ValueError:
            print(error)


def yes_no_instructions(question):
    while True:
        response = input(question).lower()
        # checks user response to question
        # only accepts yes or no
        if response == "yes" or response == "y":
            instructions()
            return ""

        elif response == "no" or response == "n":
            print("You chose no")
            return ""

        else:
            print("Please answer yes or no ")


def yes_no(question):
    while True:
        response = input(question).lower()
        # checks user response to question
        # only accepts yes or no
        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes or no ")


def statement_generator(text, decoration):
    # Make string with five characters
    ends = decoration * 2

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def instructions():
    statement_generator("Instructions/information", "-")
    print('''
To begin, choose the number of rounds (or press <enter> for infinite mode).

Then play against the computer. YOu can choose between R (rock), P (paper) or S (scissors).

The rules are as follows:
o Paper beats rock
o Rock beats scissors
o Scissors beats paper

Type <quit> to end the game at anytime.

💀💀💀Good Luck💀💀💀
''')
    print()
    return ""


# Main routine goes here

# what the game is supposed to be
mode = "regular"
rounds_played = 0

# Title
statement_generator("Rock, Paper, Scissors", "🗿🏳️🔪")

rps_list = ["rock", "paper", "scissors", "quit"]

# instructions
want_instructions = yes_no_instructions("Do you want to see the instructions?")

# Ask user for number of rounds
num_rounds = num_check("How many rounds would you like? Push <enter> for 🚂infinite mode🚂: ")

if num_rounds == "":
    mode = "infinite"
    print("you chose infinite")
    num_rounds = 5

# game loops ends here
while rounds_played < num_rounds:

    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played} (Infinite Mode)"
    else:
        rounds_heading = f"\n Round {rounds_played} of {num_rounds}"
    input("Choose: ")
    rounds_played += 1
    print("rounds played: ", rounds_played)

    # but infinite?
    if mode == "infinite":
        num_rounds += 1

    print("num rounds: ", num_rounds)


user_choice = string_checker("Choose: ", rps_list)
print("You chose: ", user_choice)

print("   Thank you for playing")
statement_generator("Rock, Paper, Scissors", "🗿🏳️🔪")
print()
