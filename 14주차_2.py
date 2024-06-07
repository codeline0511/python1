import tkinter as tk
from tkinter import ttk

def buildGUI():
    btn1 = ttk.Button(win, text='버튼1')
    btn2 = ttk.Button(win, text = '매우 긴~~~ 너비와 높이를 갖는 \n버\n튼\n2')
    btn_group = ttk.Frame(win)
    btn3 = ttk.Button(btn_group, text = '버튼3')
    btn4 = ttk.Button(btn_group, text = '버튼4')
    btn5 = ttk.Button(win, text = '버튼5')

    btn1.grid(row = 0, column = 0, sticky = 'se')
    btn2.grid(row = 0, column = 1)
    btn3.pack(side=tk.LEFT)
    btn4.pack(side=tk.LEFT)
    btn_group.grid(row=1, column =1, sticky ='w')
    btn5.grid(row=2, column=0)

win = tk.Tk()
win.title('FRAME() 배치의 예')
win.geometry('300x200')
buildGUI()
win.mainloop()
