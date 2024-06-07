import tkinter as tk
from tkinter import ttk

class MemberJoin:
    habbit_list = ['영화시청', '음악감상', '사진찍기', '운동']
    
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('회원 가입')
        self.__buildGUI()

    def __buildGUI(self):
        self.__input_name_frame().pack()
        self.__choose_grade_frame().pack()
        self.__choose_habbit_frame().pack()
        self.__create_button_frame().pack()

    def __input_name_frame(self):
        frame = ttk.Frame(self.win)

        self.name_label = ttk.Label(frame, text ='이름:')

        self.name = tk.StringVar()
        input_name = ttk.Entry(frame, textvariable=self.name)

        self.name_label.grid()
        input_name.grid(row=0, column=1)

        return frame

    def __choose_grade_frame(self):
        frame = ttk.Frame(self.win)

        self.grade_label = ttk.Label(frame, text = '학년:')

        self.grade = tk.IntVar()
        for i in range(1, 5):
            radio_btn = ttk.Radiobutton(frame,
                                        text = f'{i}학년',
                                        value = i,
                                        variable = self.grade
                                        )
            radio_btn.pack()

        return frame

    def __choose_habbit_frame(self):
        frame = ttk.Frame(self.win)
        
        self.habbit_label = ttk.Label(frame, text = '취미:')
       
        self.check_habbit = []
        for i in range(4):
            self.check_habbit.append(tk.IntVar())
            check_habbit_btn = ttk.Checkbutton(frame,
                                               text = self.habbit_list[i],
                                               variable = self.check_habbit[i]
                                               )
            check_habbit_btn.pack()
            
        return frame

    def __create_button_frame(self):
        frame = ttk.Frame(self.win)

        input_btn = ttk.Button(frame, text = '입력', command=self.__input_btn_handler)
        quit_btn = ttk.Button(frame, text ='종료', command=self.win.destroy)

        input_btn.pack(side=tk.RIGHT)
        quit_btn.pack(side=tk.RIGHT)

        return frame

    def __input_btn_handler(self):
        print(self.name.get())
        print(self.grade.get())

        for i in range(4):
            if self.check_habbit[i].get() == True:
                print(self.habbit_list[i])
        
        

Member = MemberJoin()
Member.win.mainloop()
              

    
