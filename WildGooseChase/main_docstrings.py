import pygame
import math

pygame.init()

clock = pygame.time.Clock()
"""The Clock object to be used to control framerate."""
FPS = 60
"""The framerate."""

SCREEN_WIDTH = 1000
"""The width of the window."""
SCREEN_HEIGHT = 600
"""The height of the window."""

# create game window and icon
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
"""The game window."""
pygame.display.set_caption("Wild Goose Chase")
pygame_icon = pygame.image.load('menus/goose_icon.png')
"""The window icon."""
pygame.display.set_icon(pygame_icon)

# load menu art
title = pygame.image.load("menus/title.png")
"""The game's title image."""
title = pygame.transform.scale(title, (550, 350))
game_over_png = pygame.image.load("menus/game_over.png")
"""The game's game-over image."""
game_over_png = pygame.transform.scale(game_over_png, (700, 400))

# load bg images
sky = pygame.image.load("backgrounds/sunset.png")
"""The background sky image."""
bg = pygame.image.load("backgrounds/skyline.png")
"""The background setting image."""
bg_width = bg.get_width()
"""The width of the bg."""
bg_rect = bg.get_rect()
"""The rect object of the bg."""

# load obstacles
cone = pygame.image.load("obstacles/cone.png")
"""The cone obstacle image."""
cone_rect = cone.get_rect()
"""The rect object of the cone obstacle."""

# load goose sprite
goose_height = 175
"""The height of the goose sprite."""
goose_width = 175
"""The width of the goose sprite."""
goose = pygame.image.load("sprites/goose_small.png")
"""The goose sprite image."""
goose = pygame.transform.scale(goose, (goose_height, goose_width))

# load buttons
start_button = pygame.image.load('menus/start_button.png').convert_alpha()
"""The start button image."""
start_button_x = SCREEN_WIDTH - start_button.get_width()*2.8
"""The x-position of the start button."""
start_button_y = SCREEN_HEIGHT - 175
"""The y-position of the start button."""
start_button_rect = pygame.Rect(start_button_x, start_button_y, 220, 100)
"""The rect object of the start button."""

camera_offset_x = 0
"""Value that determines how far obstacles are in relation to goose."""

image_x = SCREEN_WIDTH // 2 - goose_width // 2
"""Value that helps determine goose's x-coordinate."""
image_y = SCREEN_HEIGHT // 2 - goose_height
"""Value that helps determine goose's y-coordinate."""

movement_speed = 3
"""The value of the goose's, obstacles', and bg's speed."""

scroll = 0
"""The value that controls bg scroll.."""


def draw_background(scr):
    """
    Handles the different backgrounds, will draw scrolling backgrounds.

    Params:
        scr (int): The value that controls bg scroll.
    """
    # define game variables
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1

    # draw sky
    screen.blit(sky, (0, 0))

    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scr, 0))
        bg_rect.x = i * bg_width + scr
        pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)

# game loop


running = True
"""The value of if the program is running."""
game_started = False
"""The value of if the game has started."""
game_over = False
"""The value of if the game is over."""

while running:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if (not game_started and event.type ==
                pygame.MOUSEBUTTONDOWN and
                start_button_rect.collidepoint(event.pos) and
                not game_over):
            game_started = True

    clock.tick(FPS)

    if game_started:
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_UP] and image_y - movement_speed > 0):
            image_y -= movement_speed

        if (keys[pygame.K_DOWN] and image_y + movement_speed <
                (SCREEN_HEIGHT // 2) - 50):
            image_y += movement_speed

        image_x += movement_speed

        camera_offset_x = screen.get_width() // 2 - image_x - goose_width // 2

        # draw scrolling background
        draw_background(scroll)

        # scroll background
        scroll -= movement_speed

        # reset scroll
        if abs(scroll) > bg_width:
            scroll = 0

        screen.blit(cone, (camera_offset_x + 800, SCREEN_HEIGHT - 100))
        rect_draw_pos = cone_rect.move(camera_offset_x + 800,
                                       SCREEN_HEIGHT - 100)

        screen.blit(cone, (camera_offset_x + 1600, SCREEN_HEIGHT - 100))
        rect_draw_pos2 = cone_rect.move(camera_offset_x + 1600,
                                        SCREEN_HEIGHT - 100)

        screen.blit(goose, (image_x + camera_offset_x - 300, image_y + 300))
        goose_rect = goose.get_rect().move(image_x + camera_offset_x - 300,
                                           image_y + 300)

        if (goose_rect.colliderect(rect_draw_pos) or
                goose_rect.colliderect(rect_draw_pos2)):
            game_over = True
            movement_speed = 0
            screen.fill((255, 255, 255))
            screen.blit(game_over_png,
                        (SCREEN_WIDTH - game_over_png.get_width()*1.2,
                            SCREEN_HEIGHT - game_over_png.get_height()*1.3))

    else:
        screen.fill((255, 255, 255))
        screen.blit(title, (SCREEN_WIDTH - title.get_width()*1.42, 50))
        screen.blit(start_button, (start_button_x, start_button_y))

    pygame.display.update()

pygame.quit()
