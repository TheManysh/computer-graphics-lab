import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, 0.5)
    glEnd()


def reflect(vertices, axis='y'):
    if axis == 'x':
        reflection_matrix = [
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ]
    elif axis == 'y':
        reflection_matrix = [
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
    else:
        return vertices

    reflected_vertices = []
    for vertex in vertices:
        new_vertex = [
            vertex[0] * reflection_matrix[0][0] + vertex[1] *
            reflection_matrix[0][1] + reflection_matrix[0][2],
            vertex[0] * reflection_matrix[1][0] + vertex[1] *
            reflection_matrix[1][1] + reflection_matrix[1][2]
        ]
        reflected_vertices.append(new_vertex)
    return reflected_vertices


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('2D Reflection using PyOpenGL')
    gluOrtho2D(-1, 1, -1, 1)

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(0.0, 0.0, 0.0)

    vertices = [
        [-0.5, -0.5, 1],
        [0.5, -0.5, 1],
        [0.0, 0.5, 1]
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Original triangle
        glColor3f(0.0, 0.0, 0.0)
        draw_triangle()

        # Reflected triangle
        glColor3f(1.0, 0.0, 0.0)  # Red color for the reflected triangle
        reflected_vertices = reflect(vertices, axis='y')
        glBegin(GL_TRIANGLES)
        for vertex in reflected_vertices:
            glVertex2f(vertex[0], vertex[1])
        glEnd()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
