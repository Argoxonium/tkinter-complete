import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack parenting')
window.geometry('400x600')

top_frame = ttk.Frame()
bottom_frame = ttk.Frame()
#widgets
label1 = ttk.Label(top_frame, text = 'First label', background = 'red')
label2 = ttk.Label(top_frame, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Another label', background = 'green')
label4 = ttk.Label(bottom_frame, text = 'Last of the labels', background = 'orange')
button = ttk.Button(bottom_frame, text = 'A Button')
button2 = ttk.Button(bottom_frame, text = 'Another Button')

#top layout pack
label1.pack(side = "left", fill = 'both', expand = True)
label2.pack(side = "left", fill = 'both', expand = True)
top_frame.pack(fill = 'both', expand = True)

#middle layout pack
label3.pack(expand = True)

#bottom layout pack
button.pack(side = 'left', expand = True, fill = "both")
label4.pack(side = 'left', expand = True, fill = "both")
button2.pack(side = 'left', expand = True, fill = "both")
bottom_frame.pack(expand = True, fill = "both", padx = 20, pady = 20)

window.mainloop()