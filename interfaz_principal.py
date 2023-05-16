import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFrame, QApplication, QMessageBox
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPalette, QBrush, QColor, QIcon
import sys
import img
import login
# 3
import main_login_administrativo



class InterfazPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
        self.setFixedSize(1300, 700)
        self.setStyleSheet("")

        # Diseño boton "Alumnos":
        self.boton_login_alumnos = QPushButton(self)
        self.boton_login_alumnos.setGeometry(QRect(700, 210, 580, 100))
        self.boton_login_alumnos.setStyleSheet(
            "QPushButton {font: 15pt \"SimSun\"; background-color: #8B4513; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #FF8C00; border-top-left-radius: 50px; font-weight: bold}")
        self.boton_login_alumnos.setObjectName("boton_control_alumnos")

       # Diseño boton "Docentes":
        self.boton_login_docentes = QPushButton(self)
        self.boton_login_docentes.setGeometry(QRect(700, 320, 580, 100))
        self.boton_login_docentes.setStyleSheet(
            "QPushButton {font: 15pt \"SimSun\"; background-color: #8B4513; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #FF8C00; border-top-left-radius: 50px; font-weight: bold}")
        self.boton_login_docentes.setObjectName("boton_control_docentes")

        # Diseño boton "Administrativos":
        self.boton_login_administrativos = QPushButton(self)
        self.boton_login_administrativos.setGeometry(QRect(700, 430, 580, 100))
        self.boton_login_administrativos.setStyleSheet(
            "QPushButton {font: 15pt \"SimSun\"; background-color: #8B4513; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #FF8C00; border-top-left-radius: 50px; font-weight: bold}")
        self.boton_login_administrativos.setObjectName("boton_nomina")

        # Diseño del FRAME
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 1300, 800))
        self.frame.setStyleSheet("border-image:url(img/fondo_login.jpg)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")

        # Diseño de la imagen que es (una etiqueta)
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(170, 200, 400, 400))
        self.label.setStyleSheet("border-image:url(img/login_main.png)")
        self.label.setText("")
        self.label.setObjectName("label")

        # Diseño del texto principal
        self.texto_principal = QLabel(self.frame)
        self.texto_principal.setGeometry(QRect(0, 30, 1200, 71))
        self.texto_principal.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.texto_principal.setObjectName("texto_principal")
        self.frame.raise_()

        self.boton_login_alumnos.raise_()
        self.boton_login_docentes.raise_()
        self.boton_login_administrativos.raise_()

       # Otorgarle una accion a los botones:
        self.boton_login_alumnos.clicked.connect(self.show_interface_login_alumno)
        self.boton_login_docentes.clicked.connect(self.show_interface_login_docente)
        self.boton_login_administrativos.clicked.connect(self.show_interface_login_administrativo)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QApplication.translate
        self.boton_login_alumnos.setText(_translate("Form", "Alumno"))
        self.boton_login_docentes.setText(_translate("Form", "Docente"))
        self.boton_login_administrativos.setText(
            _translate("Form", "Administrativo"))
        self.texto_principal.setText(_translate(
            "Form", f"                           INICIAR SESIÓN  COMO:      "))

    def show_interface_login_alumno(self):
        pass

    def show_interface_login_administrativo(self):
        self.interface_login_administrativo= main_login_administrativo.loginAdministrativo()
        self.interface_login_administrativo.show()
        self.close()

    def show_interface_login_docente(self):
        self.interface_login_administrativo= login.LoginWindow()
        self.interface_login_administrativo.show()
        self.close()


def aplicar_estilos(boton, color):
    style = f"""
    QPushButton {{
        font: 15pt \"SimSun\";""background-color: rgb(86, 157, 218);""border-top-left-radius: 50px;
    }}
    QPushButton:hover {{
        background-color: #FF5733;
    }} 
    """
    boton.setStyleSheet(style)
    boton.setAutoFillBackground(True)
    # Cambiar color de fondo al presionar
    palette = QPalette()
    brush = QBrush(QColor(color))
    palette.setBrush(QPalette.Button, brush)
    boton.setPalette(palette)
    # Cambiar estilo del cursor al pasar sobre el botón
    boton.setCursor(Qt.PointingHandCursor)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = InterfazPrincipal()
    ui.show()
    sys.exit(app.exec_())
