import tkinter as tk
from tkinter import ttk

def buildGUI():
    btn1 = ttk.Button(win, text = '버튼1')
    btn2 = ttk.Button(win, text = '버튼2')
    btn3 = ttk.Button(win, text = '버튼3')
    btn4 = ttk.Button(win, text = '버튼4')
    btn5 = ttk.Button(win, text = '버튼5')

    btn1.pack()
    btn2.pack(ipadx=10,ipady=10) # 안 쪽 여백(+:버튼 크기를 크게 만듬)
    btn3.pack(padx=10, pady=10)  # 바깥 쪽 여백(+:버튼 크기를 작게 만듬)
    btn4.pack(fill=tk.X)  # 컨테이너의 너비에 위젯의 크기를 맞춤
    btn5.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

win = tk.Tk()
win.title('pack() 배치')
win.geometry('300x200')
buildGUI()
win.mainloop()
