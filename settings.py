import pygame

surface_x = 896
surface_y = 504
resolution_x = 1280
resolution_y = 720
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Q*cat")
icon = pygame.image.load("assets/icon.png")  # Cat icon created by Freepik
pygame.display.set_icon(icon)
surface = pygame.Surface((896, 504))  # Create game surface with actual game resolution

edge_size = 37
map_size = 7
