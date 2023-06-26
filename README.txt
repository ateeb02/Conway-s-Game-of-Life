Introduction to Conways Game of Life:
This is an application for Conway's gamoe of life. It simulates the real algorithm that was built by John Conway.  It is often termed as a zero player game, as it only requires initial input of cell pattern of alive and dead cells, then the game will continue itself in steps or iterations. It'll decide whether a cell will be alive or dead based on the universal algorithm. The algorithm states:

At each step in time, the following transitions occur:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules can be condensed into the following algorithm:

1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.



Application:
The current applicaton simulates the game in a 60x28 matrix that can be extended or reduced through the presets.py file. The cell size is 20 pixels and the game has 3 control buttons, start, pause and reset, that are pretty self explanatory of their functions. At the bottom you'll see the cordinates of the cell where the mouse is hovering. On the left side at the bottom there are 5 preset buttons, each of them will load a different pattern. The Size of individual cell can also be modifed in the presets.py file.

The main.py file  is the main file to execute as it contains the conway_app class responsible for the working of application. The application GUI is based on tkinter.

The algorithm is contained in conway.py file and is written in python. There is also a conway.js file in which the same algorithm is written in javascript. Ideally, in the future, the algorithm file written in python will be replpaced by the javascript file as it is much faster at processing than python which is quite slow.

In the cursor.py file, there is a function to detect mouse movement and translate it into the grid coordinates of the cells of the simulation.

In the presets.py file ther are important variables such as grid array size and grid cell size as well as the preset patterns saved as arrays.With 5 preset buttons, clicking on each of them will render a corresponding pattern, saved in the presets file, they can also be modified to output any pattern.



Bugs:
1. Clicking on preset buttons, loads a state of the pattern after one iteration. Meaning instead of the real pattern, a different pattern (of the next iteration) loads. This doesn't corrupt the output of the game since the game proceeds from the same initial conditions and results in the same output.