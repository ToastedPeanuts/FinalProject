import pygame
import time
import random
import keyboard
import os

def draw_text(screen,text,font,text_col,x,y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))

def anim_print(text):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(0.1)

def exit_on_key(keyname):
    def callback(event):
        if event.name == keyname:
            os._exit(1)
    return callback

def introScene():

    anim_print("You come to a grove in the middle of the forest\n")
    anim_print("          \n")
    anim_print("There are multiple paths you can take; Right, Left,\n")
    anim_print("Backwards, and Escape\n")
    anim_print("          \n")
    anim_print("Which path will you take?\n")
    anim_print("          \n")
    direction = ["RIGHT", "LEFT", "BACKWARD", "ESCAPE"]
    userInput = ""
    while userInput not in direction:
        userInput = input()
        capInput = userInput.upper()
        if capInput == "RIGHT":
            anim_print("You slowly move through a thick collection of trees.\n")
            anim_print("The branches on these trees are closely knitted together\n")
            anim_print("making this path rather dark and weary\n")
            anim_print("          \n")
            monsterOne()

        elif capInput == "LEFT":
            anim_print("You walk along a well used path.\n")
            anim_print("The sun shines bright, almost like the light is\n")
            anim_print("guiding your way\n")
            anim_print("          \n")
            personOne()

        elif capInput == "BACKWARD":
            anim_print("Adventurers must face their fears, choose a direction\n")
            anim_print("          \n")

        elif capInput == "ESCAPE":
            anim_print("You have chosen to escape")
            anim_print("          \n")
            quit()

        else:
            anim_print("Please choose a direction\n")
            anim_print("          \n")

def monsterOne():
    attitude= random.randrange(0,1)
    if attitude == 0:
        # Initial Friendly response from Monster 1
        anim_print("A large green monster with black dots suddenly\n")
        anim_print("appears on the path in front of you.\n")
        anim_print(f"'Oh! Welcome to the woods {name}!\n")
        anim_print("What are you doing so deep in this dangerous place?'\n")
        anim_print("          \n")

        responses = ["1","2"]
        userInput = ""
        while userInput not in responses:
            anim_print("Option 1: Just peacefully adventuring through\n")
            anim_print("          \n")

            anim_print("Option 2: None of your business monster!\n")
            anim_print("          \n")

            anim_print("How will you respond?\n")
            anim_print("1 or 2?\n")

            userInput = input()
            capInput = userInput
            if capInput == "1":
                # Friendly response from Player
                anim_print(f"'Be on your way then {name}.\n")
                anim_print("Stay safe and keep your eyes and ears sharp'\n")
                anim_print("The monster slowly moves along his way\n")
                anim_print("back into the the cover of the trees\n")
                anim_print("          \n")
                ending.append("0")

            elif capInput == "2":
                # Hostile response from Player
                anim_print("*GROWL* 'I was trying to be helpful but it seems\n")
                anim_print("all you humans are the same'\n")
                anim_print("You watch as the monster stomps away\n")
                anim_print("          \n")
                ending.append("1")

            else:
                anim_print("Please choose an option\n")


    elif attitude == 1:
        # Initial Hostile response from Monster 1
        anim_print("You slowly approach a large, red monster sitting\n")
        anim_print("underneath a tree on the path.\n")
        anim_print("The monster spots you and slowly gets to it's feet.\n")
        anim_print("'What is a pathetic human like you doing\n")
        anim_print("in a place like this?'\n")
        anim_print("He grins menacingly, looking you up and down.\n")
        anim_print("          \n")

        responses = ["1","2"]
        userInput = ""
        while userInput not in responses:
            anim_print("Option 1: 'I'm not looking for any trouble.\n")
            anim_print("Please just let me pass'\n")
            anim_print("          \n")

            anim_print("Option 2: 'None of your business monster!\n")
            anim_print("Now move out of the way before I take your head as my prize.'\n")
            anim_print("          \n")
    
            anim_print("How will you respond?\n")
            anim_print("1 or 2?\n")

            userInput = input()
            capInput = userInput
            if capInput == "1":
                # Friendly response from Player
                anim_print("You feel his questioning gaze, almost like he\n")
                anim_print("doesn't fully believe you.\n")
                anim_print("          \n")
                anim_print("'Move quickly through before I change my mind.'\n")
                anim_print("          \n")
                ending.append("0")

            elif capInput == "2":
                # Hostile response from Player
                anim_print("The monster huffs and steps forward but quickly stops\n")
                anim_print("almost as if he is assessing if you really mean what you say.\n")
                anim_print("He bares his teeth and growls very deeply towards you.\n")
                anim_print("'Better move along before you lose your life human.'\n")
                anim_print("You move past him with confidence, very aware of the\n")
                anim_print("eyes glaring at you as you pass.\n")
                anim_print("          \n")
                ending.append("1")

            else:
                anim_print("Please choose an option\n")

    direction = ["RIGHT", "LEFT", "BACKWARD", "ESCAPE"]
    userInput = ""
    while userInput not in direction:
        anim_print("There are multiple paths you can take; Right, Left,\n")
        anim_print("Backwards, and Escape\n")
        anim_print("Which path would you like to take?\n")

        userInput = input()
        capInput = userInput.upper()
        if capInput == "RIGHT":
            anim_print("You slowly move along a flowing river,\n")
            anim_print("breathing in the fresh air and admiring\n")
            anim_print("all the life around you.\n")
            anim_print("          \n")
            personTwo()

        elif capInput == "LEFT":
            anim_print("The path you are following leads into\n")
            anim_print("a plain of long grass.\n")
            anim_print("The blades of grass slowly sway with the wind\n")
            anim_print("as you move through.\n")
            anim_print("          \n")
            monsterTwo()

        elif capInput == "BACKWARD":
            anim_print("The monster would probably not be very happy to see you again.\n")
            anim_print("Choose a different direction.\n")
            anim_print("          \n")

        elif capInput == "ESCAPE":
            anim_print("You have chosen to escape")
            anim_print("          \n")
            quit()

        else:
            print("Please choose a direction\n")

