import pygame

pygame.init()

# window_width = 500
window_height = 500

screen = pygame.display.set_mode((0, window_height), pygame.FULLSCREEN)

pygame.display.set_caption("testingtesting")


img_wdth = 50
img_hght = 50
duck = pygame.image.load('duck.jpg')
duck = pygame.transform.scale(duck, (img_wdth, img_hght))

# image_x = window_width // 2
# image_y = window_height //2

# image_x = 50
# image_y = (window_height //2) - 50

image_x = screen.get_width() // 2 - img_wdth // 2
image_y = window_height // 2 - img_hght


# camera_x = 0
# camera_speed = 1
camera_offset_x = 0

movement_speed = 1

w = (255, 255, 255)
b = (0, 0, 0)

line_x1 = 0
line_y1 = window_height // 2
line_x2 = screen.get_width()
line_y2 = window_height // 2

dot_radius = 10
dot_x = 400
dot_y = 225

# def crash():
#     global dot_y
#
#     if image_y < (dot_y + dot_radius):
#
#         if ((image_x > dot_x and image_x < (dot_x + dot_radius)) or ((image_y + dot_radius) > dot_x and (image_x + dot_radius) < (dot_x + dot_radius))):
#             pygame.quit()


rectangle = pygame.Rect(50,50,50,50)


def crash():
    global running

    if (
        image_x + duck.get_width() > dot_x
        and image_x < dot_x + dot_radius
        and image_y + duck.get_height() > dot_y
        and image_y < dot_y + dot_radius
    ):
        running = False

running = True



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()



    if keys[pygame.K_LEFT] and image_x - movement_speed > 0:
        image_x -= movement_speed
        # dot_x -= movement_speed
    if keys[pygame.K_RIGHT] and image_x + movement_speed < screen.get_width():
        image_x += movement_speed
        # dot_x += movement_speed
    if keys[pygame.K_UP] and image_y - movement_speed > 0:
        image_y -= movement_speed
    if keys[pygame.K_DOWN] and image_y + movement_speed < (window_height //2) - 50:
        image_y += movement_speed

    # distance = ((image_x - dot_x) ** 2 + (image_y - dot_y) ** 2) ** 0.5
    # if distance < dot_radius:
    #     running = False

    camera_offset_x = screen.get_width() // 2 - image_x - img_wdth // 2


    # pygame.draw.circle(screen, b, (dot_x - camera_offset_x, dot_y), dot_radius)
    # dot = pygame.draw.circle(screen,200,100,100)
# dot_pos =
#     rectangle = pygame.Rect(50,50,50,50)
    rect_draw_pos = rectangle.move(camera_offset_x, 0)

    screen.fill(w)

    pygame.draw.line(screen, b, (line_x1, line_y1), (line_x2, line_y2), 2)

    pygame.draw.rect(screen, (255, 0, 0), rect_draw_pos)

    screen.blit(duck, (image_x + camera_offset_x, image_y))

    duck_rect = duck.get_rect().move(image_x + camera_offset_x, image_y)
    if duck_rect.colliderect(rect_draw_pos):
        running = False
    # if duck.get_rect().move(image_x, image_y).colliderect(rect_draw_pos):
    #     running = False

    pygame.display.update()

    # crash()



pygame.quit()






import pygame
import button

pygame.init()

# create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# game variables
game_paused = False
menu_state = "main"

# define fonts
font = pygame.font.SysFont("arialblack", 40)

# define colours
TEXT_COL = (255, 255, 255)

# load button images
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
video_img = pygame.image.load('images/button_video.png').convert_alpha()
audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()

# create button instances
resume_button = button.Button(180, -120, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(265, 400, quit_img, 1)
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# game loop
run = True
while run:

    screen.fill((202, 228, 241))

    # check if game is paused

    if game_paused == True:
        # check menu state
        if menu_state == "main":
            # draw pause screen buttons
            if resume_button.draw(screen):
                game_paused = False
            if options_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                run = False
        # check if the options menu is open
        if menu_state == "options":
            # draw the different options buttons
            if video_button.draw(screen):
                print("Video Settings")
            if audio_button.draw(screen):
                print("Audio Settings")
            if keys_button.draw(screen):
                print("Change Key Bindings")
            if back_button.draw(screen):
                menu_state = "main"
    else:
        draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
