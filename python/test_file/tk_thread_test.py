#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import tkinter
import tkinter.messagebox
from threading import Thread

download_btn = None

class DownloadThread(Thread):
    def run(self):
        time.sleep(10)
        tkinter.messagebox.showinfo('Tips', 'finish download!')
        global download_btn
        download_btn.config(state=tkinter.NORMAL)

def download():
    #time.sleep(10)
    #tkinter.messagebox.showinfo('Tips', 'finish download!')
    global download_btn
    download_btn.config(state=tkinter.DISABLED)
    DownloadThread(daemon=True).start()

def show_about():
    tkinter.messagebox.showinfo('about', 'author: derekyuan')

def tk_thread_test1():
    top = tkinter.Tk()
    top.title('Single Thread')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    global download_btn
    download_btn = tkinter.Button(panel, text='download', command=download)
    download_btn.pack(side='left')
    btn2 = tkinter.Button(panel, text='about', command=show_about)
    btn2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == '__main__':
    tk_thread_test1()

