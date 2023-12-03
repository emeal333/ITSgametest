import pygame
import backgroundsHandler

collectable = ""
collectable_width = 0
collectable_rect = 0

def setCollectable():
    global collectable
    global collectable_width
    global collectable_rect

    # select bg's corresponding collectable
    if backgroundsHandler.bg_name == "city":
        collectable = "coin"
    elif backgroundsHandler.bg_name == "fields":
        collectable = "flower"
    elif backgroundsHandler.bg_name == "beach":
        collectable = "dollar"
    else:
        collectable = "gold"

    # load collectable image
    collectable = pygame.image.load("collectables/" + collectable + ".png")
    """The collectable image."""
    collectable_width = collectable.get_width()
    """The width of the collectable."""
    collectable_rect = collectable.get_rect()
    """The rect object of the collectable."""

def drawCollectable(screen, cam_x, s_height):
    global collectable
    global collision
    global collectable_rect

    screen.blit(collectable, (cam_x + 800, s_height - 100))
    collision = collectable_rect.move(cam_x + 800, s_height - 100)