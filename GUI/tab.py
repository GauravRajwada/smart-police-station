
from tkinter import *
import databse as db

def new_case():

	def command(text):
		T.insert(END, text)

	def screen():
		command(db.fir(5))

	new = Toplevel()

	#new = Tk()
	new.wm_iconbitmap("E:/Python Project/Smart Police Station/GUI/title (1).ico")
	new.geometry("700x700")
	new.maxsize(700, 700)
	new.minsize(700, 700)
	new.title('Smart Police Station')
	# title_label = Label(text ="Smart Police Station",bg="white", fg="Black", font="Airblack 15 bold", borderwidth=1, relief=FLAT).place(x=250,y=0)

	T = Text(new, height=35, width=50)
	l = Label(new, text="Smart Police Station")
	l.config(font=("Airblack 15 bold"))
	l.pack()

	T.pack()
	# T.insert(END, "Fact")

	T.insert(END, "Gaurav")

	"""For button"""
	start_frame = Frame(new, bg='steelblue', borderwidth=1, relief=FLAT).place()
	b1 = Button(start_frame, fg='black', bg="white", text='Start', command=screen).place(x=290, y=670)
	b2 = Button(start_frame, fg='black', bg="white", text='stop', command=new.destroy).place(x=340, y=670)

	#new.mainloop()



def login():
	window=Toplevel(root)

root =Tk()
b = Button(root, text="New Case", command=new_case).pack()

b = Button(root, text="Officers Login", command=login).pack()

root.mainloop()