def monsterTwo():
    attitude= random.randrange(0,1)
    if attitude == 0:
        # Initial Friendly response from Monster 2
        anim_print("'A human! These woods are not safe for someone like you!\n")
        anim_print("Perhaps you should turn back?'\n")
        anim_print("          \n")

        responses = ["1","2"]
        userInput = ""
        while userInput not in responses:
            anim_print("Option 1: 'I do appreciate the concern, but I can handle myself.'\n")
            anim_print("          \n")

            anim_print("Option 2: 'No monster is going to tell me what to do,\n")
            anim_print("Get out of my way!'")
            anim_print("          \n")

            anim_print("How will you respond?\n")
            anim_print("1 or 2?\n")
            anim_print("          \n")

            userInput = input()
            capInput = userInput
            if capInput == "1":
                # Responding to Friendly Player
                anim_print("'Be on your way quickly then.\n")
                anim_print("These woods are not kind to those who dawdle.'\n")
                anim_print("          \n")
                ending.append("0")

            elif capInput == "2":
                # Responding to Hostile Player
                anim_print("The monster flares his nostrils at you in anger.\n")
                anim_print("'Watch your back human, you walk on thin ice\n")
                anim_print("with responses like that.'")
                anim_print("          \n")
                ending.append("1")

            else:
                anim_print("Please choose an option\n")


    elif attitude == 1:
        # Initial Hostile response from Monster 2
        anim_print("You slowly approach an orange monster with blue streaks.\n")
        anim_print("He quickly snaps his eyes to you as you get closer.\n")
        anim_print("'Wonderful, now I don't need to hunt for the evening,\n")
        anim_print("my meal has come straight to me!'\n")
        anim_print("          \n")

        responses = ["1","2"]
        userInput = ""
        while userInput not in responses:
            anim_print("Option 1: 'I am just peacefully adventuring through\n")
            anim_print("I'm not looking for any trouble'\n")
            anim_print("          \n")

            anim_print("Option 2: 'Take another step closer and it will be your last.\n")
            anim_print("          \n")
    
            anim_print("How will you respond?\n")
            anim_print("1 or 2?\n")

            userInput = input()
            capInput = userInput
            if capInput == "1":
                # Responding to Friendly Player
                anim_print("The monster studies you, almost as if\n")
                anim_print("he was trying to read your mind.\n")
                anim_print("'Luck has found you today as I am in a very good mood.\n")
                anim_print("Leave while you can, lest my mood be spoiled.\n")
                anim_print("          \n")
                ending.append("0")

            elif capInput == "2":
                # Responding to Hostile Player
                anim_print("The monster huffs and steps forward but quickly stops\n")
                anim_print("almost as if he is assessing if you really mean what you say.\n")
                anim_print("A deep and angry growl vibrates the air between the two of you.\n")
                anim_print("He snarls out 'Better move along before you lose your life human.'\n")
                anim_print("You quickly move though, not wanting to test if he\n")
                anim_print("is true to his word.")
                ending.append("1")

            else:
                anim_print("Please choose an option\n")

    direction = ["FORWARD", "BACKWARD", "ESCAPE"]
    userInput = ""
    while userInput not in direction:
        anim_print("There aren't very many options to choose from here...\n")
        anim_print("Forward, Backward, Escape\n")
        anim_print("Which way would you like to go?\n")
        anim_print("          \n")
        
        userInput = input()
        capInput = userInput.upper()
        if capInput == "FORWARD":
            anim_print("The path ascends into a hill as you move along.\n")
            anim_print("As you reach the peak, you notice\n")
            anim_print("a small cottage with a smoke stack coming from the chimney.\n")
            anim_print("          \n")
            magician()

        elif capInput == "BACKWARD":
            anim_print("Progress is only made by moving forward, trust your decision.\n")
            anim_print("Choose a different direction.\n")

        elif capInput == "ESCAPE":
            anim_print("You have chosen to escape")
            quit()
        else:
            anim_print("Please choose a direction\n")

