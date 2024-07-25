import tkinter as tk
from tkinter import ttk

def button_func():
    #get the content of the entry
    print(entry.get())

    #update the label (these do the same thing)
    #label.configure(text = 'some other text')
    label['text'] = 'some other text' #for our code we need this one. 

# window
window = tk.Tk()
window.title('Getting and setting widgets')

# widgets 
label = ttk.Label(master = window, text = 'Some text')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'The button', command = button_func)
button.pack()

# run
window.mainloop()