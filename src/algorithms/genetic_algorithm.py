import numpy as np
from src.algorithms.base_algorithm import BaseAlgorithm
from src.utils.data_processing import init_cube, evaluate_cube, random_swap, get_rows, get_cols, get_pillars, get_side_diagonals, get_space_diagonals
import random

class GeneticAlgorithm(BaseAlgorithm):
    def __init___(self, cube: np.ndarray, max_iter: int, population_size: int, mutation_rate: float):
        """ Initialize genetic algorithm """
        super().__init__(cube, max_iter)
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = self.init_population()

    def init_population(self) -> list:
        """ Generate initial population """
        return [init_cube(self.cube.shape[0]) for _ in range(self.population_size)]
    
    def fitness_function(cube: np.ndarray) -> int:
        """ Fitness function to evaluate individual """
        n = cube.shape[0]
        magic_number = 1/2 * n * (n**3 + 1)
        fitness = 0

        rows = get_rows(cube)
        cols = get_cols(cube)
        pills = get_pillars(cube)
        side_diags = get_side_diagonals(cube)
        space_diags = get_space_diagonals(cube)

        for component in [rows, cols, pills, side_diags, space_diags]:
            for c in component:
                if np.sum(c) == magic_number:
                    fitness += 1

        return fitness
    
    def is_solution(self, individual: np.ndarray) -> bool:
        """ Check if individual is solution """
        n = individual.shape[0]
        return self.fitness_function(individual) == (3*(n**2) + 6*n + 4)
    
    def evaluate_population(self) -> list:
        """ Evaluate all individuals in population """
        return [self.fitness_function(individual) for individual in self.population]
    
    def select_parents(self) -> tuple:
        """ Select parents based on fitness value """
        fitness_val = self.evaluate_population()
        total_fitness = sum(fitness_val)
        prob = [val / total_fitness for val in fitness_val]
        parents = np.random.choice(self.population, size=2, p=prob, replace=False)
        return parents[0], parents[1]
    
    def crossover(self, parent1, parent2) -> np.ndarray:
        """ Crossover between two parents """
        point = np.random.randint(parent1.size)
        child = parent1.copy()
        child.flat[point:] = parent2.flat[point:]
        return child.reshape(parent1.shape)
    
    def mutate(self, individual: np.ndarray) -> np.ndarray:
        """ Mutate individual with random swap """
        if random.random() < self.mutation_rate:
            return random_swap(individual)
        return individual
    
    def run(self):
        """ Run genetic algorithm """
        self.iter = 0
        best_individual = None
        best_fitness = 0
        found_sol = False

        while self.iter < self.max_iter and not found_sol:
            new_population = []
            fitness_vals = self.evaluate_population()
            pop_best_fitness = max(fitness_vals)
            if pop_best_fitness > best_fitness:
                best_fitness = pop_best_fitness
                best_individual = self.population[np.argmax(fitness_vals)]
            # Check if solution is found
            if self.is_solution(best_individual):
                found_sol = True
                break

            self.tracker.append(best_fitness)
            # Generate new population
            for _ in range(self.population_size // 2):
                parent1, parent2 = self.select_parents()
                child1 = self.crossover(parent1, parent2)
                child2 = self.crossover(parent2, parent1)
                mutate_child1 = self.mutate(child1)
                mutate_child2 = self.mutate(child2)
                new_population.extend([mutate_child1, mutate_child2])
            self.population = new_population
            self.iter += 1

        self.cube = best_individual