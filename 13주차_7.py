import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

def buildGUI():
    global text_area
    text_area = scrolledtext.ScrolledText(win,
                                          width = 30, height = 5, wrap = tk.WORD)
    
    input_btn = ttk.Button(win, text = '출력',
                           command = input_btn_handler)

    text_area.pack()
    input_btn.pack()

def input_btn_handler():
    print(text_area.get(0.0, tk.END))
    text_area.delete(0.0, tk.END)


win = tk.Tk()
win.title('버튼 위젯')
win.geometry('-1000+300')
buildGUI()                  
win.mainloop()
