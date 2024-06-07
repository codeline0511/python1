import tkinter as tk
from tkinter import ttk

def buildGUI():
    global F_label
    F_label = ttk.Label(win, text = '화씨')
    
    global F_num
    F_num =tk.IntVar()
    input_F_entry = ttk.Entry(win, textvariable = F_num)

    F_to_C_btn = ttk.Button(win, text = '화씨->섭씨',
                           command = F_to_C_handler)

    global C_label
    C_label = ttk.Label(win, text = '섭씨')
    
    global C_num
    C_num =tk.DoubleVar()
    input_C_entry = ttk.Entry(win, textvariable = C_num)

    C_to_F_btn = ttk.Button(win, text = '섭씨->화씨',
                            command = C_to_F_handler)

    reset_btn= ttk.Button(win, text = '초기화',
                          command = reset_handler)
    
    quit_btn = ttk.Button(win, text = '종료',
                          command = win.destroy)

    F_label.pack()
    input_F_entry.pack()
    F_to_C_btn.pack()
    C_label.pack()
    input_C_entry.pack()
    C_to_F_btn.pack()
    reset_btn.pack()
    quit_btn.pack()                   
    
    def F_to_C_handler():
        input_C_entry.configure(F_num.get())
        C_num = (F_num - 32) * 5 / 9
        C_num.set(f'{C_num:2f}')

    def C_to_F_handler():
        input_F_entry.configure(C_num.get())
        F_num = (C_num - 32) * 5 / 9
        F_num.set(f'{F_num:0f}')

    def reset_handler():
        C_num.set('')
        F_num.set('')

        
win = tk.Tk()
win.title('온도변환기-1단계')
# win.geometry('100x100-1000+300')
buildGUI()                  
win.mainloop()


