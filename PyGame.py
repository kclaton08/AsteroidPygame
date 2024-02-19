import pygame 
import math
import random

# Initialize the pygame
pygame.init()

# Create the screen and setting global vars
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
color = (0,0,0)
font = pygame.font.Font(None, 50)
bg_scroll = 0
bulletVelo = 0
bulletList = []
asteroidList = []
click_start = 0 

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship(1).png')
bg = pygame.image.load('space2.png')
bulletLeft = pygame.Surface((4, 4))
asteroid = pygame.image.load('asteroid.png')
bulletRight = bulletLeft
bulletLeft.fill('Red')
pygame.display.set_icon(icon)
playerImg = pygame.image.load('spaceship(1).png')
# Setting the background and the player icon 
#text = font.render('ASTEROIDS', False, 'White')
start_button = pygame.image.load('start.png')
screen.blit(start_button, (150, 50))

#Creating player class with the attribute to shoot when the spacebar is pressed
class player: 
    def __init__(self, posX, posY): 
        self.posX = posX
        self.posY = posY 

    def move_player(posX, posY): 
        screen.blit(playerImg, (posX, posY))
        pygame.display.update()
    
    def shoot(playerPosX, playerPosY):
        screen.blit(bulletLeft, (playerPosX, playerPosY))
        screen.blit(bulletRight, (playerPosX + 27, playerPosY))
        bulletVelo = -10 
        #Creating a list of all bullets that are currently on the screen, setting a base velocity of -10 
        bulletList.append([playerPosX, playerPosY, bulletVelo])
        return bulletList

spaceship = player(400, 450)
      
class bullet: 
    def __init__(self, bulletX, bulletY): 
        self.bulletX = bulletX
        self.bulletY = bulletY 
    
    def bulletmove(bulletList): 
        for i in range(len(bulletList)): 
            bulletList[i][2] += -10 
            bulletVelo = bulletList[i][2]
            if bulletList[i][0] + bulletVelo <= -800:
                bulletList.remove(bulletList[i])
                bulletVelo = 0
                break
            else:
                screen.blit(bulletLeft, (bulletList[i][1], bulletList[i][0] + bulletVelo))
                screen.blit(bulletRight, (bulletList[i][1] + 27, bulletList[i][0] + bulletVelo))  
        
class asteroid: 
    def __init__(self, asteroidX, asteroidY): 
        self.asteroid = pygame.image.load('asteroid.png')
        self.asteroidX = asteroidX
        self.asteroidY = asteroidY 
    
    def generate_asteroid(started, randIntX, asteroidY): 
        if started == 1 and randIntX == 1: 
            asteroidX = randIntX
            asteroidY = 0 
            asteroidVelo = 2
            asteroid = pygame.image.load('asteroid.png')
            screen.blit(asteroid, (asteroidX, asteroidY))
            asteroidList.append([asteroidX, asteroidY, asteroidVelo])
            return asteroidList
        
    def move_asteroid(asteroid, asteroidList, asteroidVelo, i): 
        screen.blit(asteroid, (asteroidList[i][0], asteroidVelo))

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.blit(bg, (0, 0))
    screen.blit(bg, (0, 0 + bg_scroll))
    screen.blit(bg, (0, -600 + bg_scroll))
    bg_scroll += 5
    if bg_scroll > 600: 
        bg_scroll = 0
    if click_start == 0:
        screen.blit(start_button, (285, 300))
    for i in range(len(asteroidList)):
        asteroidList[i][2] += .99
        asteroidVelo = asteroidList[i][2] 
        if asteroidVelo >= 600: 
            asteroidList.remove(asteroidList[i])
            asteroidVelo = 0
            break
        else:
            asteroid.move_asteroid(asteroid, asteroidList, asteroidVelo, i)
    #screen.blit(text, (260, 200))
    screen.blit(playerImg, (spaceship.posX, spaceship.posX))
    
    if len(bulletList) >= 1: 
        bullet.bulletmove(bulletList)
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        else:
            # Check for the keystrokes
            if event.type == pygame.MOUSEBUTTONDOWN: 
                x, y = pygame.mouse.get_pos()
                print(x, y)
                print(click_start)
                if x in range(285, 540) and y in range(300, 360):
                    click_start = 1 
                    print(click_start)
            if click_start == 1: 
                keys = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN: 
                    if keys[pygame.K_LEFT]:
                        spaceship.posX  += -20
                        player.move_player(spaceship.posX, spaceship.posY)
                    elif keys[pygame.K_RIGHT]:
                        spaceship.posX  += 20
                        player.move_player(spaceship.posX, spaceship.posY)
                    elif keys[pygame.K_UP]:
                        spaceship.posY -= 20
                        player.move_player(spaceship.posX, spaceship.posY)
                    elif keys[pygame.K_DOWN]: 
                        spaceship.posY += 20
                        player.move_player(spaceship.posX, spaceship.posY)
                    if event.key == pygame.K_SPACE:
                        bulletInstance = player.shoot(spaceship.posX, spaceship.posY)
    asteroidTest = round(random.randint(0, 100))
    asteroid.generate_asteroid(click_start, round(random.randint(0,800)),0)       
    pygame.display.update()

    

 
 