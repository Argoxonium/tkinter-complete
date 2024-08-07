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

# Widgets
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


## Configuring Widgets in a Loop
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

## Buttons
There are three kinds of buttons used in `tkinter` witch are **Buttons, Checkbuttons, and Radiobuttons**. To use any button properly you need `tkinter` variables. Here we will show what we already have seen before, where there is a window and a basic button that has a name and prints text when pressed. In addition we are going to attach a stringvar to it. 

> [!info]
> The first argument of any button is what is the master. Therefore you can just type `window` and it be the same as `master = window`.

```python
import tkinter as tk
from tkinter import ttk

#Window
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

#Basic Button
def button_func():
	print('a basic button')

#stringvar
button_string = tl.StringVar(value = 'A button with string var')

button = ttk.Button(winow, text = 'A simple button', command = button_func)

...

#run
window.mainloop()
```

### Checkbox
When we want to add a checkbox button its similar to a button; we use ttk, and need to set the same arguments. 
```python
import tkinter as tk
from tkinter import ttk

...

check = ttk.Checkbutton(window, text = 'checkbox1', command = lambda: print('hello'))
check.pack()

...

```
Though what happens when we do `check.get()`? unfortunately we get an error. In order to get a value we need a `tk variable`. for in this case we can use a string var. **But** there is no textvariable with a checkbox, just a variable. This is because we aren't going to change the text variable but we are going to store weather this variable exists or not. Then in that case we can use `.get()` with our variable. 

```python
import tkinter as tk
from tkinter import ttk

...
check_var = tk.StringVar()
check = ttk.Checkbutton(window, 
						text = 'checkbox1', 
						command = lambda: print(check_var.get())
						Variable = check_var)
check.pack()

...

```

This this case when we print this it will return a 1 or 0. but instead we can also use an `.IntVar()`. Storing an integer var. or we can run a `tk.BooleanVar()` to return True or False.
But what if you don't want to return an 1 or 0. well you can edit this with the `onvalue` & `offvalue` arguments in the a check button.
```python
import tkinter as tk
from tkinter import ttk

...
check_var = tk.StringVar()
check = ttk.Checkbutton(window, 
						text = 'checkbox1', 
						command = lambda: print(check_var.get())
						Variable = check_var,
						onvalue = 10,
						offvalue = 5)
check.pack()

...

```

### Radio Button
Just like the two other buttons you use `ttk.Radiobuttion` to create a button, set it to window and describe its text. Though something weird happens when you create a radio button this way. If you click one, it also checks the other button. 

```python
import tkinter as tk
from tkinter import ttk

...
radio1 = ttk.Radiobuttion(window, text = 'Radiobuttion 1')
radio1.pack()
radio2 = ttk.Radiobuttion(window, text = 'Radiobuttion 2')
radio2.pack()
...

```

> [!important]
> Each Radio button needs its own value!

The default value is always 0 and if you have the same value it returns both checks. 

```python
import tkinter as tk
from tkinter import ttk

...
radio1 = ttk.Radiobuttion(window, text = 'Radiobuttion 1', value = 'radio1)
radio1.pack()
radio2 = ttk.Radiobuttion(window, text = 'Radiobuttion 2', value = 2)
radio2.pack()
...

```

And just like the other buttons, you can set a command and just like the checkbox, you need to set variables to do `.get()`. A radio button is set up the same way as a checkbox but the major difference is that only one variable can be true. This means that if we attach this to the `button_func()` and print it after checking a ratio button, it will only display that variable for that button. Unlike a checkbox where multiple can be true. 

```python
import tkinter as tk
from tkinter import ttk

...
radio_var = tk.StringVar()

radio1 = ttk.Radiobuttion(window, 
						  text = 'Radiobuttion 1', 
						  value = 'radio1',
						  variable = radio_var,
						  command = lambda: print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobuttion(window, 
						  text = 'radio 2', 
						  value = 2,
						  variable = radio_var,
						  command = lambda: print(radio_var.get()))
radio2.pack()
...

```

This is the code together to demonstrate that you can have multiple check boxes while the radio cannot. 

```python
import tkinter as tk
from tkinter import ttk

#Window
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

#Basic Button
def button_func():
	print('a basic button')
	print(radio_var.get())

#stringvar
button_string = tl.StringVar(value = 'A button with string var')

button = ttk.Button(winow, text = 'A simple button', command = button_func)

check_var = tk.StringVar()
check1 = ttk.Checkbutton(window, 
						text = 'checkbox1', 
						command = lambda: print(check_var.get())
						Variable = check_var,
						onvalue = 10,
						offvalue = 5)
check1.pack()

check2 = ttk.Checkbutton(window, 
						text = 'checkbox1', 
						command = lambda: print(check_var.get()))
check2.pack()

radio_var = tk.StringVar()

radio1 = ttk.Radiobuttion(window, 
						  text = 'Radiobuttion 1', 
						  value = 'radio1',
						  variable = radio_var,
						  command = lambda: print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobuttion(window, 
						  text = 'radio 2', 
						  value = 2,
						  variable = radio_var,
						  command = lambda: print(radio_var.get()))
radio2.pack()

#run
window.mainloop()
```

But if you wanted to have the check buttons connected you can set the value to the `offvalue`. So you can if you want to but radios are always connected. This is because `tkinter` is going to check if the variable is equal to the value of the radio button and if it is it will check it. This is what happens when you want to have multiple checks. 
```python
check_var = tk.StringVar()
check1 = ttk.Checkbutton(window, 
						text = 'checkbox1', 
						command = lambda: print(check_var.get())
						Variable = check_var,
						onvalue = 10,
						offvalue = 5)
check1.pack()

check2 = ttk.Checkbutton(window, 
						text = 'checkbox1', 
						command = lambda: check_var.set(5))
check2.pack()
```

#### create another checkbutton and 2 radiobuttons
radio button:
- values for the buttons are A and B
- ticking either prints the value of the checkbutton
- ticking the radio button unchecks the checkbutton