def personOne():
    attitude= random.randrange(0,1)
    if attitude == 0:
        # Friendly response from Person 1
        anim_print("With such a clear view ahead, you quickly see\n")
        anim_print("the shopkeeper carefully looking at the plantlife by the path.\n")
        anim_print("As you approach, he waves to you.\n")
        anim_print(f"'Hello {name}! So nice to see a friendly face\n")
        anim_print("so far out here.'\n")
        anim_print("          \n")

        responses = ["1","2"]
        userInput = ""
        while userInput not in responses:
            anim_print("OPTION 1: You wave back towards the man.\n")
            anim_print("'Hello there shopkeep!\n")
            anim_print("Finding anything good out here?'\n")
            anim_print("          \n")

            anim_print("OPTION 2: Your face slowly shifts into a scowl.\n")
            anim_print("'I'm really busy, please move out of my way'\n")
            anim_print("          \n")

            anim_print("How will you respond?\n")
            anim_print("1 or 2?\n")

            userInput = input()
            capInput = userInput
            if capInput == "1":
                # Responding to Friendly Player
                anim_print("'Just some various mushrooms and herbs'\n")
                anim_print("nothing too fancy.'\n")
                anim_print("'Should probably get home to the wife\n")
                anim_print("she really hates me being out here this late.'\n")
                anim_print("He slowly picks up his bag and starts down\n")
                anim_print("the path you just walk up.\n")
                anim_print("          \n")
                ending.append("0")

            elif capInput == "2":
                # Responding to Hostile Player
                anim_print("RESPONSE FROM PERSON 1\n")
                anim_print("          \n")
                ending.append("1")

            else:
                anim_print("Please choose an option\n")


    elif attitude == 1:
        # Hostile response from Person 1
        anim_print("HOSTILE RESPONSE FROM PERSON 1\n")
        anim_print("          \n")
        responses = ["1","2"]
        userInput = ""
        while userInput not in responses:
            anim_print("OPTION 1: FRIENDLY PLAYER RESPONSE\n")
            anim_print("          \n")

            anim_print("OPTION 2: HOSTILE PLAYER RESPONSE\n")
            anim_print("          \n")
    
            anim_print("How will you respond?\n")
            anim_print("1 or 2?\n")

            userInput = input()
            capInput = userInput
            if capInput == "1":
                # Friendly response from Player
                anim_print("FRIENDLY RESPONSE FROM PLAYER 1\n")
                anim_print("          \n")
                ending.append("0")

            elif capInput == "2":
                # Hostile response from Player
                anim_print("HOSTILE RESPONSE FROM PLAYER 1\n")
                anim_print("          \n")
                ending.append("1")

            else:
                anim_print("Please choose an option\n")

    direction = ["RIGHT", "LEFT", "BACKWARD", "ESCAPE"]
    userInput = ""
    while userInput not in direction:
        anim_print("Which way will you go? Right, Left, Backward, Escape\n")
        userInput = input()
        capInput = userInput.upper()
        if capInput == "RIGHT":
            anim_print("You have chosen to go right\n")
            anim_print("          \n")
            personTwo()
        elif capInput == "LEFT":
            anim_print("You have chosen to go left\n")
            anim_print("          \n")
            monsterTwo()
        elif capInput == "BACKWARD":
            anim_print("That person would not like to see you return\n")
            anim_print("back this way\n")
            anim_print("Please choose another direction\n")
        elif capInput == "ESCAPE":
            anim_print("You have chosen to escape")
            quit()
        else:
            anim_print("Please choose a direction\n")

