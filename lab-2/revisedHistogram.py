import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import matplotlib.pyplot as plt


def draw_histogram(unique_values, frequencies):
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

        # Draw histogram bars
        bar_width = (700 - 50) // len(unique_values)
        x1, y1 = 50, 50
        for i, value in enumerate(unique_values):
            x2 = 50 + (i + 1) * bar_width
            # Scale frequency for better visualization
            y2 = 50 + frequencies[i] * 100
            # Draw a line segment representing the histogram bar
            glBegin(GL_LINES)
            glVertex2f(x1, y1)
            glVertex2f(x2, y2)
            glEnd()
            x1, y1 = x2, y2

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    # Sample data for the histogram
    data = [10, 20, 15, 25, 30, 20, 10, 5, 30, 20]
    # Get unique values and their frequencies
    unique_values = list(set(data))
    frequencies = [data.count(value) for value in unique_values]
    # plt.hist(data, bins=len(unique_values))
    # plt.show()
    draw_histogram(unique_values, frequencies)
