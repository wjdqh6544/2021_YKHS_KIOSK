# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Balance_Update.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1121, 835)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Warning1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(60)
        self.Warning1.setFont(font)
        self.Warning1.setAlignment(QtCore.Qt.AlignCenter)
        self.Warning1.setObjectName("Warning1")
        self.gridLayout.addWidget(self.Warning1, 0, 0, 1, 5)
        spacerItem = QtWidgets.QSpacerItem(100, 100, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 2, 1)
        self.Warning3 = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.Warning3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(30)
        self.Warning3.setFont(font)
        self.Warning3.setAlignment(QtCore.Qt.AlignCenter)
        self.Warning3.setObjectName("Warning3")
        self.gridLayout.addWidget(self.Warning3, 8, 0, 1, 5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        self.f_balinfo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_balinfo.sizePolicy().hasHeightForWidth())
        self.f_balinfo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.f_balinfo.setFont(font)
        self.f_balinfo.setObjectName("f_balinfo")
        self.gridLayout.addWidget(self.f_balinfo, 3, 2, 1, 2)
        self.inputid = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputid.sizePolicy().hasHeightForWidth())
        self.inputid.setSizePolicy(sizePolicy)
        self.inputid.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.inputid.setFont(font)
        self.inputid.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.inputid.setObjectName("inputid")
        self.gridLayout.addWidget(self.inputid, 2, 1, 1, 1)
        self.returnhome = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returnhome.sizePolicy().hasHeightForWidth())
        self.returnhome.setSizePolicy(sizePolicy)
        self.returnhome.setMinimumSize(QtCore.QSize(125, 60))
        self.returnhome.setSizeIncrement(QtCore.QSize(0, 0))
        self.returnhome.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(15)
        self.returnhome.setFont(font)
        self.returnhome.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.returnhome.setObjectName("returnhome")
        self.gridLayout.addWidget(self.returnhome, 5, 1, 1, 3)
        self.f_inputid = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_inputid.sizePolicy().hasHeightForWidth())
        self.f_inputid.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.f_inputid.setFont(font)
        self.f_inputid.setObjectName("f_inputid")
        self.gridLayout.addWidget(self.f_inputid, 2, 2, 1, 2)
        self.balinfo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.balinfo.sizePolicy().hasHeightForWidth())
        self.balinfo.setSizePolicy(sizePolicy)
        self.balinfo.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.balinfo.setFont(font)
        self.balinfo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.balinfo.setObjectName("balinfo")
        self.gridLayout.addWidget(self.balinfo, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(100, 100, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 4, 2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YKHS Cafeteria KIOSK (alpha v1.0 / Last Updated 22.01.03)"))
        self.Warning1.setText(_translate("MainWindow", "잔액 추가가 완료되었습니다."))
        self.Warning3.setText(_translate("MainWindow", "잔액 미 업데이트시 담당자 호출바랍니다."))
        self.f_balinfo.setText(_translate("MainWindow", "[잔액출력부]"))
        self.inputid.setText(_translate("MainWindow", "Username (ID)"))
        self.returnhome.setText(_translate("MainWindow", "처음으로"))
        self.f_inputid.setText(_translate("MainWindow", "[ID출력부]"))
        self.balinfo.setText(_translate("MainWindow", "잔액"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
