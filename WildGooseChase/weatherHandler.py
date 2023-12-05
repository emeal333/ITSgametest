import pygame
import backgroundsHandler

stormy = pygame.image.load("weather/stormy.png")

rainydesertList = [pygame.image.load("weather/rainD1.png"),
                   pygame.image.load("weather/rainD2.png")]
rainycityList = [pygame.image.load("weather/rainC1.png"),
                 pygame.image.load("weather/rainC2.png")]
rainyfieldsList = [pygame.image.load("weather/rainF1.png"),
                   pygame.image.load("weather/rainF2.png")]
rainybeachList = [pygame.image.load("weather/rainB1.png"),
                  pygame.image.load("weather/rainB2.png")]

snowydesertList = [pygame.image.load("weather/snowD1.png"),
                   pygame.image.load("weather/snowD2.png")]
snowycityList = [pygame.image.load("weather/snowC1.png"),
                 pygame.image.load("weather/snowC2.png")]
snowyfieldsList = [pygame.image.load("weather/snowF1.png"),
                   pygame.image.load("weather/snowF2.png")]
snowybeachList = [pygame.image.load("weather/snowB1.png"),
                  pygame.image.load("weather/snowB2.png")]

weathersList = {"rainydesertList" : rainydesertList,
               "rainycityList" : rainycityList,
               "rainyfieldsList" : rainyfieldsList,
               "rainybeachList" : rainybeachList,
               "snowydesertList" : snowydesertList,
               "snowycityList" : snowycityList,
               "snowyfieldsList" : snowyfieldsList,
               "snowybeachList" : snowybeachList}

currentWeatherList = ""
weather = ""
w_name = "clear"
weatherNumber = 0
weatherRect = ""
frame = 0

def drawWeatherFront(screen):
    global currentWeatherList
    global weather
    global w_name
    global weatherNumber
    global weatherRect
    global frame

    if w_name == "snowy" or w_name == "rainy":
        if frame >= 15:
            frame = 0
            weatherNumber += 1
        
            if weatherNumber >= len(currentWeatherList):
                weatherNumber = 0
                    
            weather = currentWeatherList[weatherNumber]
            weatherRect = weather.get_rect()

        else:
            frame += 1
    
        screen.blit(weather, (0, 0))

def setWeather(w):
    global w_name
    global currentWeatherList
    global weathersList
    global weather

    w_name = w
    if w_name == "snowy" or w_name == "rainy":
        currentWeatherList = weathersList[w + backgroundsHandler.bg_name + "List"]
    weather = currentWeatherList[weatherNumber]

    backgroundsHandler.set_sky(w)
