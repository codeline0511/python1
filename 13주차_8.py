import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def buildGUI():
    global check
    check = tk.IntVar()  # 세크 상태 저장 위해
    check_btn = ttk.Checkbutton(win, text = '옵션을 선택하세요',
                                variable = check,
                                command = open_dialog_box)

    check_btn.pack()

def open_dialog_box():
    if check.get() == 1:
        messagebox.showinfo('확인', '옵션 선택')
    else:
        messagebox.showinfo('확인', '옵션 해제')

win = tk.Tk()
win.title('옵션 위젯')
win.geometry('-1000+300')
buildGUI()                  
win.mainloop()
