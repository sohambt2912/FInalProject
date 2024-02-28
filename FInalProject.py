# Module used for sound
import os


def l():
    os.system("afplay L.wav&")
    print("You were one question away from winning")


# Function used when player loses
def end():
    os.system("afplay dsim.wav&")
    print("You have lost the game")


# Rules and instructions
print(
    "Welcome to the Dating Simulator Game. \nInstructions: The goal of the game is to answer correctly until you beat the game(It will be quite obvious). The female you chose will say a phrase and you will be given a range from 2 to 4 choices of  what to say in response. In some occasions there will be more than one correct answer. If you get it wrong, you go back to the beginning. The choices can sometimes be an action. \nImportant: You choose an option by typing CAPITAL A, B, C or D. It will not work if you don't use capital.")

# Starting Question
MQ = input("Choose between Alice and Lory: ")
MQ = MQ.capitalize()
MQ = MQ.strip()

# What happens in the game depends on the character you choose
if MQ == "Alice":
    print(
        "You have gone to the library to buy the newest release of a book series you really like. It is your lucky day and it is the last copy of the book. You go to get it, but at the same time a girl touches the book at the same time(FYI, you are antisocial).")
    A = input(
        "Oh sorry, you can have it. \n A: It's fine, you take it. Can come another day. \n B: Really? Are you sure? Thank you. \n C: Ha! Go suck my lolipop. \n D: If this is a trick, you will live the same fate as Ned Stark. \n Choose an option: ")
    if A == "C" or A == "D":
        end()
    elif A == "A" or A == "B":
        B = input(
            "I suppose you are interested in this book? \n A: Not really \n B: Yes, I love it! \n Choose an option: ")
        if B == "A":
            end()
        elif B == "B":
            # The correct answer will lead to another variable and so on
            C = input(
                "I have an idea! How about I give you the book once I finish it? \n A: Give phone number \n B: Sorry, I don't have a phone \n C: Digusting, not to a person with an android \n Choose an option: ")
            if C == "B":
                print("Thats a shame")
                end()
            elif C == "C":
                end()
            elif C == "A":
                print(
                    "I forgot to tell you, my name is Alice.\n You and Alice have been sending messages to each other and you both decide to go on a date during the week-end. \n You have been waiting for 5 minutes and she still isn't there")
                D = input(
                    "Sorry I'm late, have you been waiting for long? \n A: Yes \n B: What the Hell? It's been 15 minutes \n C: Maybe, maybe not \n D: No, I only just arrived myself. \n Choose an option: ")
                if D == "A" or D == "B" or D == "C":
                    end()
                elif D == "D":
                    E = input(
                        "Is there anything else you would ike to say to me? \n A: You look good, I suppose \n B: No, not really \n C: Winter is coming! \n D: You Probably want me to say that you look good, but I find those tyoes of girls annoying \n Choose an option: ")
                    if E == "A" or E == "B" or E == "D":
                        print("Too boring")
                        end()
                    elif E == "C":
                        # Game of Thrones theme song
                        os.system("afplay got.wav&")
                        print("You have an amazing first date and it is already the time to end the date")
                        F = input(
                            "The was fun! Let's head back now. \n A: Walk her home \n B: Invite her to a love hotel \n C: I also had fun. I have to go home to wacth the new episode, so goodbye \n Choose an option: ")
                        if F == "B":
                            print("Not on the first date")
                            end()
                        elif F == "A" or F == "C":
                            print("Proceed to the next chapter")
                            print(
                                "You are on a date in the arcade and like the weirdo that you are, you have completed many many video games")
                            G = input(
                                "Let's play Mario. \n A: Okay, but if I win you owe me an ice-cream \n B: You are probably shit \n C: I prefer street fighter \n Choose an option: ")
                            if G == "A":
                                # For the variable G, all the possibilities can lead to beating the game
                                ga = input(
                                    "What if I win? \n A: Absolutely nothing \n B: I'll let you suck my toes \n C: I'll buy you a chocolate \n Choose an option: ")
                                if ga == "A":
                                    end()
                                elif ga == "B":
                                    print("You have beaten the game, every girl would want to be with you")
                                elif ga == "C":
                                    print("You have decided to go eat dinner.")
                                    fff = input(
                                        "Let's go eat in that Italian restaurant. \n A: Only if you pay for the food \n B: I will pay for the food \n C: I strive for gender equality, so we each pay our own food. \n Choose an option: ")
                                    if fff == "A" or fff == "B":
                                        l()
                                    elif fff == "C":
                                        print(
                                            "Coongratulations, you have completed the game. You will certainly get a girlfriend and loose your...")
                                        os.system("afplay GJ.wav&")
                            elif G == "B":
                                gb = input(
                                    "We will see about that. \n A: Let her win. \n B: Beat her. \n Choose an option: ")
                                if gb == "A":
                                    end()
                                elif gb == "B":
                                    fff = input(
                                        "Let's go eat in that Italian restaurant. \n A: Only if you pay for the food \n B: I will pay for the food \n C: I strive for gender equality, so we each pay our own food. \n Choose an option: ")
                                    if fff == "A" or fff == "B":
                                        l()
                                    elif fff == "C":
                                        print(
                                            "Coongratulations, you have completed the game. You will certainly get a girlfriend and loose your...")
                                        os.system("afplay GJ.wav&")
                            elif G == "C":
                                gc = input(
                                    "Scared? I'll beat you in that aswell though. \n A: You probably will \n B: I can't see the future, so there is 50 percent chance you win \n C: You reealy wont though \n D: Maybe, maybe not \n choose an option: ")
                                if gc == "A" or gc == "C" or gc == "D":
                                    end()
                                elif gc == "B":
                                    print("You have decided to go eat dinner.")
                                    fff = input(
                                        "Let's go eat in that Italian restaurant. \n A: Only if you pay for the food \n B: I will pay for the food \n C: I strive for gender equality, so we each pay our own food. \n Choose an option: ")
                                    if fff == "A" or fff == "B":
                                        l()
                                    elif fff == "C":
                                        print(
                                            "Coongratulations, you have completed the game. You will certainly get a girlfriend and loose your...")
                                        os.system("afplay GJ.wav&")
