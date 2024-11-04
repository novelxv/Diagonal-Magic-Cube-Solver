import numpy as np
from algorithms.hill_climbing.steepest_ascent import SteepestAscent
from algorithms.hill_climbing.sideways_move import SidewaysMove
from algorithms.hill_climbing.random_restart import RandomRestart
from algorithms.hill_climbing.stochastic import Stochastic
from algorithms.simulated_annealing import SimulatedAnnealing
from algorithms.genetic_algorithm import GeneticAlgorithm
from utils.cube_visualizer import visualize_experiment
from utils.data_processing import init_cube
from utils.file_manager import save_experiment_results, load_experiment_results

def run_experiment(algorithm_class, cube, **kwargs):
    algo = algorithm_class(cube=cube, **kwargs)
    algo.run()
    results = algo.get_results()
    visualize_experiment(results, algo_name=algorithm_class.__name__)
    return results

def main():
    n = 5  
    max_iter = 10 
    
    initial_cube = init_cube(n)

    # # Eksperimen menggunakan Steepest Ascent
    # print("Running Steepest Ascent...")
    # results_sa = run_experiment(
    #     SteepestAscent,
    #     cube=initial_cube,
    #     max_iter=max_iter
    # )

    # # Eksperimen menggunakan Sideways Move
    # print("Running Sideways Move Hill Climbing...")
    # results_sm = run_experiment(
    #     SidewaysMove,
    #     cube=initial_cube,
    #     max_iter=max_iter,
    #     max_sideways_moves=100
    # )

    # # Eksperimen menggunakan Random Restart Hill Climbing
    # print("Running Random Restart Hill Climbing...")
    # results_rr = run_experiment(
    #     RandomRestart,
    #     cube=initial_cube,
    #     max_iter=max_iter,
    #     max_restart=2
    # )

    # # Eksperimen menggunakan Stochastic Hill Climbing
    # print("Running Stochastic Hill Climbing...")
    # results_sh = run_experiment(
    #     Stochastic,
    #     cube=initial_cube,
    #     max_iter=max_iter
    # )

    # Eksperimen menggunakan Simulated Annealing
    print("Running Simulated Annealing...")
    results_sa = run_experiment(
        SimulatedAnnealing,
        cube=initial_cube,
        max_iter=max_iter,
        initial_temp=1000,
        cooling_rate=0.95
    )
    save_path = save_experiment_results(results_sa, "delete-later-sa.json")

    # # Eksperimen menggunakan Genetic Algorithm
    # print("Running Genetic Algorithm...")
    # results_ga = run_experiment(
    #     GeneticAlgorithm,
    #     cube=initial_cube,
    #     max_iter=max_iter,
    #     population_size=50,
    #     mutation_rate=0.05
    # )
    # save_path = save_experiment_results(results_ga, "delete-later-ga.json")

if __name__ == "__main__":
    main()
