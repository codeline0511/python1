import tkinter as tk
from tkinter import ttk

def buildGUI():
    global text_area
    text_area = tk.Text(win,
                        width = 30, height = 5, wrap = tk.WORD) # tk.CHAR 방법도 가능
                        
    input_btn = ttk.Button(win, text = '출력',
                           command = input_btn_handler)

    text_area.pack()
    input_btn.pack()

def input_btn_handler():
    print(text_area.get(0.0, tk.END))
    text_area.delete(0.0, tk.END)

win = tk.Tk()
win.title('라벨 위젯 예1')
win.geometry('-1000+300')
buildGUI()                  
win.mainloop()
