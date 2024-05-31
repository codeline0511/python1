import tkinter as tk
from tkinter import ttk

GENDERS = [ '남성', '여성', '기타' ]
COLORS = [ 'red', 'yellow', 'purple' ]

def buildGUI():
    text_label = ttk.Label(win, text = '당신의 성별은? ')
    text_label.pack()

    global gender
    gender = tk.IntVar()
    for i in range(3):
        radio_btn = ttk.Radiobutton(win,
                                    text = GENDERS[i],
                                    value = i,
                                    variable = gender,
                                    command = radio_btn_handler
                                    )
        radio_btn.pack()

    gender.set(-1)  # 라디오 버튼 선택 지우기(n < 0)

def radio_btn_handler():
    choice = gender.get()
    win.configure(background = COLORS[choice])

win = tk.Tk()
win.title('버튼 위젯')
buildGUI()
win.mainloop()
