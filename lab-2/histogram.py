import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def bresenham_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    return points


def draw_histogram(frequencies):
    # Setup the initial OpenGL environment
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Histogram using Bressenham")
    gluOrtho2D(0, 800, 0, 600)
    glClearColor(1.0, 1.0, 1.0, 1.0)

    glColor3f(0.0, 0.0, 0.0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw axes
        glBegin(GL_LINES)
        glVertex2f(50, 50)
        glVertex2f(50, 550)
        glVertex2f(50, 50)
        glVertex2f(750, 50)
        glEnd()

        # Draw histogram lines
        bar_width = (700 - 50) // len(frequencies)
        x1, y1 = 50, 50
        for i, frequency in enumerate(frequencies):
            x2 = 50 + (i + 1) * bar_width
            y2 = 50 + frequency * 5  # Scale frequency for better visualization
            points = bresenham_line(x1, y1, x2, y2)
            glBegin(GL_POINTS)
            for point in points:
                glVertex2f(point[0], point[1])
            glEnd()
            x1, y1 = x2, y2

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    # Sample frequency inputs for the histogram
    frequencies = [10, 20, 15, 25, 30, 20, 10, 5, 30, 20]
    draw_histogram(frequencies)
