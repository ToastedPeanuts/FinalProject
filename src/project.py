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
        anim_print("Options: Right, Left, Backward, Escape\n")
        userInput = input()
        capInput = userInput.upper()
        if capInput == "RIGHT":
            anim_print("You have chosen to go right\n")
            anim_print("          \n")
            monsterOne()
        elif capInput == "LEFT":
            anim_print("You have chosen to go left\n")
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
        # Friendly response
        anim_print(f"Welcome to the woods {name}!\n")
        anim_print("What are you doing so deep in these dangerous woods?\n")
        anim_print("          \n")
        responses = ["1","2"]
        userInput = ""
        while userInput not in responses:
            anim_print("Option 1: Just peacefully adventuring through\n")
            anim_print("Option 2: None of your business monster!\n")
            anim_print("How will you respond?\n")
            anim_print("1 or 2?\n")
            userInput = input()
            capInput = userInput
            if capInput == "1":
                anim_print(f"Well on your way {name}, travel safely!\n")
            elif capInput == "2":
                anim_print("*GROWL* Better move along before you lose your life human.\n")
            else:
                anim_print("Please choose and option\n")
    elif attitude == 1:
        # Hostile response
        print("Hostile\n")
    direction = ["RIGHT", "LEFT", "BACKWARD", "ESCAPE"]
    userInput = ""
    while userInput not in direction:
        anim_print("Options: Right, Left, Backward, Escape\n")
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
            anim_print("Adventurers must face their fears, choose a direction\n")
            anim_print("          \n")
        elif capInput == "ESCAPE":
            anim_print("You have chosen to escape")
            anim_print("          \n")
            quit()
        else:
            print("Please choose a direction\n")

def monsterTwo():
    print("--Text to add--\n")
    print("--Text to add--\n")
    print("--Text to add--\n")
    direction = ["FORWARD", "BACKWARD", "ESCAPE"]
    userInput = ""
    while userInput not in direction:
        print("Options: Forward, Backward, Escape\n")
        userInput = input()
        capInput = userInput.upper()
        if capInput == "FORWARD":
            print("You have chosen to go forward\n")
            lastPerson()
        elif capInput == "BACKWARD":
            print("Adventurers must face their fears, choose a direction\n")
        elif capInput == "ESCAPE":
            print("You have chosen to escape")
            quit()
        else:
            print("Please choose a direction\n")

def personOne():
    print("--Text to add--\n")
    print("--Text to add--\n")
    print("--Text to add--\n")
    direction = ["RIGHT", "LEFT", "BACKWARD", "ESCAPE"]
    userInput = ""
    while userInput not in direction:
        print("Options: Right, Left, Backward, Escape\n")
        userInput = input()
        capInput = userInput.upper()
        if capInput == "RIGHT":
            print("You have chosen to go right\n")
            personTwo()
        elif capInput == "LEFT":
            print("You have chosen to go left\n")
            monsterTwo()
        elif capInput == "BACKWARD":
            print("Adventurers must face their fears, choose a direction\n")
        elif capInput == "ESCAPE":
            print("You have chosen to escape")
            quit()
        else:
            print("Please choose a direction\n")

def personTwo():
    print("--Text to add--\n")
    print("--Text to add--\n")
    print("--Text to add--\n")
    direction = ["FORWARD", "BACKWARD", "ESCAPE"]
    userInput = ""
    while userInput not in direction:
        print("Options: Forward, Backward, Escape\n")
        userInput = input()
        capInput = userInput.upper()
        if capInput == "FORWARD":
            print("You have chosen to go forward\n")
            lastPerson()
        elif capInput == "BACKWARD":
            print("Adventurers must face their fears, choose a direction\n")
        elif capInput == "ESCAPE":
            print("You have chosen to escape")
            quit()
        else:
            print("Please choose a direction\n")

def lastPerson():
    print("--Text to add--\n")

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
    anim_print("Hello there brave adventurer!\n")
    anim_print("You have decided to venture through\n")
    anim_print("the dark and mysterious woods today.\n")
    anim_print("There is rumoured to be a magician that will reward you with riches!\n")
    anim_print("What is your name traveler?\n")
    global name
    name = input()
    anim_print(f'Good luck {name}, travel safely!\n')
    anim_print("          \n")
    anim_print("          \n")
    keyboard.hook(exit_on_key('esc'))
    main()