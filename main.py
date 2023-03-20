import pygame
import math
from settings import *

pygame.init()
running = True
clock = pygame.time.Clock()

segments = []


def mapSegment(edge_size, segment_object):
    x = segment_object.pos_x
    y = segment_object.pos_y
    a = edge_size
    pygame.draw.polygon(
        surface,
        segment_object.color1,
        [
            (x, y),
            (x + math.sqrt(3) / 2 * a, y + a / 2),
            (x, y + a),
            (x - math.sqrt(3) / 2 * a, y + a / 2),
        ],
    )
    pygame.draw.polygon(
        surface,
        segment_object.color2,
        [
            (x, y + a),
            (x + math.sqrt(3) / 2 * a, y + a / 2),
            (x + math.sqrt(3) / 2 * a, y + a * 1.5),
            (x, y + 2 * a),
        ],
    )
    pygame.draw.polygon(
        surface,
        segment_object.color3,
        [
            (x, y + a),
            (x - math.sqrt(3) / 2 * a, y + a / 2),
            (x - math.sqrt(3) / 2 * a, y + a * 1.5),
            (x, y + 2 * a),
        ],
    )


class Field:
    visited = False
    deathly = False
    pos_x = 0
    pos_y = 0
    color1 = "red"
    color2 = "blue"
    color3 = "green"


temp = 0
for y in range(map_size):
    for x in range(y):
        segments.append(Field())
        segments[temp].pos_x = (
            surface_x / 2
            - (y - 1) * edge_size * math.sqrt(3) / 2
            + x * edge_size * math.sqrt(3)
        )
        segments[temp].pos_y = (y - 1) * 3 / 2 * edge_size + 2 * edge_size
        temp = temp + 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Map Generation
    for x in range(len(segments)):
        mapSegment(edge_size, segments[x])

    screen.blit(pygame.transform.scale(surface, (resolution_x, resolution_y)), (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
