import pygame
import time
import random

def introScene():
    print("You come to a grove in the middle of the forest\n")
    print("There are two paths to take: Right or Left?\n")
    print("Which path will you take?\n")
    direction = ["Right", "Left", "Backward", "Escape"]
    userInput = ""
    while userInput not in direction:
        print("Right or Left?\n")
        userInput = input()
        if userInput == "Right":
            #monsterOne()
            print("You have chosen to go right\n")
        elif userInput == "Left":
            #personOne()
            print("You have chosen to go left\n")
        elif userInput == "Backward":
            print("Adventurers must face their fears, choose a direction\n")
        elif userInput == "Escape":
            quit()
        else:
            print("Please choose a direction\n")

#def monsterOne():

#def monsterTwo():

#def personOne():

#def personTwo():

#def lastPerson():

def draw_text(screen,text,font,text_col,x,y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))

def anim_print(text):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(0.1)

def main():
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
    #anim_print("Hello there brave adventurer!\n")
    #anim_print("You have decided to brave the dark and mysterious woods today\n")
    #anim_print("What is your name traveler?\n")
    #name = input()
    #anim_print(f'Good luck {name}, travel safely!\n')
    main()