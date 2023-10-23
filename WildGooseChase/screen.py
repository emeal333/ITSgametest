import pygame, math

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1000 - 1
SCREEN_HEIGHT = 600 - 1

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wild Goose Chase")

#load images
sky = pygame.image.load("backgrounds/sunset.png")
bg = pygame.image.load("backgrounds/skyline.png")
bg_width = bg.get_width()
bg_rect = bg.get_rect()

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
        self.goose_sprites = []
        self.goose_sprites.append(pygame.image.load('sprites/goose_run0.png'))
        self.goose_sprites.append(pygame.image.load('sprites/goose_run1.png'))
        self.goose_sprites.append(pygame.image.load('sprites/goose_run2.png'))
        self.goose_sprites.append(pygame.image.load('sprites/goose_run3.png'))
        self.goose_sprites.append(pygame.image.load('sprites/goose_run4.png'))
        self.goose_sprites.append(pygame.image.load('sprites/goose_run5.png'))
        self.goose_sprites.append(pygame.image.load('sprites/goose_run6.png'))
        self.goose_sprites.append(pygame.image.load('sprites/goose_run7.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
     
        self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def update(self,speed):
		self.current_sprite += speed
		self.image = self.sprites[int(self.current_sprite)]

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

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()

#game loop
run = True
while run:

    clock.tick(FPS)

    draw_background(scroll)

    # scroll background
    scroll -= 5

    # reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    # drawing sprites
	screen.fill((0,0,0))
	moving_sprites.draw(screen)
	moving_sprites.update(0.25)
	pygame.display.flip()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()