import tkinter.ttk as ttk
import time
from tkinter import *

root = Tk()
root.title("HJ GUI")
root.geometry("640x640")

'''progressbar = ttk.Progressbar(root, maximum=100, mode = "determinate")    # mode = "indeterminate"  이면 좌-우로 왔다갔다 무한반복, determinate 이면 게이지가 좌->우로 차는거 반복
progressbar.start(10)   # 10ms 마다 출력
progressbar.pack()

def btncmd():
    progressbar.stop()

btn = Button(root, text = "중지", command = btncmd)
btn.pack()'''

pvar = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length = 200, variable = pvar)
progressbar2.pack()

def btncmd2():
    for i in range(1,101):
        time.sleep(0.01)    # 0.01초 대기
        pvar.set(i) # progressbar2 의 값을 설정
        progressbar2.update()   # 변경되는 값들을 실시간으로 출력하여 바의 게이지가 계속 변동되는 것을 출력
        print(pvar.get())
btn = Button(root, text="시작", command=btncmd2)
btn.pack()
root.mainloop()