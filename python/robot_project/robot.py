import random
import itertools

from motor import Wheels, Legs, MockMotor


class BaseRobot:
    def __init__(self):
        self.get_motor()
        self.my_moves = list()
        self.my_orientation = random.choice([x for x in range(0, 360)])

    def get_motor(self):
        raise NotImplementedError('You must implement the get_motor method.')

    def get_moves(self):
        return self.my_moves

    def move_forward(self, moves):
        for _ in itertools.repeat(None, moves):
            self.my_motor.perform_move()
            self.my_moves.append('forward')

    def move_back(self, moves):
        for _ in itertools.repeat(None, moves):
            self.reset_orientation(-180)
            self.my_motor.perform_move()
            self.my_moves.append('back')

    def move_right(self, moves):
        for _ in itertools.repeat(None, moves):
            self.reset_orientation(90)
            self.my_motor.perform_move()
            self.my_moves.append('right')

    def move_left(self, moves):
        for _ in itertools.repeat(None, moves):
            self.reset_orientation(-90)
            self.my_motor.perform_move()
            self.my_moves.append('left')

    def reset_orientation(self, new_direction):
        self.my_orientation += new_direction
        self.my_orientation = abs(self.my_orientation % 360)

class WheeledRobot(BaseRobot):
    def get_motor(self):
        self.my_motor = Wheels()


class LeggedRobot(BaseRobot):
    def get_motor(self):
        self.my_motor = Legs()


class MockRobot(BaseRobot):
    def get_motor(self):
        self.my_motor = MockMotor()
