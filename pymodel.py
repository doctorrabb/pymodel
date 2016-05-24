from core.config import parse

__version__ = '0.1'
__author__ = 'DOCTOR_RABB'
__configpath__ = 'config.json'
__config__ = parse (__configpath__)

from core.formats import OBJ

import sys, pygame
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *

print '''
      _____         __  __           _      _
     |  __ \       |  \/  |         | |    | |
     | |__) |   _  | \  / | ___   __| | ___| |
     |  ___/ | | | | |\/| |/ _ \ / _` |/ _ \ |
     | |   | |_| | | |  | | (_) | (_| |  __/ |
     |_|    \__, | |_|  |_|\___/ \__,_|\___|_|
             __/ |
            |___/

    Version: {0}
    Developer: {1}
'''.format (__version__, __author__)
 
pygame.init ()
viewport = (800,600)
hx = viewport[0]/2
hy = viewport[1]/2
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
 
glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glShadeModel(GL_SMOOTH)           
 
obj = OBJ (sys.argv[1], swapyz=True)
 
clock = pygame.time.Clock()
 
glMatrixMode(GL_PROJECTION)
glLoadIdentity ()
width, height = viewport
gluPerspective(90.0, width/float(height), 1, 100.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_MODELVIEW)

glClearColor(__config__ ['clearColor'][0], __config__ ['clearColor'][1], __config__ ['clearColor'][2], __config__ ['clearColor'][3])
 
rx, ry = (0,0)
tx, ty = (0,0)
zpos = 5
rotate = move = False

while True:
    clock.tick(30)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN and e.key == K_ESCAPE:
            print 'Good Bye!'
            sys.exit (0)
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 4: zpos = max(1, zpos-1)
            elif e.button == 5: zpos += 1
            elif e.button == 1: rotate = True
            elif e.button == 3: move = True
        elif e.type == MOUSEBUTTONUP:
            if e.button == 1: rotate = False
            elif e.button == 3: move = False
        elif e.type == MOUSEMOTION:
            i, j = e.rel
            if rotate:
                rx += i
                ry += j
            if move:
                tx += i
                ty -= j
 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
 
    glTranslate(tx/20., ty/20., - zpos)
    glRotate(ry, 1, 0, 0)
    glRotate(rx, 0, 1, 0)
    glCallList(obj.gl_list)

    pygame.display.set_caption ('PyModel')
    pygame.display.flip()
