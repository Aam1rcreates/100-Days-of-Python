import random

# import the logo from the art
from art import logo
print(logo)

# Select the difficulty
difficulty = input("Which mode do you wanna play? Type 'easy' or 'hard'\n")

# According to difficulty, player get limited chances to guess for hard 5 chances and 10 chances for easy
times = 0
if difficulty == "easy":
    times = 10
else:
    times = 5

# The random number is generate, which player has to guess
the_num = random.randint(1,100)

# toggle to check if the game goes on or end. Game ends when player guesses the correct number Or he runs out of chances
game_over = False

counter = 0
while game_over == False:
    # Player takes a guess
    user_input = int(input("What's your guess? "))

    # Count the number of guess player has already taken
    counter = counter + 1

    # check if the user guesses the correct number, or their guess is greater or smaller than the actual number    
    if the_num == user_input:
        print("You guessed it right!")
        game_over = True
        break
    elif the_num > user_input:
        print("Too Low")
    else:
        print("Too High")
    if times == counter:
        print("You Lose! You couldn't guessed the right number in the limited chances.")
        game_over = True  

# Happy Playing         
