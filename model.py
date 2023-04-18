import tkinter as tk
from tkinter import ttk

class CoordinatesUpdater:
    def __init__(self, window):
        self.window = window


    # Create a function to update the label with the current mouse pointer coordinates
    def update_coordinates(self):
        # Get the current mouse pointer coordinates relative to the screen
        x, y = self.window.winfo_pointerxy()

        # Convert the screen coordinates to window coordinates
        window_x = self.window.winfo_x()
        window_y = self.window.winfo_y()
        x -= window_x
        y -= window_y

        # Update the label with the current coordinates
        print(f"Mouse pointer coordinates: ({x}, {y})")

        # Schedule the next update
        self.window.after(1000, self.update_coordinates)