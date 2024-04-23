from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *
from math import cos, sin, pi

PRIMARY_COLOR = (40/255, 40/255, 125/255)


def draw_triangle(point1, point2, point3, color):
    glColor3f(*color)
    glBegin(GL_TRIANGLES)
    glVertex2f(*point1)
    glVertex2f(*point2)
    glVertex2f(*point3)
    glEnd()


def draw_semi_circle(radius, x_center, y_center, color=(1, 1, 1)):
    glColor3f(*color)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x_center, y_center)  # Center point
    for i in range(0, 181, 1):  # 0 to 180 degrees, change step for smoother circle
        rad = i * pi / 180  # Convert degrees to radians
        x = radius * cos(rad) + x_center
        y = radius * sin(rad) + y_center
        glVertex2f(x, y)
    glEnd()


def draw_rectangle(x1, y1, x2, y2, color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()


def displayLogo():
    glLineWidth(10)
    # blue triangle (mountain with white snow)
    draw_triangle((-1.2, -1), (0.5, 0), (1.5, -1), color=PRIMARY_COLOR)
    # draw_triangle(-1.5, -1, 0.5, 0, 1.5, -1, (1, 1, 1))
    # white triangle
    draw_triangle((-1.8 + 0.3, -1 - 0.2), (0.5 + 0.3, 0 - 0.2),
                  (1.5 + 0.3, -1 - 0.2), color=PRIMARY_COLOR)
    draw_triangle((-1.8 + 0.3, -1 - 0.4), (0.5 + 0.3, 0 - 0.4),
                  (1.5 + 0.3, -1 - 0.4), (1, 1, 1))

    # semicircle
    draw_semi_circle(0.8, -0.2, -1, color=PRIMARY_COLOR)
    draw_semi_circle(0.7, -0.2, -1 - 0.1, color=(1, 1, 1))


def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClearColor(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        displayLogo()
        pygame.display.flip()
        # pygame.time.wait(10)


if __name__ == "__main__":
    main()
