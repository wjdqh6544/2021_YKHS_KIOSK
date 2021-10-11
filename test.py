from tkinter import *
import time
import threading

root=Tk()
root.title("YKHS Cafeteria KIOSK v1.0 (Alpha)")
root.attributes('-fullscreen', True) # 추후 Alt+F4, 작업관리자 등 방지하기. 종료는 관리자 로그인 필요.

while True:
    a=time.strftime("%H:%M:%S")
    threading.Timer(1000, a).start()
    print(a)
