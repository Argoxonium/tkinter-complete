import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Menu')

#Menu
menu=tk.Menu(window)


#sub Menu
file_menu = tk.Menu(menu, tearoff = False)
file_menu.add_command(label = 'New', command = lambda: print('New File'))
file_menu.add_command(label = 'Open', command = lambda: print('Open File'))
menu.add_cascade(label = "file", menu = file_menu)

window.configure(menu = menu)

window.mainloop()