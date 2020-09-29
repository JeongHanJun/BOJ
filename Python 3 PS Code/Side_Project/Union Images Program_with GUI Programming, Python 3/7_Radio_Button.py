from tkinter import *

root = Tk()
root.title("HJ GUI")
root.geometry("640x640")

Label(root, text="햄버거 선택").pack()

Radiovar = IntVar()#int형 Radiovar
btn_1 = Radiobutton(root, text="치즈버거", value=1, variable=Radiovar)
btn_1.select()
btn_1.pack()
btn_2 = Radiobutton(root, text="빅맥", value=2, variable=Radiovar).pack()
btn_3 = Radiobutton(root, text="상하이스파이스 치킨버거", value=3, variable=Radiovar).pack()
btn_4 = Radiobutton(root, text="쿼터파운드 치즈버거", value=4, variable=Radiovar).pack()
'''btn_1.pack()
btn_2.pack()
btn_3.pack()
btn_4.pack()'''

Label(root, text="음료 선택").pack()
drinkvar=StringVar()
btn_drink_1 = Radiobutton(root, text="콜라", value="콜라", variable=drinkvar)
btn_drink_1.select()
btn_drink_1.pack()
btn_drink_2 = Radiobutton(root, text="사이다", value="사이다", variable=drinkvar).pack()
btn_drink_3 = Radiobutton(root, text="환타", value="환타", variable=drinkvar).pack()


def btncmd():
    print(Radiovar.get())
    print(drinkvar.get())

btn = Button(root, text = "메뉴 주문", command = btncmd)
btn.pack()

root.mainloop()