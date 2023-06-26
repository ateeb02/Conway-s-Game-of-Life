import numpy as np
import tkinter as tk
import presets as prs
from conway import conway_step
from presets import GRID_SIZE, CELL_SIZE
from cursor import MouseHoverDetector

#GRID_SIZE defined in presets.py
#CELL_SIZE defined in presets.py


class GameOfLifeApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Conway's Game of Life")
        self.root.configure(bg='#222222')
        self.running = False
        print("[Launching Conway's Game Of Life]")
        print("[Drawing the Canvas]")
        # Create the canvas for drawing the grid
        self.canvas = tk.Canvas(self.root, width=GRID_SIZE[0] * CELL_SIZE, height=GRID_SIZE[1] * CELL_SIZE,
                                bg='#222222', highlightthickness=0)
        self.canvas.pack()

        # Create the buttons
        start_button = tk.Button(self.root, text='Start', command=self.start, bg='#444444', fg='#ffffff',
                                 relief='flat', font=('Arial', 14))
        start_button.pack(side='left', padx=10, pady=10)

        pause_button = tk.Button(self.root, text='Pause', command=self.pause, bg='#444444', fg='#ffffff',
                                 relief='flat', font=('Arial', 14))
        pause_button.pack(side='left', padx=10, pady=10)

        reset_button = tk.Button(self.root, text='Reset', command=self.reset, bg='#444444', fg='#ffffff',
                                 relief='flat', font=('Arial', 14))
        reset_button.pack(side='left', padx=10, pady=10)

        #Presets buttons:
        preset_1 = tk.Button(self.root, text='Glider', command=self.preset1, bg='#444444', fg='#ffffff',
                                 relief='flat', font=('Arial', 14))
        preset_1.pack(side='right', padx=10, pady=10)

        preset_2 = tk.Button(self.root, text='Spaceship', command=self.preset2, bg='#444444', fg='#ffffff',
                                 relief='flat', font=('Arial', 14))
        preset_2.pack(side='right', padx=10, pady=10)

        preset_3 = tk.Button(self.root, text='Toad', command=self.preset3, bg='#444444', fg='#ffffff',
                                 relief='flat', font=('Arial', 14))
        preset_3.pack(side='right', padx=10, pady=10)

        preset_4 = tk.Button(self.root, text='Beacon', command=self.preset4, bg='#444444', fg='#ffffff',
                                 relief='flat', font=('Arial', 14))
        preset_4.pack(side='right', padx=10, pady=10)

        preset_5 = tk.Button(self.root, text='Pulsar', command=self.preset5, bg='#444444', fg='#ffffff',
                                 relief='flat', font=('Arial', 14))
        preset_5.pack(side='right', padx=10, pady=10)

        # Initialize the grid with zeros
        self.grid = np.zeros(GRID_SIZE, dtype=int)

        # Build the fixed grid for subsequent calculations
        self.fixed_grid = np.zeros(GRID_SIZE, dtype=int)

        # Draw the initial grid
        self.draw_grid()

        # Bind mouse events to the canvas
        self.canvas.bind('<Button-1>', self.on_mouse_click)
        self.canvas.bind('<B1-Motion>', self.on_mouse_drag)

        author_label = tk.Label(self.root, text="Built By: Ateeb Tahir", bg='#222222', fg='#ffffff',
                        font=('Century Gothic', 11))
        author_label.pack(side='bottom', padx=5, pady=2)

        coords_label = tk.Label(self.root, text="", bg='#444444', fg='#ffffff',
                        font=('Arial', 12))
        coords_label.pack(side='bottom', padx=10, pady=5)
        hover_detector = MouseHoverDetector(self.canvas, CELL_SIZE, coords_label)


    #Preset functions to call the preset shapes
    def preset1(self):
        """Projects Glider on Canvas"""
        self.grid = prs.glider()
        self.running = True
        self.update()
        self.running = False
        
    def preset2(self):
        """Projects Spaceship on Canvas"""
        self.grid = prs.spaceship()
        self.running = True
        self.update()
        self.running = False

    def preset3(self):
        """Projects Toad on Canvas"""
        self.grid = prs.toad()
        self.running = True
        self.update()
        self.running = False

    def preset4(self):
        """Projects Beacon on Canvas"""
        self.grid = prs.beacon()
        self.running = True
        self.update()
        self.running = False

    def preset5(self):
        """Projects Pulsar on Canvas"""
        self.running = True
        self.grid = prs.pulsar()
        self.update()
        self.running = False

    def start(self):
        """Start the simulation."""
        self.running = True
        self.update()
        print("[Running the Simulation]")

    def pause(self):
        """Pause the simulation."""
        self.running = False
        print("[Pause Call]")


    def reset(self):
        """Reset the grid to all zeros and clear the selected preset."""
        self.running = False
        self.grid = np.zeros(GRID_SIZE, dtype=int)
        self.fixed_grid = np.zeros(GRID_SIZE, dtype=int)
        self.selected_preset = None
        self.draw_grid()
        print("[Reset Call]")

    def update(self):
        """Update the grid and redraw it."""
        if self.running:
            self.grid = conway_step(self.grid)
            self.fixed_grid = np.copy(self.grid)
            self.draw_grid()
            self.root.after(50, self.update)

    def draw_grid(self):
        """Draw the grid on the canvas."""
        self.canvas.delete('rect')

        for i in range(GRID_SIZE[0]):
            for j in range(GRID_SIZE[1]):
                if self.fixed_grid[i, j] == 1:
                    color = '#ffffff'
                else:
                    color = '#222222'

                x1 = i * CELL_SIZE
                y1 = j * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='#444444', tags='rect')
                #print("[Grid Drawn]")

    def on_mouse_click(self, event):
        """Handle mouse click event to toggle cell state."""
        x = event.x // CELL_SIZE
        y = event.y // CELL_SIZE
        self.toggle_cell(x, y)

    def on_mouse_drag(self, event):
        """Handle mouse drag event to toggle cell state."""
        x = event.x // CELL_SIZE
        y = event.y // CELL_SIZE
        self.toggle_cell(x, y)

    def toggle_cell(self, x, y):
        """Toggle the state of the cell at the given coordinates."""
        if 0 <= x < GRID_SIZE[0] and 0 <= y < GRID_SIZE[1]:
            self.grid[x, y] = 1 - self.grid[x, y]
            self.fixed_grid[x, y] = self.grid[x, y]
            self.draw_cell(x, y)

    def draw_cell(self, x, y):
        """Draw the state of the cell at the given coordinates."""
        if self.fixed_grid[x, y] == 1:
            color = '#ffffff'
        else:
            color = '#222222'

        x1 = x * CELL_SIZE
        y1 = y * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='#444444', tags='rect')

    
if __name__ == '__main__':
    app = GameOfLifeApp()
    app.root.mainloop()



