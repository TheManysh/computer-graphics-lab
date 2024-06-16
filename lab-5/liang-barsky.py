import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def liang_barsky(x0, y0, x1, y1, xmin, ymin, xmax, ymax):
    def clip_test(p, q, tE, tL):
        if p < 0.0:
            r = q / p
            if r > tL:
                return False, tE, tL
            elif r > tE:
                tE = r
        elif p > 0.0:
            r = q / p
            if r < tE:
                return False, tE, tL
            elif r < tL:
                tL = r
        elif q < 0.0:
            return False, tE, tL
        return True, tE, tL

    dx = x1 - x0
    dy = y1 - y0
    tE = 0.0
    tL = 1.0
    checks = [
        (-dx, x0 - xmin),
        (dx, xmax - x0),
        (-dy, y0 - ymin),
        (dy, ymax - y0)
    ]
    accept = True
    for p, q in checks:
        accept, tE, tL = clip_test(p, q, tE, tL)
        if not accept:
            break
    if accept:
        if tL < 1.0:
            x1 = x0 + tL * dx
            y1 = y0 + tL * dy
        if tE > 0.0:
            x0 = x0 + tE * dx
            y0 = y0 + tE * dy
        return (x0, y0, x1, y1)
    return None


def draw_line(x0, y0, x1, y1, color):
    glColor3f(*color)
    glBegin(GL_LINES)
    glVertex2f(x0, y0)
    glVertex2f(x1, y1)
    glEnd()


def main():
    pygame.init()
    pygame.display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Liang-Barsky Line Clipping")
    gluOrtho2D(-1, 1, -1, 1)
    glClearColor(1.0, 1.0, 1.0, 1.0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)

        # Window coordinates for clipping
        xmin, ymin = -0.5, -0.5
        xmax, ymax = 0.5, 0.5

        # Draw clipping window
        glColor3f(0.0, 0.0, 0.0)
        glBegin(GL_LINE_LOOP)
        glVertex2f(xmin, ymin)
        glVertex2f(xmax, ymin)
        glVertex2f(xmax, ymax)
        glVertex2f(xmin, ymax)
        glEnd()

        # Lines to clip
        lines = [
            (-0.7, -0.7, 0.7, 0.7),
            (-0.7, 0.3, 0.7, -0.3),
            (-0.8, 0.8, -0.6, -0.6),
            (0.4, -0.4, 0.6, 0.6)
        ]

        for line in lines:
            x0, y0, x1, y1 = line
            clipped_line = liang_barsky(x0, y0, x1, y1, xmin, ymin, xmax, ymax)
            if clipped_line:
                # Clipped line in red
                draw_line(*clipped_line, (1.0, 0.0, 0.0))
            else:
                # Original line in blue
                draw_line(x0, y0, x1, y1, (0.0, 0.0, 1.0))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