check button:
- ticking the checkbutton prints the value of the radio button value
- use tkinter var for Booleans!
```python
#data
der radio_func():
	print(check_bool.get())
	check_var.set(False)
	
#widgets
radio_string = tk.StingVar()
radio_1 = ttk.Radiobutton(window,
						text = 'check button1',
						Variable = radio_var,
						value = 'A',
						command = radio_func)

radio_2 = ttk.Radiobutton(window,
						text = 'check button2',
						Variable = radio_var,
						value = 'B',
						command = radio_func)

check_var = tk.BooleanVar()
check = ttk.Checkbutton(window, 
					   text = 'check buttion',
					   variable = check_var,
					   command = lambda: print(radio_string.get()))
					   
#layout
radio_1.pack()
radio_2.pack()
check.pack()

```


## Functions with Arguments
Though we have already done this. How? with `lambda:`! Therefore, if you just run a `function()` your code will run but not as intended. It will be running the `button_fun()` with its first argument with none. In that case you can use `lambda:` as your to go to. 

```python
import tkinter as tk
from tkinter import ttk

#Window
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

#Basic Button
def button_func(entry_string):
	print('a button was pressed')
	print(entry_string.get())

#stringvar
button_string = tk.StringVar(value = 'test')
entry = ttk.Entry(window, textvariable = entru_string)
entry.pack()

button = ttk.Button(winow, text = 'A simple button', command = lambda: button_func())

...

#run
window.mainloop()
```

If you didn't want to use `lambda()` you need to create a function withing a function. Now, the outer function will contain you parameter while the inner one will not have any parameters. Instead of printing the `entry_string` variable we will be printing the `parameter.get()`. Because the item being entered is the `entry_string`. Then you need to return the `inner_func()`.

```python
def outer_func(parameter):
	def inner_func():
		print('a button was pressed')
		print(perameter.get())
	return inner_func
```
since the parameter is acting like the `entry_string` variable that's fine. The important part is the `return` and that its returning the `inner_func`. To know more, you need to understand functions and how they interact with return. 

## Event Binding
Events can be lots of things and they can be observed and used. Some events are:
- Keyboard inputs
- widgets getting changed
- widgets getting selected or unselected
- mouse click/motion/wheel

Events can be used easily, by binding events to a widget like so;
`Widget.bind(event, function)`

to format the event the following format would be: modifier - type - detail like so:
`Alt-Keypress-a`

Here we will create a event through by creating our window with a text widget, entry, button and an event using a lambda function. The event will be a key binging `Alt+a` that will activate a print function when the window is selected. Therefore the event will be tied to our window. 
```python
import tkinter as tk
from tkinter import ttk

#Window
window = tk.Tk()
window.title('Event Binding')
window.geometry('600x400')

#widgets
#test
text = tk.Text(window)
text.pack()
#Entry
entry = ttk.Entry(window)
entry.pack()
#button
button = ttk.Button(window, text = 'A button')
button.pack()

#events
window.bind(event, lambda: print('an event'))

#run
window.mainloop()
```

Though this will not run because our event argument isn't in the correct format as stated above. Events are always made as a sting and it needs a modifier-type-detail then enclose that in like so `'<modifier-type-detail>'`.
> [!important]
> Tkinter will automatically input an argument into you function so you need to account for that.
> 

To accept a argument with lambda you do the following: `lambda Arg: print('An Event')` and knowing all that your event should look like this;

```python
#events
window.bind('<Alt-KeyPress-a>', lambda event: print('an event'))
```
 
But if you print your argument `event` you will notice it returns multiple items that you can use when working with events. There are quite a few events that you can work with and you can find them all on [Python Tutorial](https://www.pythontutorial.net/tkinter/tkinter-event-binding/). Hello this is anting works for the window what if we wanted to tie it to other things say a button. Using the following text we can go ahead and tie this tool button when the button is selected and then press the key bindings `Alt+a`. Here we can have a and then tied to the button variable and then tied to the window variable doing different things. For the window event we're going to do something new and try to print the position of the even. We can do this by using the event variable or argument that is inputted to our function that we discussed earlier that Tkinter always inputs for events so for our command or functions we will call it get_pos.

```python
#events
button.bind('<Alt-KeyPress-a>', lambda event: print('an event'))
window.bind('<Motion>', get_pos)
```
Using the Motion, We are able to track the mouse in real time while it is on the window. in order to print this and identify it with the get position function we accept an argument of advent which is given automatically by taking inter and within the many items inside that variable we are going to pull the ax position using `event.x & event.y`. For display reasons we are going to use an F string within the print statement to help show the numbers in real time changing.  

> [!info]
> This kind of detection works well with the window because the window is always selected but you can change it for a specific widget say the text widget. If you do select the text widget the recording of the position will only be active while you're on or have the text which it selected otherwise moving your cursor somewhere else on the window it will stop recording the position.

```python
#define the function get_pos:
def get_pos(event): #has to accept an argument
	print(f'X: {event.x} Y: {event.y}')
```

And as you can see with the motion detection you can tell that the format`Alt-KeyPress-a` Doesn't need in all cases. Case we could just do keypress and then tie the print statement up in a F string so that we can detect what buttons are being pressed at every moment within the window.  Here we can see that when a button is pressed within the window it'll be displayed in the terminal what buttons were pressed. This could be used for key bindings or other specifics for program.

```python
#events
window.bind('<KeyPress>', lambda event: print(f'a button was pressed({event.char})'))
```

Another very powerful item in events that you might be using quite often is detecting whether something is selected or deselected. Here we can bind an event to the entry widget and determine whether it is selected or deselected by changing the invent characteristics to `FocusIn & FocusOut`. Allowing us to detect when the entry widget is selected and deselected.
```python
entry.bind('<FocusIn>', lambda event: print('Entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('Entry field was deselected'))
```

### Exercise:
My Answer and this is correct :)
```python
text.bind('<Shift-MouseWheel>'), lambda event: print('Mousewheel')
```

## Combobox and Spinbox
A `combobox` is basically a dropdown menu while a `spinbox` is switching through items. Both need a list of values to be inputted and both can be connected with a `Tkinter` variable. Fairly simple and like the other widgets we have seen. Here for the combo box we are looking at a simple window with a combo box widget. We're going to also create a list of 3 items that are going to go into that combo box. In order to get that list into the combo box which there are a couple of ways that you can do it but we will use [[#Configuring Widgets in a Loop| Configure method]] to show first. In addition we're going to set a string variable to our combo box. But just like using the string method in other widgets this starting value needs to be set and in our case we're going to set it to the first item within the list.

