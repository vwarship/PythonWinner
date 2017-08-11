from tkinter import Tk
from tkinter import Label


tk = Tk()

# 设置窗口的大小宽x高+偏移量。中间的是小写字母x
tk.geometry('640x480+0+0')
tk.title('Hello')
# tk.iconbitmap('logo.ico') # 不起作用

label = Label(tk, text='Hello World!')
label.grid()

tk.mainloop()
