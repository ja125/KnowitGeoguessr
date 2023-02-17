import pygame
import sys
pygame.init()

size = width, height = 494*2, 684

screen = pygame.display.set_mode(size)
pin = pygame.image.load("pin.png")
pin = pygame.transform.scale(pin, (20, 20))
map = pygame.image.load("map2.png")
map = pygame.transform.scale(map, (494, 684))


rectangle = pin.get_rect()

WHITE = (255, 255, 255)
RED   = (255,   0,   0)
FPS = 30

rectangle_draging = False

# - mainloop -

clock = pygame.time.Clock()

running = True

while running:

    # - events -

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rectangle.collidepoint(event.pos):
                    rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle.x - mouse_x
                    offset_y = rectangle.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                rectangle_draging = False
                print("(x, y) = (" + str(rectangle.x) + ", " + str(rectangle.y) + ")")


        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                rectangle.x = mouse_x + offset_x
                rectangle.y = mouse_y + offset_y

    # - updates (without draws) -

    # empty

    # - draws (without updates) -

    #screen.fill(WHITE)
    screen.blit(map, (0,0))
    pygame.draw.rect(screen, RED, rectangle)


    #pygame.draw.rect(screen, rectangle)

    pygame.display.flip()

    # - constant game speed / FPS -

    clock.tick(FPS)

# - end -

pygame.quit()