# code1(루트 윈도우)
import tkinter as tk

root_win = tk.Tk()  # 기본 윈도우 객체 반환
root_win.title('First Interface') # 제목표시줄에 윈도우 제목 표시
root_win.geometry('1000x1000-500+0') # 윈도우의 크기 및 위치 설정
root_win.resizable(width = False, height = False) # 윈도우 크기 고정 

# 화면 구성 및 이벤트 처리
root_win.mainloop() # 윈도우에서 다양한 이벤트 처리 시작을 지시
# .mainloop():지속적으로 사용자 이벤트를 전달반아 주어진 일을 처리할 수 있게 


