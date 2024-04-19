#Now let’s see how to create a digital clock GUI application with Python.
#I will first start with importing the libraries:

from tkinter import Label, Tk
import time

# Now let’s define the title and size of our application.
# Note that in the code below I will set both the height and width of the resizable function as True(True,True)
# if you want a fixed window and don’t want to maximize or minimize the output you can set it to False(False,False):

app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("860x150")
app_window.resizable(False, False)

# Now here I will define the font of the time and its colour, its border width and
# the background colour of the digital clock:

text_font = ("Boulder", 68, 'bold')
background = "black"
foreground = "red"
border_width = 25

# Now here I will combine all the elements to define the label of the clock application:

label1 = Label(app_window, text="Ali Raza: ", font=text_font, bg=background, fg=foreground, bd=border_width)
label1.grid(row=0, column=1)
label1.config()

label2 = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label2.grid(row=0, column=2)

# Now let’s define the main function of our digital clock. Here I will set the text of the label as the realtime:


def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label2.config(text=time_live)
    label2.after(200, digital_clock)


digital_clock()
app_window.mainloop()
