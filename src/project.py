import pygame
import time

def anim_print(text):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(0.1)

def main():
    pygame.init()
    pygame.display.set_caption('Background')
    resolution=(1500,1000)
    screen=pygame.display.set_mode(resolution)
    imp = pygame.image.load("Darkwoods.jpeg")
    screen.blit(imp,(0,0))
    pygame.display.flip()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                pygame.KEYDOWN == pygame.K_ESCAPE
                running = False  
        #Game Logic:
        #Render and Display
    pygame.quit()


if __name__ == "__main__":
    #anim_print("Hello there brave adventurer!\n")
    #anim_print("You have decided to brave the dark and mysterious woods today\n")
    #anim_print("What is your name traveler?\n")
    #name = input()
    #anim_print(f'Good luck {name}, travel safely!\n')
    main()