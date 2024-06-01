import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def dda(start_pos, end_pos, color):
    glColor3f(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0)

    # Unpack start and end positions
    x1, y1 = start_pos
    x2, y2 = end_pos

    dx = x2 - x1
    dy = y2 - y1

    # Determine number of steps required for the algorithm
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # Calculate the increment in x and y for each step
    x_inc = dx / float(steps)
    y_inc = dy / float(steps)

    # Initialize starting point
    x = x1
    y = y1

    glBegin(GL_POINTS)
    for i in range(steps):
        glVertex2f(x, y)
        x += x_inc
        y += y_inc
    glEnd()


def init_gl(screen_width, screen_height):
    glViewport(0, 0, screen_width, screen_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, screen_width, 0, screen_height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    # Initialize Pygame
    pygame.init()

    # Set screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode(
        (screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("DDA Line Drawing Algorithm")
    # Set line color
    line_color = (255, 0, 0)  # Red

    # Set start and end positions for the line
    start_pos = (100, 100)
    end_pos = (500, 300)

    # Initialize OpenGL
    init_gl(screen_width, screen_height)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the line using DDA
        dda(start_pos, end_pos, line_color)

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
