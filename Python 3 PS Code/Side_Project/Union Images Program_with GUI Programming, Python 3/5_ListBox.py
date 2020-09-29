from tkinter import *

root = Tk()
root.title("HJ GUI")
root.geometry("640x640")

listbox = Listbox(root, selectmode = "extended", height = 0)
# select mode의경우
# selectmode = "single"의 경우 한개의 list만 사용 가능
# height = 3이면 3개단위로 보여짐, 0으로 하면 list의 모든 원소 다 보여줌

listbox.insert(0, "Apple")
listbox.insert(1, "Orange")
listbox.insert(2, "Banana")
listbox.insert(END, "Grape")
listbox.insert(END, "Melon")
listbox.pack()


def btncmd():
    # 삭제
    # listbox.delete(END)# 맨 뒤의 항목을 삭제

    # 갯수 확인
    # print("In the List", listbox.size(), "elements exist")

    # 항목 확인
    # print("1~3번째 항목 : ", listbox.get(0,2))

    # 선택된 항목 확인
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text = "Click", command = btncmd)
btn.pack()

root.mainloop()