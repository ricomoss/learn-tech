from unittest import TestCase

from robot import BaseRobot, MockRobot
from motor import MockMotor


class BaseRobotTest(TestCase):
    def test_get_motor(self):
        with self.assertRaises(NotImplementedError) as context:
            BaseRobot()


class MockRobotTest(TestCase):
    def test_get_motor(self):
        robot = MockRobot()
        self.assertIsInstance(robot.my_motor, type(MockMotor()))

    def test_get_moves(self):
        robot = MockRobot()
        self.assertEqual(robot.my_moves, list())
        robot.move_back(1)
        robot.move_forward(2)
        expected = ['back', 'forward', 'forward']
        self.assertEqual(robot.my_moves, expected)

    def test_move_forward(self):
        robot = MockRobot()
        starting_orientation = robot.my_orientation
        self.assertEqual(robot.my_moves, list())

        robot.move_forward(2)
        expected = ['forward', 'forward']
        self.assertEqual(robot.my_moves, expected)
        self.assertEqual(robot.my_orientation, starting_orientation)

    def test_move_backward(self):
        robot = MockRobot()
        starting_orientation = robot.my_orientation
        self.assertEqual(robot.my_moves, list())

        robot.move_back(1)
        expected = ['back']
        self.assertEqual(robot.my_moves, expected)
        expected = (starting_orientation - 180) % 360
        self.assertEqual(robot.my_orientation, expected)

        robot.move_back(1)
        expected = ['back', 'back']
        self.assertEqual(robot.my_moves, expected)
        expected = (starting_orientation - 2 * 180) % 360
        self.assertEqual(robot.my_orientation, expected)

    def test_move_right(self):
        robot = MockRobot()
        starting_orientation = robot.my_orientation
        self.assertEqual(robot.my_moves, list())

        robot.move_right(1)
        expected = ['right']
        self.assertEqual(robot.my_moves, expected)
        expected = (starting_orientation + 90) % 360
        self.assertEqual(robot.my_orientation, expected)

        robot.move_right(1)
        expected = ['right', 'right']
        self.assertEqual(robot.my_moves, expected)
        expected = (starting_orientation + 2 * 90) % 360
        self.assertEqual(robot.my_orientation, expected)

    def test_move_left(self):
        robot = MockRobot()
        starting_orientation = robot.my_orientation
        self.assertEqual(robot.my_moves, list())

        robot.move_left(1)
        expected = ['left']
        self.assertEqual(robot.my_moves, expected)
        expected = (starting_orientation - 90) % 360
        self.assertEqual(robot.my_orientation, expected)

        robot.move_left(1)
        expected = ['left', 'left']
        self.assertEqual(robot.my_moves, expected)
        expected = (starting_orientation - 2 * 90) % 360
        self.assertEqual(robot.my_orientation, expected)

    def test_reset_orientation(self):
        robot = MockRobot()
        robot.my_orientation = 90

        robot.reset_orientation(10)
        self.assertEqual(robot.my_orientation, 100)

        robot.reset_orientation(275)
        self.assertEqual(robot.my_orientation, 15)
