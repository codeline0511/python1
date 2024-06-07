import tkinter as tk
from tkinter import ttk

class SayHelloWin:
    def __init__(self):
        self.win = tk.Tk()                  
        self.win.title('버튼 위젯 예-OOP')
        self.__buildGUI()

    def __buildGUI(self):
        self.__create_input_frame().pack()
        self.__create_button_frame().pack()

    def __create_input_frame(self):
        frame = ttk.Frame(self.win)

        self.text_label = ttk.Label(frame, text='안녕하세요')

        self.name = tk.StringVar()
        input_entry = ttk.Entry(frame, textvariable=self.name)

        self.text_label.grid()
        input_entry.grid(row=0, column=1)

        return frame

    def __create_button_frame(self):
        frame = ttk.Frame(self.win)

        input_btn = ttk.Button(frame, text = '입력', command=self.__input_btn_handler)
        quit_btn = ttk.Button(frame, text ='종료', command=self.win.destroy)

        input_btn.pack(side=tk.LEFT)
        quit_btn.pack(side=tk.LEFT)

        return frame

    def __input_btn_handler(self):
        self.text_label.configure(
            text='반가워요, '+ self.name.get())
        self.name.set('')

hello = SayHelloWin()
hello.win.mainloop()
