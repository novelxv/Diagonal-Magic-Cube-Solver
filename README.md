# Diagonal-Magic-Cube-Solver

## Table of Contents

- [Description](#description)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running the Program](#running-the-program)
- [Features](#features)
- [Demo Video](#demo-video)
- [Team Members and Responsibilities](#team-members-and-responsibilities)

---

## Description

This repository contains the **Diagonal Magic Cube Solver**, a project that aims to solve and visualize various configurations of a 3D magic cube using multiple search algorithms. The solver includes a variety of local search and optimization algorithms such as Hill Climbing, Simulated Annealing, and Genetic Algorithm to find optimal or near-optimal solutions. The project also provides an interactive GUI to replay and visualize the solution process iteratively.

---

## Project Structure

The project is organized as follows:
```
Diagonal-Magic-Cube-Solver/
│
├── src/
│   ├── algorithms/
│   │   ├── __init__.py
│   │   ├── base_algorithm.py
│   │   ├── hill_climbing/
│   │   │   ├── steepest_ascent.py
│   │   │   ├── sideways_move.py
│   │   │   ├── random_restart.py
│   │   │   └── stochastic.py
│   │   ├── simulated_annealing.py
│   │   └── genetic_algorithm.py
│   │
│   ├── utils/
│   │   ├── cube_visualizer.py
│   │   ├── file_manager.py
│   │   └── data_processing.py
│   │
│   ├── experiments/
│   │   └── experiment_runner.py
│   │
│   ├── replay/
│   │   └── player.py
│   │
│   └── main.py
│
├── assets/
│   └── results/
│      ├── graphs/
│      └── results/
│
├── docs/
│   └── Tubes1_Kelompok1.pdf
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Setup and Installation

Follow these steps to set up the project:

### Prerequisites
- Python 3.10 or above
- `pip` (Python package installer)

### Install Dependencies
Install all required dependencies using the following command:
```bash
pip install -r requirements.txt
```

### Run the Program
To run the program, execute the following command:
```bash
python src/main.py
```

This will open the terminal interface, where you can choose either to:
- Run an experiment with a selected algorithm and parameters.
- Replay a previously saved experiment in the GUI.

---

## Running the Program

1. **Run Experiment**: 
   - Follow the prompts to specify cube size, maximum iterations, algorithm choice, and algorithm-specific parameters.
   - Results will be displayed in the console and saved in the `assets/results` directory.

2. **Replay Experiment**:
   - Select this option to load and replay an existing experiment file.
   - The GUI will allow you to visualize each iteration, adjust speed, and track progress.

---

## Features

- **Multiple Algorithms**: Implements a variety of local search and optimization algorithms.
- **Interactive Replay**: GUI to replay experiments, visualize cube states at each iteration, and control playback.
- **Configurable Parameters**: Allows customization of algorithm parameters such as max iterations, restarts, and mutation rates.
- **Experiment Tracking**: Saves results of each experiment, including initial and final states, iteration history, and performance metrics.

---

## Demo Video

Here is a short demo video showcasing the interactive replay feature of the Diagonal Magic Cube Solver:
![Demo Video](assets/demo.gif)

---

## Team Members and Responsibilities

**Kelompok 1:**

| Name              | NIM          | Task Description                                                                                                                                             |
|-------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Nabila Shikoofa Muida**    | 13522069      | base_algorithm.py, steepest_ascent.py, sideways_move.py, laporan                                                                                    |
| **Novelya Putri Ramadhani**    | 13522096      | genetic_algorithm.py, cube_visualizer.py, file_manager.py, main.py, replay/
| **Hayya Zuhailii Kinasih**    | 13522102      | random_restart.py, stochastic.py, experiments/, assets/
| **Diana Tri Handayani**    | 13522104      | simulated_annealing.py, data_processing.py, laporan

---