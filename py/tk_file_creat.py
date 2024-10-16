import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

label = tk.Label(window, text='', bg='green')
label.pack()

counter = 0

def do_job():
    global counter
    counter += 1
    label.config(text='do' + str(counter))

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()  # 添加一条分隔线
filemenu.add_command(label='Exit', command=window.quit)  # 用tkinter里面自带的quit()函数

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

submenu = tk.Menu(filemenu)
submenu.add_command(label='Submenu 1', command=do_job)

filemenu.add_cascade(label='Import', menu=submenu, underline=0)  # 给放入的菜单submenu命名为Import

menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Edit', menu=editmenu)

window.config(menu=menubar)
window.mainloop()