```python
import tkinter as tk
from tkinter import ttk

#Window
window = tk.Tk()
window.title('Event Binding')
window.geometry('600x400')

#items list
items = ['Ice Cream', 'Pizza', 'Broccoli']

#tkvariables
food_string = tk.StringVar(value = item[0]) the

#Widget
combo = ttk.Combobox(window)
combo['values'] = items #using our configure method

#run
window.mainloop()
```

In addition we can set events to combo boxes and uniquely the combo box has one event type that is set to it call the combo box selected. This is identified with `<< >>`.

```python
combo.bind('<<ComboboxSelected>>', lambda event: ptint(food_string.get()))
```

Thin boxes work almost similarly to a combo box which is why they're explained at the same time. You had them in like a normal widget and then you pack it on to the window. Once attached to the window you will have an up and down arrow to cycle through the different options. To set the different options you do the same thing where you use the  [[#Configuring Widgets in a Loop|Configure method]].  

```python
import tkinter as tk
from tkinter import ttk

#Window
window = tk.Tk()
window.title('Event Binding')
window.geometry('600x400')

#items list
items = ['Ice Cream', 'Pizza', 'Broccoli']

....

#Spinbox
spin = ttk.Spinbox(window)
spin['value']=[1,2,3,4,5]
spin.pack()


#run
window.mainloop()
```

So in our case there isn't much easier way to add a number line within a spin box since this is going to be your primary dedication for a spin boxes to adjusting numbers. Here instead you can set the to and from within a spin box between a number range that way I can cycle through.
> [!danger]
> When using from you need to have it types out as `from_`. Otherwise you'll get an error.

In addition you can set the increments of the number range of how much they increase instead of it being at one it can be incremental 23 and so on and so forth. Unfortunately increments can also be quite glitchy so you do need to keep in mind when you're doing that because it will set up a cut off point if your numbers are not in the increment range.
```python
#Spinbox
spin = ttk.Spinbox(window, from_ = 3, to = 20, incrament = 3)
#spin['value']=[1,2,3,4,5]
spin.pack()
```

Just like other widgets you can also set the spin box with a command and events can be controlled within the spinbox. Specialized defense that you can use are increment and decrement which adjusts when the up air or down arrow is being used.

```python
#Spinbox
spin = ttk.Spinbox(window, from_ = 3, to = 20, incrament = 3, command = lambda: print('a arror was pressed'))
spin.bind('<<Increment>>', lambda event: print("UP"))
spin.bind('<<Decrement>>', lambda event: print("DOWN"))
spin.pack()
```

Variables can also be used and set within a Spinbox. In our case we can use a spin integer and set the spin box with its text variable.
```python
#Spinbox
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(window, 
				   from_ = 3, 
				   to = 20, 
				   incrament = 3, 
				   command = lambda: print(spin_int.get()),
				   textvariable = spin_int)
spin.bind('<<Increment>>', lambda event: print("UP"))
spin.bind('<<Decrement>>', lambda event: print("DOWN"))
spin.pack()
```

### Exercise:
```python
#create a list of letters
exercise_letters = ['A', 'B', 'C', 'D', 'E']
exercise_string = tk.StringVar(value = exercise_letters[0])
exercise_spin = ttk.Spinbox(
							window, 
							textvariable = exercise_string, 
							values = exercise_letters
							)
#or you can do
excersie_spin['values'] = exercise_letters

exercise_spin.pack()

#create a event to print a value when value decreases
excercise_spin.bind('<<Decrement>>', lambda event: print("DOWN"))
```

## Canvas
He campuses a widget that allows you to draw shapes. like a drawing squares circles limes tacks etc. In the most basic sense we are creating a very basic version of paint. Here you can find that while we're doing this which the only import that we need is tk. Now if you just introduce the widget within the program window you will find that there doesn't seem to be anything but in the actual sense the widget is there it is just invisible due to the background color. So in our case we're going to set the background to white so we can visually see the canvas.

```python
import tkinter as tk

#Window
window = tk.Tk()
window.title('Canvas')
window.geometry('600x400')

#canvas
canvas = tk.Canvas(window, bg = 'white')
canvas.pack()

#run
window.mainloop()
```

We can start with creating a rectangle within the campus. this is to help us look at the different methods that can be used in campus. Case we're going to create an outlined rectangle with a tuple variable. But that variable we will describe the four points of the rectangle and where those lines will be located. In addition we will want to fill the rectangle with red using the fill argument and describe the width as zero so that it removes the borderline. 

```python
#canvas
canvas = tk.Canvas(window, bg = 'white')
canvas.pack()

canvas.create_rectangle((50, 20, 100, 200), fill = 'red', width = 0)
```

> [!info]
> For more details on this widget you can go to [New Mexico Techs](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html) website.

**I skipped the rest of the video at 2:14:00 because I can learn this later.**

## Treeview(table)
Just like canvases paint tree view is like Excel but we're creating a table. Here we're going to be looking at creating a window that makes a table where you can select the entries and delete entries. In activating the tree view widget you will find that a blank square pops up and that is because we need to start adding in our elements into the table. To do this we need to tell the program how many columns there are by naming those columns. Case we're going to name three columns first, last, email. After that we want to give each of those columns a headache so that data does not show up first for each of those columns. Therefore afterwards we're going to specify the heading by doing the variable name dot heading as the method Within the hair we're going to specify the column and then the next argument is going to be what we're naming that heading. We have to go back to the table and say that we want to show the headings for each column.

```python
import tkinter as tk

#Window
window = tk.Tk()
window.title('Canvas')
window.geometry('600x400')

# data

first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']

last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

table = ttk.Treeview(window, columns = ('first', 'last', 'email'), show = 'headings')
table.heading('first', text = 'First Name')
table.heading('last', text = 'Last Name')
table.heading('email', text = 'Emai')
table.pack()

#run
window.mainloop()
```

To put this information within the table you're going to use the insert method on the table variable. First argument within the insert is going to be parent. Used for relating data within the table if you're trying to identify particular item but in this case we're going to have it blanked for now. Then you want index and values. We're going to currently set to this one item and since we have three columns we need to have three items in our tuple.
```python
#insert values into table
table.insert(parent = '', index = 0, values = ('John', 'DOE', 'JohnDoe@emal.com'))
```

