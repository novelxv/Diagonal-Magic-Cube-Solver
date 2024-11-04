from algorithms.base_algorithm import BaseAlgorithm
from utils.data_processing import evaluate_cube, random_swap
import time

class Stochastic(BaseAlgorithm):
    def run(self):
        self.start_time = time.time()
        self.iter = 0
        while self.iter < self.max_iter:
            c_val = self.evaluate()
            self.tracker.append(c_val)

            neighbor = random_swap(self.cube)
            n_val = evaluate_cube(neighbor)

            if c_val < n_val:
                self.cube = neighbor
            if n_val == 0:
                break

            self.iter += 1
        self.end_time = time.time()
        