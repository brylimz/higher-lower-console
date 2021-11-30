# display art
import art
import random
from game_data import data
from art import logo, vs
print(art.logo)


def format_data(account):
    """ Format the account data and returns into printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """ Take the user guess and follower counts and returns if they got it right"""



# generate a random account from the game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)
print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_b)}")

# ask user for a guess
guess = input("Who has more followers?, Type 'A' or 'B'").lower()

# check if user is correct
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]

# # get follower count of each account
# # use if statement to check if user is correct
# give user feedback on their guess
# score keeping
# make the game repeatable
# making account at position B become the next account at position A
# clear the screen between rounds
