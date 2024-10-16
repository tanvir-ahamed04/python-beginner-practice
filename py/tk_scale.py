import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

label = tk.Label(window, bg='green', fg='white', width=20, text='empty')
label.pack()

def print_selection(v):
    if float(v) > 5:  
        label.config(bg='blue')
    elif float(v) > 8:
        label.config(bg='black')    # have some issue on that line , black doesn't work         
    else:
        label.config(bg='green')  
    label.config(text='You have selected ' + str(v))

s = tk.Scale(window, label='try me',
             from_=0,
             to=10,
             orient=tk.HORIZONTAL,
             length=200,
             showvalue=0,
             tickinterval=2,
             resolution=0.01,
             command=print_selection)
s.pack()

window.mainloop()
