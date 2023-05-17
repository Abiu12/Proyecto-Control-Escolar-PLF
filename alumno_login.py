from PySide2.QtCore import *
from PySide2.QtWidgets import *

from PyQt6 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setMaximumSize(QSize(800, 500))
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                 "border-radius:20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(170, 170, 255, 255), stop:1 rgba(255, 255, 255, 255)); \n  }")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)




        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(210, 190, 371, 71))
        self.label.setStyleSheet("font: 75 28pt \"Tw Cen MT\";")
        self.label.setObjectName("label")

        self.label_2 = QLabel(self.frame)
        self.label_2.setGeometry(QRect(320, 30, 171, 161))
        self.label_2.setStyleSheet("border-image: url(img/alumnitos.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.label_3 = QLabel(self.frame)
        self.label_3.setGeometry(QRect(260, 270, 101, 31))
        self.label_3.setStyleSheet("font: 18pt \"Tw Cen MT\";")
        self.label_3.setObjectName("label_3")


        self.label_4 = QLabel(self.frame)
        self.label_4.setGeometry(QRect(220, 330, 141, 31))
        self.label_4.setStyleSheet("font: 18pt \"Tw Cen MT\";")
        self.label_4.setObjectName("label_4")

        # Entrada del usuario
        self.users = QLineEdit(self.frame)
        self.users.setGeometry(QRect(380, 280, 171, 22))
        self.users.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.users.setObjectName("users")

        # Entrada de la contraseña
        self.password = QLineEdit(self.frame)
        self.password.setGeometry(QRect(380, 340, 171, 22))
        self.password.setStyleSheet("border-radius: 10px;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.password.setObjectName("password")
        self.password.setEchoMode(QLineEdit.Password)


        self.bt_ingresar = QPushButton(self.frame)
        self.bt_ingresar.setGeometry(QRect(240, 400, 151, 41))
        self.bt_ingresar.setStyleSheet("border-radius: 20px;\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(162, 162, 243);")
        self.bt_ingresar.setObjectName("bt_ingresar")


        self.btn_salir = QPushButton(self.frame)
        self.btn_salir.setGeometry(QRect(440, 400, 151, 41))
        self.btn_salir.setStyleSheet("border-radius: 20px;\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(162, 162, 243);")
        self.btn_salir.setObjectName("btn_salir")


        self.credencial_incorrecta = QLabel(self.frame)
        self.credencial_incorrecta.setGeometry(QRect(320, 368, 181, 31))
        self.credencial_incorrecta.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(255, 38, 38);\n"
                                   "font: 87 italic 9pt \"Segoe UI Black\";")
        self.credencial_incorrecta.setObjectName("credencial_incorrecta")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Bienvenido AlumnITO</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Usuario:"))
        self.label_4.setText(_translate("MainWindow", "Contraseña:"))
        self.credencial_incorrecta.setText(_translate("MainWindow", ""))
        self.bt_ingresar.setText(_translate("MainWindow", "Ingresar"))
        self.btn_salir.setText(_translate("MainWindow", "Salir"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())