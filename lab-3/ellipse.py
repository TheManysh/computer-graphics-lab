import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def plotPoint(points, x, y, xc, yc):
    points.append((xc + x, yc + y))
    points.append((xc - x, yc + y))
    points.append((xc + x, yc - y))
    points.append((xc - x, yc - y))


def drawEllipseMidpoint(rx, ry, xc=0, yc=0):
    x = 0
    y = ry
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    points = []

    p1 = ry * ry - rx * rx * ry + 0.25 * rx * rx

    while dx < dy:
        plotPoint(points, x, y, xc, yc)
        x += 1
        dx += 2 * ry * ry
        p1 += dx + ry * ry
        if p1 >= 0:
            y -= 1
            dy -= 2 * rx * rx
            p1 -= dy

    p2 = ry * ry * (x + 0.5) * (x + 0.5) + rx * rx * \
        (y - 1) * (y - 1) - rx * rx * ry * ry

    while y >= 0:
        plotPoint(points, x, y, xc, yc)
        y -= 1
        dy -= 2 * rx * rx
        p2 += rx * rx - dy
        if p2 <= 0:
            x += 1
            dx += 2 * ry * ry
            p2 += dx + rx * rx

    return points


def display(rx, ry, xc, yc):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    points = drawEllipseMidpoint(rx, ry, xc, yc)

    glBegin(GL_POINTS)
    for point in points:
        glVertex2i(point[0], point[1])
    glEnd()

    pygame.display.flip()


def main():
    pygame.init()
    pygame.display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Midpoint Ellipse Drawing Algorithm")
    gluOrtho2D(-100, 100, -100, 100)

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(1.0, 0.0, 0.0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display(50, 30, 0, 0)
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
