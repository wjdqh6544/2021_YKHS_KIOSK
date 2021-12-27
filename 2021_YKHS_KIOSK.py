import pymysql
from tkinter import *
from tkinter import messagebox as msg

root=Tk()
root.title("YKHS Cafeteria KIOSK v1.0 (Alpha)")
root.attributes('-fullscreen', True) # 추후 Alt+F4, 작업관리자 등 방지하기. 종료는 관리자 로그인 필요.

def DB_info():
    db_conn=pymysql.connect(
        host='localhost',
        port=3306,
        user='yk_cafe', 
        passwd='qwerfdsazxcv1!', # root: Ykhs.Cafe!qwer@2
        db='yk_cafe',
        charset='utf8' )        

def 준비중입니다():  #Push 팝업
    msg.showinfo("준비중입니다.","준비중입니다.")

def main():
    # Title ~ Login Form 여백
    blank_r2c0=Label(root, text="", height=8, width=50) 
    blank_r2c0.grid(row=2, column=0)
    blank_r5c0=Label(root, text="", width=50, height=12)
    blank_r5c0.grid(row=5, column=0)


    exit=Button(root, font=("맑은 고딕", 15),  text="EXIT", command=root.destroy)
    exit.grid(row=0, column=0, sticky="W")
    title=Label(root, font=('맑은 고딕', 45, 'bold'), text="\n영광고등학교 매점 키오스크\n") 
    title.grid(row=1, column=1, sticky="", columnspan=5)


 
    username=StringVar()
    password=StringVar()## ID, PW 변수로 저장
    usernameLabel=Label(root, text="UserName(ID)", font=('맑은 고딕', 30, 'bold'))
    usernameEntry=Entry(root, textvariable=username, font=('맑은 고딕', 20))
    usernameLabel.grid(row=3, column=1, sticky="E")
    usernameEntry.grid(row=3, column=2, sticky="W", padx=100, ipadx=100, ipady=15)
    passwdLabel=Label(root, text="Password", font=('맑은 고딕', 30, 'bold'))
    passwdEntry=Entry(root, textvariable=password, font=('맑은 고딕', 20), show="*")
    passwdLabel.grid(row=4, column=1, sticky="E")
    passwdEntry.grid(row=4, column=2, sticky="W", padx=100, pady=15, ipadx=100, ipady=15)
    LoginBtn=Button(root, font=("맑은 고딕", 30), padx=10, pady=10, width=10, text="계정 로그인", command=준비중입니다)
    LoginBtn.grid(row=3, column=3, rowspan=2)


    RegisBtn=Button(root, font=("맑은 고딕", 30), padx=10, pady=10, width=10, text="계정 만들기", command=준비중입니다)
    RegisBtn.grid(row=6, column=1)
    btn1=Button(root, font=('맑은 고딕', 30), padx=30, pady=10, text="예치금 충전하기", command=준비중입니다)
    btn1.grid(row=6, column=2)
    btn1=Button(root, font=('맑은 고딕', 30), padx=30, pady=10, text="주문하기", command=준비중입니다)
    btn1.grid(row=6, column=3)
    root.mainloop()
main()