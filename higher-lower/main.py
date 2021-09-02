from art import logo, vs
from game_data import data
from replit import clear
import random

# compare the number of followers between two person
def compare(random_person_A, random_person_B):
  print(f'Compare A: {random_person_A["name"]}, {random_person_A["description"]}, from {random_person_A["country"]}.')
  print(vs)
  print(f'Against B: {random_person_B["name"]}, {random_person_B["description"]}, from {random_person_B["country"]}.')
  if random_person_A["follower_count"] > random_person_B["follower_count"]:
    return "A"
  else:
    return "B"
  
# Main Program
clear()
print(logo)

end_game = False
current_score = 0
random_person_A = random.choice(data)
random_person_B = random.choice(data)  
while not end_game:    
  # Avoid duplicate data
  while random_person_A == random_person_B:
    random_person_B = random.choice(data)
  winner = compare(random_person_A, random_person_B)
  user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
  if user_choice == winner:
    clear()
    print(logo)
    current_score += 1
    if user_choice == "A":      
      random_person_B = random.choice(data)
      while random_person_A == random_person_B:
        random_person_B = random.choice(data)  
    else:
      random_person_A = random_person_B
      random_person_B = random.choice(data)
      while random_person_A == random_person_B:
        random_person_B = random.choice(data)
    print(f"You're right! Current score: {current_score}.")  
  else:
    clear()
    print(logo)  
    print(f"Sorry, that's wrong. Final score: {current_score}")
    end_game = True
