'''
this code just has added elements built on top of jennas main code
'''

import pygame
import math
import random
from pygame import mixer

#initiate music
mixer.init()
mixer.music.load('game_music.wav')
mixer.music.set_volume(0.2)
mixer.music.play()

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


# create game window and icon
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wild Goose Chase")
pygame_icon = pygame.image.load('goose_icon.png')
pygame.display.set_icon(pygame_icon)

# load menu art
title = pygame.image.load("title.png")
title = pygame.transform.scale(title, (550, 350))
game_over_png = pygame.image.load("game_over.png")
game_over_png = pygame.transform.scale(game_over_png, (700, 400))

# load bg images
sky = pygame.image.load("sunset.png")
bg = pygame.image.load("skyline.png")
bg_width = bg.get_width()
bg_rect = bg.get_rect()

# load obstacles
cone = pygame.image.load("cone.png")
cone_rect = cone.get_rect()
missile = pygame.image.load("missle.png")
missile_rect = missile.get_rect()
coin = pygame.image.load("coin.png")
coin_rect = coin.get_rect()

# load goose sprite
goose_height = 175
goose_width = 175
goose = pygame.image.load("goose_icon.png")
goose = pygame.transform.scale(goose, (goose_height, goose_width))
jumping_goose = pygame.image.load("jumping_goose.png")
jumping_goose = pygame.transform.scale(jumping_goose, (goose_height, goose_width))
ducking_goose = pygame.image.load("ducking.png")
ducking_goose = pygame.transform.scale(ducking_goose, (goose_height, goose_width//2))

# load buttons
start_button = pygame.image.load('start_button.png').convert_alpha()
start_button_x = SCREEN_WIDTH - start_button.get_width()*2.8
start_button_y = SCREEN_HEIGHT - 175
start_button_rect = pygame.Rect(start_button_x, start_button_y, 220, 100)

camera_offset_x = 0

image_x = SCREEN_WIDTH // 2 - goose_width // 2
image_y = SCREEN_HEIGHT // 2 - goose_height

#jumping logic
jumping = False
ducking = False
Y_GRAVITY = 0.5
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT


rectangle = pygame.Rect(SCREEN_WIDTH,
                       (SCREEN_HEIGHT // 2) - goose_height, 50, 50)

movement_speed = 5

scroll = 0

obstacles = []

collectables = []

hitbox_color = (255, 0, 0)

coin_spacing = 300

# Set up the font for displaying the score
font = pygame.font.Font(None, 36)

coins = 0

score = 0

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= movement_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)

#class is made for each type of obstacle
class Cone(Obstacle):
    def __init__(self, image, goose_spawn_y):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = goose_spawn_y + 50
        self.index = 0

class HighOb(Obstacle):
    def __init__(self, image, goose_spawn_y):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = goose_spawn_y - (goose_height)


class Collectable:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= movement_speed
        if self.rect.x < -self.rect.width:
            collectables.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)


class Coin(Collectable):
    def __init__(self, image, goose_spawn_y, collectable_type):
        super().__init__(image, collectable_type)
        self.type = collectable_type
        self.rect.y = goose_spawn_y + 50

        #make coin smaller
        scaled_width = 150
        scaled_height = 150
        self.image = pygame.transform.scale(self.image, (scaled_width, scaled_height))

    def get_rect(self):
        return self.image.get_rect(topleft=(self.rect.x, self.rect.y))



def draw_background(scr):
    '''
    handles the different backgrounds, will draw scrolling background
    :param scr:
    :return:
    '''
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
game_started = False
game_over = False

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

        # if (keys[pygame.K_UP] and image_y - movement_speed > 0):
        #     image_y -= movement_speed
        #
        # if (keys[pygame.K_DOWN] and image_y + movement_speed <
        #         (SCREEN_HEIGHT // 2) - 50):
        #     image_y += movement_speed

        if keys[pygame.K_SPACE]:
            jumping = True
            ducking = False

        if keys[pygame.K_DOWN]:
            ducking = True
        else:
            ducking = False
            #jumping = False

        if jumping:
            image_y -= Y_VELOCITY
            Y_VELOCITY -= Y_GRAVITY
            if Y_VELOCITY < -JUMP_HEIGHT:
                jumping = False
                Y_VELOCITY = JUMP_HEIGHT

        image_x += movement_speed

        camera_offset_x = screen.get_width() // 2 - image_x - goose_width // 2

        # draw scrolling background
        draw_background(scroll)

        # scroll background
        scroll -= movement_speed

        # reset scroll
        if abs(scroll) > bg_width:
            scroll = 0


        # Update goose_rect without altering its x and y position
        goose_rect = goose.get_rect().copy().move(image_x + camera_offset_x - 300, SCREEN_HEIGHT - 100 - goose.get_height())

        #different duck image blit depending on key pressed or not pressed
        if jumping:
            rectangle = jumping_goose.get_rect(topleft=(image_x + camera_offset_x - 300, image_y + 300))
            screen.blit(jumping_goose, rectangle)
        elif ducking:
            rectangle = ducking_goose.get_rect(topleft=(image_x + camera_offset_x - 300, image_y + 350))
            screen.blit(ducking_goose, rectangle)
        else:
            rectangle = goose.get_rect(topleft=(image_x + camera_offset_x - 300, image_y + 300))
            screen.blit(goose, rectangle)

        #draw hitbox on goose
        goose_hitbox = pygame.Rect(rectangle.topleft, (goose_width, goose_height))
        pygame.draw.rect(screen, hitbox_color, goose_hitbox, 2)

        goose_rect = rectangle.copy()

        if len(obstacles) == 0:
            if random.randint(0, 1) == 0:
                obstacles.append(Cone(cone, goose_spawn_y=image_y + 300))
            elif random.randint(0, 1) == 1:
                obstacles.append(HighOb(missile, goose_spawn_y=image_y + 300))

        for obstacle in obstacles:
            obstacle.draw(screen)
            obstacle.update()

            if obstacle.type == 0:  # Cone obstacle
                obstacle_hitbox = pygame.Rect(obstacle.rect.x, obstacle.rect.y, obstacle.rect.width,
                                              obstacle.rect.height)
            elif obstacle.type == 1:  # Missile obstacle
                obstacle_hitbox = pygame.Rect(obstacle.rect.x, obstacle.rect.y, obstacle.rect.width,
                                              obstacle.rect.height)
            # draw hotbox on obstacles
            obstacle_hitbox_draw = pygame.Rect(obstacle.rect.topleft, (obstacle.rect.width, obstacle.rect.height))
            pygame.draw.rect(screen, hitbox_color, obstacle_hitbox_draw, 2)

            # if not goose_rect.colliderect(obstacle_hitbox):
            #     if goose_rect.x > obstacle.rect.x + obstacle.rect.width:
            #         score += 1

            if goose_rect.colliderect(obstacle_hitbox):
                game_over = True
                movement_speed = 0
                screen.fill((255, 255, 255))
                screen.blit(game_over_png,
                            (SCREEN_WIDTH - game_over_png.get_width() * 1.2,
                             SCREEN_HEIGHT - game_over_png.get_height() * 1.3))

            if len(collectables) == 0:
                if random.randint(0, 0) == 0:
                    collectables.append(Coin(coin, goose_spawn_y=image_y, collectable_type=0))

            for collectable in collectables:
                if game_over != True:
                    collectable.draw(screen)
                    collectable.update()

                    if collectable.type == 0:
                        # hitbox is adjusted for the scaled coin image size, if we add other collectables
                        # i would need to fix it to work for other types
                        collectable_hitbox = pygame.Rect(collectable.rect.x, collectable.rect.y, 150, 150)

                    #draw hitboxed for coins
                    collectable_hitbox_draw = pygame.Rect(collectable.rect.topleft, (150, 150))
                    pygame.draw.rect(screen, hitbox_color, collectable_hitbox_draw, 2)

                    if goose_rect.colliderect(collectable_hitbox):
                        # Collision with coin
                        coins += 1  # Increase the score by 1
                        collectables.remove(collectable)

                    # if not goose_rect.colliderect(obstacle_hitbox):
                    #     if goose_rect.x > obstacle.rect.x + obstacle.rect.width:
                    #         score += 1
        for obstacle in obstacles:
            if not goose_rect.colliderect(
                    pygame.Rect(obstacle.rect.x, obstacle.rect.y, obstacle.rect.width, obstacle.rect.height)):
                if goose_rect.x > obstacle.rect.x + obstacle.rect.width:
                    score += 1

    else:
        screen.fill((255, 255, 255))
        screen.blit(title, (SCREEN_WIDTH - title.get_width()*1.42, 50))
        screen.blit(start_button, (start_button_x, start_button_y))
        # mixer.music.pause()

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))
    #coin total score in top left corner
    coin_score = font.render(f"$ {coins}", True, (255, 255, 255))
    screen.blit(coin_score, (10, 10))

    pygame.display.update()

pygame.quit()