In our case we don't have a plethora of data to use so we're going to have to randomize it. In importing the randomizing library we are able to import choice for random choice from the list that we have provided for first name and last name. We want to create at least 100 entries into the table so we will create a for loop to go for a range of 100 and we're going to create a first name last name and then generate an email from that. Once that's created we'll insert that into the table like we saw before. In our case we're going to use our variable that is a tuple that has first last and email and insert that into the table. In addition you can also see that we're wanting to expand the table fully so you can see that pack as fill as in both and expand equal true.
```python
# data

first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']

last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

table = ttk.Treeview(window, columns = ('first', 'last', 'email'), show = 'headings')
table.heading('first', text = 'First Name')
table.heading('last', text = 'Last Name')
table.heading('email', text = 'Emai')
table.pack(fill = 'both', expand = True)

for i in range(100)
	first = choice(first_names)
	last = choice(last_names)
	email = f'{first}{last}@gmail.com'
	data = (first, last, email)
	table.insert(parent = '', index = 0, values = data)
```

Now what if we wanted to place items in a very particular order. For that is the point of `index` Within the arguments. Say we wanted to create a variable tuple that will insert a random set of data into the table but we wanted it at the first position, we would set the index equal to zero but if we wanted it at the second position we would set it to one. Though sometimes we don't understand how large our tables are in putting items at the end of the table is crucial but you don't know exactly what the number is. Therefore you can fetch the end of the table with `tk.END`.

```python
table.insert(parent = '', index = 1, values = ('XXXXX', 'YYYYY', 'ZZZZZ'))
table.insert(parent = '', index = tk.END, values = ('XXXXX', 'YYYYY', 'ZZZZZ'))
```

They're just like other widgets you can use advance and items are involved inside the table. Combining these two together can be extremely powerful and what you want to do with the data within the table. In our case we can create a binding event that specialized to tables and whenever we select an item within the table it will print that item in the terminal.

```python
#event
table.bind('<<TreeviewSelect>>', lambda event: print(table.selection()))
```

Now in our case we want to grab a selection of the items within the table and have it print out the variables or values itself. And doing this we're going to need to create a new function that deals with the items within the event. Case well we've captured those items for each piece we'll print it. One while doing this we have to keep in mind that our selection if not just by one variable so the return will always be a tuple therefore you should have a for loop within there so that we can evaluate all the selected items in case of there's more than one.

```python
#event
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])
    # table.item(table.selection())

table.bind('<<TreeviewSelect>>', item_select)
```

In our case we've used the table selection as a variable item and in that case we can do something quite unique when selecting the items, delete them. So in the event of deleting those items we can create a new bind argument to the table or when delete is pressed it will run the function to delete items In that function we've printed delete saying to the user that we deleted stuff but we're also going to need to do a selection for each of those items that we've selected we're going need to evaluate them and then remove them from the table using the delete method.
```python
# events

def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])
    # table.item(table.selection())

def delete_items(_):
    print('delete')
    for i in table.selection():
        table.delete(i)

  

table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)
```

> [!attention]
> Staples are probably one of the most complicated pieces of the widgets as they get quite complicated in their code and what they want you to do. So evaluate the documentation and follow through and you might be able to create something really interesting.

## Sliders
The fighters can be a few things to wear through the interactive scrolling bar button that you can use to see further down in the document its progress bars or additional edit bars. There are two main widgets to create sliders; Progress bars or slider. These are both one dimension and can be set independently but only sliders can be moved by the user. 
Here we can create a simple program that is going to demonstrate the scale. We're going to use our basic introduction code with the window and the window main loop but here we're going to use the slider widget. Similar to all the rest of the widgets you will have it as in `TTK` and it will be related to the window variable. But just like some of the other widgets this one automatically gives a value within a function that is called upon within the widget. Therefore a function that is being used inside of the command argument always needs to have a value that is ready to take an argument. 
```python
import tkinter as tk

#Window
window = tk.Tk()
window.title('Canvas')
window.geometry('600x400')

#slider
scale = ttk.Scale(window,command = lambda value: print(value))
scale.pack()
#run
window.mainloop()
```

In addition just like previous additions to codes you have a to and from variable that can edit from a sliding scale going from zero to 25 for example. In addition you can also determine the length of the slider and pixel size and here we can do it by 300 pixels In addition you can determine the orientation of the slider, the natural orientation is always horizontal but if you want to make it vertical this is what you would need to type.
```python
#slider
scale = ttk.Scale(window,
				  command = lambda value: print(value), 
				  from_ = 0, 
				  to = 25,
				  length = 300,
				  orient = 'vertical')
scale.pack()
```

In addition you can also set `tk `variables to the widget in this example we can set the int var `tk` variable to say 15. Before if you had the int variable set to nothing the program would act as normal but setting it to 15 when you use the widget will set the widget to 15 when it is opened.
> [!attention]
> This widget only takes int values. If you need something more you need to use `tk.DoubleVar()`.


```python
#slider
scale_int = tk.IntVar(value = 15)
scale = ttk.Scale(window,
				  command = lambda value: print(value), 
				  from_ = 0, 
				  to = 25,
				  length = 300,
				  orient = 'vertical',
				  variable = scale_int)
scale.pack()
```

And justice like the scale which you can set a progress bar using ttk. Uniquely that when you find that you've attached the progress bar together with the slider variable so that when the sliders at certain position the progress barns with it you'll notice that the progress bar doesn't quite match up and that is due to the range. You might think you need to use the two argument but in this case you actually need to use maximum. 
```python
progress = ttk.Progressbar(window,
						   variable = scale_float,
						   maximum = 25)
progress.pack()
```

In addition you can also orient the progress bar in a specific way you can change how the Podrus Bar shows its progress by the mode and you can determine the actual length of the progress bar as well by pixel size.
```python
progress = ttk.Progressbar(window,
						   variable = scale_float,
						   maximum = 25,
						   orient = 'horizontal',
						   mode = 'indetermininate',
						   length = 400)
progress.pack()
```

In addition to the progress bar you have progress start and progress stop. progress start start the activization of the progress bar and it will act a little wonky in that case there really isn't if her need to use progress start progress stop stops that sort of progress. That's something to really practically use but something to keep in mind.
```python
scale_int = tk.IntVar(value = 15)
scale = ttk.Scale(window,
				  command = lambda value: progress.stop(), 
				  from_ = 0, 
				  to = 25,
				  length = 300,
				  orient = 'vertical',
				  variable = scale_int)
scale.pack()

progress = ttk.Progressbar(window,
						   variable = scale_float,
						   maximum = 25,
						   orient = 'horizontal',
						   mode = 'indetermininate',
						   length = 400)
progress.start(1000)

progress.pack()
```

