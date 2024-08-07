import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack parenting')
window.geometry('400x600')

# Top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text = 'First label', background = 'red')
label2 = ttk.Label(top_frame, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Another label', background = 'green')
label4 = ttk.Label( text = 'Last of the labels', background = 'orange')
button = ttk.Button( text = 'A Button')
button2 = ttk.Button( text = 'Another Button')
