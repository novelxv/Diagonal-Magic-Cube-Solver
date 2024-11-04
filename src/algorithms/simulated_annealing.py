import numpy as np
import math
from algorithms.base_algorithm import BaseAlgorithm
from utils.data_processing import evaluate_cube, random_swap
import time

class SimulatedAnnealing(BaseAlgorithm):
    def __init__(self, cube: np.ndarray, max_iter: int, initial_temp: float, cooling_rate: float):
        super().__init__(cube, max_iter)
        self.initial_temp = initial_temp
        self.cooling_rate = cooling_rate
        self.prob_values = []  
        self.stuck_freq = 0   

    def run(self):
        self.start_time = time.time()
        self.iter = 0
        temperature = self.initial_temp
        stuck_threshold = 10   
        consec_stuck = 0  

        while self.iter < self.max_iter and temperature > 0:
            self.track_value() 
            
            neighbor = random_swap(self.cube)
            delta_e = evaluate_cube(neighbor) - self.evaluate()

            if delta_e > 0:
                # Accept the neighbor if it has a higher value
                self.cube = neighbor
                consec_stuck = 0
            else:
                # Accept the neighbor with a certain probability
                probability = math.exp(delta_e / temperature)
                self.prob_values.append(probability) 
                
                if np.random.rand() < probability:
                    self.cube = neighbor
                    consec_stuck = 0  
                else:
                    consec_stuck += 1
            # Increase stuck frequency if stuck for a certain number of iterations
            if consec_stuck >= stuck_threshold:
                self.stuck_freq += 1
                consec_stuck = 0  
            # Update temperature
            temperature *= self.cooling_rate
            self.iter += 1
        self.end_time = time.time()

    def get_results(self) -> dict:
        results = super().get_results()
        results.update({
            "prob_values": self.prob_values,  
            "stuck_freq": self.stuck_freq   
        })
        return results