from tkinter import *
import time
import threading

root=Tk()
root.title("YKHS Cafeteria KIOSK v1.0 (Alpha)")
root.attributes('-fullscreen', True) # 추후 Alt+F4, 작업관리자 등 방지하기. 종료는 관리자 로그인 필요.

def main():
    def t2label():
        showtime=time.strftime("%H:%M:%S")
        t2=Label(frame, font=('맑은 고딕', 30, 'bold'), fg='blue', text="\n현재 시각: "+str(showtime))
        t2.pack()
        time.sleep(1)
        t2.forget()
        threading.Timer(0, t2label).start()
    
    exit=Button(root, font=("맑은 고딕", 15),  text="EXIT", command=root.destroy)
    exit.pack(anchor=NE)

    frame=Frame(root, bd=40, bg='gray')
    frame.pack(anchor=CENTER)

    t1=Label(frame, font=('맑은 고딕', 45, 'bold'), text="\n영광고등학교 매점 키오스크\n")
    t1.pack()
    t2label()
    #mainlogo = PhotoImage(file=".\Sources\Logo.gif")
    #label2 = Label(root, image = mainlogo)
    #label2.pack()
    
    btn1=Button(root, padx=10, pady=10, width=25, height=10, text="예치금 충전하기")
    btn1.pack(side=LEFT)
    btn1=Button(root, padx=10, pady=10, width=25, height=10, text="주문하기")
    btn1.pack(side=RIGHT)
    root.mainloop()

main()