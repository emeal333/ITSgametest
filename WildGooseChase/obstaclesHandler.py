import pygame
import backgroundsHandler
import random

coneSprites = [pygame.image.load("obstacles/cone.png")]
pigeonSprites = [pygame.image.load("obstacles/pigeon1.png"),
                 pygame.image.load("obstacles/pigeon2.png")]
ratSprites = [pygame.image.load("obstacles/rat1.png"),
              pygame.image.load("obstacles/rat2.png")]

tumbleweedSprites = [pygame.image.load("obstacles/tumbleweed.png")]
cactusSprites = [pygame.image.load("obstacles/cactus.png")]
waspSprites = [pygame.image.load("obstacles/wasp1.png"),
               pygame.image.load("obstacles/wasp2.png")]

bushSprites = [pygame.image.load("obstacles/bush.png")]
bluebirdSprites = [pygame.image.load("obstacles/bluebird1.png"),
                   pygame.image.load("obstacles/bluebird2.png")]

ballSprites = [pygame.image.load("obstacles/ball.png")]
crabSprites = [pygame.image.load("obstacles/crab1.png"),
               pygame.image.load("obstacles/crab2.png")]

col = [coneSprites, pigeonSprites, ratSprites]
dol = [tumbleweedSprites, cactusSprites, waspSprites]
fol = [bushSprites, bluebirdSprites]
bol = [ballSprites, crabSprites]

obstaclesList = {"cityObstacleList": col,
                 "desertObstacleList": dol,
                 "fieldsObstacleList": fol,
                 "beachObstacleList": bol}

currentList = fol
obstacle = bluebirdSprites
obstacle_sprite = pygame.image.load("obstacles/bluebird1.png")
obstacle_width = obstacle_sprite.get_width()
obstacle_rect = obstacle_sprite.get_rect()
collision = 0
spriteNumber = 0
frame = 0


def randomize():
    global currentList
    global obstacle
    global collision
    global obstaclesList
    global obstacle_sprite

    currentList = obstaclesList[backgroundsHandler.bg_name + "ObstacleList"]

    obstacle = random.choice(currentList)
    """The obstacle image choice."""

    obstacle_sprite = pygame.transform.scale(obstacle[0], (100, 100))


def drawObstacle(screen):
    global obstacle
    global collision
    global obstacle_rect
    global obstacle_sprite
    global obstacle_width
    global spriteNumber
    global frame

    if frame >= 10:
        frame = 0
        spriteNumber += 1

        if spriteNumber >= len(obstacle):
            spriteNumber = 0

        obstacle_sprite = pygame.transform.scale(obstacle[spriteNumber],
                                                 (150, 150))
        obstacle_width = obstacle_sprite.get_width()
        """The width of the obstacle."""
        obstacle_rect = obstacle_sprite.get_rect()
        """The rect object of the obstacle."""

        screen.blit(obstacle_sprite, obstacle_rect)
    else:
        frame += 1
