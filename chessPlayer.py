import time
from data import Board, config, RobotArm
import pygame
import sys

sys.path.insert(0, 'C:\\Users\\cordr\\PycharmProjects\\ChessPlayer\\data')

pygame.init()
pygame.display.set_caption(config.WINDOW_NAME)

screen = config.screen

board_background = pygame.image.load("data/assets/boards/wood_board.png")
board_background = pygame.transform.scale(board_background, (config.WIDTH, config.HEIGHT))

board = Board.board()

robo_arm = RobotArm.arm((0, 145, 0))


# Main game loop
def run():
    last_move = time.time()
    running = True

    pygame.time.delay(10000)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                pass

        board.advance_to_next_move()

        robo_arm.target_pos = RobotArm.chess_board_pos_to_screen_pos(board.moveslist[board.curr_move][:2])
        robo_arm.update()
        robo_arm.draw()

        pygame.display.update()

        pygame.time.delay(config.TIME_BETWEEN_MOVES)
        screen.blit(board_background, (0, 0))
        board.draw_fen()

        pygame.display.update()

        robo_arm.target_pos = RobotArm.chess_board_pos_to_screen_pos(board.moveslist[board.curr_move][2:])
        robo_arm.update()
        robo_arm.draw()

        pygame.display.update()
        pygame.time.delay(config.TIME_BETWEEN_MOVES)

        screen.blit(board_background, (0, 0))

        board.draw_fen()

        if board.game_done:
            running = False

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    run()
