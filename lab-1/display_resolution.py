from OpenGL.GL import *
from OpenGL.GLUT import *
import pygame


def display_resolution_pyopengl():
    # Initialize Pygame to get display info
    pygame.init()

    # Get the resolution of the display
    display_info = pygame.display.Info()
    screen_width = display_info.current_w
    screen_height = display_info.current_h

    # Print the resolution
    print(f"Display Resolution: {screen_width}x{screen_height}")

    # Clean up and quit Pygame
    pygame.quit()


if __name__ == "__main__":
    display_resolution_pyopengl()
