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


def apply_translation(vertices, tx, ty):
    translation_matrix = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

    translated_vertices = []
    for vertex in vertices:
        translated_vertex = np.dot(translation_matrix, vertex)
        translated_vertices.append(translated_vertex)

    return translated_vertices


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
    pygame.display.set_caption('2D Translation')
    gluOrtho2D(-1, 1, -1, 1)

    glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(0.0, 0.0, 0.0)

    vertices = [
        [-0.5, -0.5, 1.0],
        [0.5, -0.5, 1.0],
        [0.5, 0.5, 1.0],
        [-0.5, 0.5, 1.0]
    ]

    tx, ty = 0.0, 0.0  # Initial translation values

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

        translated_vertices = apply_translation(vertices, tx, ty)
        display(translated_vertices)
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
