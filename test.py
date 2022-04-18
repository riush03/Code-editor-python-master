import tkinter as tk
import tkinter.ttk as ttk
'''
   The ttk submodule -> contains themed widgets that match those native to system they are being run on
'''
win = tk.Tk()

button_tk = tk.Button(win,text="tk")
button_ttk = ttk.Button(win,text="ttk")

button_tk.pack(padx=10,pady=10)
button_ttk.pack(padx=10,pady=10)

win.mainloop()