def main ():
    from core.const import __version__, __author__, CLEAR_COLOR, GRID_SIZE, SCREEN_SIZE, HELP_MENU, DEFAULT_FONT

    from core.formats import OBJ
    from core.graphics.elements import GraphicsWorker

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
    '''.format(__version__, __author__)



    pygame.init()
    viewport = (SCREEN_SIZE [0], SCREEN_SIZE [1])
    pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
    #screen.openglblit (DEFAULT_FONT.render("Hello There", 1, (10, 10, 10)), (0, 0))
    pygame.display.set_caption('PyModel')

    glLightfv(GL_LIGHT0, GL_POSITION, (-40, 200, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    if len(sys.argv) >= 2:
        obj = OBJ(sys.argv[1], swapyz=True)


    clock = pygame.time.Clock()

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    width, height = viewport
    gluPerspective(90.0, width / float(height), 1, 100.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)



    glClearColor(CLEAR_COLOR[0], CLEAR_COLOR[1], CLEAR_COLOR[2], CLEAR_COLOR[3])

    rx, ry = (0, 0)
    tx, ty = (0, 0)
    rz = 0
    zpos = 5
    rotate = move  = modelLook = False
    modelZPlus = modelZMinus = False


    while True:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit ()
            elif e.type == KEYDOWN and e.key == K_ESCAPE:
                sys.exit(0)
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 4:
                    zpos = max(1, zpos - 1)
                elif e.button == 5:
                    zpos += 1
                elif e.button == 1:
                    rotate = True
                elif e.button == 3:
                    move = True
            elif e.type == MOUSEBUTTONUP:
                if e.button == 1:
                    rotate = False
                elif e.button == 3:
                    move = False
            elif e.type == MOUSEMOTION:
                i, j = e.rel
                if rotate:
                    rx += i
                    ry += j
                if move:
                    tx += i
                    ty -= j
            elif e.type == KEYDOWN:
                if e.key == K_c:
                    GraphicsWorker.createCube ()
                elif e.key == K_LEFT:
                    modelZPlus = True
                elif e.key == K_RIGHT:
                    modelZMinus = True
                elif e.key == K_UP:
                    ry += 1
                elif e.key == K_DOWN:
                    ry -= 1
                elif e.key == K_r:
                    rx = ry = rz = tx = ty = 0
                    zpos = 5
                elif e.key == K_h:
                    for i in HELP_MENU:
                        print '{0} - {1}'.format (i, HELP_MENU [i])
                elif e.key == K_TAB:
                    modelLook = not modelLook
            elif e.type == KEYUP:
                if e.key == K_LEFT:
                    modelZPlus = False
                elif e.key == K_RIGHT:
                    modelZMinus = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

      #  GraphicsWorker.drawText ((0, 0, 0), 'Hello', DEFAULT_FONT)

        if modelZMinus:
            rz -= 1
        elif modelZPlus:
            rz += 1

        if modelLook:
            rz += 0.5

        glTranslate(tx / 20., ty / 20., - zpos)
        glRotate(ry, 1, 0, 0)
        glRotate(rx, 0, 1, 0)
        glRotate (rz, 0, 0, 1)
        if len (sys.argv) >= 2:
            glCallList (obj.gl_list)



        GraphicsWorker.drawGrid (GRID_SIZE [0], GRID_SIZE [1])


        pygame.display.flip()
