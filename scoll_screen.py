import pygame
import math

pygame.init()

clock = pygame.time.Clock()
FPS = 60

WIDTH = 1200
HEIGHT = 800

# create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Scroll")


# load image
bg = pygame.image.load("bg-1.bmp").convert()
bg_width = bg.get_width()

# define game variables
scroll = 0
titles = math.ceil(bg_width)
print(titles)

# game loop
run = True
while run:

    clock.tick(FPS)

    # draw scrolling backround
    for i in range(0, titles):
        screen.blit(bg, (i * bg_width + scroll, 0))

    # scroll backround
    scroll -= 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
