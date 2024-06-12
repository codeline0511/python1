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
#-------------------------------------------
class SayHelloWin1:
    def __init__(self):
        self.win = tk.Tk()                  # 기본 윈도우 객체 생성
        self.win.title('버튼 위젯 예-OOP')
        self.__buildGUI()                   # 화면 구성

    def __buildGUI(self):
        self.text_label = ttk.Label(self.win,
                                    text = '안녕하세요')

        self.name = tk.StringVar()
        input_entry = ttk.Entry(self.win,
                                textvariable=self.name)

        input_btn = ttk.Button(self.win, text ='입력',
                               command=self.__input_btn_handler)

        quit_btn = ttk.Button(self.win, text = '종료', command=self.win.destroy)

        self.text_label.pack()
        input_entry.pack()
        input_btn.pack()
        quit_btn.pack()

    def __input_btn_handler(self):
        self.text_label.configure(
            text ='반가워요,' + self.name.get())
        self.name.set('')

hello = SayHelloWin1()
hello.win.mainloop()
#--------------------------------------------
class SayHelloWin2:
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

hello = SayHelloWin2()
hello.win.mainloop()

