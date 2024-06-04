#Nested Decisions: The Adventure Game
#Task 1
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

#Task 2
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    torch_action = input("Do you want to light a torch or proceed in the dark?")
    if torch_action == "light a torch":
        print("You light a torch and discover an ancient cave painting!")
    elif torch_action == "proceed in the dark":
        print("You stumble and fall into a pit!")
    else:
        print("Invalid input! Please choose either 'light a torch' or 'proceed in the dark'.")

#Task 3 
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    torch_action = input("Do you want to light a torch or proceed in the dark?")
    if torch_action == "light a torch":
        print("You light a torch and discover an ancient cave painting!")
    elif torch_action == "proceed in the dark":
        print("You stumble and fall into a pit!")
    else:
        pass
else:
    pass
