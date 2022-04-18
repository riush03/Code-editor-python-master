import tkinter as tk

win = tk.Tk()

text = tk.Text(win,fg="black",bg="white")
t = text

def on_control_o(event=None):
    t.insert(1.0,'aaa')

    return "break"

t.bind('<Control-o>',on_control_o())

text.pack()
win.mainloop()