# Second Character
elif MQ == "Lory":
    print(
        "You have chosen Lory. Lory is person from your school. You are a shy person who doesn't really like talking to people. You see her in the rooftop of the school. She notices you and thinks you are weird")
    A = input(
        "Stop staring at me! \n A: Run Away \n B: Sorry \n C: I wasn't looking at you \n D: Not my fault you dress like a thot \n Choose an option: ")
    if A == "A":
        end()
    elif A == "D":
        print(
            "There is no reason for you to play this dumb simulator. You are already a genius when it comes to dating")
    elif A == "B":
        aa = input(
            "So you were staring at me. You Weirdo. \n A: I didn't mean to \n B: I said sorry already \n C: It's because you are beautiful. \n Choose an option: ")
        if aa == "A" or aa == "B":
            end()
        elif aa == "C":
            print("I prefer people liking me for my personality")
            end()
    elif A == "C":
        B = input(
            "What were you looking at then? \n A: Your ankles \n B: The floor \n C: Nothing really. I was just imagining a life where I had powers \n Choose an option: ")
        if B == "A" or B == "B":
            end()
        elif B == "C":
            C = input(
                "What powers? \n A: Not being noticed \n B: Being able to see girls naked \n C: Being able to fly \n Choose an option: ")
            if C == "B":
                end()
            elif C == "C":
                print("Boring")
                end()
            elif C == "A":
                print("Since then you have spoken a lot to each other and she invited you to her house")
                D = input(
                    "What should we do? \n A: Sleep \n B: Study for the Science test \n C: Fornicate \n D: Watch something \n Choose an option: ")
                if D == "A" or D == "C":
                    end()
                elif D == "D":
                    da = input(
                        "What do you want to watch? \n A: How to train your dragon 1 \n B: Titanic \n C: Spaceballs \n D: Shaolin Soccer \n Choose an option: ")
                    if da == "B":
                        end()
                    elif da == "A" or da == "C" or da == "D":
                        print("After watchin the movie, you are both hungry")
                        E = input(
                            "Do you want anyhting to eat or drink? \n A: Your toes \n B: How about we go somehwere out? \n C: No \n Choose an option: ")
                        if E == "A" or E == "C":
                            end()
                        elif E == "B":
                            F = input(
                                "Where would you like to go? \n A: Mcdonalds \n B: My grandparents house \n Choose an option: ")
                            if F == "B":
                                end()
                            elif F == "A":
                                print("You ended up going to your grandma's house")
                                print(
                                    "You are on a date with Lory on a week-end and you go buy a drink for her. When you come back you see her talking with a guy.")
                                G = input(
                                    "What do you do? \n A: Ignore it \n B: Throw a shuriken at the guy \n C: Confront him \n D: Get with another girl, cause you are awsome \n Choose an option: ")
                                if G == "A" or G == "C":
                                    end()
                                elif G == "B":
                                    print("You missed")
                                    end()
                                elif G == "D":
                                    print("Confidence is key")
                                    H = input(
                                        "What are you going to give me for my birthday? \n A: All the episodes of GOT \n B: My collection of Hentai \n C: Nothing \n D: My banana \n Choose an option: ")
                                    if H == "B" or H == "C" or H == "D":
                                        end()
                                    elif H == "A":
                                        I = input(
                                            "Will we be together forever? \n A: Yes, until we die \n B: Can't see the future, so I don't know \n C: Hell No \n Choose an option: ")
                                        if I == "A":
                                            print("Don't promise things you are not certain will happen")
                                            l()
                                        elif I == "C":
                                            l()
                                        elif I == "B":
                                            print("This is why I really love you")
                                            print("Thanks for dating me, even though I am your sister")
                                            print(
                                                "Congratulations you have won the game and now live a happy life with your sister")
                                            os.system("afplay GJ.wav&")

                # In the variable of D, there are 2 correct answers that can lead to the end
                elif D == "B":
                    E = input(
                        "Do you want anyhting to eat or drink? \n A: Your toes \n B: How about we go somehwere out? \n C: No \n Choose an option: ")
                    if E == "A" or E == "C":
                        end()
                    elif E == "B":
                        F = input(
                            "Where would you like to go? \n A: Mcdonalds \n B: My grandparents house \n Choose an option: ")
                        if F == "B":
                            end()
                        elif F == "A":
                            print("You ended up going to your grandma's house")
                            print(
                                "You are on a date with Lory on a week-end and you go buy a drink for her. When you come back you see her talking with a guy.")
                            G = input(
                                "What do you do? \n A: Ignore it \n B: Throw a shuriken at the guy \n C: Tell him she's dating you \n D: Get with another girl, cause you are awsome \n Choose an option: ")
                            if G == "A" or G == "C":
                                end()
                            elif G == "B":
                                print("You missed")
                                end()
                            elif G == "D":
                                print("Confidence is key")
                                H = input(
                                    "What are you going to give me for my birthday? \n A: All the episodes of GOT \n B: My collection of Hentai \n C: Nothing \n D: My banana \n Choose an option: ")
                                if H == "B" or H == "C" or H == "D":
                                    end()
                                elif H == "A":
                                    I = input(
                                        "Will we be together forever? \n A: Yes, until we die \n B: Can't see the future, so I don't know \n C: Hell No \n Choose an option: ")
                                    if I == "A":
                                        print("Don't promise things you are not certain will happen")
                                        end()
                                    elif I == "C":
                                        print("You are too intelligent to get a GF")
                                        l()
                                    elif I == "B":
                                        print("This is why I really love you")
                                        print("Thanks for dating me, even though I am your sister")
                                        print(
                                            "Congratulations you have won the game and now live a happy life with your sister")
                                        os.system("afplay GJ.wav&")

# Statement if something other than names is typed
else:
    print("Invalid Character")














