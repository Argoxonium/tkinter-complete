import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Three Frames Example")

# Create a main frame to hold everything
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky="nsew")

# Configure the grid layout for the main frame
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)

# Create the left frame
left_frame = ttk.Frame(main_frame, width=200, height=400, relief="sunken")
left_frame.grid(row=0, column=0, rowspan=2, sticky="ns")

# Create the top right frame
top_right_frame = ttk.Frame(main_frame, width=200, height=200, relief="raised")
top_right_frame.grid(row=0, column=1, sticky="ew")

# Create the bottom right frame
bottom_right_frame = ttk.Frame(main_frame, width=200, height=200, relief="raised")
bottom_right_frame.grid(row=1, column=1, sticky="ew")

# Add some widgets to the frames to distinguish them
ttk.Label(left_frame, text="Left Frame").grid(row=0, column=0, padx=10, pady=10)
ttk.Label(top_right_frame, text="Top Right Frame").grid(row=0, column=0, padx=10, pady=10)
ttk.Label(bottom_right_frame, text="Bottom Right Frame").grid(row=0, column=0, padx=10, pady=10)

# Configure grid weights for resizing behavior
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=3)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)

# Run the application
root.mainloop()