There is something more unique from the rest of the widgets called scrolled text. Something that you have to import individually as it's almost like a combination of widgets together but it acts like TTK inter. This widget is very similar to a text widget.
> [!info]
> We will learn how to make this on our own later on.


```python
from tkinter import scrolledtext

scrolled_text = scrolledtext.ScrolledText(window, width = 100, height = 15)
scrolled_text.pack()
```

## Frames and Parenting
So far for our programming and using widgets we have used in window as the mastered but in most cases this isn't what you want. What you should do is have a menu item and have that said as your master. A tad entry should have a tab which is as the master. And for complex layouts you also create a container widget to organize your widgets. Here we're going to learn about French and implementing widgets inside them and using parenting as the placement for these frames to create a more detailed window.

And in our case we are going to be using `ttk.Frame` Which is just an empty widget and then he will place your widgets inside of it. our main focus is to learn how parenting works. 

Here to show you how a frame is going to interact with the window we're going to comment out the window geometry size and when you run the frame without a width or height you will see that there is just the window controls and nothing else. Because as stated before there is no elements to a frame it is completely empty. But you can set the size of the frame which will create the size of the window in our case easing the width and height.
```python
import tkinter as tk
from tkinter import ttk

#Window
window = tk.Tk()
window.title('Frames and parenting')
#window.geometry('600x400')

#Frame
frame = ttk.Frame(window, width=100, height=200)
frame.pack()

#run
window.mainloop()
```

Here in our case we're going to try to visually show what the border looks like with the geometry window if you put back the 600 and 400 and then add a border with a relief you can see that there is an outline of the frame. You don't have to set it to RIDGE, you can also set it as:
- RIDGE - with a border
- SUNKEN
- FLAT - This is default 
- RAISED
- GROOVE
```python
#Frame
frame = ttk.Frame(window, 
				  width=100, 
				  height=200, 
				  borderwith = 10, 
				  relief = tk.RIDGE)
frame.pack()
```

In our case one or implementing a new label within the frame we're going to go ahead and use the master as the frame instead of the window. In this case you'll see that the label is inputted inside the frame but the frame even though originally was set to a height of 100 and 200 is a different size and borders the label. This is because frames Tend to auto adjust to the size that the children are inside. So therefore the child widget in this case is a label and a label is only a specific size so the frame is automatically going to adjust to this.
> [!info]
> If you wanted to disable this and allow it to actually stay the original size stated you need to use `frame.pack_propagate(False)`. Wear true sets size of the frame to the widget and False leaves it to what it was set at.

```python
#Frame
frame = ttk.Frame(window, 
				  width=100, 
				  height=200, 
				  borderwith = 10, 
				  relief = tk.GROOVE)
frame.pack()

#master setting
label = ttk.Label(frame, text= "label in frame")
label.pack()
```

In addition you can go ahead and plug multiple items into the frame like you can do with a window. Just like how it was discussed previously with implementing widgets within a window there is an order to operations. But the order of operations will be changed since this will be its own group. Here we'll have all of these items within the frame be displayed label that button.
```python
#Frame
frame = ttk.Frame(window, 
				  width=100, 
				  height=200, 
				  borderwith = 10, 
				  relief = tk.GROOVE)
frame.pack()

#master setting
label = ttk.Label(frame, text= "label in frame")
label.pack()

button = ttk.Button(frame, text='button within a frame')
button.pack()
```

In the event though that we have other items outside of the frame we're going to be packing it differently and depending on when that widget is packed the items can be displayed differently. Here displayed in the packing order you can see that the frame is packed first into the window and then the 2 items are packed within the frame and then outside the frame he button is packed. This will display a label and button within the frame and then outside the frame will be displayed a button. When following option two we will find that the items will be packed within the frame first the button will be displayed outside the frame and then the frame will be displayed with the 2 widgets inside of it. So think about it as the widgets that get packed into a frame are part of a group and packing them at that point packs all those items within that point.

```python
#option 1
frame.pack() window
button.pack() frame
label.pack() frame

button.pack() window

#option 2
button.pack() frame
label.pack() frame

button.pack() window
frame.pack() window
```

In addition to placement within going from top to bottom you can also place widgets to the side. In our case we're going to place the widgets to the left for the frame is placed first and then the button is placed next to it. With the following packing below the frame will go all the way to the left then the button then there will be a space gap on the window. 
```python
frame.pack(side = left)
button.pack(side = left)
```

## Tabs
Tats are quite easy and they are implemented using `ttk.Notebook()`. Notebook has a couple of children which are also noted as frames and each frame is one tab. Implementing this tab structure is quite simple and in the first case you're just adding a notebook variable to the window. Implementing each tab you're going to use the frame widget for both or each tab. To add the tabs into the notebook as an actual item you need to `notebook.add()` Each tab frame into the notebook in order to create a tab don't forget to name them.
> [!info]
> The frames for the notebook you do not need to pack. In addition you do not need to set the frames master to the notebook it can be still sent a window. Just makes much more sense to use the notebook as the parent.


```python
import tkinter as tk
from tkinter import ttk

#Window
window = tk.Tk()
window.title('Tabs Widget')
#window.geometry('600x400')

#Notebooks
notebook = ttk.Notebook(window)

tab1 = ttk.Frame(notebook)

tab2 = ttk.Frame(notebook)

notebook.add(tab1 , text = 'tab 1')
notebook.add(tab2 , text = 'tab 2')
notebook.pack()

#run
window.mainloop()
```

Now if you remember the discussion in setting up frames within a window you know that there needs to be the master that is set to either the frame tab or window. In that case when it is added in it changes the order of operations of when it will be displayed on to the window. In this case when you're creating new widgets for each tab you align them to the frames that you made for each tab not to the notebook itself. So for example if you wanted to create a label and a button within the first frame you need to create that and set its master to the 1st frame which in this case is labeled `tab1`.
```python
import tkinter as tk
from tkinter import ttk

#Window
window = tk.Tk()
window.title('Tabs Widget')
#window.geometry('600x400')

#Notebooks
notebook = ttk.Notebook(window)

tab1 = ttk.Frame(notebook)
label1 =ttk.Label(tab1, text = 'Text in tab 1')
button1 = ttk.Button(tab1, text = 'button in tab 1')
label1.pack()
button1.pack()

tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text = 'label in tab 2')
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()

notebook.add(tab1 , text = 'tab 1')
notebook.add(tab2 , text = 'tab 2')
notebook.pack()

#run
window.mainloop()
```

