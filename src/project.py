import pygame

def main():
    pygame.init()
    pygame.display.set_caption('Character')
    resolution=(800,600)
    screen=pygame.display.set_mode(resolution)
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        #Game Logic:
        #Render and Display
        screen.fill('Green')
        pygame.flip()
    pygame.quit()


if __name__ == "__main__":
    main()