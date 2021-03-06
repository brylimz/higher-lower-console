import art
import random
from game_data import data
from art import logo, vs
print(art.logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


def format_data(account):
    """ Format the account data and returns into printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """ Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# make the game repeatable

while game_should_continue:

    # generate a random account from the game data
    # making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # ask user for a guess
    guess = input("Who has more followers?, Type 'A' or 'B'").lower()

    # check if user is correct
    # # get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # # use if statement to check if user is correct
    is_correct = check_answer(guess, a_follower_count,b_follower_count)
    # give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
        play = input("do you wanna play again? 'Y' or 'N'").lower()
        if play == "y":
            game_should_continue = True
        else:
            print("Have a nice day")
