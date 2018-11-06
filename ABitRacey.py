import pygame
import time
import random

pygame.init()
display_width = 800
display_height = 600

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('arts/car.png')
car_width = 85

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def crash():
    messageDisplay('You Crashed')


def messageDisplay(text):
    largeTxt = pygame.font.Font('freesansbold.ttf', 90)
    TextSurf, TextRect = textObjects(text, largeTxt)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
    gameLoop()

def textObjects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def gameLoop():

    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    thingStartx = random.randrange(0, display_width)
    thingStarty = -600
    thingChange = 7
    thingWidth = 100
    thingHeight = 100
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            print(event)

        x += x_change

        gameDisplay.fill(WHITE)
        things(thingStartx,thingStarty,thingWidth,thingHeight,BLACK)
        thingStarty += thingChange
        car(x,y)

        if x > (display_width - car_width) or x < 0:
            crash()
        if thingStarty > display_height:
            thingStartx = random.randrange(0, display_width)
            thingStarty = 0 - thingHeight

        if y < thingStarty+thingHeight:
            print('y crossover')
            if x > thingStartx and x < thingStartx+thingWidth or x+car_width > thingStartx and x+car_width < thingStartx + thingWidth:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)

gameLoop()
pygame.quit()
quit()
