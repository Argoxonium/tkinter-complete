import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Layout intro')
window.geometry('600x400')

# widgets 
label1 = ttk.Label(window, text = 'Position NW', background = 'red')
label2 = ttk.Label(window, text = 'Position NE', background = 'blue')
label3 = ttk.Label(window, text = 'Position SW', background = 'green')
label4 = ttk.Label(window, text = 'Position SE', background = 'yellow')
label5 = ttk.Label(window, text = 'Position 0,2', background = 'white')
label6 = ttk.Label(window, text = 'Position 1,2', background = 'orange')

# pack
# label1.pack(side = 'left', expand = True, fill = 'y')
# label2.pack(side = 'left', expand = True, fill = 'both')

# grid 
#window.columnconfigure(0, weight = 1)
#window.columnconfigure(1, weight = 1)
#window.columnconfigure(2, weight = 2)
#window.rowconfigure(0, weight = 1)
#window.rowconfigure(1, weight = 1)
#
#label1.grid(row = 0, column = 0, sticky = 'n')
#label2.grid(row = 1, column = 0, sticky = 's')
#label3.grid(row = 0, column = 1, sticky = 'e')
#label4.grid(row = 1, column = 1, sticky = 'w')
#label5.grid(row = 0, column = 2, sticky = 'nsew')
#label6.grid(row = 1, column = 2, sticky = 'nsew')

# place
#label1.place(x = 100 , y = 200, width = 200, height = 100)
#label2.place(relx = 0.5, rely = 0.5, relwidth = 1, anchor = 'se')

label1.place(relx = 0.5, rely = 0.5, anchor = 'nw')
label2.place(relx = 0.5, rely = 0.5, anchor = 'ne')
label3.place(relx = 0.5, rely = 0.5, anchor = 'sw')
label4.place(relx = 0.5, rely = 0.5, anchor = 'se')


# run
window.mainloop()