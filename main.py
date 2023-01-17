import random
import click
from art import logo
from game_data import data
from art import vs

score = 0
print("*************guess who has more follower***********")
def format_data(source):
    """format the source data into printable format"""
    source_name = source["name"]
    source_desc = source["description"]
    source_country = source["country"]
    return f"{source_name}, a {source_desc}, from {source_country}"

def check_answer(guess, a_followers, b_followers):
    """take the user guess and follower count and return if the user guessed it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
game_is_on = True

#ask user if he want to play the game 
play_game = input("Do you want to play the game of higher and lower?\nType 'y' if you want to play or type 'n' if you want to exit: ").lower()
if play_game == "y":
    game_is_on = True
elif play_game == "n":
    game_is_on = False
else:
    print("Invalid input will be taken as exit")
    game_is_on = False

while game_is_on is True:
    #disply art
    print(logo)

    #generate a random output for game data
    source_1 = random.choice(data)
    source_2 = random.choice(data)
    if source_1 == source_2:
        source_2 = random.choice(data)

    print(f"compare A: {format_data(source_1)}")
    print(vs)
    print(f"compare B: {format_data(source_2)}")

    #ask user for guess
    user_guess = input("Type 'A' to select option A or Type 'B' to select option B: ").lower()

    #get follower count for each account
    a_follower_count = source_1["follower_count"]
    b_follower_count = source_2["follower_count"]

    #check if user is correct
    if_correct = check_answer(user_guess, a_follower_count, b_follower_count)

    #give user feedback on their guess and score tracking
    if if_correct:
        click.clear()
        score += 1
        print(f"You are right! your score is {score}")
        
    else:
        print(f"sorry you are wrong! your final score is {score}")
        game_is_on = False
    

