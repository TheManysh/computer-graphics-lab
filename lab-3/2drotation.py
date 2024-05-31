import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math


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


def apply_rotation(vertices, angle):
    rotation_matrix = np.array([
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ])

    rotated_vertices = []
    for vertex in vertices:
        rotated_vertex = np.dot(rotation_matrix, vertex)
        rotated_vertices.append(rotated_vertex)

    return rotated_vertices


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
    pygame.display.get_caption('2D Rotation')
    gluOrtho2D(-1, 1, -1, 1)

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(0.0, 0.0, 0.0)

    vertices = [
        [-0.5, -0.5, 1.0],
        [0.5, -0.5, 1.0],
        [0.5, 0.5, 1.0],
        [-0.5, 0.5, 1.0]
    ]

    angle = 0.0  # Initial rotation angle

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    angle -= math.radians(10)
                elif event.key == pygame.K_RIGHT:
                    angle += math.radians(10)

        rotated_vertices = apply_rotation(vertices, angle)
        display(rotated_vertices)
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
