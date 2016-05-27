from core.config import parse
import pygame

# Program Info
__version__ = '0.1'
__author__ = 'DOCTOR_RABB'
# -------------------------

CONFIG_PATH = 'config.json'
MAIN_CONFIG = parse (CONFIG_PATH)


# Main Constants
CLEAR_COLOR = MAIN_CONFIG ['clearColor']
GRID_SIZE = MAIN_CONFIG ['gridSize']
SCREEN_SIZE = MAIN_CONFIG ['screenSize']
DEFAULT_CUBE_VERTS = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)
DEFAULT_CUBE_EDGES = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)
HELP_MENU = {
    'h button' : 'show this message',
    'r button' : 'reset position and rotation',
    'Left Arrow' : 'Rotate to left',
    'Right Arrow' : 'Rotate to right',
    'Left Mouse Button' : 'Rotate by mouse axis',
    'Right Mouse Button' : 'Move by mouse axis',
    'Mouse Wheel' : 'Set Z axis'
}
pygame.font.init ()
DEFAULT_FONT = pygame.font.Font (None, 64)
