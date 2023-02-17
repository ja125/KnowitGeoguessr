import pygame
import sys
pygame.init()

size = width, height = 1536, 864
black = 0,0,0

screen = pygame.display.set_mode(size)
#map = pygame.image.load("map.png")
pin = pygame.image.load("pin.png")
ballrect = pin.get_rect()

while True: #run game
    #TODO: Load images and labels (true coordinates)
    for image in images: ##TODO: Loop over all images
        #TODO: Random sample image
        #TODO: display image
        #TODO: Display map

        #TODO: Move mechanics for pin



        pass


    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    screen.fill(black)
    screen.blit(pin, ballrect)
    pygame.display.flip()