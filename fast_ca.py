"""
Certainly! I'll create a Python script that calculates and saves all frames for an nxn cellular automaton with customizable "Born" and "Survive" rulesets. This script will use NumPy for efficient array operations and Matplotlib to save the frames as images. Here's the implementation:
"""
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def initialize_grid(n):
    return np.random.choice([0, 1], size=(n, n))

def apply_rules(grid, born, survive):
    n = grid.shape[0]
    new_grid = np.zeros((n, n), dtype=int)
    
    for i in range(n):
        for j in range(n):
            neighbors = np.sum(grid[max(0, i-1):min(n, i+2), max(0, j-1):min(n, j+2)]) - grid[i, j]
            if grid[i, j] == 1:
                new_grid[i, j] = 1 if neighbors in survive else 0
            else:
                new_grid[i, j] = 1 if neighbors in born else 0
    
    return new_grid

def save_frame(grid, frame_number, output_folder):
    plt.figure(figsize=(10, 10))
    plt.imshow(grid, cmap='binary')
    plt.axis('off')
    plt.savefig(output_folder / f"frame_{frame_number:04d}.png", bbox_inches='tight', pad_inches=0.1)
    plt.close()

def run_cellular_automaton(n, born, survive, num_generations, output_folder):
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    grid = initialize_grid(n)
    save_frame(grid, 0, output_folder)

    for gen in range(1, num_generations + 1):
        grid = apply_rules(grid, born, survive)
        save_frame(grid, gen, output_folder)
        print(f"Generation {gen} completed")

if __name__ == "__main__":
    # Example usage
    n = 100  # Grid size (n x n)
    born = {3}  # Cells are born if they have exactly 3 neighbors
    survive = {2, 3}  # Cells survive if they have 2 or 3 neighbors
    num_generations = 100
    output_folder = "cellular_automaton_frames"

    run_cellular_automaton(n, born, survive, num_generations, output_folder)
    print("All frames have been generated and saved.")

"""

This script does the following:

1. We import the necessary libraries: NumPy for array operations and Matplotlib for saving images.

2. The `initialize_grid` function creates a random initial grid of size n x n.

3. The `apply_rules` function applies the cellular automaton rules to the grid. It checks the number of neighbors for each cell and applies the "Born" and "Survive" rules accordingly.

4. The `save_frame` function saves the current state of the grid as an image using Matplotlib.

5. The `run_cellular_automaton` function is the main driver of the simulation. It initializes the grid, runs the simulation for the specified number of generations, and saves each frame.

6. In the `if __name__ == "__main__":` block, we set up example parameters and run the simulation.

To use this script:

1. Adjust the parameters in the `if __name__ == "__main__":` block as needed:
   - `n`: The size of the grid (n x n)
   - `born`: A set of neighbor counts for which a dead cell becomes alive
   - `survive`: A set of neighbor counts for which a live cell stays alive
   - `num_generations`: The number of generations to simulate
   - `output_folder`: The folder where the frame images will be saved

2. Run the script. It will generate and save all frames as PNG images in the specified output folder.

This implementation allows for flexible "Born" and "Survive" rulesets, making it possible to simulate various cellular automaton rules, including Conway's Game of Life (B3/S23) and other interesting variations.
"""