import pygame
from numpy import *
import config


# Converts the pygame coordinates to normal graph coordinates
def pos_to_cartesian(pos):
    x = pos[0] - config.WIDTH / 2
    y = -(pos[1] - config.HEIGHT / 2)
    return x, y


def chess_board_pos_to_screen_pos(pos):
    x = (ord(pos[0]) - 97) * config.TILE_WIDTH + (config.TILE_WIDTH / 2)
    y = (int(pos[1])-1) * config.TILE_HEIGHT + (config.TILE_WIDTH / 2)
    return x, y


class arm:
    def __init__(self, _color):
        # Line 1
        self.line1_length = sqrt(((config.HEIGHT / 2) ** 2) + ((config.WIDTH / 2) ** 2)) / 2
        self.line1_angle = 0
        self.l1y = None
        self.l1x = None

        # Line 2
        self.line2_length = sqrt(((config.HEIGHT / 2) ** 2) + ((config.WIDTH / 2) ** 2)) / 2
        self.line2_angle = 0
        self.l2y = None
        self.l2x = None

        self.target_pos = (90, 87)

        self.color = _color

        self.a1 = self.line1_length
        self.a2 = self.line2_length

    def update(self):
        self.line1_angle, self.line2_angle = self.inverse_kinematics(pos_to_cartesian(self.target_pos))
        # Line 1
        self.l1x = config.WIDTH / 2 + self.line1_length * cos(self.line1_angle)
        self.l1y = config.HEIGHT / 2 + self.line1_length * sin(self.line1_angle)
        # Line 2
        self.l2x = (self.line2_length * cos(self.line2_angle + self.line1_angle)) + self.l1x
        self.l2y = (self.line2_length * sin(self.line2_angle + self.line1_angle)) + self.l1y

    # Calculates the angles for the arms to be at to go to the desired position
    def inverse_kinematics(self, pos):
        # Equations for Inverse kinematics
        r1 = sqrt(pos[0] * pos[0] + pos[1] * pos[1])  # eqn 1
        if math.isclose(r1, 0):
            return 0, 0
        phi_1 = arccos((self.a2 * self.a2 - self.a1 * self.a1 - r1 * r1) / (-2 * self.a1 * r1))  # eqn 2
        phi_2 = arctan2(-pos[1], pos[0])  # eqn 3
        theta_1 = phi_2 - phi_1

        phi_3 = arccos((r1 * r1 - self.a1 * self.a1 - self.a1 * self.a2) / (-2 * self.a1 * self.a2))
        theta_2 = pi - phi_3

        return theta_1, theta_2

    def draw(self):
        pygame.draw.lines(config.screen, self.color, False,
                          [(config.WIDTH / 2, config.HEIGHT / 2), (self.l1x, self.l1y), (self.l2x, self.l2y)], 3)

    def clear_arm(self):
        pygame.draw.lines(config.screen, self.color, False,
                          [(config.WIDTH / 2, config.HEIGHT / 2), (self.l1x, self.l1y), (self.l2x, self.l2y)], 3)
