# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *
from time import strftime

# creating tkinter window
root = Tk()
root.title('Menu Demonstration')
def menu():
# Creating Menubar
    menubar = Menu(root)

    # Adding File Menu and commands
    file = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='File', menu = file)
    file.add_command(label ='Booking', command = None)
    file.add_command(label ='Loading', command = None)
    file.add_command(label ='Unloading', command = None)
    file.add_separator()
    file.add_command(label ='Exit', command = root.destroy)

    # Adding Edit Menu and commands
    edit = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Account', menu = edit)
    edit.add_command(label ='Kanpur', command = None)
    edit.add_command(label ='Varansi', command = None)
    """edit.add_command(label ='Paste', command = None)
    edit.add_command(label ='Select All', command = None)"""
    """edit.add_separator()
    edit.add_command(label ='Find...', command = None)
    edit.add_command(label ='Find again', command = None)"""

    """# Adding Help Menu
    help_ = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Tools', menu = help_)
    help_.add_command(label ='Search', command = None)
    help_.add_command(label ='Challan', command = None)
    help_.add_separator()
    help_.add_command(label ='About Tk', command = None)
    """
    # display Menu
    root.config(menu = menubar)


mainloop()
