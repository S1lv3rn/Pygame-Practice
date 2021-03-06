import pygame

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

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def gameLoop:

    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

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
        car(x,y)

        if x > display_width - car_width or x < 0:
            gameExit = True
            except Exception as e:
                raise

        pygame.display.update()

        clock.tick(50)

gameLoop()
pygame.quit()
quit()
