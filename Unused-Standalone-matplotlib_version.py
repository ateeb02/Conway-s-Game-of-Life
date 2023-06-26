import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the size of the initial grid
initial_grid_size = (100, 100)

# Set up the initial configuration
initial_grid = np.zeros(initial_grid_size, dtype=int)

# Set the initial live cells
initial_live_cells = [(2, 3), (3, 3), (4, 3), (4, 2), (3, 1)]

# Populate the initial live cells
for cell in initial_live_cells:
    initial_grid[cell] = 1

# Define the neighbors' relative positions
neighbor_offsets = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

# Function to get the neighbors of a cell
def get_neighbors(cell):
    x, y = cell
    neighbors = [(x + dx, y + dy) for dx, dy in neighbor_offsets]
    return neighbors

# Function to update the grid for each generation
def update_grid():
    global initial_grid

    # Create a new grid with extended size
    new_grid_size = (initial_grid.shape[0] + 2, initial_grid.shape[1] + 2)
    new_grid = np.zeros(new_grid_size, dtype=int)

    # Copy the existing grid to the new grid
    new_grid[1:-1, 1:-1] = initial_grid

    # Iterate over each cell in the new grid
    for i in range(1, new_grid_size[0] - 1):
        for j in range(1, new_grid_size[1] - 1):
            cell = (i, j)
            neighbors = get_neighbors(cell)

            # Count the number of alive neighbors
            alive_neighbors = sum(new_grid[n] for n in neighbors)

            # Apply the rules of the Game of Life
            if new_grid[i, j] == 1:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    initial_grid[i - 1, j - 1] = 0
            else:
                if alive_neighbors == 3:
                    initial_grid[i - 1, j - 1] = 1

# Function to generate the next generation
def generate_next_generation(frame):
    update_grid()
    ax.clear()
    ax.imshow(initial_grid, cmap='binary')

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, generate_next_generation, frames=50, interval=50)

# Display the animation
plt.show()
