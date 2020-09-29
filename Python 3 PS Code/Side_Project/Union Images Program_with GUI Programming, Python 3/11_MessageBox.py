from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("HJ GUI")
root.geometry("640x640")

def inform():
    msgbox.showinfo("알림", "정상동작 완료")

def warning():
    msgbox.showwarning("경고", "비정상 동작")

def error():
    msgbox.showerror("에러", "오류 발생")

def okcancel():
    response = msgbox.askokcancel("확인 / 취소", "확인 or 취소 선택")
    if response == 1:
        print("확인")
    elif response == 0:
        print("취소")

def retrycancel():
    response = msgbox.askretrycancel("다시 시도 / 취소", "다시 시도 or 취소 선택")
    if response == 1:
        print("다시 시도")
    elif response == 0:
        print("취소")

def yesno():
    response = msgbox.askyesno("예 / 아니오", "예 or 아니오 선택")
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")    
    
def yesnocancel():
    response = msgbox.askyesnocancel("예 / 아니오 / 취소", "내용을 저장하시겠습니까?")
    # 예 -> 저장 후 종료 , 아니오 -> 저장안하고 종료 , 취소 ->  그냥 취소
    print("응답 :", response)
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")

Button(root, command=inform, text="알림").pack()
Button(root, command=warning, text="경고").pack()   # !(느낌표)
Button(root, command=error, text="에러").pack()     # 삼각형 빨간색
Button(root, command=okcancel, text="확인 및 취소").pack() # 확인 or 취소 선택
Button(root, command=retrycancel, text="다시 시도 및 취소").pack()
Button(root, command=yesno, text="예 및 아니오").pack()
Button(root, command=yesnocancel, text="예 및 아니오 및 취소").pack()

root.mainloop()