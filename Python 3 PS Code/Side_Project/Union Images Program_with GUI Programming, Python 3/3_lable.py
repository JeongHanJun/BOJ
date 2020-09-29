from tkinter import *

root = Tk()
root.title("HanJun GUI")
root.geometry("640x480+300+100")    # 가로x세로 + x좌표 + y좌표
#root.resizable(False, False)        # x, y 값 변경 불가 ( 창 크기 변경 불가)

label1 = Label(root, text="Hi")
label1.pack()

photo = PhotoImage(file = "GUI\Side_Project/1.png")
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text = "Re Hi")
    global photo2
    photo2 = PhotoImage(file = "GUI\Side_Project/2.png")
    label2.config(image = photo2)

btn = Button(root, text = "Click", command = change)
btn.pack()
root.mainloop()