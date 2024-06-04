import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np


def draw_rectangle(vertices, color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()


def apply_reflection(vertices, axis):
    if axis == 'x':
        reflection_matrix = np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
    elif axis == 'y':
        reflection_matrix = np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])

    reflected_vertices = []
    for vertex in vertices:
        reflected_vertex = np.dot(reflection_matrix, vertex)
        reflected_vertices.append(reflected_vertex)

    return reflected_vertices


def display(original_vertices, current_vertices):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw the original rectangle in faint red
    draw_rectangle(original_vertices, (1.0, 0.5, 0.5))  # Faint red color

    # Draw the reflected rectangle in solid red
    draw_rectangle(current_vertices, (1.0, 0.0, 0.0))  # Solid red color

    pygame.display.flip()


def main():
    pygame.init()
    pygame.display.set_mode((600, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption('2D Reflection')
    gluOrtho2D(-1, 1, -1, 1)
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Place the rectangle in the third quadrant
    original_vertices = [
        [-0.75, -0.75, 1.0],
        [-0.25, -0.75, 1.0],
        [-0.25, -0.25, 1.0],
        [-0.75, -0.25, 1.0]
    ]

    # This will store all the reflected versions of the rectangle
    reflected_vertices_list = [original_vertices]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Reflect the last reflected image on the y-axis
                    new_reflection = apply_reflection(
                        reflected_vertices_list[-1], 'y')
                    reflected_vertices_list.append(new_reflection)
                elif event.key == pygame.K_UP:
                    # Reflect the last reflected image on the x-axis
                    new_reflection = apply_reflection(
                        reflected_vertices_list[-1], 'x')
                    reflected_vertices_list.append(new_reflection)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw all previous reflections in faint red
        for vertices in reflected_vertices_list[:-1]:
            draw_rectangle(vertices, (1.0, 0.5, 0.5))  # Faint red color

        # Draw the current reflection in solid red
        # Solid red color
        draw_rectangle(reflected_vertices_list[-1], (1.0, 0.0, 0.0))

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
