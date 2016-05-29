'''
Default elements. Cube, grid, text and other...
'''

from OpenGL.GL import *
from core.const import *

class GraphicsWorker (object):
    @classmethod
    def drawGrid (self, cx, cy):
        _cx = cx / 2
        _cy = cy / 2

        glColor3f (128, 128, 128)

        for i in range (-_cx, cx):
            glBegin (GL_LINES)
            glVertex3f (i, _cy, 0.0)
            glVertex3f(i, -_cy, 0.0)
            glEnd ()

        for i in range(-_cy, _cy):
            glBegin(GL_LINES)
            glVertex3f(_cx, i, 0.0)
            glVertex3f(-_cx, i, 0.0)
            glEnd()

    @classmethod
    def createCube (self, EDGES=DEFAULT_CUBE_EDGES, VERTS=DEFAULT_CUBE_VERTS):

        glPushMatrix()
        glBegin (GL_POLYGON)

        for e in EDGES:
            for v in e:
                glVertex3fv (VERTS [v])

        glEnd ()
        glTranslatef(0, 0, 0)
        glTranslatef (10, 10, 10)
        glPopMatrix()

    @classmethod
    def drawText(self, position, textString, font):
        textSurface = font.render(textString, True, (255, 255, 255, 255), (0, 0, 0, 255))
        textData = pygame.image.tostring(textSurface, "RGBA", True)
        glRasterPos3d(*position)
        glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

