import os
import random

sound_path = "/Users/sohamb22/Desktop/L.mp3"
Soundpathtwo = "/Users/sohamb22/Desktop/Victory.mp3"
def lose():
    os.system(f"afplay {sound_path}&")
    print("Oh no! You have lost the game!")

def win():
    os.system(f"afplay {Soundpathtwo}&")
    print("Congratulations! You've won the Pokémon battle!")


def capture_success():
    print("You successfully captured the wild Pokémon!")

def escape_success():
    print("You safely escaped.")



def final_challenge():
    correct_number = random.randint(1, 10)  # Randomly choose a number between 1 and 10
    print("You have arrived at the final challenge, the Johto region Gym.")
    csix = input("To win this battle you must correctly choose a number between 1-10: ")

    try:
        guess = int(csix)
        if 1 <= guess <= 10:
            if guess == correct_number:
                print(f"Congratulations! The correct number was indeed {correct_number}. You win the battle!")
                win()
                return True
            else:
                print(f"Unfortunately, the correct number was {correct_number}. You lose the battle.")
                lose()
                return False
        else:
            print("Your guess must be between 1 and 10. Please try again.")
            return False
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")
        return False


print("""Welcome to the Pokémon Adventure Game.
Instructions: Your goal is to capture Pokémon, win gym badges, and become a Pokémon Master.
During your journey, you'll face various challenges and make decisions that will affect your success.""")


starter_pokemon = input("Choose your starter Pokémon: (A) Bulbasaur (B) Charmander (C) Squirtle: ")
starter_pokemon = starter_pokemon.capitalize()

if starter_pokemon == "A":
    print("You've chosen Bulbasaur!")
elif starter_pokemon == "B":
    print("You've chosen Charmander!")
elif starter_pokemon == "C":
    print("You've chosen Squirtle!")
else:
    print("Invalid choice, you get Pikachu by default!")
    starter_pokemon = "Pikachu"

# Choosing a region
print("Now, choose the region you'd like to start your adventure in:")
region = input("A: Kanto Region (classic adventure) \nB: Johto Region (new challenges) \nChoose an option: ")

if region == "A":
    print("You have chosen to commence your adventure in the Kanto Region with", starter_pokemon)
    encounter = random.choice(['Pidgey', 'Rattata'])
    print(f"You encounter a wild {encounter}!")
    a = input("Do you: \n A: Attempt to capture it. \n B: Try to flee. \nChoose an option: ")
    if a == "A":
        capture_success()
    elif a == "B":
        escape_success()
    else:
        lose()

    b = input("As you continue walking you encounter a path that is divided in 3 sections. Choose the correct one to continue playing. \n A: Right. \n B: Middle. \n C: Left \n Choose an option:")
    if b == "A" or b == "C":
        lose()
    elif b == "B":
        c = input("You have chosen the correct path. In the corner you notice an old woman needing help hanging off a cliff. \n A: Ignore her and continue \n B: Call police \n C: Be the hero and saver her yourself \n D: Push her off \n Choose an option ")
        if c == "A" or c == "B" or c == "D":
            lose()
        elif c == "C":
            print(f"{starter_pokemon} has saved the woman, but got hurt in the process. The grateful woman has given you berries")
            d = input(f"Would you like to feed {starter_pokemon}, berries? \n A: Yes \n B: No \n Choose an option:")
            if d == "B":
                print("You idiot, your pokemon is your life")
                lose()
            elif d == "A":
                team_rocket = input(
                    "Team Rocket appears and tries to steal your Pokémon! Do you: \n A: Fight them off. \n B: Try to outsmart them. \nChoose an option: ")
                if team_rocket == "A":
                    print("You bravely fought off Team Rocket and saved your Pokémon!")

                elif team_rocket == "B":
                    print("Your clever tactics have foiled Team Rocket's plan!")


                gym_battle = input(
                    "You've reached the first Gym. The Gym Leader challenges you to a battle! Do you: \n A: Accept the challenge. \n B: Decline and train more. \nChoose an option: ")
                if gym_battle == "A":
                    print("You've won the battle and earned the Boulder Badge! Your adventure in the Kanto region has ended.")
                    win()

                elif gym_battle == "B":
                    print("Incorrect. Never back down from a challenge.")
                    lose()






elif region == "B":
    print(f"You have chosen to commence your adventure in the Johto Region with {starter_pokemon}. This region consists more of luck based and general knowledge in order to win the final gym battle")
    print("As you leave the initial village, you are approached by your teacher. He challenges you to a battle before you embark on your journey.")
    initial_challenge = input("In order to win you must correctly answer. What is Newtons 2nd law. \n A: For every action, there is an equal and opposite reaction \n B: Every Object moves in a straight line unless acted upon by force \n C: The acceleration of an object is directly proportional to the objects mass \n CHoose an option: ")
    if initial_challenge == "A" or initial_challenge == "B":
        lose()
    elif initial_challenge == "C":
        print("Well done, you are certainly a smart boy")
        ctwo = input("As you are walking you encounter a wild pokemon trying to attack you. To fend yourself you must win a coin flip. \n Choose between heads or tails:")
        flip_result = random.choice(["heads", "tails"])
        print(f"The coin landed on {flip_result}.")
        if ctwo == flip_result:
            print("You have won the battle. As you continue your journey, you run into a random an old man")
            cthree = input("The old man says that if you get the answer correct he is willing to give you an evolution stone. What year did World War 1 start?")
            if cthree == "1914":
                if starter_pokemon == "A":
                    print(f"Your {starter_pokemon} has evolved into a Ivysaur")
                elif starter_pokemon == "B":
                     print(f"Your {starter_pokemon} has evolved into a Charmeleon")
                elif starter_pokemon == "C":
                    print(f"Your {starter_pokemon} has evolved into a Wartotle")
                else:
                    print(f"Your {starter_pokemon} has evolved into a Raichu")
                cfour = input("Team rocket have appeared! If you type Messi is better than Ronaldo, you will win the battle. ")
                if cfour == "Messi is better than Ronaldo":
                    print("You have won. Team Rocket respected you and drew back")
                    cfive = input("As you try to make it to the next village a guard has stopped you. If you correctly answer this equation he´ll let you pass \n 4x - 10 = 2 \n What is the value of X:")
                    if cfive == "3":
                        print("Correct! He has allowed you through.")
                        print(final_challenge())


                    else:
                        ("No Stupid")
                        lose()
                else:
                    print("Idiot of course Messi is better")
                    lose()


            else:
                lose()
        else:
            print("Unlucky")
            lose()

else:
    print("Invalid choice, start again.")










