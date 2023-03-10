import pygame
from data import Piece
from Piece import piece
import sys

sys.path.insert(0, 'C:\\Users\\cordr\\PycharmProjects\\ChessPlayer\\data')

# Name of the window
WINDOW_NAME = "Chess Player"

# Width and height of the window
WIDTH = 500
HEIGHT = 500

# Seconds to wait before advancing to next move
TIME_BETWEEN_MOVES = 400

# Width and height of each tile on the board
TILE_WIDTH = int(WIDTH/8)
TILE_HEIGHT = int(HEIGHT/8)

# Screen that is drawn to
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Dictionary of each piece type and color, and their respective fen code
piece_dict = {"P": piece("pawn", "white"), "R": piece("rook", "white"), "N": piece("knight", "white"), "B": piece("bishop", "white"), "Q": piece("queen", "white"), "K": piece("king", "white"),
              "p": piece("pawn", "black"), "r": piece("rook", "black"), "n": piece("knight", "black"), "b": piece("bishop", "black"), "q": piece("queen", "black"), "k": piece("king", "black")}

# The path to the folder with the game fen strings
PATH_TO_GAMES = "data/games"
