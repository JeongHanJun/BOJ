import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("HJ GUI")
root.geometry("640x640")

menuval = Menu(root)

def Create_new_file():
    print("Create new file")

menu_file = Menu(menuval, tearoff=0)
menu_file.add_command(label="New File", command = Create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File")
menu_file.add_separator()
menu_file.add_command(label="Save")
menu_file.add_command(label="Sabe All", state = "disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)


# 메뉴 라벨
menuval.add_cascade(label="File", menu=menu_file)
menuval.add_cascade(label="Edit")

# 언어 메뉴 추가    radiobutton 이라서 누른 메뉴에 대해 체크표시가 적용되어있음
menu_lang = Menu(menuval, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menuval.add_cascade(label="Language", menu=menu_lang)

# View 메뉴
menu_view = Menu(menuval, tearoff=0)
menu_view.add_checkbutton(label="Show minimap")
menuval.add_cascade(label="View", menu=menu_view)


root.config(menu=menuval)
root.mainloop()