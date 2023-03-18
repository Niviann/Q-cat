import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1600, 900))

running = True
clock = pygame.time.Clock()

pygame.display.set_caption("Q*cat")
icon = pygame.image.load('assets/icon.png') #Cat icons created by Freepik
pygame.display.set_icon(icon)

surface = pygame.Surface((736/2, 414/2)) #Create game surface with actual game resolution

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    a = 37
    x = 100
    y = 120
    
    pygame.draw.polygon(surface, 'gray', [(x - 0.5*a*math.sqrt(3),y+0.5*a), (x - 0.5*a*math.sqrt(3), y+1.5*a), (x , y+2*a), (x ,y+a)])
    pygame.draw.polygon(surface, 'blue', [(x,y),(x + 0.5*a*math.sqrt(3),y+0.5*a),(x,y+a),(x - 0.5*a*math.sqrt(3),y+0.5*a)])
    pygame.draw.polygon(surface, 'yellow', [(x + 0.5*a*math.sqrt(3),y+0.5*a), (x + 0.5*a*math.sqrt(3), y+1.5*a), (x , y+2*a), (x ,y+a)])

    x = x +a*math.sqrt(3)

    pygame.draw.polygon(surface, 'gray', [(x - 0.5*a*math.sqrt(3),y+0.5*a), (x - 0.5*a*math.sqrt(3), y+1.5*a), (x , y+2*a), (x ,y+a)])
    pygame.draw.polygon(surface, 'blue', [(x,y),(x + 0.5*a*math.sqrt(3),y+0.5*a),(x,y+a),(x - 0.5*a*math.sqrt(3),y+0.5*a)])
    pygame.draw.polygon(surface, 'yellow', [(x + 0.5*a*math.sqrt(3),y+0.5*a), (x + 0.5*a*math.sqrt(3), y+1.5*a), (x , y+2*a), (x ,y+a)])



    x = x + a*math.sqrt(3)

    pygame.draw.polygon(surface, 'gray', [(x - 0.5*a*math.sqrt(3),y+0.5*a), (x - 0.5*a*math.sqrt(3), y+1.5*a), (x , y+2*a), (x ,y+a)])
    pygame.draw.polygon(surface, 'blue', [(x,y),(x + 0.5*a*math.sqrt(3),y+0.5*a),(x,y+a),(x - 0.5*a*math.sqrt(3),y+0.5*a)])
    pygame.draw.polygon(surface, 'yellow', [(x + 0.5*a*math.sqrt(3),y+0.5*a), (x + 0.5*a*math.sqrt(3), y+1.5*a), (x , y+2*a), (x ,y+a)])

    x = 100 + 0.5*a*math.sqrt(3)
    y= y-1.5*a
    pygame.draw.polygon(surface, 'gray', [(x - 0.5*a*math.sqrt(3),y+0.5*a), (x - 0.5*a*math.sqrt(3), y+1.5*a), (x , y+2*a), (x ,y+a)])
    pygame.draw.polygon(surface, 'blue', [(x,y),(x + 0.5*a*math.sqrt(3),y+0.5*a),(x,y+a),(x - 0.5*a*math.sqrt(3),y+0.5*a)])
    pygame.draw.polygon(surface, 'yellow', [(x + 0.5*a*math.sqrt(3),y+0.5*a), (x + 0.5*a*math.sqrt(3), y+1.5*a), (x , y+2*a), (x ,y+a)])

    x = x + a*math.sqrt(3)
    pygame.draw.polygon(surface, 'gray', [(x - 0.5*a*math.sqrt(3),y+0.5*a), (x - 0.5*a*math.sqrt(3), y+1.5*a), (x , y+2*a), (x ,y+a)])
    pygame.draw.polygon(surface, 'blue', [(x,y),(x + 0.5*a*math.sqrt(3),y+0.5*a),(x,y+a),(x - 0.5*a*math.sqrt(3),y+0.5*a)])
    pygame.draw.polygon(surface, 'yellow', [(x + 0.5*a*math.sqrt(3),y+0.5*a), (x + 0.5*a*math.sqrt(3), y+1.5*a), (x , y+2*a), (x ,y+a)])

    x = 100 + a*math.sqrt(3)
    y= y-1.5*a
    pygame.draw.polygon(surface, 'gray', [(x - 0.5*a*math.sqrt(3),y+0.5*a), (x - 0.5*a*math.sqrt(3), y+1.5*a), (x , y+2*a), (x ,y+a)])
    pygame.draw.polygon(surface, 'blue', [(x,y),(x + 0.5*a*math.sqrt(3),y+0.5*a),(x,y+a),(x - 0.5*a*math.sqrt(3),y+0.5*a)])
    pygame.draw.polygon(surface, 'yellow', [(x + 0.5*a*math.sqrt(3),y+0.5*a), (x + 0.5*a*math.sqrt(3), y+1.5*a), (x , y+2*a), (x ,y+a)])
    screen.blit(pygame.transform.scale(surface,(1600, 900)), (0,0))

    #Game scale



    pygame.display.flip()
    clock.tick(60)

pygame.quit()