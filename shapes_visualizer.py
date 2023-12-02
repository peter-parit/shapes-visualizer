import pygame as pg
from pygame.locals import *
from sys import exit
import numpy as np
from math import sin, cos
import shapes

pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen_size = (700, 500)
size = 80
transX = 250
transY = 250

pg.display.set_caption('3D Shapes Visualizer')
screen = pg.display.set_mode(screen_size)
axis_legend = pg.image.load("images/axis.png").convert_alpha()
axis_legend = pg.transform.scale(axis_legend, (200, 100))
font = pg.font.Font('freesansbold.ttf', 16)
keys = font.render('[a]: show/hide axes, [arrow keys]: rotate plane, [s]: change shape', True, WHITE, BLACK)
keys_rect = keys.get_rect()
clock = pg.time.Clock()


# matrices
def calc_r(x, y, z):
    rx = np.array([
        [1, 0, 0],
        [0, cos(x), -sin(x)],
        [0, sin(x), cos(x)]
    ])
    ry = np.array([
        [cos(y), 0, sin(y)],
        [0, 1, 0],
        [-sin(y), 0, cos(y)]
    ])
    rz = np.array([
        [cos(z), -sin(z), 0],
        [sin(z), cos(z), 0],
        [0, 0, 1]
    ])
    r = np.matmul(np.matmul(rz, ry), rx)  # R(z)R(y)R(x)
    return r


# starting angle values for coordinate plane
thX = 3
thY = 0
thZ = 1.8

s = 1  # shapes
axis = -1  # axis
changeZ, changeX = 0, 0
speedZ, speedX = 0, 0
myCube = shapes.Cube()
myPrism = shapes.Prism()
while True:
    screen.fill(BLACK)
    screen.blit(keys, (10, 475))
    screen.blit(axis_legend, (470, 20))

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pg.quit()
                exit()
            elif event.key == K_LEFT:
                speedZ += 0.003
            elif event.key == K_RIGHT:
                speedZ -= 0.003
            elif event.key == K_DOWN:
                speedX -= 0.003
            elif event.key == K_UP:
                speedX += 0.003
            elif event.key == K_a:
                axis = -axis  # toggle axis
            elif event.key == K_s:  # change shapes
                s = -s
        elif event.type == KEYUP:
            if event.key in (K_LEFT, K_RIGHT):
                speedZ = 0
            elif event.key in (K_UP, K_DOWN):
                speedX = 0

    # speed
    changeX += speedX
    changeZ += speedZ

    # decelerate
    if speedX == 0:
        changeX *= 0.9
    if speedZ == 0:
        changeZ *= 0.9

    # update angle
    thZ += changeZ
    thX += changeX

    # update rotation
    locations = []
    R = calc_r(thX, thY, thZ)
    if s == 1:
        shapes.update(myCube, R, locations, screen)
    else:
        shapes.update(myPrism, R, locations, screen)

    # axis
    if axis == 1:
        shapes.show_axis(R, screen)

    pg.display.update()
    clock.tick(60)
