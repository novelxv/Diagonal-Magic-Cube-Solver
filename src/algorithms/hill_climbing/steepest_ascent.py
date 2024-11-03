from src.algorithms.base_algorithm import BaseAlgorithm
from src.utils.data_processing import best_neighbor, evaluate_cube

class SteepestAscent(BaseAlgorithm):
    def run(self):
        self.iter = 0
        while self.iter < self.max_iter:
            self.track_value()
            neighbor = best_neighbor(self.cube)
            if evaluate_cube(neighbor) > self.evaluate():
                self.cube = neighbor
            else:
                break
            self.iter += 1
            