## Menus
You create a menu using `tk.Menu()`. One complex thing you learn about menus is that you use several of them and you nest them a lot. This can cause some confusion. For example if you place ATK menu inside of another TK menu it becomes an option. If we did this and we put the tk menu at the top of the window and then put another menu inside of it it would become its own option piece and then one interacted with it would display other options to be used like the image below. Similar to the top row of a Windows file or you're trying to find file edit section view go run terminal and help all those are little items or options within your menu at the top of the window. 

![[Pasted image 20240730155511.png]]

Adding menus acts as a different type and widgets and it's slightly different than what you're used to. In this case we're still going to start with importing TK and TTK and we're going to build our window. Though when you introduce a menu you're going to name a variable and call it characteristics to menu and set that master to the window. Now one year starting to create the window with a venue you then have to use `window.configure(menu = menu)` Saying that you're going to configure the  Menu inside of the window. Then if you're to create sub menus you're going to head and create a new variable mimic the same steps with menu implementation but in this case in order to add that menu to your regular menu you use `menu.add_cascade(label = 'file', menu = file_menu)`. Dictating that you're having a new menu type called file menu to your menu window. This is different than using the pack method. Uniquely if you're wanting to add commands to that menu you need to use the `file_menu.add_command()` Which will help give you a new command to give to that menu item. **This is the most confusing part about menus and if you can get this you're good.** To learn more about the entries of menus visit [tutorialspoint](https://www.tutorialspoint.com/python/tk_menu.htm). 
> [!attention]
> to prevent a new window forming you need to set the argument `tearoff =False`


```python
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
menu.add_cascade(label = "file", menu = file_menu)

window.configure(menu = menu)

window.mainloop()
```

Though this tutorials for [[tkinter additional methods for menu]] will be on a different time. 

Just like regular widgets you can add different types of unique widgets into menu buttons. One could be a check button in the event of your help case and when initiated will check off the button and giving you different characteristics. In our case we're setting the value on or off and then setting it equal to a health check string for your variable that could be used at a later time.
```python
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

# another sub menu
help_menu = tk.Menu(menu, tearoff = False)
help_menu.add_command(label = 'Help entry', command = lambda: print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label = 'check', onvalue = 'on', offvalue = 'off', variable = help_check_string)  

menu.add_cascade(label = 'Help', menu = help_menu)

window.configure(menu = menu)

window.mainloop()
```

## Changning the Window
So far we have changed the title, size of the window but there are many other things you can change in a window. 
Something unique in basic that you can do with the geometry method is a point where the window is going to be on the screen. Case we can go ahead and move it by pixel length and have it so that the program doesn't start in the same position or the same windows starts in the same position every time. Despite adding pixel length to your geometry method.
```python
import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('More on the window')
window.geometry('400x600+100+200')

#run
window.mainloop()
```

Another thing you can change is the tkinter logo with a ICO file type. Once you have your ICO file you can implement it using `window.icobitmap()`.

```python
import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('More on the window')
window.geometry('400x600+100+200')
window.icobitmap('python.ico')

...

#run
window.mainloop()
```

If needed you can also set the screen attributes so that it has a minimum and maximum size as well as which resizable direction you will allow the user to have. In this case we will show a mint size and a max size of the window and then allow resizing in the vertical direction.
```python
#window attribures
window.minsize(200,100)
window.maxsize(800,700)
window.resizable(True,False)
```

One additional things that would be extremely useful to know is to determine the size of a screen do the puzzling. In this case you can display using tkinter what the size of your window links are using the Winfo screen width and height method.
```python
print(window.winfo_screenwidth())
print(window.winfo_screenheight())
```

In addition you can set the attributes of the window so that you can have transparency which can be done through the alpha, one and the adjusting the one down to point one and above will adjust the transparency. Whereas adding an attribute of topmost and setting it to true will always have the windows stay on the top.
```python
#window attributes
window.attributes('-alpha', 1)
window.attributes('-topmost',True)
```

Sometimes these functions or pieces can add some complications and you might want to add in some binding events so that you can exit the window when needed in this case sending the escape button to exit. Then if you set the attribute to disabled you're not going to be able to interact with the window. Addition you won't be able to exit the program either in this case setting a bind event to the escape button where you quit the program allows you to still quit the program.
```python
#security event
window.bind('<Escape>', lambda event: window.quit())
window.attributes('-disable',True)
```

Another I've been setting a program to a bind event to exit is having the full screen attribute enabled. In order to set the full screen attribute you need to remove both the minimum and maximum sizes of a window. So in this case you will go full screen but not able to exit the window and in this case you can press exit through escape key.
```python
window.attributes('-fullscreen', True)
```

At the event you want it to be more creative but remove the title bar you can use the override redirect and set it to true so that that way the title bar is removed in addition you can set the size of the window now by using the grip and then using grip place you can anchor in the window adjuster into the southeast corner.
```python
# title bar
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx = 1.0, rely = 1.0, anchor = 'se')
```

# Layouts
Unfortunately layouts can be one of the hardest things to learn in Tkinter due to the proper sizing and placement of certain items. In this case with TK enter you have three different methods you can use:
- `pack()` - widget go from top to bottom  and stack from left to right. Simplest method to use
- `grid()` - Such a grid onto your window which you can adjust the size of the columns and rows in places your item within the specific grid frame.
- `place()` - simplest method and more flexibility than `pack()`
Though it is not like you're going to just use one of these methods throughout your program it is mostly possible that you're going to use all 3. What if key to every program is parenting and frames! That way you can combine different layouts easily and keep them organized. For example if we take a new window and we want to have two different sections we're going to pack that in then our left section will be a grid based with maybe different sliders and our right section will have placed different widgets within it and on some occasions you can place your widget on top of a grid.
![[Pasted image 20240801120923.png]]