def personTwo():
    attitude= random.randrange(0,1)
    if attitude == 0:
        # Friendly response from Person 2
        anim_print("FRIENDLY RESPONSE FROM PERSON 2\n")
        anim_print("          \n")

        responses = ["1","2"]
        userInput = ""
        while userInput not in responses:
            anim_print("OPTION 1: FRIENDLY RESPONSE FROM PLAYER\n")
            anim_print("          \n")

            anim_print("OPTION 2: HOSTILE RESPONSE FROM PLAYER\n")
            anim_print("          \n")

            anim_print("How will you respond?\n")
            anim_print("1 or 2?\n")
            anim_print("          \n")

            userInput = input()
            capInput = userInput
            if capInput == "1":
                # Friendly response from Player
                anim_print("FRIENDLY RESPONSE FROM PERSON 2\n")
                anim_print("          \n")
                ending.append("0")

            elif capInput == "2":
                # Hostile response from Player
                anim_print("HOSTILE RESPONSE FROM PERSON 2\n")
                anim_print("          \n")
                ending.append("1")

            else:
                anim_print("Please choose an option\n")


    elif attitude == 1:
        # Hostile response from PERSON 2
        anim_print("HOSTILE RESPONSE FROM PERSON 2\n")
        anim_print("          \n")

        responses = ["1","2"]
        userInput = ""
        while userInput not in responses:
            anim_print("OPTION 1: FRIENDLY RESPONSE FROM PLAYER")
            anim_print("          \n")

            anim_print("OPTION 2: HOSTILE RESPONSE FROM PLAYER\n")
            anim_print("          \n")
    
            anim_print("How will you respond?\n")
            anim_print("1 or 2?\n")

            userInput = input()
            capInput = userInput
            if capInput == "1":
                # Friendly response from Player
                anim_print("FRIENDLY RESPONSE FROM PERSON 2\n")
                ending.append("0")

            elif capInput == "2":
                # Hostile response from Player
                anim_print("HOSTILE RESPONSE FROM PERSON 2\n")
                ending.append("1")

            else:
                anim_print("Please choose an option\n")

    direction = ["FORWARD", "BACKWARD", "ESCAPE"]
    userInput = ""
    while userInput not in direction:
        anim_print("Which way will you go? Forward, Backward, Escape\n")
        userInput = input()
        capInput = userInput.upper()
        if capInput == "FORWARD":
            anim_print("The path ascends into a hill as you move along.\n")
            anim_print("As you reach the peak, you notice\n")
            anim_print("a small cottage with a smoke stack coming from the chimney.\n")
            anim_print("          \n")
            magician()
        elif capInput == "BACKWARD":
            anim_print("They seemed nice, but it is best to keep moving forward\n")
            anim_print("Choose a different direction.\n")

        elif capInput == "ESCAPE":
            anim_print("You have chosen to escape")
            quit()
        else:
            anim_print("Please choose a direction\n")

def magician():
    if ending == ["0","0"]:
        #GOOD ENDING
        anim_print("You have won! Congratulations!")
        anim_print("          \n")
        quit()
    elif ending == ["1","1"]:
        #BAD ENDING
        anim_print("Game Over")
        quit()
    else:
        #DECENT ENDING
        anim_print("You are a human, good job")
        quit()


def main():
    running = True
    while running:
    #pygame.init()
    #pygame.display.set_caption('Background')
    #resolution=(800,571)
    #screen=pygame.display.set_mode(resolution)
    #imp = pygame.image.load("DarkWoods.png")
    #screen.blit(imp,(0,0))
    #pygame.display.flip()
    #text_font=pygame.font.SysFont("Arial", 30)
        introScene()



    #running=True
    #while running:
        #draw_text(imp,"Hello there brave adventurer!", text_font, (255,255,255), 400,420)
        #for event in pygame.event.get():
            #if event.type==pygame.QUIT:
               # running=False
            #if event.type == pygame.KEYDOWN:
                #pygame.KEYDOWN == pygame.K_ESCAPE
                #running = False  
        #Game Logic:
        #Render and Display
    #pygame.quit()

if __name__ == "__main__":
    keyboard.hook(exit_on_key('esc'))
    # setting up for the ending calculation
    global ending
    ending = []
    anim_print("What is your name?\n")
    # Input from user 
    global name
    name = input().upper()
    #Setup & introduction
    anim_print(f"Hello there {name}!\n")
    anim_print("          \n")
    anim_print("You are a well known traveler and today you have decided to venture through\n")
    anim_print("the dark and mysterious woods.\n")
    anim_print("There is a rumor that a magician resides there\n")
    anim_print("and will reward you with riches if you find him!")
    anim_print("          \n")
    anim_print(f'Good luck on your quest {name}, stick to the path!\n')
    anim_print("          \n")
    anim_print("          \n")
    main()