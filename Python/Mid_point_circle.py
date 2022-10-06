from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(0, 500, 0, 500)


def CirclePlotPoints(x_centre, y_centre, x, y):
    glVertex2i(x_centre + x, x_centre + y)
    glVertex2i(x_centre - x, y_centre + y)
    glVertex2i(x_centre + x, y_centre - y)
    glVertex2i(x_centre - x, y_centre - y)
    glVertex2i(x_centre + y, y_centre + x)
    glVertex2i(x_centre - y, y_centre + x)
    glVertex2i(x_centre + y, y_centre - x)
    glVertex2i(x_centre - y, y_centre - x)


def MidPointCircleDraw(x_centre, y_centre, r):
    x = 0
    y = r

    CirclePlotPoints(x_centre, y_centre, x, y)

    D = 1 - r

    glColor3f(0.0, 1.0, 0.5)
    glPointSize(3.0)
    glBegin(GL_POINTS)

    while x <= y:

        if D < 0:
            D = D + 2 * x + 1

        else:
            y -= 1
            D = D + 2 * (x - y) + 1

        CirclePlotPoints(x_centre, y_centre, x, y)
        x += 1

    glEnd()
    glFlush()


def main():
    choice = 0
    while choice != -1:
        choice = input(
            "Please Choose \n\t1. Plot a Circle Using MidPoint Algorithm\n\t2. Exit\n"
        )
        if int(choice) == 1:
            x = int(input("\nEnter center:\n\tx: "))
            y = int(input("\n\ty: "))
            r = int(input("\nRadius: "))
            print("starting window....")
            glutInit(sys.argv)
            glutInitDisplayMode(GLUT_RGB)
            glutInitWindowSize(500, 500)
            glutInitWindowPosition(0, 0)
            glutCreateWindow("Plot Circle using Midpoint Circle Drawing Algorithm")
            glutDisplayFunc(lambda: MidPointCircleDraw(x, y, r))
            glutIdleFunc(lambda: MidPointCircleDraw(x, y, r))
            init()
            glutMainLoop()


main()