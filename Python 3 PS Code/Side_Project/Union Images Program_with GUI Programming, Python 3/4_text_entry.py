from tkinter import *

root = Tk()
root.title("HanJun GUI")
root.geometry("640x480+300+100")    # 가로x세로 + x좌표 + y좌표


txt = Text(root, width = 30, height = 5)
txt.pack()
txt.insert(END, "텍스트 입력")

e = Entry(root, width = 30)
e.pack()
e.insert(0, "One Line")

def btncmd():
    #내용 출력
    print(txt.get("1.0", END))
    print(e.get())
    #내용삭제
    txt.delete("1.0", END)
    e.delete(0,END)

btn = Button(root, text = "Click", command = btncmd)
btn.pack()
root.mainloop()