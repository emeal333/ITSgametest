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