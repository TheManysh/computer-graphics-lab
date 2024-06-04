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


def apply_composite_transformations(vertices, tx, ty, angle, sx, sy):
    translation_matrix = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

    rotation_matrix = np.array([
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ])

    scaling_matrix = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

    transformation_matrix = np.dot(
        translation_matrix, np.dot(rotation_matrix, scaling_matrix))

    transformed_vertices = []
    for vertex in vertices:
        transformed_vertex = np.dot(transformation_matrix, vertex)
        transformed_vertices.append(transformed_vertex)

    return transformed_vertices


def display(vertices, original_vertices):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw original rectangle with faint red color
    glColor3f(1.0, 0.6, 0.6)
    glBegin(GL_QUADS)
    for vertex in original_vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

    # Draw transformed rectangle with red color
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

    pygame.display.flip()


def main():
    pygame.init()
    pygame.display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Composite 2D Transformations')
    gluOrtho2D(-1, 1, -1, 1)

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(1.0, 0.0, 0.0)

    vertices = [
        [-0.5, -0.5, 1.0],
        [0.5, -0.5, 1.0],
        [0.5, 0.5, 1.0],
        [-0.5, 0.5, 1.0]
    ]

    tx, ty = 0.0, 0.0  # Translation values
    angle = 0.0  # Rotation angle
    sx, sy = 1.0, 1.0  # Scaling factors

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tx -= 0.1
                elif event.key == pygame.K_RIGHT:
                    tx += 0.1
                elif event.key == pygame.K_UP:
                    ty += 0.1
                elif event.key == pygame.K_DOWN:
                    ty -= 0.1
                elif event.key == pygame.K_q:
                    angle += math.radians(10)
                elif event.key == pygame.K_w:
                    angle -= math.radians(10)
                elif event.key == pygame.K_a:
                    sx *= 1.1
                elif event.key == pygame.K_s:
                    sx /= 1.1
                elif event.key == pygame.K_z:
                    sy *= 1.1
                elif event.key == pygame.K_x:
                    sy /= 1.1

        transformed_vertices = apply_composite_transformations(
            vertices, tx, ty, angle, sx, sy)
        display(transformed_vertices, vertices)
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
