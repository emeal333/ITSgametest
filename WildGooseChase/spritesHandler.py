import pygame

defl = [pygame.image.load("sprites/d1.png"),
        pygame.image.load("sprites/d2.png"),
        pygame.image.load("sprites/d3.png"),
        pygame.image.load("sprites/d2.png")]
defd = [pygame.image.load("sprites/dd1.png"),
        pygame.image.load("sprites/dd2.png"),
        pygame.image.load("sprites/dd3.png"),
        pygame.image.load("sprites/dd2.png")]

flal = [pygame.image.load("sprites/f1.png"),
        pygame.image.load("sprites/f2.png"),
        pygame.image.load("sprites/f3.png"),
        pygame.image.load("sprites/f2.png")]
flad = [pygame.image.load("sprites/fd1.png"),
        pygame.image.load("sprites/fd2.png"),
        pygame.image.load("sprites/fd3.png"),
        pygame.image.load("sprites/fd2.png")]

cowl = [pygame.image.load("sprites/cw1.png"),
        pygame.image.load("sprites/cw2.png"),
        pygame.image.load("sprites/cw3.png"),
        pygame.image.load("sprites/cw2.png")]
cowd = [pygame.image.load("sprites/cwd1.png"),
        pygame.image.load("sprites/cwd2.png"),
        pygame.image.load("sprites/cwd3.png"),
        pygame.image.load("sprites/cwd2.png")]

sanl = [pygame.image.load("sprites/s1.png"),
        pygame.image.load("sprites/s2.png"),
        pygame.image.load("sprites/s3.png"),
        pygame.image.load("sprites/s2.png")]
sand = [pygame.image.load("sprites/sd1.png"),
        pygame.image.load("sprites/sd2.png"),
        pygame.image.load("sprites/sd3.png"),
        pygame.image.load("sprites/sd2.png")]

bowl = [pygame.image.load("sprites/b1.png"),
        pygame.image.load("sprites/b2.png"),
        pygame.image.load("sprites/b3.png"),
        pygame.image.load("sprites/b2.png")]
bowd = [pygame.image.load("sprites/bd1.png"),
        pygame.image.load("sprites/bd2.png"),
        pygame.image.load("sprites/bd3.png"),
        pygame.image.load("sprites/bd2.png")]

canl = [pygame.image.load("sprites/cn1.png"),
        pygame.image.load("sprites/cn2.png"),
        pygame.image.load("sprites/cn3.png"),
        pygame.image.load("sprites/cn2.png")]
cand = [pygame.image.load("sprites/cnd1.png"),
        pygame.image.load("sprites/cnd2.png"),
        pygame.image.load("sprites/cnd3.png"),
        pygame.image.load("sprites/cnd2.png")]

pail = [pygame.image.load("sprites/p1.png"),
        pygame.image.load("sprites/p2.png"),
        pygame.image.load("sprites/p3.png"),
        pygame.image.load("sprites/p2.png")]
paid = [pygame.image.load("sprites/pd1.png"),
        pygame.image.load("sprites/pd2.png"),
        pygame.image.load("sprites/pd3.png"),
        pygame.image.load("sprites/pd2.png")]

spritesList = {"defaultList" : defl, "defaultDuck" : defd,
               "flamingoList" : flal, "flamingoDuck" : flad,
               "cowList" : cowl, "cowDuck" : cowd,
               "santaList" : sanl, "santaDuck" : sand,
               "bowList" : bowl, "bowDuck" : bowd,
               "canadaList" : canl, "canadaDuck" : cand,
               "paintList" : pail, "paintDuck" : paid}

currentSkinList = defl
currentDuckList = defd
currentSkin = "default"
sprite = defl[1]
spriteNumber = 0
spriteRect = sprite.get_rect()
frame = 0

def drawSprite(screen, rectangle, jumping, ducking):
    global currentSkinList
    global currentSkin
    global sprite
    global spriteNumber
    global spriteRect
    global frame

    spriteNumber += 1
 
    if spriteNumber >= len(currentSkinList) or jumping:
        spriteNumber = 0
        
    if frame >= 10:
        frame = 0    
        if not jumping and not ducking:
                sprite = pygame.transform.scale(currentSkinList[spriteNumber],
                                                (150, 150))
        elif jumping and not ducking:
                sprite = pygame.transform.scale(pygame.image.load("sprites/" + currentSkin + "Jump.png"),
                                                (150, 150))
        else:
                sprite = pygame.transform.scale(currentDuckList[spriteNumber],
                                                (150, 150))
    else:
        frame += 1

    screen.blit(sprite, rectangle)

    spriteRect = sprite.get_rect()

def setSkin(skin):
    global currentSkinList
    global currentDuckList 
    global spritesList
    global currentSkin

    currentSkinList = spritesList[skin + "List"]
    currentDuckList = spritesList[skin + "Duck"]
    currentSkin = skin