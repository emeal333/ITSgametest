import pygame, math

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1000 - 1
SCREEN_HEIGHT = 600 - 1

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wild Goose Chase")

#load images
sky = pygame.image.load("backgrounds/sunset.png")
bg = pygame.image.load("backgrounds/skyline.png")
bg_width = bg.get_width()
bg_rect = bg.get_rect()

scroll = 0

def draw_background(scroll):
    #define game variables
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
    
    #draw sky
    screen.blit(sky, (0, 0))

    #draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
        bg_rect.x = i * bg_width + scroll
        pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)

#game loop
run = True
while run:

    clock.tick(FPS)

    draw_background(scroll)

    # scroll background
    scroll -= 5

    # reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
