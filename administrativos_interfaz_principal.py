import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFrame, QApplication
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPalette, QBrush, QColor
import sys
import img

import administrativos_interfaz_control_alumnos
import administrativos_interfaz_control_docentes
# import administrativos_interfaz_nomina
# import administrativos_interfaz_eventos

class InterfazAdministrativo(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VENTANA PRINCIPAL")
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
        self.setFixedSize(1300, 700)
        self.setStyleSheet("")

        #Diseño boton "control de alumnos":
        self.boton_ctrl_alumnos = QPushButton(self)    
        self.boton_ctrl_alumnos.setGeometry(QRect(700, 140, 580, 100))
        self.boton_ctrl_alumnos.setStyleSheet("QPushButton {font: 15pt \"SimSun\"; background-color: #FF5733; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #FF8C00; border-top-left-radius: 50px; font-weight: bold}" )
        self.boton_ctrl_alumnos.setObjectName("boton_control_alumnos")

       #Diseño boton "control de docentes":
        self.boton_ctrl_docentes =  QPushButton(self)
        self.boton_ctrl_docentes.setGeometry(QRect(700, 250, 580, 100))
        self.boton_ctrl_docentes.setStyleSheet("QPushButton {font: 15pt \"SimSun\"; background-color: #FF5733; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #FF8C00; border-top-left-radius: 50px; font-weight: bold}" )
        self.boton_ctrl_docentes.setObjectName("boton_control_docentes")

        #Diseño boton "nomina":
        self.boton_nomina = QPushButton(self)
        self.boton_nomina.setGeometry(QRect(700, 470, 580, 100))
        self.boton_nomina.setStyleSheet("QPushButton {font: 15pt \"SimSun\"; background-color: #FF5733; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #FF8C00; border-top-left-radius: 50px; font-weight: bold}" )
        self.boton_nomina.setObjectName("boton_nomina")

        #Diseño boton "actividades":
        self.boton_actividades = QPushButton(self)
        self.boton_actividades.setGeometry(QRect(700, 360, 580, 100))
        self.boton_actividades.setStyleSheet("QPushButton {font: 15pt \"SimSun\"; background-color: #FF5733; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #FF8C00; border-top-left-radius: 50px; font-weight: bold}" )
        self.boton_actividades.setObjectName("boton_actividades")

        #Diseño del FRAME
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 1300, 800))
        self.frame.setStyleSheet("border-image:url(img/fondo_admin.jpg)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised) 
        self.frame.setObjectName("frame")

        #Diseño de la imagen que es (una etiqueta)
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(170, 200, 400, 400))
        self.label.setStyleSheet("border-image:url(img/administracion.png)")
        self.label.setText("")
        self.label.setObjectName("label")

        #Diseño del texto principal
        self.texto_principal = QLabel(self.frame)
        self.texto_principal.setGeometry(QRect(0, 30, 1200, 71))
        self.texto_principal.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.texto_principal.setObjectName("texto_principal")
        self.frame.raise_()
    
        self.boton_ctrl_alumnos.raise_()
        self.boton_ctrl_docentes.raise_()
        self.boton_nomina.raise_()
        self.boton_actividades.raise_()


       #Otorgarle una accion a los botones:
        self.boton_ctrl_alumnos.clicked.connect(self.show_interface_control_alumnos)
        self.boton_ctrl_docentes.clicked.connect(self.show_interface_control_docentes)
        self.boton_nomina.clicked.connect(self.show_interface_nomina)
        self.boton_actividades.clicked.connect(self.show_interface_eventos)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QApplication.translate
        self.boton_ctrl_alumnos.setText(_translate("Form", "Control alumnos"))
        self.boton_ctrl_docentes.setText(_translate("Form", "Control docentes"))
        self.boton_nomina.setText(_translate("Form", "Nómina"))
        self.boton_actividades.setText(_translate("Form", "Actividades"))
        self.texto_principal.setText(_translate("Form", "            BIENVENIDO AL SISTEMA ADMINISTRADOR"))

    def show_interface_control_alumnos(self):
        self.interface_control_alumnos = administrativos_interfaz_control_alumnos.InterfazControlAlumnos()
        self.interface_control_alumnos.show()
        self.close()
    def show_interface_control_docentes(self):
        pass
        self.interface_control_docentes = administrativos_interfaz_control_docentes.InterfazControlDocentes()
        self.interface_control_docentes.show()
        self.close()
    def show_interface_nomina(self):
        pass
        # self.interface_nomina= InterfazNomina()
        # self.interface_nomina.show()
        # self.close()
    def show_interface_eventos(self):
        pass
        # self.interface_eventos= InterfazEventos()
        # self.interface_eventos.show()
        # self.close()
def aplicar_estilos(boton,color):
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
    ui = InterfazAdministrativo()
    ui.show()
    sys.exit(app.exec_())

