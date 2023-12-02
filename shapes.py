# Parit Vacharaskunee 6580209
# Project for ICCS 205 Numerical Methods, MUIC
import pygame as pg
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

size = 80
transX = 250
transY = 250


class Cube:
    def __init__(self):
        # https://www.malinc.se/math/linalg/rotatecubeen.php
        self.vertices = size * np.array([
            [1, 1, 1],
            [1, -1, 1],
            [-1, -1, 1],
            [-1, 1, 1],
            [1, 1, -1],
            [1, -1, -1],
            [-1, -1, -1],
            [-1, 1, -1]
        ])
        self.lines = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 4),
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7)
        ]


class Prism:
    def __init__(self):
        self.vertices = size * np.array([
            [1, 1, 0],
            [1, -1, 0],
            [-1, -1, 0],
            [-1, 1, 0],
            [1, 0, 1],
            [-1, 0, 1]
        ])
        self.lines = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
            (4, 5),
            (4, 1),
            (4, 0),
            (5, 2),
            (5, 3)
        ]


def update(shape, r, locations, screen):
    for point in shape.vertices:
        rotation = np.matmul(point, r)
        px, py = rotation[0], rotation[2]

        locations.append((px + transX, py + transY))
        pg.draw.circle(screen, RED, ((px + transX), py + transY), 6)

    for pos in shape.lines:
        pg.draw.line(screen, WHITE, locations[pos[0]], locations[pos[1]], 4)


def show_axis(r, screen):  # recheck coordinates
    locations = []
    points = size * np.array([
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2],
        [0, 0, 0]
    ])
    lines = [
        (3, 0),
        (3, 1),
        (3, 2)
    ]
    colors = [RED, GREEN, BLUE]
    i = 0
    for point in points:
        rotation = np.matmul(point, r)
        px, py = rotation[0], rotation[2]

        locations.append((px + transX, py + transY))

    for pos in lines:
        pg.draw.line(screen, colors[i], locations[pos[0]], locations[pos[1]], 4)
        i += 1
