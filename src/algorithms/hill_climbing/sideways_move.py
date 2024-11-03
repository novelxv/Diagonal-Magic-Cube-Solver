from src.algorithms.base_algorithm import BaseAlgorithm
from src.utils.data_processing import best_neighbor, evaluate_cube

class SidewaysMove(BaseAlgorithm):
    def __init__(self, cube, max_iter, max_sideways_moves):
        super().__init__(cube, max_iter)
        self.max_sideways_moves = max_sideways_moves

    def run(self):
        self.iter = 0
        sideways_count = 0

        while self.iter < self.max_iter:
            self.track_value()
            neighbor = best_neighbor(self.cube)
            
            if evaluate_cube(neighbor) > self.evaluate():
                self.cube = neighbor
                sideways_count = 0 
            elif evaluate_cube(neighbor) == self.evaluate():
                self.cube = neighbor
                sideways_count += 1
                if sideways_count >= self.max_sideways_moves:
                    break  
            else:
                break 

            self.iter += 1
            