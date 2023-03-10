import os
import random
import chess.pgn

from data import config
import sys

sys.path.insert(0, 'C:\\Users\\cordr\\PycharmProjects\\ChessPlayer\\data')

def parse_pgn(inpgn):
    fen_list = []
    moves_list = [None]
    with open(inpgn, encoding='utf-8') as h:
        while True:
            game = chess.pgn.read_game(h)
            if game is None:
                break

            for node in game.mainline():
                moves_list.append(node.move.uci())
                pnode = node.parent
                _board = pnode.board()

                fen_list.append(_board.fen())
    print(fen_list)

    return fen_list, moves_list


class board:

    def __init__(self):
        self.fenlist, self.moveslist = parse_pgn("data/games/game1.pgn")

        self.curr_move = 0

        self.prev_fen = None
        self.current_fen = self.fenlist[0]

        self.game_done = False

        # 0 = Black : 1 = White
        self.colors_turn = self.update_color_turn()

    # Draws each of the pieces in a fen string
    def draw_fen(self):
        cur_x = 0
        cur_y = config.HEIGHT - config.TILE_HEIGHT

        if self.curr_move >= len(self.fenlist):
            return

        for i in self.fenlist[self.curr_move]:
            if i == ' ':
                return
            elif i == '/':
                cur_y -= config.TILE_HEIGHT
                cur_x = 0
                continue
            elif i.isnumeric():
                cur_x += config.TILE_WIDTH * int(i)
                continue
            else:
                config.piece_dict[i].draw((cur_x, cur_y))
                cur_x += config.TILE_WIDTH

    # Steps the current move ahead by 1
    def advance_to_next_move(self):
        self.curr_move += 1

    def update_color_turn(self):
        if self.current_fen.split(' ')[1][0] == 'b':
            return 0
        return 1
