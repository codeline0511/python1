# code1
import tkinter as tk
from tkinter import ttk

# w = ttk.Label(None)
# print(w.winfo_class())

def buildGUI():
    s = ttk.Style()        # Style()로 스타일 설정 가능
    s.configure('WR.TLabel',
               foreground = 'white',
               background = 'red',
               font = ('돋움체', 30)
               )

    text_label1 = ttk.Label(win, text = '안녕하세요', style = 'WR.TLabel')

    text_label2 = ttk.Label(win)
    text_label2.configure(text = '반가워요', style = 'WR.TLabel')

    text_label1.pack()
    text_label2.pack()

win = tk.Tk()
win.title('라벨 위젯 예1')
win.geometry('1000x1000-1000+10')
buildGUI()                  
win.mainloop()
