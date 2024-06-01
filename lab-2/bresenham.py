import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw_bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    if dx > dy:
        err = dx / 2.0
        while x1 != x2:
            glVertex2i(x1, y1)
            err -= dy
            if err < 0:
                y1 += sy
                err += dx
            x1 += sx
    else:
        err = dy / 2.0
        while y1 != y2:
            glVertex2i(x1, y1)
            err -= dx
            if err < 0:
                x1 += sx
                err += dy
            y1 += sy
    glVertex2i(x2, y2)  # Ensuring the last point is drawn


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)  # Red color
    glBegin(GL_POINTS)
    draw_bresenham_line(-50, -50, 50, 50)
    glEnd()

    glColor3f(0.0, 1.0, 0.0)  # Green color
    glBegin(GL_POINTS)
    draw_bresenham_line(-50, 50, 50, -50)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)  # Blue color
    glBegin(GL_POINTS)
    draw_bresenham_line(-50, 0, 50, 0)
    glEnd()

    glColor3f(0.0, 0.0, 0.0)  # black color
    glBegin(GL_POINTS)
    draw_bresenham_line(0, -50, 0, 50)
    glEnd()

    pygame.display.flip()


def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Bresenham Line Drawing Algorithm')
    gluOrtho2D(-100, 100, -100, 100)

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(1.0, 0.0, 0.0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display()
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