To revert back to the previous method that we had learned which is `pack()`. Pack places the items with in the window in a certain order and from our previous discussions you can either go from top to bottom or left or right. In our case if we wanted to move this to the left to right we would use the *side* argument within `pack()`. Another argument within pack is *expand* Which will expand the items space to its entire availability. Then you have *fill* which will *fill* the entire widget within the certain field and you can dictate which direction *fill* will happen (X, Y, or both). Here our widget will be a label.
```python
import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('MLayout Intro')
window.geometry('400x600')

#widgets
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')

#pack Option 1
label1.pack()
label2.pack()

#Pack Option 2
label1.pack(side = 'left', expand = True, fill = 'y')
label2.pack(side = 'right', expand = True, fill = 'both')

#run
window.mainloop()
```

one of the newer methods that we talked about is the `grid()` method. In order to use the grid method you need to set it up properly prior to placing a item within the grid. To create a grid you need to determine the number of columns and rows with the `columnconfigure()` and `rowconfigure()` methods. In this method you will have two arguments you need to have`(arg1, arg2)`. *arg1* determines what number of row or column you are creating and *arg2 = weight* is determining the size. In our case below we are going to create three columns where the first two are the same size but the 3rd one will be double the size of the first two and two rows.
```python
# grid
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 2)
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)

```

If we were to create this window and have a label for each position with an identified color you would be able to identify that the grid that was created would be as follows:
![[Pasted image 20240806161158.png]]

To put our two labels within the grid frame we need to use `grid()` But specify where the widget will be placed. the first two arguments you will need is *row & column* and set them equal to the row and column you are wanting to place the widget. When doing so you will be placing the widget at its specific size within the grit so it might not take up too much space. In order to dictate how much space the widget can take up or its placement within the cell you use the argument `sticky` and use one of the 4 variables `(n s e w)`. Say you wanted to let the widget cross multiple areas like the merge function within excel, there is the `columnspan or rowspan` arguments.
```python
label1.grid(row = 0, column = 1, sticky = 'nsew')
label2.grid(row = 1, column = 1, columnspan = 2, sticky = 'nsew')
```
He can identify how sticky would interact by creating the labels and setting him to N (0,0) S(1,0) E(0,1) and W(1,1). 
![[Pasted image 20240806161341.png]]

The place method interacts with the window by using the entire windows as a coordinate system with pixels. In this case when you're placing an item you're going to determine the X and Y arguments and where they set. This is where using the `geometry()` helps a lot since you will know the size of your window.
> [!attention]
> Increasing X moves the widget to the right and increasing Y moves the widget down.

In addition with youth in the place method if you want to dictate the size of the widget you can use the *width & height* arguments. Keep in mind you can extend  the widget beyond the window. 

You can also use a different way to place items using the place method using relative X and Y coordinates. Relative X and Y coordinates *relx & rely* treats the entire grid between zero and one so that even if the window size changes the widgets automatically adjust to the size of the window. When placing the widget, by default it will always uses the top left corner. Therefore, if you place the widget at (0,0) its top left corner is going to be placed at the top left corner of the window. But if you place the widget at (.5, .5) it will be placed in the center of the window and even when you adjust the window it will stay in the center. You can also adjust the point that you want to use for your anchoring spot within the window by using *anchor* argument. The options of corners are:
![[Pasted image 20240806160448.png]]

A better example to show how placement can be affected by the corner that you choose is to create a label for each corner and place it within the center of the window. Like so:
![[Pasted image 20240806162151.png]]

```python
label1.place(x = 100 , y = 200, width = 200, height = 100)
label2.place(relx = 0.5, rely = 0.5, relwidth = 1, anchor = 'se')
```

## Pack Continued
We already know the general ability of pack and how to use it but to know how to use pack well you need to know these three arguments. 
**side**: 'left', 'right', 'top', 'bottom' | The side the widget is added to
**expand**: True, False | Determines the vertical or horizontal space a widget *can* occupy
**fill**: 'X', 'Y', 'both', None | Sets how much space the widget *will* occupy

To starter example we will develop a window with 3 labels and a button to use for our example as follows: 
```python
import tkinter as tk
from tkinter import ttk 

# window
window = tk.Tk()
window.title('Pack')
window.geometry('400x600')

  

# widgets
label1 = ttk.Label(window, text = 'First label', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Last of the labels', background = 'green')
button = ttk.Button(window, text = 'Button')

# run
window.mainloop()
```

Here traditionally if we're going to use the packed method to introduce each of these widgets into our window we will have them stacked in order with the minimal amount of space taken up.
```python
label1.pack()
label2.pack()
label3.pack()
button.pack()
```
![[Pasted image 20240806202222.png]]
### side
But if we want to change location and the order that it is stacked we can use the site argument within the method to dictate which side we want the widget to show up. Though choosing different sides at the same time can result in unexpected results.
```python
label1.pack(side = 'bottom')
label2.pack(side = 'bottom')
label3.pack(side = 'bottom')
button.pack(side = 'bottom')
```

### expand
Expand is a trickier concept since the additions to it are dictated by what type of work you're currently doing. Expand determines how much space a widget *can* occupy. **Widgets only expand in one direction** In this direction is determined by the stacking of the objects in which direction that they're going in. 
> [!info] 2 kinds of spaces:
> - The space a widget *can* occupy
> - The space a widget *will* occupy

By default a widget will only be as big as the content (foe example, a label is just as bug as the text). However, the widget can occupy more space than that. by default, widgets will only occupy the space they need to display the content. But they *can* occupy more space! 

| side = top or bottom                   | side = left or right                    |
| -------------------------------------- | --------------------------------------- |
| Widget can be as wide as the container | Widget can be as heigh as the container |
| expand determines the height           | expand determines the width             |
But if we put this idea into action we really need to determine how expand works. In our case we're going to set the first label and the button to expand this way we can see how much space it takes up whereas the other two labels will not. When the code is run in action you can see that the label and the button itself will try to take up as much **space** as possible whereas the other two labels are going to stay as close together as possible.
```python
# layout
label1.pack(side = 'left', expand = True)
label2.pack(side = 'left')
label3.pack(side = 'left')
button.pack(side = 'left', expand = True)
```

![[Pasted image 20240806204043.png]]

### fill
Phil will determine if a widget will occupy the available space unlike expand which can occupy the space. The options that you have for fill are as follows:
![[Pasted image 20240806205722.png]]

