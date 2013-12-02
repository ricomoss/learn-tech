from unittest import TestCase

from motor import Wheels, Legs


class WheelsTest(TestCase):
    def test_perform_move(self):
        wheels = Wheels()
        self.assertEqual(wheels.wheel_rotations, 0)
        wheels.perform_move()
        self.assertEqual(wheels.wheel_rotations, 1)

    def test_get_total_distance(self):
        wheels = Wheels()
        self.assertEqual(wheels.get_total_distance(), 0)
        wheels.perform_move()
        expected = 1 * 5.5 / .86
        self.assertEqual(wheels.get_total_distance(), expected)

    def test_distance_per_rotation(self):
        wheels = Wheels()
        self.assertIsInstance(wheels.distance_per_rotation(), float)


class LegsTest(TestCase):
    def test_perform_move(self):
        legs = Legs()
        self.assertEqual(legs.steps_taken, 0)
        legs.perform_move()
        self.assertEqual(legs.steps_taken, 1)

    def test_get_total_distance(self):
        legs = Legs()
        self.assertEqual(legs.get_total_distance(), 0)
        legs.perform_move()
        expected = 22.131 - .01
        self.assertEqual(legs.get_total_distance(), expected)

    def test_distance_per_step(self):
        legs = Legs()
        self.assertIsInstance(legs.distance_per_step(), float)
