import matplotlib.pyplot as plt
import numpy as np

def display_cube(cube: np.ndarray, title: str = "State"):
    """ Display the cube """
    print(title)
    print("----------")
    for layer in cube:
        print(layer)
        print()

def plot_obj_vs_iter(tracker: list, title: str = "Objective Function vs Iterations"):
    """ Plot the objective function vs iterations """
    plt.figure()
    plt.plot(range(len(tracker)), tracker, marker='o', linestyle='-', color='b')
    plt.xlabel("Iterations")
    plt.ylabel("Objective Function Value")
    plt.title(title)
    plt.show()

def plot_prob_vs_iter(prob_values: list, title="Probability (e^ΔE/T) vs Iterations"):
    """ Plot the probability values vs iterations """
    plt.figure()
    plt.plot(range(len(prob_values)), prob_values, marker='x', linestyle='--', color='g')
    plt.xlabel("Iterations")
    plt.ylabel("Probability (e^ΔE/T)")
    plt.title(title)
    plt.show()

def visualize_experiment(results, algo_name="Algorithm"):
    """ Visualize the results of the experiment """
    print(f"\nVisualization for {algo_name}\n")
    # Display the initial and final state of the cube
    display_cube(results["initial_state"], title="Initial State")
    display_cube(results["final_state"], title="Final State")
    # Plot the objective function vs iterations
    plot_obj_vs_iter(results["tracker"], title=f"{algo_name} - Objective Function vs Iterations")
    # Print the results
    print(f"Initial Objective Value: {results['initial_value']}")
    print(f"Final Objective Value: {results['final_value']}")
    print(f"Iterations: {results['iterations']}")
    print(f"Duration: {results['duration']}")
    # Print additional results of Simulated Annealing Algorithm
    if "prob_values" in results and "stuck_freq" in results:  
        plot_prob_vs_iter(results["prob_values"], title=f"{algo_name} - Probability (e^ΔE/T) vs Iterations")
        print(f"Stuck Frequency (Local Optima): {results['stuck_freq']}")
    # Print additional results of Genetic Algorithm
    if "population_size" in results:  
        print(f"Population Size: {results['population_size']}")
    # Print additional results of Random Restart Algorithm
    if "restarts" in results and "iter_per_restart" in results:  
        print(f"Restarts: {results['restarts']}")
        print(f"Iterations per Restart: {results['iter_per_restart']}")