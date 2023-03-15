import pygame

pygame.init()

screen = pygame.display.set_mode((1600, 900))

running = True
clock = pygame.time.Clock()

pygame.display.set_caption("Q*cat")
icon = pygame.image.load('assets/icon.png') #Cat icons created by Freepik
pygame.display.set_icon(icon)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('red')
    pygame.display.flip()
    clock.tick(60)

pygame.quit()