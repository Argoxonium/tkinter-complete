This is a video series from [clear code](https://www.youtube.com/watch?v=mop6g-c5HEY) on youtube for their 18 hour long video. 

# Important notes:

## Importing
There are two types of widgets within `tkinter`, `tk widgets` and which are the original ones in `ttk widgets` which are added on later. These are the ones that are more moderate in what we will be using further on. 

`ttk`is another sub-module in `tkinter`. This is what you want to be using most of the time. 
```python
import tkinter as tk
from tkinter import ttk
```
> [!bug]
> It's best to test if this code runs with importing and if you do have an error then you want to look up how to properly uninstall and install tkinter.

## Main Loop

First you want to do is create a window and then set it to a variable. Most people call the variable app, root or window. For these notes we will continue to use window.
```python
import tkinter as tk

#create a window
window = tk.Tk() #make sure its uppercase T
```
Unfortunately when you run this it's not going to create a window for that you need to **call**, using `()`, the window by running it through a main loop run command. So at the end of your initiation loop or whatever or at the end of your code you need to have the following:

```python 
#run loop
window.mainloop()
```

The main loop function does two things:
1. It updates the GUI
	Updating the GUI allows functions like text to be shown in real time so as you start typing into your keyboard GUI is updated so that you can see the text entered in the soothe box. 
2. Checks for events
	Events could be something like button clicking the mouse movement or closing a window. 

> [!info]
> Be aware that anything that comes after the main loop is not going to be initiated until after the main loop is closed for example a windows closed or an action is completed in the closest itself. Once that main loop is finalized then the following code afterwards will be initiated. 

## Forming a Window with methods
There are many different ways that you can form or modify a window within `tkinter`. Looking at more in depth methods later on but a few that will introduce currently are something like titling windows that it has a name above it and the geometry of window, meaning how big or small it is. 

Here in order to title or create the geometry of a window you will call the method itself and then have that attached to your window variable that you've called: 
```python
import tkinter as tk

#create a window
window = tk.Tk() #make sure its uppercase T

#create a title and geometry of window
window.title('Window and widgets')
window.geometry('800x500')

#run loop
window.mainloop()
```

Title refers to the nameage of the window on the top bar that will show up. Geometry refers to the size of the window in pixel length. Here you can see that it's going to be 100 by 500 in the numbers are separated by an X.

## Widgets
Calling a widget can be simple first you start out by calling it through `TK` and then the widget that you want to call. Then inside the widget you need to assign what window you're going to be placing the widget on. For example if you're going to create a widget that is a text box and you're going to be placing it on your main window you need to have it set to your window. To do this inside of your method you're going to be setting the master equal to the area or window that you want later on this will give more complicated but for now we are going to set it to the window.

```python
tk.Text(master = window)
```
To finalize this you need to initiate the pasting of the widget onto the window and this is done by using pack(). There are a couple other different methods but pack is what we're going to be using currently. Use pack you're going to be placing it in the center and it is going to be the topmost position. Therefore if you have a button that a text box and then a title that is the order that is displayed in the code that is the order that will be displayed on the window. 

```python
tk.Text(master = window).pack()
```

> [!info]
> Most times people store the text widget into its own separate variable and then pack it later. like so:
> ```python
>text = tk.Text(master = window)
>text.pack()
>```

### TTK Widgets
Initiating a `TTK widget` is the same as initiating a `TK widget` as long as you have imported it correctly as described in [[#Importing]]. Here when importing a label into your window you can see that you from the `ttk` which is pretty much used in the same manner. In addition, as stated before the order that these will be displayed onto the window is in the same order that you call it. Therefore the label from `TTK` will be displayed first then the text box.
```python
#ttk label
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

#tk text
text = tk.Text(master = window)
text.pack()
```

### Data entries
Just like when you start to learn python you want to start learning how to input data into your program and also display it. Here when you're inputting data you want to go ahead and use an entry widget which can be found in ttk then in order for something to happen you can initiate a button. And when calling a button and a boost clicked it can do something and you can get and receive that data from the entry line or from whatever the button does and allow the system to use that data in your code. Here we'll add a button and an entry widget to our code.
Entering an entry is quite simple you are just applying it to the window but when you are adding a button you can see that there is additional fields that are filled in the text that is displayed in the button in the command that is going to run a function.

> [!important]
> Notice that the command section of the button method is executing a function and not calling it using parentheses. Parentheses who give you errors you want to execute a function launch the button is pressed therefore you don't want parentheses. 


```python
import tkinter as tk
from tkinter import ttk

#functions
def button_fuc():
	print('A button was pressed')


#create a window
window = tk.Tk() #make sure its uppercase T

#create a title and geometry of window
window.title('Window and widgets')
window.geometry('800x500')

#Widgets:
#ttk label
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

#tk text
text = tk.Text(master = window)
text.pack()

#Entry and button
entry = tk.Entry(master = window)
entry.pack()
text = tk.Button(master = window, text = 'A button', command = button_func)
button.pack()

#run loop
window.mainloop()
```

> [!info]
> The command inside the button doesn't need to be a function. It can also be a lambda function as well. Lambda is good for simplistic functions.

### Getting Data
There are two major ways to get data from a widget:
1. Tkinter variables (used most of the time)
2. `.get()` method
Lots of widgets have obvious data that the user would want to get hence there is a method for example entry has a `.get()` method that returns text. For example if we mimic the similar code that we had made and create a window that has a displayable label entry and button we can use the button to capture the data within the entry field or widget. You can do this by tying the command in the button which it to a function that will pull the entry information. To do this you need to call entry the variable that you have set to `ttk.entry()` and have it use the `.get()` method.

```python
import tkinter as tk
from tkinter import ttk

def button_func():
	#get the content of the entry
	print(entry.get())

#create a window
window = tk.Tk() #make sure its uppercase T
window.title('getting and setting widgets')

#widgets
##label
label = ttk.Label(master = window, text = 'Some Text')
lebel.pack()
##entry
entry = ttk.Entry(master = window)
entry.pak()
##button
button = ttk.Button(master = window, text = 'The button', command = button_func)
button.pack()

#run loop
window.mainloop()
```

This example code will run and form a window with a label entry field and button when you input information into the entry field and press the button it will print on the terminal window the information that was inputted into the entry field. 
> [!danger]
> You do have to be careful with the `.get()` method because not a lot of widgets actually use the docket method. 


## Changing Widgets in a Loop
Every single widget in `Tkingter` has a config method. You can update information and these two methods are the same.
```python
Label.config(text='some new text')
Label['text'] = 'some new text'
```

Say that we want the label text to change when the button is pressed. Not only do we want it to change but we want it to be the same as whatever was inputted into the entry field. The way we could do this is inputting the `.config()` or `.configure()` Method within the function to update the label with the inputted text. Here we'll first look at where to input the method and change the label to 'some other text'. 

> [!caution]
> `.config()` and `.configure()` Are the same but it is believed that Config is going to be removed so it might be advantageous to use configure.

```python
import tkinter as tk
from tkinter import ttk

def button_func():
	#get the content of the entry
	print(entry.get())
	
	#Update the label text here
	label.configure(text='sone other text')
	''' or use this:
	label['text'] = 'some other text'
	'''
	

#create a window
window = tk.Tk() #make sure its uppercase T
window.title('getting and setting widgets')

#widgets
##label
label = ttk.Label(master = window, text = 'Some Text')
lebel.pack()
##entry
entry = ttk.Entry(master = window)
entry.pak()
##button
button = ttk.Button(master = window, text = 'The button', command = button_func)
button.pack()

#run loop
window.mainloop()
```

Now that we know where the label configure method is going to be placed we know that the update function is going to be the same. Using the button function we will extract the text from the entry into a variable and then use that as our replacement piece for the configure. 
```python
def button_func():
	#get the content of the entry
	entry_text = entry.get())
	
	#Update the label text here
	label['text'] = entry_text
	
```

But you can do additional things with the configure method like determine the state of the widget. Say if the entry widget is filled with text and you wanted it to be disabled when it has text filled. You could set the status of the entry widget within the function like so:
```python
def button_func():
	#get the content of the entry
	entry_text = entry.get())
	
	#Update the label text here
	label['text'] = entry_text
	entry['state'] = 'dosabled'
	
```

## `Tkinter` Variables
`tkinter` variables are probably something that you want to use most of the time. Since `Tkinter` has inbuilt variables that are designed to work with widgets. They are automatically updated by the widget and they update a widget. Although they still store basic data like strings, integers and Booleans. Here we will use strings as an example. 
For an example program let's make a label that should always have the same text as the entry at all times. Basically we are creating a **StringVar**. The string variable will automatically be set from the entry widget and will automatically set this string for the label.
![[Pasted image 20240725151042.png]]

In order to perform this connection we're going to create a window that has label and entry. In order to connect the label in the entry so that the label displays whatever is in the entry we will need to use a `.StringVar()` That is set to a variable. Within both the label and the entry we are actually going to add another argument called text variable and set it equal to our `.StringVar()` 
variable. This way the entry will be automatically updating the text variable argument while the label will have an override to the text argument with the text variable argument. 

```python
import tkinter as tk
from tkinter import ttk

#Window
window = tk.Tk()
window.title('Tkinter Variables')

#tkinter variable
string_var = tk.StringVar()

#widgets
label = ttk.Label(master = window, text = 'label', textvariable = string_var)
label.pack()
entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

#run
window.mainloop()
```

In addition you could create another entry variable called entry variable two and have that set to the entry widget. Then that witch's argument for the text variable could also be set to the string var variable and All the widgets would be set to the same string variable at all times. 

You can even go beyond this and pull the string variable and get the information from it. If you used a button and set the command to the button function and within that button function your printing the string variable with `.get()`, You will receive the string variable that is currently in that variable imprinted out. Below is an example of what the button code would look like and the function. Not only can you get information when you press the button but also you can set information with the `.set()` method. Therefore after the button is pressed it will change the string variable after recording and printing to the terminal what was already in the sting variable. 

```python
def button_func():
	print(string_var.get())
	string_var.set('button pressed')

button = ttk.Button(master = window, text = 'button', command = button_func)
button.pack()
```

