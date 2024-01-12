from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5 import uic
import sys
import pymysql
import time
import os
from threading import Timer

#global conn, cur ## isdup: 0: 중복확인 통과 / 1: 중복확인 불통 or 안함.
isdup=1
conn=pymysql.connect(host="localhost", user='ykhs', password='qwerfdsazxcv1!', db='ykhs', charset='utf8')
cur=conn.cursor()
loginuser=''
loginpasswd=''
Home_Window=uic.loadUiType("./Home_Window.ui")[0]

class Home(QMainWindow, Home_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.digital_clock()
        self.ExitBtn.clicked.connect(self.EXIT_Warning)
        self.RegisBtn.clicked.connect(self.call_Account_create)
        self.loginBtn.clicked.connect(self.Login)
    def Login(self):
        self.username=self.usernameEntry.text()
        self.passwd=self.passwdEntry.text()
        conn.ping(True)
        sql="SELECT * FROM userinfo WHERE ID=%s and passwd=%s" #아이디 확인
        self.CheckID=cur.execute(sql, (self.username, self.passwd)) # Check: 0 - ID/PW 불일치, 1 - ID/PW 일치
        conn.close()
        self.usernameEntry.clear()
        self.passwdEntry.clear()
        if self.CheckID==0:
            QMessageBox.warning(self, "ID/PW 불일치", "ID 또는 비밀번호를 확인하십시오.")
        else:
            Home_Window_Logined(self)        
    def call_Home_Window_Logined(self):
        Home_Window_Logined(self)
    def digital_clock(self):
        t=time.time()
        kortime=time.localtime(t)
        self.Hour.display(kortime.tm_hour)
        self.Minute.display(kortime.tm_min)
        self.Second.display(kortime.tm_sec)
        timer=Timer(1, self.digital_clock)
        timer.start()    
    def EXIT_Warning(self, Event):
        message=QMessageBox.question(self, "경고", "종료하시겠습니까?", QMessageBox.Yes|QMessageBox.No)
        if message==QMessageBox.Yes:
            sys.exit(app.exec_())
        else:
            pass
    def call_Account_create(self): #BtnAction
        Account_Create(self)

class Home_Window_Logined(QMainWindow):
    def __init__(self, parent):
        super(Home_Window_Logined, self).__init__(parent)
        uic.loadUi("Home_Window_Logined.ui", self)
        self.showFullScreen()  
        self.LogoutBtn.clicked.connect(self.Logout)
        self.ChargeBtn.clicked.connect(self.call_Account_Check)
        self.OrderBtn.clicked.connect(self.call_Order_Menu)
    def Logout(self):
        loginuser=''
        loginpasswd=''
        self.close()
    def call_Account_Check(self): #BtnAction
        Account_Check(self)
    def call_Order_Menu(self): #BtnAction
        QMessageBox.information(self, "준비중입니다.", "준비중입니다.")



class Account_Create(QMainWindow):
    def __init__(self, parent):
        super(Account_Create, self).__init__(parent)
        uic.loadUi("Account_Create.ui", self)
        self.showFullScreen()
        self.CancelBtn.clicked.connect(self.Cancel_Warning) #메인화면 ""
        self.CreateBtn.clicked.connect(self.Registration)
        self.CheckBtn.clicked.connect(self.CheckID)
    def CheckID(self): 
        self.username=self.f_inputid.text()
        if self.username=="":
            QMessageBox.warning(self, "ID 공백 발생", "ID를 입력하십시오.")
        elif len(self.username)<6:
            QMessageBox.warning(self, "ID 입력 오류", "ID는 6자 이상 작성하십시오.")
        else:
            conn.ping(True)
            sql="SELECT ID FROM userinfo WHERE ID = %s"
            self.duplicated=cur.execute(sql, self.username)
            conn.close();
            global isdup
            if self.duplicated==0:
                QMessageBox.information(self, "ID 중복확인", "해당 ID는 사용가능합니다.")
                isdup=0
            else:
                QMessageBox.critical(self, "ID 중복확인", "해당 ID는 이미 사용중입니다.")
                isdup=1
    def Cancel_Warning(self):
        message=QMessageBox.question(self, "경고", "취소하시겠습니까?", QMessageBox.Yes|QMessageBox.No)
        if message==QMessageBox.Yes:
            self.close()
        else:
            pass
    def Registration(self):
        if isdup==0:
            self.username=self.f_inputid.text()
            self.passwd=self.f_inputpasswd.text()
            self.birthday=self.f_inputbirth.text()
            if self.passwd=="" and self.birthday=="":
                QMessageBox.warning(self, "PW 및 생년월일 공백 발생", "비밀번호 및 생년월일 8자리를 입력하십시오.")
            elif self.birthday=="":
                QMessageBox.warning(self, "생년월일 공백 발생", "생년월일 8자리를 입력하십시오.")
            elif self.passwd=="":
                QMessageBox.warning(self, "PW 공백 발생", "비밀번호를 입력하십시오.")
            else:
                if len(self.passwd)<6 and len(self.birthday)!=8:
                    QMessageBox.warning(self, "비밀번호 및 생년월일 입력 오류", "비밀번호는 6자 이상 입력하고, 생년월일을 올바르게 입력하시오.")
                elif len(self.passwd)<6:
                    QMessageBox.warning(self, "비밀번호 입력 오루", "비밀번호는 6자 이상 작성하십시오.")
                elif len(self.birthday)!=8:
                    QMessageBox.warning(self, "생년월일 입력 오류", "생년월일 8자를 올바르게 입력하세요.")
                else:
                    message=QMessageBox.question(self, "입력 정보 확인", "입력한 정보가 맞습니까?\n아이디: %s / 생년월일: %s" % (self.username, self.birthday))  
                    if message==QMessageBox.Yes:
                        try: 
                            conn.ping(True)
                            sql="INSERT INTO userinfo (ID, passwd, birthday, balance) VALUES(%s, %s, %s, 0)"
                            cur.execute(sql, (self.username, self.passwd, self.birthday))
                        except:
                            QMessageBox.critical(self, 'Error', '데이터 입력 오류 발생.\n다시 입력해 보십시오.')
                            conn.close()
                        else:
                            QMessageBox.information(self, 'Created Successfully!', '성공적으로 등록되었습니다.\n메인화면으로 돌아갑니다.')
                            conn.commit()
                            conn.close()
                            self.close()
                    else: 
                        pass
        else:
            QMessageBox.warning(self, "ID 중복 체크", "중복확인 버튼을 클릭하세요")

                      
class Account_Check(QMainWindow):
    def __init__(self, parent):
        super(Account_Check, self).__init__(parent)
        uic.loadUi("Account_Check.ui", self)
        self.CancelBtn.clicked.connect(self.Cancel_Warning)
        self.showFullScreen()
    def Cancel_Warning(self, event):
        message=QMessageBox.question(self, "경고", "취소하시겠습니까?", QMessageBox.Yes|QMessageBox.No)
        if message==QMessageBox.Yes:
            self.close()
        else:
            pass
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    HomeWindow=Home()
    HomeWindow.showFullScreen()
    app.exec_()