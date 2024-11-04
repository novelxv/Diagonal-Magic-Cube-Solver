from algorithms.hill_climbing.steepest_ascent import SteepestAscent
from algorithms.hill_climbing.sideways_move import SidewaysMove
from algorithms.hill_climbing.random_restart import RandomRestart
from algorithms.hill_climbing.stochastic import Stochastic
from algorithms.simulated_annealing import SimulatedAnnealing
from algorithms.genetic_algorithm import GeneticAlgorithm
from utils.cube_visualizer import visualize_experiment
from utils.data_processing import init_cube
from utils.file_manager import save_experiment_results
from replay.player import ReplayPlayer
import tkinter as tk

def run_experiment(algorithm_class, cube, **kwargs):
    algo = algorithm_class(cube=cube, **kwargs)
    algo.run()
    results = algo.get_results()
    visualize_experiment(results, algo_name=algorithm_class.__name__)
    return results

def get_user_input():
    print("Choose Mode:")
    print("1. Run Experiment")
    print("2. Replay Experiment")
    mode = input("Enter choice (1 or 2): ")

    if mode == '1':
        n = int(input("Enter cube size: "))
        max_iter = int(input("Enter max iterations: "))

        print("\nChoose Algorithm:")
        print("1. Steepest Ascent Hill Climbing")
        print("2. Hill Climbing with Sideways Move")
        print("3. Random Restart Hill Climbing")
        print("4. Stochastic Hill Climbing")
        print("5. Simulated Annealing")
        print("6. Genetic Algorithm")
        algo_choice = input("Enter choice (1-6): ")

        algorithm_params = {"max_iter": max_iter}
        if algo_choice == '2':
            algorithm_params["max_sideways_moves"] = int(input("Enter max sideways moves: "))
        elif algo_choice == '3':
            algorithm_params["max_restart"] = int(input("Enter max restarts: "))
        elif algo_choice == '5':
            algorithm_params["initial_temp"] = float(input("Enter initial temperature: "))
            algorithm_params["cooling_rate"] = float(input("Enter cooling rate (e.g., 0.95): "))
        elif algo_choice == '6':
            algorithm_params["population_size"] = int(input("Enter population size: "))
            algorithm_params["mutation_rate"] = float(input("Enter mutation rate (e.g., 0.05): "))

        return "experiment", n, algo_choice, algorithm_params

    elif mode == '2':
        return "replay",
    else:
        print("Invalid choice.")
        return None

def main():
    user_input = get_user_input()
    if user_input is None:
        return

    mode = user_input[0]

    if mode == "experiment":
        _, n, algo_choice, algorithm_params = user_input
        initial_cube = init_cube(n)
        
        algorithm_mapping = {
            '1': SteepestAscent,
            '2': SidewaysMove,
            '3': RandomRestart,
            '4': Stochastic,
            '5': SimulatedAnnealing,
            '6': GeneticAlgorithm
        }
        algorithm_class = algorithm_mapping.get(algo_choice)

        if algorithm_class is None:
            print("Invalid algorithm choice.")
            return

        print(f"Running {algorithm_class.__name__}...")
        results = run_experiment(algorithm_class, cube=initial_cube, **algorithm_params)
        filename = f"{algorithm_class.__name__}_results.json"
        save_path = save_experiment_results(results, filename)
        print(f"Results saved to {save_path}")

    elif mode == "replay":
        root = tk.Tk()
        root.title("Diagonal Magic Cube Replay Player")
        player = ReplayPlayer(root, {}) 
        root.mainloop()

if __name__ == "__main__":
    main()
