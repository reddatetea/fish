from tkinter import *
def callback(*args):
    print('data changed : '.xE.get())
root = Tk()
root.title('ch6_3')
xE = StringVar()
entry = Entry(root,textvariable = xE)
entry.pack(pady = 5,padx = 10)
xE.trace('w',callback)
root.mainloop()
