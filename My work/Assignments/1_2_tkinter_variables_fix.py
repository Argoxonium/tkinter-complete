import tkinter as tk
from tkinter import ttk

# window 
window = tk.Tk()
window.title('Tkinter Variables')

# tkinter variable
string_var = tk.StringVar()

# widgets 
label = ttk.Label(master = window, text = 'label', textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()


# run 
window.mainloop()

