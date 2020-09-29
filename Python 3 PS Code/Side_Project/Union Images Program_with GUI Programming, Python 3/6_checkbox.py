from tkinter import *

root = Tk()
root.title("HJ GUI")
root.geometry("640x640")

checkvar = IntVar() #checkvar 에 int형으로 값을 저장한다
checkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=checkvar)
#checkbox.select()   #화면에 checkbox가 체크되있는 상태로
#checkbox.deselect() # 위와 반대 , 기본값 디폴트값은 deselect 임
checkbox.pack()     #화면에 checkbox 출력

checkvar2 = IntVar()
checkbox2 = Checkbutton(root, text = "1주일동안 보지 않기",variable=checkvar2)
checkbox2.pack()

def btncmd():
   print(checkvar.get())    #0 은 체크 해제, 1은 체크
   print(checkvar2.get())


btn = Button(root, text = "Click", command = btncmd)
btn.pack()

root.mainloop()