import tkinter as tk
import scrreen

window = tk.Tk()
window.title("")
window.geometry('200x100')
var = tk.StringVar()  # Corrected

label = tk.Label(window,
                 textvariable=var,
                 bg="green",
                 font=('Arial', 12),  # Corrected
                 width=15, height=2
                 )
label.pack()

click_me = False

def for_press_btn():
    global click_me
    if click_me:  # Changed to if statement
        click_me = True  # Corrected
        var.set("RC St")
        from scrreen import ScreenRecorder  # Adjust with the actual function from scrreen module
    else:
        click_me = False
        var.set("RC Stop")
for_press_btn()

window.mainloop()
