import tkinter as tk
from tkinter import ttk

def button_func():
	print('a button was pressed')

def reset_func():
	print('hello')

# window
window = tk.Tk()
window.title('Getting and setting widgets')

# widgets 
label = ttk.Label(master = window, text = 'Some text')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

#adding a label
exercise_label = ttk.Label(master=window, text="my label")
exercise_label.pack()

button = ttk.Button(master = window, text = 'The button', command = button_func)
button.pack()

exercise_button = ttk.Button(master = window, text = 'exercise button', command = reset_func)
exercise_button.pack()

# run
window.mainloop()