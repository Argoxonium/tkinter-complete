import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Combined layout')
window.geometry('600x600')
window.minsize(600,600)

#main layout widgets
#these are the widgets/frames that will contain everything else.
menu_frame = ttk.Frame(window)
main_frame = ttk.Frame(window)

#Place the main layout
menu_frame.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)
main_frame.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)

#label examples
ttk.Label(menu_frame, background = 'red').pack(expand = True, fill = 'both')
ttk.Label(main_frame, background = 'blue').pack(expand = True, fill = 'both')


#run
window.mainloop()