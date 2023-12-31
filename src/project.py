import pygame
import time
import random
import keyboard
import os

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
    anim_print("What is your name?\n")
    # Input from user 
    global name
    name = input().capitalize()
    #Setup & introduction
    anim_print(f"Hello there {name}!\n")
    anim_print("          \n")
    anim_print("You are a well known traveler and today you have decided to venture through\n")
    anim_print("the dark and mysterious woods.\n")
    anim_print("There is a rumor that a magician resides there\n")
    anim_print("and will reward you with riches if you find him!\n")
    anim_print("          \n")
    anim_print(f'Good luck on your quest {name}, stick to the path!\n')
    anim_print("          \n")
    anim_print("          \n")
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
            anim_print("making this path rather dark and weary.\n")
            anim_print("          \n")
            monsterOne()

        elif capInput == "LEFT":
            anim_print("You walk along a well used path.\n")
            anim_print("The sun shines bright, almost like the light is\n")
            anim_print("guiding your way.\n")
            anim_print("          \n")
            personOne()

        elif capInput == "BACKWARD":
            anim_print("Adventurers must face their fears, choose a direction.\n")
            anim_print("          \n")

        elif capInput == "ESCAPE":
            anim_print("You have chosen to escape\n")
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
            anim_print("You have chosen to escape\n")
            anim_print("          \n")
            quit()

        else:
            print("Please choose a direction\n")

def monsterTwo():
    attitude= random.randrange(0,1)
    if attitude == 0:
        # Initial Friendly response from Monster 2
        anim_print("In the grass you spot what seems to be\n")
        anim_print("a large purple monster laying in the grass.\n")
        anim_print("His head pops up as he hears the grass shift.\n")
        anim_print("'A human! These woods are not safe for someone like you!\n")
        anim_print("Perhaps you should turn back?'\n")
        anim_print("          \n")

        responses = ["1","2"]
        userInput = ""
        while userInput not in responses:
            anim_print("Option 1: 'I do appreciate the concern, but I can handle myself.'\n")
            anim_print("          \n")

            anim_print("Option 2: 'No monster is going to tell me what to do,\n")
            anim_print("Get out of my way!'\n")
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
                anim_print("with responses like that.'\n")
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
            anim_print("You have chosen to escape\n")
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
                anim_print("'Should probably get home to the wife though.\n")
                anim_print("She really hates me being out here this late.'\n")
                anim_print("He slowly picks up his bag and starts down\n")
                anim_print("the path you just walked up.\n")
                anim_print("          \n")
                ending.append("0")

            elif capInput == "2":
                # Responding to Hostile Player
                anim_print("The shopkeep looks at you with surprise.\n")
                anim_print("He grabs his bag in silence and quickly pushes past you\n")
                anim_print("back down the road.\n")
                anim_print("          \n")
                ending.append("1")

            else:
                anim_print("Please choose an option\n")


    elif attitude == 1:
        # Hostile response from Person 1
        anim_print("On the path ahead, you can see a dark-hooded\n")
        anim_print("figure rifling through a small bag and throwing\n")
        anim_print("contents to the ground with disappointment.\n")
        anim_print("He notices you as you come up the path.\n")
        anim_print("The man quickly throws the bag onto his shoulder and grabs out a knife.\n")
        anim_print("'Watch it there buddy, I know how to use this thing!'\n")
        anim_print("          \n")

        responses = ["1","2"]
        userInput = ""
        while userInput not in responses:
            anim_print("OPTION 1: You quickly raise your hands up to show you are unarmed\n")
            anim_print("'I'm just on a walk, there is no need for violence please.'\n")
            anim_print("          \n")

            anim_print("OPTION 2: You place your hand on your hip where your concealed knife is.\n")
            anim_print("'You think I'm afraid of some petty thief?\n")
            anim_print("Get out of my way you pathetic scum!\n")
            anim_print("          \n")
    
            anim_print("How will you respond?\n")
            anim_print("1 or 2?\n")

            userInput = input()
            capInput = userInput
            if capInput == "1":
                # Responding to Friendly Player
                anim_print("The man slowly lowers the knife, but still remains cautious\n")
                anim_print("'Just forget you saw me, I was never here!'\n")
                anim_print("The man slowly backs away and sprints\n")
                anim_print("to the trees, escaping your sight.\n")
                anim_print("          \n")
                ending.append("0")

            elif capInput == "2":
                # # Responding to Hostile Player
                anim_print("The man's eyes widen as he considers how serious and threatening you are.\n")
                anim_print("He drops the bag and knife and sprints as fast as he can\n")
                anim_print("to the trees to escape from your sight.\n")
                anim_print("          \n")
                ending.append("1")

            else:
                anim_print("Please choose an option\n")

    direction = ["RIGHT", "LEFT", "BACKWARD", "ESCAPE"]
    userInput = ""
    while userInput not in direction:
        anim_print("There are multiple paths up ahead.\n")
        anim_print("Which way would you like to go?\n")
        anim_print("Right, Left, Backward, Escape\n")
        userInput = input()
        capInput = userInput.upper()
        if capInput == "RIGHT":
            anim_print("You walk along a very dense path, crowded with weeds, grass, and shrubbery.\n")
            anim_print("          \n")
            personTwo()

        elif capInput == "LEFT":
            anim_print("You walk on an often traversed path.\n")
            anim_print("All the grass has been stepped on and flattened to the ground.\n")
            anim_print("          \n")
            monsterTwo()

        elif capInput == "BACKWARD":
            anim_print("There is nothing back that direction for you.\n")
            anim_print("Please choose another direction\n")

        elif capInput == "ESCAPE":
            anim_print("You have chosen to escape\n")
            quit()
        else:
            anim_print("Please choose a direction\n")

