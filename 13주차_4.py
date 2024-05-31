import tkinter as tk
from tkinter import ttk

def buildGUI():
    global text_label  # 이벤트 핸들러에서 접근 위해
    text_label = ttk.Label(win, text = '안녕하세요')

    input_btn = ttk.Button(win, text = '입력',
                           command = input_btn_handler)  # 함수 이름 뒤에 ()가 붙지 않음에 유의
    quit_btn = ttk.Button(win, text = '종료',
                          command = win.destroy)

    text_label.pack()
    input_btn.pack()
    quit_btn.pack()

def input_btn_handler():
    text_label.configure(text = '반가워요')

win = tk.Tk()
win.title('라벨 위젯 예1')
win.geometry('100x100-1000+300')
buildGUI()                  
win.mainloop()
