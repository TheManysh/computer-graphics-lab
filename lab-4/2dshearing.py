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


def apply_shearing(vertices, shx, shy):
    shearing_matrix = np.array([
        [1, shx, 0],
        [shy, 1, 0],
        [0, 0, 1]
    ])

    sheared_vertices = []
    for vertex in vertices:
        sheared_vertex = np.dot(shearing_matrix, vertex)
        sheared_vertices.append(sheared_vertex)

    return sheared_vertices


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
    pygame.display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption('2D Shearing')
    gluOrtho2D(-1, 1, -1, 1)

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(1.0, 0.0, 0.0)

    vertices = [
        [-0.5, -0.5, 1.0],
        [0.5, -0.5, 1.0],
        [0.5, 0.5, 1.0],
        [-0.5, 0.5, 1.0]
    ]

    shx, shy = 0.0, 0.0  # Initial shearing values

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    shx -= 0.1
                elif event.key == pygame.K_RIGHT:
                    shx += 0.1
                elif event.key == pygame.K_UP:
                    shy += 0.1
                elif event.key == pygame.K_DOWN:
                    shy -= 0.1

        sheared_vertices = apply_shearing(vertices, shx, shy)
        display(sheared_vertices)

    pygame.quit()


if __name__ == "__main__":
    main()
