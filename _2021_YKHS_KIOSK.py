from tkinter import *

root=Tk()
root.title("YKHS Cafeteria KIOSK v1.0 (Alpha)")
root.attributes('-fullscreen', True) # 추후 Alt+F4 방지하기. 종료는 관리자 로그인 필요.

btn1=Button(root, padx=10. pady=10, width=100, height=100, text="선결재")
btn1.pack()
root.mainloop()

