import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

label = tk.Label(window, bg='yellow', width=20, text='empty')
label.pack()


def print_selection():
    if (var1.get() == 1) and (var2.get() == 0):  
        label.config(text='I love only Python')
    elif (var1.get() == 0) and (var2.get() == 1):  
        label.config(text='I love only C++')
    elif (var1.get() == 0) and (var2.get() == 0):  
        label.config(text='I do not love either')
    else:
        label.config(text='I love both')


var1 = tk.IntVar()  
var2 = tk.IntVar()


c1 = tk.Checkbutton(window, text='Python',
                    variable=var1, onvalue=1,
                    offvalue=0,
                    command=print_selection)
c1.pack()

c2 = tk.Checkbutton(window,
                    text='C++',
                    variable=var2,
                    onvalue=1,
                    offvalue=0,
                    command=print_selection)
c2.pack()

window.mainloop()
