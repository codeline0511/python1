import tkinter as tk
from tkinter import ttk

def buildGUI():
    global text_label  
    text_label = ttk.Label(win, text = '안녕하세요')

    global name           # 이벤트 핸들러에서 접근 위해
    name = tk.StringVar() # 엔트리 위젯에서 문자열 저장 위해
    input_entry = ttk.Entry(win, textvariable = name)

    input_btn = ttk.Button(win, text = '입력',
                           command = input_btn_handler)
    quit_btn = ttk.Button(win, text = '종료',
                          command = win.destroy)

    text_label.pack()
    input_entry.pack()
    input_btn.pack()
    quit_btn.pack()

def input_btn_handler():
    text_label.configure(text = '반가워요,' + name.get())
    name.set('')          # 작은따옴표 두 개로 빈문자열을 인수로 지정

win = tk.Tk()
win.title('라벨 위젯 예1')
win.geometry('100x100-1000+300')
buildGUI()                  
win.mainloop()
