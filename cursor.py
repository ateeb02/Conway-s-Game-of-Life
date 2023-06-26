import tkinter as tk

class MouseHoverDetector:
    def __init__(self, canvas, box_size, label):
        self.canvas = canvas
        self.box_size = box_size
        self.label = label
        self.current_box_coords = None

        self.canvas.bind("<Motion>", self.on_mouse_motion)
        print("[Cursor Tracing Active]")

    def on_mouse_motion(self, event):
        col = event.x // self.box_size
        row = event.y // self.box_size
        self.current_box_coords = (col, row)

        self.label.config(text=f"Position: {self.current_box_coords}")

    def get_current_box_coords(self):
        return self.current_box_coords
