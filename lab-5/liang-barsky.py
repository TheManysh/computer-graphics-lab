import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *


def init_window(width, height):
    pygame.init()
    display = (width, height)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glOrtho(-width // 2, width // 2, -height // 2, height // 2, -1, 1)


def plot_line(x0, y0, x1, y1, color):
    glColor3f(*color)
    glBegin(GL_LINES)
    glVertex2f(x0, y0)
    glVertex2f(x1, y1)
    glEnd()


def liang_barsky(x0, y0, x1, y1, xmin, ymin, xmax, ymax):
    dx, dy = x1 - x0, y1 - y0
    p = [-dx, dx, -dy, dy]
    q = [x0 - xmin, xmax - x0, y0 - ymin, ymax - y0]

    u1, u2 = 0.0, 1.0

    for i in range(4):
        if p[i] == 0 and q[i] < 0:
            return None
        if p[i] < 0:
            u1 = max(u1, q[i] / p[i])
        elif p[i] > 0:
            u2 = min(u2, q[i] / p[i])

    if u1 > u2:
        return None

    x0_clipped = x0 + u1 * dx
    y0_clipped = y0 + u1 * dy
    x1_clipped = x0 + u2 * dx
    y1_clipped = y0 + u2 * dy

    return x0_clipped, y0_clipped, x1_clipped, y1_clipped


def main():
    init_window(800, 600)
    pygame.display.set_caption("Liang-Barsky Line Clipping Algorithm")

    x0, y0 = -100, -100
    x1, y1 = 200, 150
    xmin, ymin = -50, -50
    xmax, ymax = 150, 100

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)

        # Plot clipping window
        glColor3f(0.0, 0.0, 1.0)  # Blue
        glBegin(GL_LINE_LOOP)
        glVertex2f(xmin, ymin)
        glVertex2f(xmax, ymin)
        glVertex2f(xmax, ymax)
        glVertex2f(xmin, ymax)
        glEnd()

        # Plot original line
        plot_line(x0, y0, x1, y1, (1.0, 0.0, 0.0))  # Red

        # Plot clipped line
        clipped_line = liang_barsky(x0, y0, x1, y1, xmin, ymin, xmax, ymax)
        if clipped_line:
            plot_line(*clipped_line, (0.0, 1.0, 0.0))  # Green

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
