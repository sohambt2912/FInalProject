# First challenge
challenge = input("You encounter a wild Pidgey! Do you: \n A: Attempt to capture it. \n B: Try to flee. \nChoose an option: ")
if challenge == "A":
    print("You successfully captured Pidgey!")
elif challenge == "B":
    print("You safely escaped.")
else:
    lose()

# Gym battle
gym_battle = input("You've reached the first Gym. The Gym Leader challenges you to a battle! Do you: \n A: Accept the challenge. \n B: Decline and train more. \nChoose an option: ")
if gym_battle == "A":
    print("You've won the battle and earned the Boulder Badge!")
    win()
elif gym_battle == "B":
    print("Training pays off! You feel more prepared for the Gym battle.")
else:
    lose()

# Team Rocket encounter
team_rocket = input("Team Rocket appears and tries to steal your Pokémon! Do you: \n A: Fight them off. \n B: Try to outsmart them. \nChoose an option: ")
if team_rocket == "A":
    print("You bravely fought off Team Rocket and saved your Pokémon!")
    win()
elif team_rocket == "B":
    print("Your clever tactics have foiled Team Rocket's plan!")
    win()
else:
    lose()

print("Thank you for playing the Pokémon Adventure Game. Your journey continues...")

def team_rocket_encounter():
    print("You encounter Team Rocket!")
    choice = input("Do you fight them? (Yes/No): ")
    if choice.lower() == 'yes':
        return gym_battle()
    else:
        print("You avoided the conflict but missed out on a battle opportunity.")
        return False

def battle():
    outcome = random.choice(['win', 'lose'])
    if outcome == 'win':
        win()
        return True
    else:
        lose()
        return False