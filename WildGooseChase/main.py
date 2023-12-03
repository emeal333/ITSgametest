import pygame
import weatherHandler
import backgroundsHandler
import spritesHandler
import collectablesHandler
import obstaclesHandler
import random
import button
import weatherH
from pygame import mixer

pygame.init()

global clock
clock = pygame.time.Clock()
"""The Clock object to be used to control framerate."""
global FPS
FPS = 60
"""The framerate."""

global SCREEN_WIDTH
SCREEN_WIDTH = 1000
"""The width of the window."""
global SCREEN_HEIGHT
SCREEN_HEIGHT = 600
"""The height of the window."""

# saved high score
with open('max_score.txt', 'r') as file:
    content = file.read()
    max_score = int(content)

# score during game
score = int(0)

# initiate music & sound effect
mixer.init()
mixer.music.load('sound/game_music.wav')
mixer.music.set_volume(0.1)
mixer.music.play()
collected_sound = mixer.Sound('sound/collected.wav')
crash_sound = mixer.Sound('sound/crash.wav')

# create game window and icon
global screen 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
"""The game window."""
pygame.display.set_caption("Wild Goose Chase")
pygame_icon = pygame.image.load('menus/goose_icon.png')
"""The window icon."""
pygame.display.set_icon(pygame_icon)

# --- pause info ---
# draws text for pause display during gameplay
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# --- obstacle info ---

obstacles = []

collectables = []

obstaclesHandler.randomize()
obstacle_hitbox = obstaclesHandler.obstacle_sprite.get_rect()

hitbox_color = (255, 0, 0)

collectable_spacing = 300

movement_speed = 6

spriteNumber = 0
frame = 0

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= movement_speed
        if self.rect.x < -self.rect.width - 50:
            obstacles.pop()

    def draw(self, SCREEN):
        global spriteNumber
        global frame

        if frame >= 15:
            frame = 0
            spriteNumber += 1
        
            if spriteNumber >= len(obstaclesHandler.obstacle):
                spriteNumber = 0
        
            self.image = pygame.transform.scale(
                obstaclesHandler.obstacle[spriteNumber], (100, 100))
        else:
            frame += 1

        SCREEN.blit(self.image, self.rect)

# class is made for each type of obstacle
class LowOb(Obstacle):
    def __init__(self, image, goose_spawn_y):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = goose_spawn_y + 50
        self.index = 0

class HighOb(Obstacle):
    def __init__(self, image, goose_spawn_y):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = goose_spawn_y - (spritesHandler.sprite.get_height())


# --- collectable info ---

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

class Item(Collectable):
    def __init__(self, image, goose_spawn_y, collectable_type):
        super().__init__(image, collectable_type)
        self.type = collectable_type
        self.rect.y = goose_spawn_y + 50

        #make item smaller
        scaled_width = 80
        scaled_height = 80
        self.image = pygame.transform.scale(self.image, (scaled_width, scaled_height))

    def get_rect(self):
        return self.image.get_rect(topleft=(self.rect.x, self.rect.y))


# --- game loop ---

