import numpy as np
from itertools import combinations

def init_cube(n: int) -> np.ndarray:
    numbers = np.arange(1, n**3 + 1)
    np.random.shuffle(numbers)
    return numbers.reshape((n, n, n))

def get_rows(cube: np.ndarray) -> np.ndarray:
    n = cube.shape[0]
    rows = []
    for layer in range(n):
        for row in range(n):
            rows.append(cube[layer, row, :])
    return np.array(rows)

def get_cols(cube: np.ndarray) -> np.ndarray:
    n = cube.shape[0]
    cols = []
    for layer in range(n):
        for col in range(n):
            cols.append(cube[layer, :, col])
    return np.array(cols)

def get_pillars(cube: np.ndarray) -> np.ndarray:
    n = cube.shape[0]
    pills = []
    for row in range(n):
        for col in range(n):
            pills.append(cube[:, row, col])
    return np.array(pills)

def get_side_diagonals(cube: np.ndarray) -> np.ndarray:
    n = cube.shape[0]
    diagonals = []

    # diagonal sisi tiap layer
    for layer in range(n):
        diagonals.append([cube[layer, i, i] for i in range(n)])
        diagonals.append([cube[layer, i, n-i-1] for i in range(n)])

    # diagonal sisi tiap baris
    for row in range(n):
        diagonals.append([cube[i, row, i] for i in range(n)])
        diagonals.append([cube[i, row, n-i-1] for i in range(n)])

    # diagonal sisi tiap kolom
    for col in range(n):
        diagonals.append([cube[i, i, col] for i in range(n)])
        diagonals.append([cube[i, n-i-1, col] for i in range(n)])

    return np.array(diagonals)

def get_space_diagonals(cube: np.ndarray) -> np.ndarray:
    n = cube.shape[0]
    diagonals = []
    diagonals.append([cube[i, i, i] for i in range(n)])
    diagonals.append([cube[i, i, n-i-1] for i in range(n)])
    diagonals.append([cube[i, n-i-1, i] for i in range(n)])
    diagonals.append([cube[i, n-i-1, n-i-1] for i in range(n)])
    return np.array(diagonals)

def evaluate_cube(cube: np.ndarray) -> int:
    n = cube.shape[0]
    magic_number = 1/2 * n * (n**3 + 1)
    h = 0

    rows = get_rows(cube)
    cols = get_cols(cube)
    pills = get_pillars(cube)
    side_diagonals = get_side_diagonals(cube)
    space_diagonals = get_space_diagonals(cube)

    for component in [rows, cols, pills, side_diagonals, space_diagonals]:
        for c in component:
            h -= abs(np.sum(c) - magic_number)

    return h

def swap(cube: np.ndarray, a: tuple, b: tuple) -> np.ndarray:
    cube = cube.copy()
    cube[a], cube[b] = cube[b], cube[a]
    return cube

def random_swap(cube: np.ndarray) -> np.ndarray:
    n = cube.shape[0]
    a = np.random.randint(0, n, 3)
    b = np.random.randint(0, n, 3)
    while np.array_equal(a, b):
        b = np.random.randint(0, n, 3)
    return swap(cube, tuple(a), tuple(b))

def best_neighbor(cube: np.ndarray) -> np.ndarray:
    n = cube.shape[0]
    best_neighbor = cube.copy()
    best_value = evaluate_cube(swap(cube, (0, 0, 0), (0, 0, 1)))

    indices = [(i, j, k) for i in range(n) for j in range(n) for k in range(n)]
    for (i, j, k), (x, y, z) in combinations(indices, 2):
        neighbor = swap(cube, (i, j, k), (x, y, z))
        neighbor_value = evaluate_cube(neighbor)
        if neighbor_value > best_value:
            best_neighbor = neighbor
            best_value = neighbor_value

    return best_neighbor

def is_goal(cube: np.ndarray) -> bool:
    return evaluate_cube(cube) == 0