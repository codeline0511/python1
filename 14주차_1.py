import tkinter as tk
from tkinter import ttk

def buildGUI():
    btn1 = ttk.Button(win, text = '버튼1')
    btn2 = ttk.Button(win, text = '매우 긴~~~ 너비와 높이를 갖는 \n버\n튼\n2')
    btn3 = ttk.Button(win, text = '버튼3')
    btn4 = ttk.Button(win, text = '버튼4')
    btn5 = ttk.Button(win, text = '버튼5')
    
    btn1.grid(row=0, column=0)  # btn1.grid()와 동일
    btn2.grid(row=1, column=1, columnspan = 2)
    btn3.grid(row=1, column=2, sticky = 'se') # 여백 존재 시 특정 방향으로 치중
    btn4.grid(row=2, column=2)
    btn5.grid(row=3, column=2)

win = tk.Tk()
win.title('grid() 배치의 예')
win.geometry('500x200')
buildGUI()
win.mainloop()
