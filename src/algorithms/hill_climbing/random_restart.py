import time
from algorithms.base_algorithm import BaseAlgorithm
from utils.data_processing import is_goal, init_cube
from algorithms.hill_climbing.steepest_ascent import SteepestAscent

class RandomRestart(BaseAlgorithm):
    def __init__(self, cube, max_iter, max_restart):
        super().__init__(cube, max_iter)
        self.max_restart = max_restart
        self.results = []
        self.restarts = 0

    def run(self):
        self.start_time = time.time()
        self.iter = 0
        steepest_algo = SteepestAscent(self.cube, self.max_iter)

        for _ in range(self.max_restart):
            steepest_algo.run()
            self.results.append(steepest_algo)
            if (is_goal(steepest_algo.cube)):
                break
            else:
                self.cube = init_cube(self.cube.shape[0])
                steepest_algo = SteepestAscent(self.cube, self.max_iter)
                self.restarts += 1

        m = self.results[0]
        m_val = m.evaluate()
        for result in self.results:
            self.tracker += result.tracker
            self.iter += result.iter

            res_val = result.evaluate()
            if (res_val > m_val):
                m = result
                m_val = res_val
                
        self.cube = m.cube
        self.end_time = time.time()

    def get_results(self):
        result = super().get_results()
        result.update({'restarts': self.restarts,
                       'iter_per_restart': [e.iter for e in self.results]
                       })
        return result

