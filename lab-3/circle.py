import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def drawCircleMidpoint(radius):
    x = 0
    y = radius
    d = 1 - radius  # Initial decision parameter

    # List to store the coordinates of points on the circle
    circle_points = []
    while y >= x:
        # Plot points in all octants
        circle_points.append((x, y))
        circle_points.append((y, x))
        circle_points.append((-x, y))
        circle_points.append((-y, x))
        circle_points.append((-x, -y))
        circle_points.append((-y, -x))
        circle_points.append((x, -y))
        circle_points.append((y, -x))
        if d <= 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
    return circle_points


def display(circle_points):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)  # Red color
    glBegin(GL_POINTS)
    for x, y in circle_points:
        glVertex2f(x, y)
    glEnd()

    pygame.display.flip()


def main():
    pygame.init()
    pygame.display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Circle Drawing using Midpoint Algorithm')
    gluOrtho2D(-250, 250, -250, 250)

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(0.0, 0.0, 0.0)

    circle_points = drawCircleMidpoint(100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display(circle_points)
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
