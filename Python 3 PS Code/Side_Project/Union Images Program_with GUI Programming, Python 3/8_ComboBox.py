from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("HJ GUI")
root.geometry("640x640")


Dateval=[str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height = 5, values=Dateval)
combobox.pack()
combobox.set("카드 결제일 선택")


combobox2 = ttk.Combobox(root, height = 5, values=Dateval, state="readonly")
combobox2.current(0)
combobox2.pack()


def btncmd():
    print(combobox.get())
    print(combobox2.get())

btn = Button(root, text = "메뉴 주문", command = btncmd)
btn.pack()

root.mainloop()