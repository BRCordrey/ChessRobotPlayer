import pygame
from data import config
import sys

sys.path.insert(0, 'C:\\Users\\cordr\\PycharmProjects\\ChessPlayer\\data')


class piece:
    def __init__(self, _type, _color):
        self.type = _type
        self.color = _color
        self.filename = "data/assets/pieces/" + self.color + "_" + self.type + ".png"
        self.image = pygame.image.load(self.filename)
        self.image = pygame.transform.scale(self.image, (config.WIDTH / 8, config.HEIGHT / 8))

    # Draws the piece to the screen
    def draw(self, pos):
        config.screen.blit(self.image, pos)
