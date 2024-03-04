import random


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

        if to_check == "":
            return ""

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


# compares user / comp choice and returns all possible results
def rps_compare(user, comp):
    # If same then tie

    if user == comp:
        the_result = "tie"

    # winning combos
    elif user == "paper" and comp == "rock":
        the_result = "win"
    elif user == "scissors" and comp == "paper" or user == "rock" and comp == "scissors":
        the_result = "win"

    # if not win/tie must be loss
    else:
        the_result = "lose"

    return the_result


# Main routine goes here

# what the game is supposed to be
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0

yes_no_list = ['yes', 'no']
rps_list = ['rock', 'paper', 'scissors', 'quit']
game_history = []
# Title
statement_generator("Rock, Paper, Scissors", "🗿🏳️🔪")

# instructions
want_instructions = string_checker("Do you want to see the instructions?", yes_no_list)

if want_instructions == "yes":
    instructions()

# Ask user for number of rounds
num_rounds = num_check("How many rounds would you like? Push <enter> for 🚂infinite mode🚂: ")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# game loops ends here
while rounds_played < num_rounds:

    # rounds based on mode
    if mode == "infinite":
        rounds_heading = f"\n👏👏👏 Round {rounds_played + 1} (Infinite Mode) 👏👏👏"
    else:
        rounds_heading = f"\n🐪🐪🐪 Round {rounds_played + 1} of {num_rounds} 🐪🐪🐪"

    print(rounds_heading)

    comp_choice = random.choice(rps_list[:-1])

    # RPS
    user_choice = string_checker("Choose: ", rps_list)
    print(f"you chose, {user_choice}  ")

    # alf-f4
    if user_choice == "quit":
        break

    # comp move but without the leave button

    the_result = rps_compare(user_choice, comp_choice)

    # adjust game lost / game tied counters and add results to game history
    if the_result == "tie":
        rounds_tied += 1
        feedback = "🐲🐲 It's a tie 🐲🐲"
    elif the_result == "lose":
        rounds_lost += 1
        feedback = "🌄🌄 YOU lost 🌄🌄"
    else:
        feedback = "🦄🦄 You won :)) 🦄🦄"

    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played + 1} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played += 1

    # but infinite?
    if mode == "infinite":
        num_rounds += 1

    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played} (Infinite Mode)"
    else:
        rounds_heading = f"\n Round {rounds_played} of {num_rounds}"

# stats for nerds
if rounds_played > 0:

    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # put stats

    print("💶💶💶 Game Statistics 💶💶💶")

    print(f"🦄 Won: {percent_won:.2f} \t")
    print()

    print(f"🌄 Lost: {percent_lost:.2f} \t")
    print()

    print(f"🐲 Tied: {percent_tied:.2f} \t")
    print()
    # ask user for history
    see_history = string_checker("Do you want to see your game history?", yes_no_list)
    if see_history == "yes":
        for item in game_history:
            print(item)

else:
    "._."

print("           Thank you for playing")
statement_generator("Rock, Paper, Scissors", "🗿🏳️🔪")
print()
