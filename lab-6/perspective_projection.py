import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw_cube():
    glBegin(GL_QUADS)
    # Front face
    glVertex3f(-1, -1,  1)
    glVertex3f(1, -1,  1)
    glVertex3f(1,  1,  1)
    glVertex3f(-1,  1,  1)
    # Back face
    glVertex3f(-1, -1, -1)
    glVertex3f(-1,  1, -1)
    glVertex3f(1,  1, -1)
    glVertex3f(1, -1, -1)
    # Top face
    glVertex3f(-1,  1, -1)
    glVertex3f(-1,  1,  1)
    glVertex3f(1,  1,  1)
    glVertex3f(1,  1, -1)
    # Bottom face
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1,  1)
    glVertex3f(-1, -1,  1)
    # Right face
    glVertex3f(1, -1, -1)
    glVertex3f(1,  1, -1)
    glVertex3f(1,  1,  1)
    glVertex3f(1, -1,  1)
    # Left face
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1,  1)
    glVertex3f(-1,  1,  1)
    glVertex3f(-1,  1, -1)
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    # Move back a bit so that the cube is in view
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
