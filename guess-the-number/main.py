#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
print(logo)

# create a function to return a number between 1 and 100
def random_number():
  number = random.randint(1, 100)
  return number

# create a function to check user's guess against actual answer.
# Return 0 if the correct answer has been found.
def check_guess(number):
  if number > answer:
    return("Too high.")
  elif number < answer:
    return("Too low.")
  else:
    return 0

# Create a function to return the max attempts according to difficulty level
def difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    max_attempts = 10    
  else:
    max_attempts = 5
  return max_attempts

# Main program
answer = random_number()
end_game = False

print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
print(f"Pssst, the correct answer is {answer}")

max_attempts = difficulty()
attempt = max_attempts
while not end_game and attempt >= 1:
  print(f"You have {attempt} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  result = check_guess(guess)
  if result == 0:
    print(f"You got it! The answer was {answer}.")
    end_game = True
  else:
    print(result)
    attempt -= 1
    if attempt < 1:
      print("You've run out of guesses, you lose.")
  