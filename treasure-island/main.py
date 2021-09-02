print('''
*******************************************************************************
888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888  
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input('You are at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if direction == "right":
  print("You fall into a hole! Game over.")
elif direction == "left":
  lake = input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
  if lake == "swin":
    print("You have been attacked by trout! Game over.")
  elif lake == "wait":
    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
    if door == "blue":
      print("You have been eaten by beasts! Game over.")
    elif door == "red":
      print("You have been burned by fire! Game over.")
    elif door == "yellow":
      print("You Win!")
    else:
      print("Game Over.") 
