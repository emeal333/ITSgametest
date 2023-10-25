import pygame, math, button

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# create game window and icon
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wild Goose Chase")
pygame_icon = pygame.image.load('menus/goose_icon.png')
pygame.display.set_icon(pygame_icon)

# load menu art
title = pygame.image.load("menus/title.png")
title = pygame.transform.scale(title, (550, 350))
game_over_png = pygame.image.load("menus/game_over.png")
game_over_png = pygame.transform.scale(game_over_png, (700, 400))

# load bg images
sky = pygame.image.load("backgrounds/sunset.png")
bg = pygame.image.load("backgrounds/skyline.png")
bg_width = bg.get_width()
bg_rect = bg.get_rect()

# load obstacles
cone = pygame.image.load("obstacles/cone.png")
cone_rect = cone.get_rect()

# load goose sprite
goose_height = 175
goose_width = 175
goose = pygame.image.load("sprites/goose_small.png")
goose = pygame.transform.scale(goose, (goose_height, goose_width))

# load buttons
start_button = pygame.image.load('menus/start_button.png').convert_alpha()
start_button_x = SCREEN_WIDTH - start_button.get_width()*2.8
start_button_y = SCREEN_HEIGHT - 175
start_button_rect = pygame.Rect(start_button_x, start_button_y, 220, 100)

camera_offset_x = 0

image_x = SCREEN_WIDTH // 2 - goose_width // 2
image_y = SCREEN_HEIGHT // 2 - goose_height

rectangle = pygame.Rect(SCREEN_WIDTH, (SCREEN_HEIGHT // 2) - goose_height, 50, 50)

movement_speed = 3

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
running = True
game_started = False
game_over = False

while running:
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_started and event.type == pygame.MOUSEBUTTONDOWN and start_button_rect.collidepoint(event.pos) and not game_over:
            game_started = True

    clock.tick(FPS)

    if game_started:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and image_y - movement_speed > 0:
            image_y -= movement_speed
        if keys[pygame.K_DOWN] and image_y + movement_speed < (SCREEN_HEIGHT //2) - 50:
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
        rect_draw_pos = cone_rect.move(camera_offset_x + 800, SCREEN_HEIGHT - 100)

        screen.blit(cone, (camera_offset_x + 1600, SCREEN_HEIGHT - 100))
        rect_draw_pos2 = cone_rect.move(camera_offset_x + 1600, SCREEN_HEIGHT - 100)

        screen.blit(goose, (image_x + camera_offset_x - 300, image_y + 300))
        goose_rect = goose.get_rect().move(image_x + camera_offset_x - 300, image_y + 300)

        if goose_rect.colliderect(rect_draw_pos) or goose_rect.colliderect(rect_draw_pos2):
            game_over = True
            movement_speed = 0
            screen.fill((255, 255, 255))
            screen.blit(game_over_png, (SCREEN_WIDTH - game_over_png.get_width()*1.2, SCREEN_HEIGHT - game_over_png.get_height()*1.3))
            
            # running = False
    else:
        screen.fill((255, 255, 255))
        screen.blit(title, (SCREEN_WIDTH - title.get_width()*1.42, 50))
        screen.blit(start_button, (start_button_x, start_button_y))

    pygame.display.update()

pygame.quit()