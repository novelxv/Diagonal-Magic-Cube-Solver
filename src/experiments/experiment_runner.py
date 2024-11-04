from utils.cube_visualizer import visualize_experiment
from utils.data_processing import init_cube
from utils.file_manager import save_experiment_results
from algorithms.hill_climbing.random_restart import RandomRestart
from algorithms.hill_climbing.sideways_move import SidewaysMove
from algorithms.hill_climbing.steepest_ascent import SteepestAscent
from algorithms.hill_climbing.stochastic import Stochastic
from algorithms.genetic_algorithm import GeneticAlgorithm
from algorithms.simulated_annealing import SimulatedAnnealing

def run_experiment(algorithm_class, cube, **kwargs):
    algo = algorithm_class(cube=cube, **kwargs)
    algo.run()
    results = algo.get_results()
    visualize_experiment(results, algo_name=algorithm_class.__name__)
    return results

def run_all():
    cube = init_cube(5)
    n_experiments = 3
    max_iter = 25

    max_iters = [15, 25, 50]
    # steepest ascent
    for i in range(n_experiments):
        result = run_experiment(SteepestAscent, cube=cube, max_iter=max_iters[i])
        save_experiment_results(result, f'steepest_{i+1}.json')
    
    # sideways move
    max_sideways = [5, 10, 25]
    for i in range(n_experiments):
        result = run_experiment(SidewaysMove, cube=cube, max_iter=max_iter,
                                max_sideways_moves=max_sideways[i])
        save_experiment_results(result, f'sideways_{i+1}.json')

    # random restart
    for i in range(n_experiments):
        result = run_experiment(RandomRestart, cube=cube, max_iter=max_iter,
                                max_restart=5)
        save_experiment_results(result, f'restart_{i+1}.json')

    max_iters = [1000, 2000, 5000]
    
    # stochastic
    for i in range(n_experiments):
        result = run_experiment(Stochastic, cube=cube, max_iter=max_iters[i])
        save_experiment_results(result, f'stochastic_{i+1}.json')
    
    # simulated annealing
    initial_temp = 1000
    cooling_rate = 0.95
    for i in range(n_experiments):
        result = run_experiment(SimulatedAnnealing, cube=cube, max_iter=max_iters[i],
                                initial_temp=initial_temp, cooling_rate=cooling_rate)
        save_experiment_results(result, f'sa_{i+1}.json')
    
    # genetic algorithm
    population_size = [50, 100, 200]

    for i in range(n_experiments):
        for j in range(n_experiments):
            result = run_experiment(GeneticAlgorithm, cube=cube, max_iter=max_iters[i],
                                    population_size=population_size[1], mutation_rate=0.05)
            save_experiment_results(result, f'ga_pop_size_control_{i+1}{j+1}.json')
    
    for i in range(n_experiments):
        for j in range(n_experiments):
            result = run_experiment(GeneticAlgorithm, cube=cube, max_iter=max_iters[1],
                                    population_size=population_size[i], mutation_rate=0.05)
            save_experiment_results(result, f'ga_iter_control_{i+1}{j+1}.json')
        