In order to see these correctly we can take the widgets and set them all to expand equal true allowing them to take up the equal amount of space between each other and fill it in each direction. You'll see that both fills up the overall area while none doesn't fill and stays limited which is the default option. Then there's X and Y which expand it to different directions.
```python
# layout
label1.pack(side = 'top', expand = True, fill = 'both')
label2.pack(side = 'top', expand = True, fill = 'x')
label3.pack(side = 'top', expand = True, fill = 'y')
button.pack(side = 'top', expand = True, fill = None)
```

![[Pasted image 20240806210143.png]]

### Creating Space inside and outside the widget
In addition to placement your pack method can also create space within and outside of the widget. Say that you want to have space around your widget at all types you could use `padx or pady` Arguments within the PAC method to dictate the amount of space while `ipadx and ipady` Expand your method and create more space without expanding the material inside the widget.
![[Pasted image 20240806210808.png]]

```python
label1.pack(side = 'top', expand = True, fill = 'both', padx = 10, pady = 10)
```

### combining different sides
You can also combine different sides. Then the order of the pack can really matter. Usually it is cleaner to use frames to organize a more complex layout. 
```python
# layout
label1.pack(side = 'top', expand = True, fill = 'both')
label2.pack(side = 'left', expand = True, fill = 'both')
label3.pack(side = 'top', expand = True, fill = 'both')
button.pack(side = 'top', expand = True, fill = 'both')
```

Say that we wanted to cycle over each widget that we have out of the 4 to help determine what kind of cause moving from the left or top would do to a window. If we set the first widget to left instead of top like the rest of them we find that it's going to take up as much horizontal space as it can using the expand argument. It knows that it needs to leave enough room for the rest of the widgets where in this case widget 3 takes up the most space because of its text in the horizontal position. Therefore, it needs to leave that much space left on the horizontal axis but it can take up the rest that it needs. Leaving that small amount of space to divide up between the rest of the widgets.
Can see that this trends for the rest of the widgets as you change where left instead of top is for the side. The only change that occurs is how much top space it is allowed to have because of its positioning. The reason why it looks like there's no difference for the button is since it is packed and last there is nothing to split with it therefore it will get all the space it needs.

| label1                               | label2                               | label3                               | button                               |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| ![[Pasted image 20240806211510.png]] | ![[Pasted image 20240806211514.png]] | ![[Pasted image 20240806211536.png]] | ![[Pasted image 20240806211542.png]] |
## pack + frames

Pack had become much easier to use when you combine it with frames. You always create layouts in a single direction but some items are frames that contain their own layout. but some items are frames that contain their own layout.
![[Pasted image 20240807132315.png]]

Here we can see we have our basic window and 6 widgets. With the additions of these widgets we are wanting to add more comments to help determine what is where. 
```python
import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack parenting')
window.geometry('400x600')

#widgets
label1 = ttk.Label(top_frame, text = 'First label', background = 'red')
label2 = ttk.Label(top_frame, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Another label', background = 'green')
label4 = ttk.Label(bottom_frame, text = 'Last of the labels', background = 'orange')
button = ttk.Button(bottom_frame, text = 'A Button')
button2 = ttk.Button(bottom_frame, text = 'Another Button')
```

To organize these we need to create the first frame that we can pack into. when packing we have to remember to pack the frame. But you need to remember that filling not only needs to happen with widgets but frames as well. Which will limit the fame to the required widget size. 

| No fill                              | Fill Widgets                         | Fill widgets and Frame               |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| ![[Pasted image 20240807135247.png]] | ![[Pasted image 20240807135337.png]] | ![[Pasted image 20240807135316.png]] |

```python
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text = 'First label', background = 'red')
label2 = ttk.Label(top_frame, text = 'Label 2', background = 'blue')
label1.pack(fill = both)
label2.pack(fill = both)
top_frame.pack(fill = both)

```
In turn if we expand the widgets so that they extend from top to bottom nothing will change. This is because the frame needs to be expanded as well. 
```python
label1.pack(fill = both, expand = True)
label2.pack(fill = both, expand = True)
top_frame.pack(fill = both, expand = True)
```
![[Pasted image 20240807135643.png]]

Now that we understand how the frame is going to work within the widget that how it needs to share similar characteristics with widgets in order to properly consume the window we can add the third label. In our case we want to add in the label but not change any of its characteristics but show that there is space around the label. This means that what we pack the label into the window it needs to have an expand argument set to true.
```python
import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack parenting')
window.geometry('400x600')

#widgets
label1 = ttk.Label(top_frame, text = 'First label', background = 'red')
label2 = ttk.Label(top_frame, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Another label', background = 'green')
label4 = ttk.Label(bottom_frame, text = 'Last of the labels', background = 'orange')
button = ttk.Button(bottom_frame, text = 'A Button')
button2 = ttk.Button(bottom_frame, text = 'Another Button')

#top layout pack
label1.pack(fill = both, expand = True)
label2.pack(fill = both, expand = True)
top_frame.pack(fill = both, expand = True)

#middle layout pack
label3.pack(expand = True)

```

When we do this we find that the widgets are not divided evenly throughout the window and the label three consumes the most horizontal space. The reason for this is because the frame and the 3rd widget are going to share the horizontal space between each other. Then within the frame widget itself the first and second label with share its horizontal space between themselves.
![[Pasted image 20240807140034.png]]

Then trying to plead our layout from our example we are going to add in the bottom layer and we want to add buttons in a row within its bottom frame pack. In this case we'll make a new variable called bottom frame that is equal to the frames in TTK. Then we'll add the buttons and pack them into the frame. But we want the buttons and the label to expand within the horizontal direction and fill up the entire frame. Using expand is not going to give us the desired output since placing the buttons and label from left to right is only going to expand it from left to right.
```python
import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack parenting')
window.geometry('400x600')

  
#frame creation
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
button.pack(side = 'left', expand = True)
label4.pack(side = 'left', expand = True)
button2.pack(side = 'left', expand = True)
bottom_frame.pack(expand = True)

window.mainloop()

```

![[Pasted image 20240807141022.png]]

This means in our case we need to use the fill command that way we can fill up the entire space available for the widgets and the frame. In addition we also want to add a little bit of padding so we'll add that with paddocks and pad Y.

```python
#bottom layout pack
button.pack(side = 'left', expand = True, fill = "both")
label4.pack(side = 'left', expand = True, fill = "both")
button2.pack(side = 'left', expand = True, fill = "both")
bottom_frame.pack(expand = True, fill = "both", padx = 20, pady = 20)
```

![[Pasted image 20240807141047.png]]

## Grids
