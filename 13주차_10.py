import tkinter as tk
from tkinter import ttk

def buildGUI():
    btn1 = ttk.Button(win, text = '버튼1')
    btn2 = ttk.Button(win, text = '버튼2')
    btn3 = ttk.Button(win, text = '버튼3')
    btn4 = ttk.Button(win, text = '버튼4')
    btn5 = ttk.Button(win, text = '버튼5')

    btn1.pack(side=tk.TOP)
    btn2.pack(side=tk.LEFT)
    btn3.pack()
    btn4.pack(side=tk.RIGHT)
    btn5.pack(side=tk.BOTTOM)

win = tk.Tk()
win.title('pack() 배치')
win.geometry('300x200')
buildGUI()
win.mainloop()