def personTwo():
    attitude= random.randrange(0,1)
    if attitude == 0:
        # Friendly response from Person 2
        anim_print("As you move through the dense forest you spot a familiar face.\n")
        anim_print("It just happens to be one of your old teachers\n")
        anim_print(f"'Well if it isn't the one and only {name}.'\n")
        anim_print("Fancy seeing you in a place like this!'\n")
        anim_print("          \n")

        responses = ["1","2"]
        userInput = ""
        while userInput not in responses:
            anim_print("OPTION 1: 'Its so nice to see you again!\n")
            anim_print("What are you doing all the way out here?'\n")
            anim_print("          \n")

            anim_print("OPTION 2: 'It is quite an interesting place.\n")
            anim_print("'I unfortunately do not have any time to chit-chat.'\n")
            anim_print("          \n")

            anim_print("How will you respond?\n")
            anim_print("1 or 2?\n")
            anim_print("          \n")

            userInput = input()
            capInput = userInput
            if capInput == "1":
                # Friendly response from Player
                anim_print("'I was actually just on my evening hike to get some exercise in.\n")
                anim_print("It seems that I have been out for awhile!\n")
                anim_print("I think its about time for me to head home for dinner.'\n")
                anim_print(f"'Have a wonderful evening {name}, see you around!'\n")
                anim_print("          \n")
                ending.append("0")

            elif capInput == "2":
                # Hostile response from Player
                anim_print("The man looks rather taken aback by your response.\n")
                anim_print("He quickly fixes his face to respond.\n")
                anim_print("'I'm very sorry to be such an inconvenience to you.\n")
                anim_print("I will go ahead and get out of your way.'\n")
                anim_print("The man slumps his shoulders and quickly moves past you\n")
                anim_print("back down the path.\n")
                anim_print("          \n")
                ending.append("1")

            else:
                anim_print("Please choose an option\n")


    elif attitude == 1:
        # Hostile response from PERSON 2
        anim_print("As you walk along the path, you see a woman\n")
        anim_print("in the middle of a clearing.\n")
        anim_print("She appears to be holding a book and talking to herself.\n")
        anim_print("As you approach, the air thickens and\n")
        anim_print("a faint glow swirls around the women.\n")
        anim_print("You stop at the edge of the clearing so as not to get too close.\n")
        anim_print("The women whips her head around quickly with an annoyed look\n")
        anim_print("'Who are you and what are you doing here?'\n")
        anim_print("          \n")

        responses = ["1","2"]
        userInput = ""
        while userInput not in responses:
            anim_print("OPTION 1: 'I didn't mean to interupt\n")
            anim_print("I was just passing though on the path'\n")
            anim_print("          \n")

            anim_print("OPTION 2: 'That is none of your business'\n")
            anim_print("          \n")
    
            anim_print("How will you respond?\n")
            anim_print("1 or 2?\n")

            userInput = input()
            capInput = userInput
            if capInput == "1":
                # Friendly response from Player
                anim_print("Shes gazes at you for a moment longer\n")
                anim_print("before turning back towards her book.\n")
                anim_print("She waves a hand in the air as if to shoo you away.\n")
                anim_print("'Please move away from the clearing,\n")
                anim_print("you are blocking my energies.'\n")
                ending.append("0")

            elif capInput == "2":
                # Hostile response from Player
                anim_print("Her gaze hardens as though she were\n")
                anim_print("trying to turn you to stone.\n")
                anim_print("'Leave the clearing before turn you into a toad!'\n")
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
        anim_print("You approach the cottage cautiously but also curiously.\n")

        anim_print("As you reach to knock on the door, it swings open by itself.\n")
        anim_print("You hear a come voice from inside\n")

        anim_print(f"'Please, come join me {name}. Make sure to take your shoes off please.\n")

        anim_print("You take your shoes off and shuffle into the home.\n")

        anim_print("As you proceed towards the living room, one of the chairs\n")
        anim_print("turns towards you, beckoning you to sit. And you ablige the chair.\n")

        anim_print("The other chair in the living room contains a middle aged man, with a pipe in his mouth\n")

        anim_print(f"'I've been watching you closely {name}.'\n")
        anim_print("'Ever since you entered this forest I have keenly observed\n")
        anim_print("to see what kind of person you are.'\n")

        anim_print("'I believe you are different, perhaps one of a kind.'\n")
        anim_print("If you would indulge me, I have a surprise of sorts for you.'\n")

        anim_print("You nod to the man, unsure of what surprises may be contained in\n")
        anim_print("a house of this size.\n")

        anim_print("The man stands up from his chair and waddles over to a table\n")
        anim_print("where a small leather bag sits atop it.\n")
        anim_print("He swiftly grabs the bag and carries it back, gingerly handing it to you.\n")

        anim_print("'This bag is now yours, take good care of it and all it contains.'\n")
        anim_print("'It is getting late as well, I will see you out.'\n")
        anim_print(f"The man guides you to the door and slowly closes it behind you. 'Good luck {name}!'\n")

        anim_print("You open the bag to investigate the contents.\n")
        anim_print("This is a magical bag! And one that contains mountains of gold!.\n")
        anim_print("You smile from ear to ear\n")
        anim_print("          \n")
        quit()

    elif ending == ["1","1"]:
        #BAD ENDING
        anim_print("You approach the cottage cautiously but also curiously.\n")

        anim_print("As you reach to knock on the door, it swings open by itself.\n")
        anim_print("The cottage looks like it has been abandoned.\n")
        anim_print("Furniture is covered with tarps and a thick\n")
        anim_print("layer of dust covers the interior.\n")
        anim_print("It seems as though all this was for nothing.\n")
        quit()
        
    else:
        #DECENT ENDING
        anim_print("You approach the cottage cautiously but also curiously.\n")

        anim_print("As you reach to knock on the door, it swings open by itself.\n")
        anim_print("You hear a come voice from inside\n")

        anim_print(f"'Please, come join me {name}. Make sure to take your shoes off please.\n")

        anim_print("You take your shoes off and shuffle into the home.\n")

        anim_print("As you proceed towards the living room, one of the chairs\n")
        anim_print("turns towards you, beckoning you to sit. And you ablige the chair.\n")

        anim_print("The other chair in the living room contains a middle aged man, with a pipe in his mouth\n")

        anim_print(f"'I've been watching you closely {name}.'\n")
        anim_print("'Ever since you entered this forest I have keenly observed\n")
        anim_print("to see what kind of person you are.'\n")

        anim_print("'It seems as though you are a normal human, which is to be expected.'\n")
        anim_print("'I can tell you would like to do the right thing\n")
        anim_print("but certain situations seem to sway your moral compass.'\n")
        anim_print("'I implore you to do some soul searching\n")
        anim_print("and return to me when you have strengthened your resolve.'\n")
        quit()

def main():
    running = True
    while running:
        introScene()

if __name__ == "__main__":
    #pressing escape to stop text adventure
    keyboard.hook(exit_on_key('esc'))
    # setting up for the ending calculation
    global ending
    ending = []
    pygame.mixer.init()
    pygame.mixer.music.load('ForestSounds.mp3')
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.2)
    main()