def main():
    global movement_speed
    global obstacles
    global collectables
    global hitbox_color
    global collectable_spacing
    global obstacle_hitbox
    global score
    global max_score

    # load menu art
    title = pygame.image.load("menus/title.png")
    """The game's title image."""

    # load game-over art
    game_over = pygame.image.load("menus/game_over.png")
    """The game's game-over image."""


    # --- create module vars ---
    weatherH.checkWeather()
    background = backgroundsHandler.bg_name
    weather = weatherHandler.w_name


    # --- buttons ---
    # load start button
    start_img = pygame.image.load('buttons/start_button.png').convert_alpha()
    start_button = button.Button(SCREEN_WIDTH // 2 - start_img.get_width() // 2, 430,
                                start_img, 1)

    # load try_again button
    restart_img = pygame.image.load('buttons/restart_button.png').convert_alpha()
    restart_button = button.Button(SCREEN_WIDTH // 2 - restart_img.get_width() // 2, 430,
                                   restart_img, 1)

    # load quit button
    quit_img = pygame.image.load('buttons/quit_button.png').convert_alpha()
    quit_button = button.Button(650, 430, quit_img, 1)

    # load skins button
    skins_img = pygame.image.load('buttons/skins_button.png').convert_alpha()
    skins_button = button.Button(SCREEN_WIDTH - 650 - skins_img.get_width(), 430, skins_img, 1)

    # load back button
    back_img = pygame.image.load('buttons/back_button.png').convert_alpha()
    back_button = button.Button(5, 430, back_img, 1)
    
    # load hard button
    hard_img = pygame.image.load('buttons/hard_difficulty_button.png').convert_alpha()
    hard_button = button.Button(SCREEN_WIDTH // 2 - start_img.get_width() // 2, 375,
                                hard_img, 1)

    # load normal button
    normal_img = pygame.image.load('buttons/normal_difficulty_button.png').convert_alpha()
    normal_button = button.Button(SCREEN_WIDTH // 2 - start_img.get_width() // 2, 225,
                                  normal_img, 1)

    # load easy button
    easy_img = pygame.image.load('buttons/easy_difficulty_button.png').convert_alpha()
    easy_button = button.Button(SCREEN_WIDTH // 2 - start_img.get_width() // 2, 75,
                                easy_img, 1)

    # load resume button
    resume_img = pygame.image.load("buttons/resume_button.png").convert_alpha()
    resume_button = button.Button(50, 430, resume_img, 1)

    # load next button
    next_img = pygame.image.load("buttons/next_button.png").convert_alpha()
    next_button = button.Button(SCREEN_WIDTH - next_img.get_width() - 5, 430,
                                next_img, 1)
    
    # load city button
    city_img = pygame.image.load("buttons/city_button.png").convert_alpha()
    city_button = button.Button(SCREEN_WIDTH // 9 * 4.5, 75, city_img, 1)
    
    # load desert button
    desert_img = pygame.image.load("buttons/desert_button.png").convert_alpha()
    desert_button = button.Button(SCREEN_WIDTH // 9 * 2.75, 225, desert_img, 1)
    
    # load beach button
    beach_img = pygame.image.load("buttons/beach_button.png").convert_alpha()
    beach_button = button.Button(SCREEN_WIDTH // 9 * 6.25, 225, beach_img, 1)
    
    # load fields button
    fields_img = pygame.image.load("buttons/fields_button.png").convert_alpha()
    fields_button = button.Button(SCREEN_WIDTH // 9 * 1.25, 75, fields_img, 1)
    
    # load default skin
    default_img = pygame.transform.scale(pygame.image.load('sprites/d1.png').convert_alpha(),
                                         (250, 250))
    default_button = button.Button(75, 50, default_img, 1)

    # load flamingo skin
    flamingo_img = pygame.transform.scale(pygame.image.load('sprites/f1.png').convert_alpha(),
                                         (250, 250))
    flamingo_button = button.Button(275, 50, flamingo_img, 1)

    # load cow skin
    cow_img = pygame.transform.scale(pygame.image.load('sprites/cw1.png').convert_alpha(),
                                         (250, 250))
    cow_button = button.Button(475, 50, cow_img, 1)

    # load santa skin
    santa_img = pygame.transform.scale(pygame.image.load('sprites/s1.png').convert_alpha(),
                                         (250, 250))
    santa_button = button.Button(675, 50, santa_img, 1)

    # load bow skin
    bow_img = pygame.transform.scale(pygame.image.load('sprites/b1.png').convert_alpha(),
                                         (250, 250))
    bow_button = button.Button(150, 225, bow_img, 1)

    # load canada skin
    canada_img = pygame.transform.scale(pygame.image.load('sprites/cn1.png').convert_alpha(),
                                         (250, 250))
    canada_button = button.Button(375, 225, canada_img, 1)

    # load paint skin
    paint_img = pygame.transform.scale(pygame.image.load('sprites/p1.png').convert_alpha(),
                                         (250, 250))
    paint_button = button.Button(600, 225, paint_img, 1)

    # define fonts for pause
    font = pygame.font.SysFont("arialblack", 40)
    small_font = pygame.font.SysFont("arialblack", 20)

    # define colours for pause
    TEXT_COL = (0, 0, 0)


    # --- jumping stuff ---
    camera_offset_x = 0
    """Value that determines how far obstacles are in relation to goose."""

    image_x = SCREEN_WIDTH // 2 - spritesHandler.sprite.get_width() // 2
    """Value that helps determine goose's x-coordinate."""
    image_y = SCREEN_HEIGHT // 2 - spritesHandler.sprite.get_height()
    """Value that helps determine goose's y-coordinate."""

    # jumping logic
    jumping = False
    ducking = False
    Y_GRAVITY = 0.5
    JUMP_HEIGHT = 16
    Y_VELOCITY = JUMP_HEIGHT

    rectangle_x = image_x + camera_offset_x - 300
    rectangle_y = image_y + SCREEN_HEIGHT + 150

    rectangle = pygame.Rect(SCREEN_WIDTH,
                        (SCREEN_HEIGHT // 2) - spritesHandler.sprite.get_height(), 50, 50)

    scroll = 0
    """The value that controls bg scroll.."""

    menu = "title"

    # --- game-state vars ---
    running = True
    """The value of if the program is running."""
    game_started = False
    """The value of if the game has started."""
    show_instructions = True

    while running:
        if not game_started:
            # menus
            if menu == "title":
                # title screen

                # update weather
                weatherH.checkWeather()
                weather = weatherHandler.w_name

                backgroundsHandler.set_background(background)
                backgroundsHandler.set_sky(weather)
                backgroundsHandler.draw_background(scroll, screen, SCREEN_WIDTH)
                weatherHandler.setWeather(weather)
                weatherHandler.drawWeatherFront(screen)

                # scroll title screen
                scroll -= movement_speed

                # reset scroll
                if abs(scroll) > backgroundsHandler.bg_width:
                    scroll = 0

                # add storm filter
                if weatherHandler.w_name == "rainy":
                    screen.blit(weatherHandler.stormy, (0, 0))

                screen.blit(title,
                            (SCREEN_WIDTH // 2 - title.get_width() // 2, 20))
                
                draw_text(f'High Score: {max_score}', font, TEXT_COL, 20, 0)

                if (start_button.draw(screen)):
                    menu = "difficulties"

                if (skins_button.draw(screen)):
                    menu = "skins"

                if (quit_button.draw(screen)):
                    running = False

                screen.blit(skins_img, (SCREEN_WIDTH - 650 - skins_img.get_width(), 430))
                screen.blit(quit_img, (650, 430))
                screen.blit(start_img, (SCREEN_WIDTH // 2 - start_img.get_width() // 2, 430))

            elif menu == "skins":
                backgroundsHandler.draw_background(scroll, screen, SCREEN_WIDTH)
                weatherHandler.drawWeatherFront(screen)

                # scroll title screen
                scroll -= movement_speed

                # reset scroll
                if abs(scroll) > backgroundsHandler.bg_width:
                    scroll = 0

                # add storm filter
                if weatherHandler.w_name == "rainy":
                    screen.blit(weatherHandler.stormy, (0, 0))

                draw_text("Unlock New Skins With Points!", font, TEXT_COL, 25, 10)

                if (default_button.draw(screen)):
                    spritesHandler.setSkin("default")
                if (flamingo_button.draw(screen) and max_score >= 10):
                    spritesHandler.setSkin("flamingo")
                if (cow_button.draw(screen) and max_score >= 20):
                    spritesHandler.setSkin("cow")
                if (santa_button.draw(screen) and max_score >= 30):
                    spritesHandler.setSkin("santa")
                if (bow_button.draw(screen) and max_score >= 40):
                    spritesHandler.setSkin("bow")
                if (canada_button.draw(screen) and max_score >= 50):
                    spritesHandler.setSkin("canada")
                if (paint_button.draw(screen) and max_score >= 60):
                    spritesHandler.setSkin("paint")

                screen.blit(default_img, (75, 50))
                draw_text("Default: 0p", small_font, TEXT_COL, 75 + 50, 80)
                screen.blit(flamingo_img, (275, 50))
                draw_text("Flamingo: 10p", small_font, TEXT_COL, 275 + 50, 80)
                screen.blit(cow_img, (475, 50))
                draw_text("Cow: 20p", small_font, TEXT_COL, 475 + 70, 80)
                screen.blit(santa_img, (675, 50))
                draw_text("Santa: 30p", small_font, TEXT_COL, 675 + 50, 80)
                screen.blit(bow_img, (150, 225))
                draw_text("Fancy: 40p", small_font, TEXT_COL, 150 + 50, 265)
                screen.blit(canada_img, (375, 225))
                draw_text("Canada: 50p", small_font, TEXT_COL, 375 + 50, 265)
                screen.blit(paint_img, (600, 225))
                draw_text("Painter: 60p", small_font, TEXT_COL, 600 + 50, 265)

                if (back_button.draw(screen)):
                    menu = "title"

                screen.blit(back_img, (5, 430))

            elif menu == "difficulties":
                # title screen
                backgroundsHandler.draw_background(scroll, screen, SCREEN_WIDTH)
                weatherHandler.drawWeatherFront(screen)

                # scroll title screen
                scroll -= movement_speed

                # reset scroll
                if abs(scroll) > backgroundsHandler.bg_width:
                    scroll = 0

                # add storm filter
                if weatherHandler.w_name == "rainy":
                    screen.blit(weatherHandler.stormy, (0, 0))

                draw_text("Select a Difficulty:", font, TEXT_COL, 25, 10)

                if (easy_button.draw(screen)):
                    movement_speed = 5
                if (normal_button.draw(screen)):
                    movement_speed = 6
                if (hard_button.draw(screen)):
                    movement_speed = 9

                screen.blit(easy_img, (SCREEN_WIDTH // 2 - start_img.get_width() // 2, 75))
                screen.blit(normal_img, (SCREEN_WIDTH // 2 - start_img.get_width() // 2, 225))
                screen.blit(hard_img, (SCREEN_WIDTH // 2 - start_img.get_width() // 2, 375))

                if (back_button.draw(screen)):
                    menu = "title"

                if (next_button.draw(screen)):
                    menu = "levels"

                screen.blit(back_img, (5, 430))
                screen.blit(next_img, (SCREEN_WIDTH - next_img.get_width() - 5, 430))
                
            elif menu == "levels":
                # title screen
                backgroundsHandler.draw_background(scroll, screen, SCREEN_WIDTH)
                weatherHandler.drawWeatherFront(screen)

                # scroll title screen
                scroll -= movement_speed

                # reset scroll
                if abs(scroll) > backgroundsHandler.bg_width:
                    scroll = 0

                # add storm filter
                if weatherHandler.w_name == "rainy":
                    screen.blit(weatherHandler.stormy, (0, 0))

                draw_text("Select a Level:", font, TEXT_COL, 25, 10)

                # level options
                if (fields_button.draw(screen)):
                    backgroundsHandler.set_background("fields")
                    backgroundsHandler.set_sky(weather)
                if (desert_button.draw(screen)):
                    backgroundsHandler.set_background("desert")
                    backgroundsHandler.set_sky(weather)
                if (city_button.draw(screen)):
                    backgroundsHandler.set_background("city")
                    backgroundsHandler.set_sky(weather)
                if (beach_button.draw(screen)):
                    backgroundsHandler.set_background("beach")
                    backgroundsHandler.set_sky(weather)

                screen.blit(fields_img, (SCREEN_WIDTH // 9 * 1.25, 75))
                screen.blit(desert_img, (SCREEN_WIDTH // 9 * 2.75, 225))
                screen.blit(city_img, (SCREEN_WIDTH // 9 * 4.5, 75))
                screen.blit(beach_img, (SCREEN_WIDTH // 9 * 6.25, 225))
            
                collectablesHandler.setCollectable()

                if (back_button.draw(screen)):
                    menu = "difficulties"

                if (next_button.draw(screen)):
                    if show_instructions:
                        menu = "instructions"
                    else:
                        game_started = True

                screen.blit(back_img, (5, 430))
                screen.blit(next_img, (SCREEN_WIDTH - next_img.get_width() - 5, 430))

            elif menu == "instructions":
                backgroundsHandler.draw_background(scroll, screen, SCREEN_WIDTH)
                weatherHandler.drawWeatherFront(screen)

                # scroll title screen
                scroll -= movement_speed

                # reset scroll
                if abs(scroll) > backgroundsHandler.bg_width:
                    scroll = 0

                # add storm filter
                if weatherHandler.w_name == "rainy":
                    screen.blit(weatherHandler.stormy, (0, 0))

                draw_text("Press SPACE to Pause!", font, TEXT_COL, 25, 10)
                draw_text("Press W to Jump!", font, TEXT_COL, 25, 60)
                draw_text("Press S to Duck!", font, TEXT_COL, 25, 110)

                if (back_button.draw(screen)):
                    menu = "levels"

                if (next_button.draw(screen)):
                    show_instructions = False
                    game_started = True

                screen.blit(back_img, (5, 430))
                screen.blit(next_img, (SCREEN_WIDTH - next_img.get_width() - 5, 430))

            elif menu == "game over":
                screen.fill((0, 0, 0))
                screen.blit(game_over,
                            (SCREEN_WIDTH // 2 - game_over.get_width() // 2, 0))
                
                # update high score
                if score > max_score:
                    max_score = score
                    with open('max_score.txt', 'w') as file:
                        file.write(str(f'{max_score}'))
                score = 0

                # clear obstacles and collectables on screen
                for collectable in collectables:
                    collectables.pop()
                for obstacle in obstacles:
                    obstacles.pop()

                if quit_button.draw(screen):
                    running = False

                if restart_button.draw(screen):
                    game_started = True    

                if (back_button.draw(screen)):
                    menu = "title"

                screen.blit(back_img, (5, 430))
                screen.blit(quit_img, (650, 430))
                screen.blit(restart_img, (SCREEN_WIDTH // 2 - start_img.get_width() // 2, 430))

            elif menu == "pause":
                backgroundsHandler.draw_background(scroll, screen, SCREEN_WIDTH)
                weatherHandler.drawWeatherFront(screen)

                # add storm filter
                if weatherHandler.w_name == "rainy":
                    screen.blit(weatherHandler.stormy, (0, 0))

                screen.blit(weatherHandler.stormy, (0, 0))

                if quit_button.draw(screen):
                    running = False
                if resume_button.draw(screen):
                    game_started = True

            # event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(FPS)
            
        elif game_started:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                jumping = True
                ducking = False

            if keys[pygame.K_s]:
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

            camera_offset_x = screen.get_width() // 2 - image_x - spritesHandler.sprite.get_width() // 2

            # draw scrolling background
            backgroundsHandler.draw_background(scroll, screen, SCREEN_WIDTH)

            # scroll background
            scroll -= movement_speed

            # reset scroll
            if abs(scroll) > backgroundsHandler.bg_width:
                scroll = 0

            # create goose rectangle
            goose_rect = spritesHandler.spriteRect.move(
                image_x + camera_offset_x - 300,
                image_y + SCREEN_HEIGHT + 175)
            
            rectangle = spritesHandler.sprite.get_rect(
                    topleft=(image_x + camera_offset_x - 300,
                              image_y + SCREEN_HEIGHT + 175))
            
            # check if goose is currently jumping or ducking
            if ducking:
                rectangle_x = image_x + camera_offset_x - 300
                rectangle_y = image_y + SCREEN_HEIGHT + 200
            else:
                rectangle_x = image_x + camera_offset_x - 300
                rectangle_y = image_y + SCREEN_HEIGHT + 175

            # draw goose
            spritesHandler.drawSprite(screen, rectangle, jumping, ducking)

            if obstacle_hitbox.left == rectangle.left:
                score += 1
            
            goose_hitbox = pygame.Rect(rectangle_x + 20, rectangle_y + 40, 80, 60)
            # pygame.draw.rect(screen, hitbox_color, goose_hitbox, 2)

            goose_rect = goose_hitbox.copy()

            if len(obstacles) == 0:
                obstaclesHandler.randomize()
                if (obstaclesHandler.obstacle == obstaclesHandler.pigeonSprites or
                        obstaclesHandler.obstacle == obstaclesHandler.waspSprites or
                        obstaclesHandler.obstacle == obstaclesHandler.bluebirdSprites):
                    obstacles.append(HighOb(obstaclesHandler.obstacle_sprite, SCREEN_HEIGHT - 50))
                else:
                    obstacles.append(LowOb(obstaclesHandler.obstacle_sprite, SCREEN_HEIGHT - 175))

            for obstacle in obstacles:
                obstacle.draw(screen)
                obstacle.update()

                obstacle_hitbox = pygame.Rect(obstacle.rect.x + 25, obstacle.rect.y + 25, 
                                              60, 60)
                
                # draw hitbox on obstacles
                # pygame.draw.rect(screen, hitbox_color, obstacle_hitbox, 2)

            if len(collectables) == 0:
                    collectables.append(Item(collectablesHandler.collectable, 
                                            SCREEN_HEIGHT - 400,
                                            collectable_type=0))

            for collectable in collectables:
                collectable.draw(screen)
                collectable.update()

                collectable_hitbox = pygame.Rect(collectable.rect.x + 22, collectable.rect.y + 22, 40, 40)

                # draw hitboxes for collectables
                # pygame.draw.rect(screen, hitbox_color, collectable_hitbox, 2)

                if goose_rect.colliderect(collectable_hitbox):
                    # Collision with collectables
                    mixer.Sound.play(collected_sound)
                    score += 1
                    collectables.remove(collectable)

            # show current score
            draw_text(f"Score: {score}", font, TEXT_COL, SCREEN_WIDTH - 250, 0)
            
            weatherHandler.drawWeatherFront(screen)

            # add dark storm filter if needed
            if weatherHandler.w_name == "rainy":
                screen.blit(weatherHandler.stormy, (0, 0))

            # check if game over
            if goose_rect.colliderect(obstacle_hitbox):
                mixer.Sound.play(crash_sound)
                menu = "game over"
                game_started = False

            # Pause Menu
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_started = False
                        menu = "pause"
                if event.type == pygame.QUIT:
                    running = False

        pygame.display.update()

    pygame.quit()

main()