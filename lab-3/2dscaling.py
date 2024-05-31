import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np


def draw_rectangle():
    vertices = [
        [-0.5, -0.5, 1.0],
        [0.5, -0.5, 1.0],
        [0.5, 0.5, 1.0],
        [-0.5, 0.5, 1.0]
    ]

    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()


def apply_scaling(vertices, sx, sy):
    scaling_matrix = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

    scaled_vertices = []
    for vertex in vertices:
        scaled_vertex = np.dot(scaling_matrix, vertex)
        scaled_vertices.append(scaled_vertex)

    return scaled_vertices


def display(vertices):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)  # Red color
    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

    pygame.display.flip()


def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption('2D Scaling')
    gluOrtho2D(-1, 1, -1, 1)

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(0.0, 0.0, 0.0)

    vertices = [
        [-0.5, -0.5, 1.0],
        [0.5, -0.5, 1.0],
        [0.5, 0.5, 1.0],
        [-0.5, 0.5, 1.0]
    ]

    sx, sy = 1.0, 1.0  # Initial scaling factors

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sx += 0.1
                    sy += 0.1
                elif event.key == pygame.K_DOWN:
                    sx -= 0.1
                    sy -= 0.1

        scaled_vertices = apply_scaling(vertices, sx, sy)
        display(scaled_vertices)
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
