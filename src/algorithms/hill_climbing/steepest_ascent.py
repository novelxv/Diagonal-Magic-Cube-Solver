from algorithms.base_algorithm import BaseAlgorithm
from utils.data_processing import best_neighbor, evaluate_cube
import time

class SteepestAscent(BaseAlgorithm):
    def run(self):
        self.start_time = time.time()
        self.iter = 0
        while self.iter < self.max_iter:
            self.track_value()
            neighbor = best_neighbor(self.cube)
            if evaluate_cube(neighbor) > self.evaluate():
                self.cube = neighbor
            else:
                break
            self.iter += 1
        self.end_time = time.time()