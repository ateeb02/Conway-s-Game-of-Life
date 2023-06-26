import numpy as np

#X-resolution(1366) / 68 = 20.08 (other sizes can be calculated using this formula)
CELL_SIZE = 20
GRID_SIZE = (60, 28)

center = np.array(GRID_SIZE) // 2
x = center[0]
y = center[1]

def glider():
    pattern = np.zeros(GRID_SIZE, dtype=int)
    pattern[x - 1, y + 1] = 1
    pattern[x,     y + 2] = 1
    pattern[x + 1, y    ] = 1
    pattern[x + 1, y + 1] = 1
    pattern[x + 1, y + 2] = 1
    print("[Pattern drawn: Glider   ]")
    return pattern

def spaceship():
    pattern = np.zeros(GRID_SIZE, dtype=int)
    pattern[x,  y - 2] = 1
    pattern[x,  y - 1] = 1
    pattern[x,  y    ] = 1
    pattern[x + 1,  y] = 1
    pattern[x + 2,  y] = 1
    pattern[x + 3,  y] = 1
    pattern[x + 1, y - 3] = 1
    pattern[x + 4, y - 3] = 1
    pattern[x + 4, y - 1] = 1
    print("[Pattern drawn: Spaceship]")
    return pattern

def toad():
    pattern = np.zeros(GRID_SIZE, dtype=int)
    pattern[x, y - 1: y + 2] = 1
    pattern[x + 1, y - 2: y + 1] = 1
    print("[Pattern drawn: Toad     ]")
    return pattern

def beacon():
    pattern = np.zeros(GRID_SIZE, dtype=int)
    pattern[x - 1, y - 1] = 1
    pattern[x    , y    ] = 1
    pattern[x + 1, y + 1] = 1
    pattern[x + 2, y + 2] = 1

    pattern[x - 1, y    ] = 1
    pattern[x    , y - 1] = 1
    pattern[x + 1, y + 2] = 1
    pattern[x + 2, y + 1] = 1
    print("[Pattern drawn: Beacon   ]")
    return pattern

def pulsar():
    pattern = np.zeros(GRID_SIZE, dtype=int)

    pattern[x - 2:x + 3, y - 1] = 1
    pattern[x - 2:x + 3, y + 1] = 1
    pattern[x - 1, y - 2:y + 3] = 1
    pattern[x + 1, y - 2:y + 3] = 1
    pattern[x - 1:x + 2, y - 1:y + 2] = 1
    pattern[x - 3:x + 4, y - 3:y + 4] = 1
    pattern[x - 3:x + 4, y - 3:y + 4] = 1
    print("[Pattern drawn: Pulsar   ]")
    return pattern
