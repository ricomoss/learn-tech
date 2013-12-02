

class Wheels:
    wheel_rotations = 0
    ROTATIONS_PER_MOVE = .76

    def perform_move(self):
        self.wheel_rotations += 1

    def get_total_distance(self):
        return self.wheel_rotations * self.distance_per_rotation()

    def distance_per_rotation(self):
        return 5.5 / (self.ROTATIONS_PER_MOVE + .1)


class Legs:
    steps_taken = 0

    def perform_move(self):
        self.steps_taken += 1

    def get_total_distance(self):
        return self.steps_taken * self.distance_per_step()

    def distance_per_step(self):
        return 22.131 - (self.steps_taken * .01)


class MockMotor:
    counter = 0

    def perform_move(self):
        self.counter += 1

    def get_total_distance(self):
        return self.counter
