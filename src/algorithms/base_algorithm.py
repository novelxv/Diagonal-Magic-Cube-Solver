from abc import ABC, abstractmethod
import numpy as np
from src.utils.data_processing import evaluate_cube

class BaseAlgorithm(ABC):
    def __init__(self, cube: np.ndarray, max_iter: int):
        self.init_cube = cube.copy()
        self.cube = cube.copy()
        self.max_iter = max_iter
        self.iter = 0
        self.tracker = []

    @abstractmethod
    def run(self):
        """ Implement for each algorithm """
        pass

    def evaluate(self) -> int:
        return evaluate_cube(self.cube) 
    
    def track_value(self):
        value = self.evaluate()
        self.tracker.append(value)

    def get_results(self):
        results = {
            "initial_state": self.init_cube,
            "final_state" : self.cube,
            "initial_value": evaluate_cube(self.init_cube),
            "final_value": self.evaluate(),
            "iterations": self.iter,
            "tracker": self.tracker
        }
        return results
    
    def reset(self):
        self.cube = self.init_cube.copy()
        self.iter = 0
        self.tracker = []
        