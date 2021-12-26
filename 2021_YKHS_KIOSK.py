from tkinter import *
from tkinter import messagebox as msg

root=Tk()
root.title("YKHS Cafeteria KIOSK v1.0 (Alpha)")
root.attributes('-fullscreen', True) # 추후 Alt+F4, 작업관리자 등 방지하기. 종료는 관리자 로그인 필요.

def 준비중입니다():
    msg.showinfo("준비중입니다.","준비중입니다."
                 )
def main():
    exit=Button(root, font=("맑은 고딕", 15),  text="EXIT", command=root.destroy)
    exit.pack(anchor=NE)

    t1=Label(root, font=('맑은 고딕', 45, 'bold'), text="\n영광고등학교 매점 키오스크\n")
    t1.pack()
    


    btn1=Button(root, font=('맑은 고딕', 30), padx=30, pady=10, width=20, height=3, text="예치금 충전하기")
    btn1.pack(side=LEFT, padx=250)
    btn1=Button(root, font=('맑은 고딕', 30), padx=30, pady=10, width=20, height=3, text="주문하기", command=준비중입니다)
    btn1.pack(side=RIGHT, padx=250)
    root.mainloop()

main()