import tkinter as tk
from tkinter import ttk

class MemberJoin():
    hobby_list = ['영화시청','음악감상','사진찍기','운동']

    def __init__(self):
        self.win = tk.Tk()
        self.win.title('회원 가입')
        #self.win.geometry('250x300')
        self.__buildGUI()

    def __buildGUI(self):
        self.__create_name_input_frame().grid(row=0,column=0,sticky='w')
        self.__create_grade_input_frame().grid(row=1,column=0,sticky='w')
        self.__create_hobby_input_frame().grid(row=2,column=0,sticky='w')
        self.__create_button_frame().grid(row=3,column=0,sticky='e')

    def __create_name_input_frame(self):
        frame = ttk.Frame(self.win)

        self.text_label = ttk.Label(frame, text='이름:')

        self.name = tk.StringVar()
        input_entry = ttk.Entry(frame, textvariable=self.name)

        self.text_label.grid(row=0,column=0)
        input_entry.grid(row=0,column=1)

        return frame

    def __create_grade_input_frame(self):
        frame = ttk.Frame(self.win)

        self.text_label = ttk.Label(frame, text='학년:')
        self.text_label.grid(row=0, column=0)

        sub_frame = ttk.Frame(frame)
        self.grade = tk.IntVar()
        for i in range(1, 5):
            grade_btn = ttk.Radiobutton(sub_frame,
                                        text=f'{i}학년',
                                        value=i,
                                        variable=self.grade)
            grade_btn.pack(side=tk.LEFT)
        sub_frame.grid(row=0,column=1)
        return frame

    def __create_hobby_input_frame(self):
        frame = ttk.Frame(self.win)

        self.text_label = ttk.Label(frame, text='취미:')
        self.text_label.grid(row=0, column=0)

        sub_frame = ttk.Frame(frame)
        self.hobby = []
        for i in range(4):
            self.hobby.append(tk.IntVar())
            hobby_btn = ttk.Checkbutton(sub_frame,
                                        text=self.hobby_list[i],
                                        variable=self.hobby[i])
            hobby_btn.pack(side=tk.LEFT)
        sub_frame.grid(row=0,column=1)
        return frame

    def __create_button_frame(self):
        frame = ttk.Frame(self.win)

        input_btn = ttk.Button(frame, text='입력',
                               command=self.__input_btn_clicked)
        quit_btn = ttk.Button(frame, text='종료',
                              command=self.win.destroy)

        input_btn.pack(side=tk.LEFT)
        quit_btn.pack(side=tk.LEFT)

        return frame

    def __input_btn_clicked(self):
        print(self.name.get())
        print(self.grade.get())

        for i in range(4):
            if self.hobby[i].get() == True:
                print(self.hobby_list[i])

member = MemberJoin()
member.win.mainloop()
