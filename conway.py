import numpy as np

def conway_step(grid):
    new_grid = np.copy(grid)
    rows, cols = grid.shape
    for i in range(rows):
        for j in range(cols):
            live_neighbors = np.sum(grid[max(0, i-1):min(i+2, rows), max(0, j-1):min(j+2, cols)]) - grid[i, j]
            if grid[i, j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and live_neighbors == 3:
                new_grid[i, j] = 1
    return new_grid
