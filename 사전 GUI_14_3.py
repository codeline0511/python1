import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

def buildGUI():
    l_word = ttk.Label(win, text='단어: ')
    global word
    word = tk.StringVar()
    e_word = ttk.Entry(win, textvariable=word, width=15)

    l_meaning = ttk.Label(win, text='뜻: ')
    global mean
    mean = tk.StringVar()
    e_meaning = ttk.Entry(win, textvariable=mean, width=15)

    b_search = ttk.Button(win, text='검색', width=5, command=search)
    b_add = ttk.Button(win, text='추가', width=5, command=add)
    b_reset = ttk.Button(win, text='초기화', width=5, command=reset)
    b_exit = ttk.Button(win, text='종료', width=5, command=end)

    l_word.grid(row=0, column=0, sticky='e', padx=10)
    e_word.grid(row=0, column=1, sticky='w', padx=10)
    b_search.grid(row=0, column=2, ipadx=10, ipady=5, sticky='w')
    b_add.grid(row=0, column=3, ipadx=10, ipady=5, sticky='w')

    l_meaning.grid(row=1, column=0, sticky='e', padx=10)
    e_meaning.grid(row=1, column=1, columnspan=3, sticky='w')

    b_reset.grid(row=2, column=0, ipadx=10, ipady=5, padx=10, sticky='w')
    b_exit.grid(row=2, column=1, ipadx=10, ipady=5, sticky='w')

def loadData():
    words = {}
    if not os.path.exists('words.txt'):
        return words
    fp = open('words.txt', 'r', encoding='utf-8')
    for line in fp:
        word = line.split(' ')
        key = word[0].strip()
        value = word[1].strip()
        words[key] = value
    fp.close()
    return words

def add():
    global words
    words[word.get()] = mean.get()
    messagebox.showinfo('추가 확인', '단어' + word.get() + '를 추가했습니다.')
    reset()

def search():
    w = word.get()
    if w not in words:
        messagebox.showinfo('검색 오류', w + '란 단어는 없습니다!')
        reset()
        return
    n = words[w]
    mean.set(n)

def reset():
    word.set('')
    mean.set('')

def end():
    fp = open('words.txt', 'w', encoding='utf-8')
    for w in words.keys():
        n = words[w]
        fp.write(w + ':' + n + '\n')
    fp.close()
    win.destroy()

win = tk.Tk()
win.title('단어장')
win.geometry('400x100')
buildGUI()
words = loadData()
win.mainloop()
