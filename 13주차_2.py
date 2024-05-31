# code1
import tkinter as tk
from tkinter import ttk

def display_options(widget):
    config = widget.configure()
    for key, value in config.items():
        print(f'{key:15s}/t{value}')

widget = ttk.Label(None)
display_options(widget)

# code2
def buildGUI():
    text_label1 = ttk.Label(win, text = '안녕하세요')  # text를 설정하든 안하든
    text_label1.configure(text = '안녕하세요',         # configure을 통해 설정 가능
                          foreground = 'green',
                          background = 'blue',
                          font = ('굴림체', 15)
                          )

    text_label2 = ttk.Label(win)
    text_label2.configure(text = '반가워요',           # 문구 출력
                          foreground = 'white',        # 문구의 색 결정
                          background = 'red',          # 배경의 색 결정
                          font = ('맑은 고딕', 20)     # 문구의 폰트, 크기 결정
                          )


    
    text_label1.pack()      # 위젯 객체 생성 시 지정한 부모 윈도우 win에 나열식으로 배치
    text_label2.pack()

win = tk.Tk()
win.title('라벨 위젯 예1')
win.geometry('100x100-1000+10')
buildGUI()                  # 화면 구성
win.mainloop()

