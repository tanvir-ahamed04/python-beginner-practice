import tkinter as tk

window = tk.Tk()
window.title("_____\\_____")
window.geometry("200x200")

var1 = tk.StringVar(value="One")  # Set an initial value

label = tk.Label(window,
                 textvariable=var1,
                 bg="yellow",
                 font=("Arial", 20), 
                 width=4, 
                 height=2)
label.pack()

def print_selection(v):
    var1.set(v)

r1 = tk.Radiobutton(window, text="Option1",
                    variable=var1,
                    value="One",
                    command=lambda: print_selection("One"))  # Use lambda to pass argument
r1.pack(anchor="w")

r2 = tk.Radiobutton(window, text="Option2",
                    variable=var1,
                    value="Two",
                    command=lambda: print_selection("Two"))  # Use lambda to pass argument
r2.pack(anchor="w")

window.mainloop()
