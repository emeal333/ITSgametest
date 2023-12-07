import pygame
import math

cleardesertSky = [pygame.image.load("weather/clearD.png")]
clearcitySky = [pygame.image.load("weather/clearC.png")]
clearfieldsSky = [pygame.image.load("weather/clearF.png")]
clearbeachSky = [pygame.image.load("weather/clearB.png")]

cloudydesertSky = [pygame.image.load("weather/cloudyD.png")]
cloudycitySky = [pygame.image.load("weather/cloudyC.png")]
cloudyfieldsSky = [pygame.image.load("weather/cloudyF.png")]
cloudybeachSky = [pygame.image.load("weather/cloudyB.png")]

sunnydesertSky = [pygame.image.load("weather/sunnyD.png")]
sunnycitySky = [pygame.image.load("weather/sunnyC.png")]
sunnyfieldsSky = [pygame.image.load("weather/sunnyF.png")]
sunnybeachSky = [pygame.image.load("weather/sunnyB.png")]

rainydesertSky = [pygame.image.load("weather/rainyD1.png"),
                   pygame.image.load("weather/rainyD2.png")]
rainycitySky = [pygame.image.load("weather/rainyC1.png"),
                 pygame.image.load("weather/rainyC2.png")]
rainyfieldsSky = [pygame.image.load("weather/rainyF1.png"),
                   pygame.image.load("weather/rainyF2.png")]
rainybeachSky = [pygame.image.load("weather/rainyB1.png"),
                  pygame.image.load("weather/rainyB2.png")]

snowydesertSky = [pygame.image.load("weather/snowyD1.png"),
                   pygame.image.load("weather/snowyD2.png")]
snowycitySky = [pygame.image.load("weather/snowyC1.png"),
                 pygame.image.load("weather/snowyC2.png")]
snowyfieldsSky = [pygame.image.load("weather/snowyF1.png"),
                   pygame.image.load("weather/snowyF2.png")]
snowybeachSky = [pygame.image.load("weather/snowyB1.png"),
                  pygame.image.load("weather/snowyB2.png")]

backgroundsList = {"cleardesertSky" : cleardesertSky,
                    "clearcitySky" : clearcitySky,
                    "clearfieldsSky" : clearfieldsSky,
                    "clearbeachSky" : clearbeachSky,
                    "cloudydesertSky" : cloudydesertSky,
                    "cloudycitySky" : cloudycitySky,
                    "cloudyfieldsSky" : cloudyfieldsSky,
                    "cloudybeachSky" : cloudybeachSky,
                    "sunnydesertSky" : sunnydesertSky,
                    "sunnycitySky" : sunnycitySky,
                    "sunnyfieldsSky" : sunnyfieldsSky,
                    "sunnybeachSky" : sunnybeachSky,
                    "rainydesertSky" : rainydesertSky,
                    "rainycitySky" : rainycitySky,
                    "rainyfieldsSky" : rainyfieldsSky,
                    "rainybeachSky" : rainybeachSky,
                    "snowydesertSky" : snowydesertSky,
                    "snowycitySky" : snowycitySky,
                    "snowyfieldsSky" : snowyfieldsSky,
                    "snowybeachSky" : snowybeachSky}

background = pygame.image.load("backgrounds/fields.png")
currentSkyList = clearfieldsSky
sky = pygame.image.load("weather/clearF.png")
skyRect = sky.get_rect()
skyNumber = 0
bg_name = "fields"
bg_width = background.get_width()
bg_rect = background.get_rect()
tiles = 0
frame = 0

def draw_background(scroll, screen, SCREEN_WIDTH):
    """
    Handles the different scrolling backgrounds.

    Params:
        scroll (int): The value that controls bg scroll.
    """

    global tiles
    global skyNumber
    global currentSkyList
    global background
    global sky
    global bg_rect
    global bg_width
    global skyRect
    global frame

    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1

    if frame >= 15:
        frame = 0
        # draw sky
        skyNumber += 1
    
        if skyNumber >= len(currentSkyList):
            skyNumber = 0
            
        sky = currentSkyList[skyNumber]
        skyRect = sky.get_rect()
    else:
        frame += 1
        
    screen.blit(sky, (0, 0))

    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(background, (i * bg_width + scroll, 0))

def set_sky(w):
    global currentSkyList
    global backgroundsList
    global bg_name

    currentSkyList = backgroundsList[w + bg_name + "Sky"]

def set_background(bg):
    global bg_name
    global background
    global bg_width
    global bg_rect

    # load bg image
    bg_name = bg
    background = pygame.image.load("backgrounds/" + bg + ".png")
    """The background setting image."""
    bg_width = background.get_width()
    """The width of the bg."""
    bg_rect = background.get_rect()
    """The rect object of the bg."""
