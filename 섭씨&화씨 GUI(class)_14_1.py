import tkinter as tk
from tkinter import ttk

class ConvTempWin():
    def __init__(self):
        self.win = tk.Tk()                  # 기본 윈도우 객체 생성
        self.win.title('온도변환기-3단계')
        self.__buildGUI()                   # 화면 구성

    def __buildGUI(self):
        self.__create_input_frame().pack()
        self.__create_button_frame().pack()

    def __create_input_frame(self):
        frame = ttk.Frame(self.win)
        
        fahr_Label = ttk.Label(frame, text='화씨')
        self.__fahr = tk.IntVar()
        fahr_entry = ttk.Entry(frame, textvariable = self.__fahr, justify="right", width=11)

        cel_Label =  ttk.Label(frame, text='섭씨')
        self.__cels = tk.DoubleVar()
        cel_entry = ttk.Entry(frame, textvariable = self.__cels, justify="right", width=11)

        fahr_Label.pack(side=tk.LEFT)
        fahr_entry.pack(side=tk.LEFT)
        cel_Label.pack(side=tk.LEFT)
        cel_entry.pack(side=tk.LEFT)

        return frame


    def __create_button_frame(self):
        frame = ttk.Frame(self.win)

        f2c_btn =ttk.Button(frame, text='화씨->섭씨',
                            command=self.__f2c_handler)
        c2f_btn =ttk.Button(frame, text='섭씨->화씨',
                            command=self.__c2f_handler)
        reset_btn =ttk.Button(frame, text='초기화',
                            command=self.__reset_handler)
        quit_btn =ttk.Button(frame, text='종료',
                            command=self.win.destroy)

        f2c_btn.pack(side=tk.LEFT)
        c2f_btn.pack(side=tk.LEFT)
        reset_btn.pack(side=tk.LEFT)
        quit_btn.pack(side=tk.LEFT)
        
        return frame

    def __f2c_handler(self):
        fahr = self.__fahr.get()
        cels = (fahr-32)*5/9
        self.__cels.set(f'{cels:.2f}')

    def __c2f_handler(self):
        cels = self.__cels.get()
        fahr = cels * 9 / 5 + 32
        self.__fahr.set(f'{fahr:.0f}')

    def __reset_handler(self):
        self.__fahr.set('')
        self.__cels.set('')

    def start(self):
        self.win.mainloop()

tConverter = ConvTempWin()
tConverter.start()
