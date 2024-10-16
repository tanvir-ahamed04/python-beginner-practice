import tkinter as tk

window = tk.Tk()
window.title("My window")
window.geometry("200x100")

var = tk.StringVar()  # Define var as a StringVar
label = tk.Label(window,
                 textvariable=var,
                 bg="green",
                 font=('Arial', 12),
                 width=15, height=2
                 )
label.pack()

on_hit = False

def hit_me():
    global on_hit  # Declare on_hit as a global variable
    if not on_hit:
        on_hit = True
        var.set("You pressed me")
    else:
        on_hit = False
        var.set("")

button = tk.Button(window, text='pass me', width=15, height=2, command=hit_me)
button.pack()

window.mainloop()
