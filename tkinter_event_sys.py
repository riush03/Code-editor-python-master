import tkinter as tk

win = tk.Tk()
can = tk.Canvas(win,width=300,height=300)
strvar = tk.StringVar()

lab = tk.Label(win,textvar=strvar)
strvar.set("Press a key")

def on_click(event=None):
    can.create_oval((event.x - 5 ,event.y - 5, event.x + 5, event.y + 5),fill="red")

def on_keydown(event=None):
    strvar.set(event.keysym)

def on_ctrl_d(event=None):
    top = tk.Toplevel(win)
    top.geometry("200*200")
    sv = tk.StringVar()
    sv.set("Hover the mouse over me")
    label = tk.Label(top,textvar=sv)
    label.pack(expand=1,fill=tk.BOTH)
    label.bind("<Enter>",lambda e,sv=sv: sv.set("Hello Mouse!"))
    label.bind("<Leave>",lambda e,sv=sv: sv.set("Goodbye mouse!"))

can.bind('<Button-1>',on_click)
win.bind('<KeyPress>',on_keydown)
win.bind('<Control-d>',on_ctrl_d)

can.pack()
lab.pack(side=tk.BOTTOM)

win.mainloop()