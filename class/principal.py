import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFrame, QApplication
from PyQt5.QtCore import Qt, QRect
import clases,tutorias, reuniones, asesorias ,actividades


class VentanaPrincipal(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VENTANA PRINCIPAL")
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint)
        self.setFixedSize(1300, 700)
        self.setStyleSheet("")


         #Diseño boton "tutorias":
        self.boton_tutorias = QPushButton(self)    
        self.boton_tutorias.setGeometry(QRect(700, 140, 580, 100))
        self.boton_tutorias.setStyleSheet("font: 15pt \"SimSun\";""background-color: rgb(86, 157, 218);""border-top-left-radius: 50px;")
        self.boton_tutorias.setObjectName("boton_tutorias")



       #Diseño boton "asesorias":
        self.boton_asesorias =  QPushButton(self)
        self.boton_asesorias.setGeometry(QRect(700, 250, 580, 100))
        self.boton_asesorias.setStyleSheet("font: 15pt \"SimSun\";""background-color: rgb(86, 157, 218);""border-top-left-radius: 50px;")
        self.boton_asesorias.setObjectName("boton_asesorias")

        #Diseño boton "actividades":
        self.boton_actividades = QPushButton(self)
        self.boton_actividades.setGeometry(QRect(700, 360, 580, 100))
        self.boton_actividades.setStyleSheet("font: 15pt \"SimSun\";""background-color: rgb(86, 157, 218);""border-top-left-radius: 50px;")
        self.boton_actividades.setObjectName("boton_actividades")

        #Diseño boton "reuniones":
        self.boton_reuniones = QPushButton(self)
        self.boton_reuniones.setGeometry(QRect(700, 470, 580, 100))
        self.boton_reuniones.setStyleSheet("font: 15pt \"SimSun\";""background-color: rgb(86, 157, 218);""border-top-left-radius: 50px;")
        self.boton_reuniones.setObjectName("boton_reuniones")

        #Diseño boton "clases":
        self.boton_clases = QPushButton(self)
        self.boton_clases.setGeometry(QRect(700, 580, 580, 100))
        self.boton_clases.setStyleSheet("font: 15pt \"SimSun\";""background-color: rgb(86, 157, 218);""border-top-left-radius: 50px;")
        self.boton_clases.setObjectName("boton_clases")

        #Diseño del FRAME
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 1300, 800))
        self.frame.setStyleSheet("border-image:url(img/fondo.png)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised) 
        self.frame.setObjectName("frame")

        #Diseño de la imagen que es (una etiqueta)
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(170, 200, 400, 400))
        self.label.setStyleSheet("border-image:url(img/profesor.png)")
        self.label.setText("")
        self.label.setObjectName("label")

        #Diseño del texto principal
        self.texto_principal = QLabel(self.frame)
        self.texto_principal.setGeometry(QRect(0, 30, 1200, 71))
        self.texto_principal.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.texto_principal.setObjectName("texto_principal")
        self.frame.raise_()
    
        self.boton_asesorias.raise_()
        self.boton_actividades.raise_()
        self.boton_reuniones.raise_()
        self.boton_clases.raise_()
        self.boton_tutorias.raise_()


       #Otorgarle una accion a los botones:
        self.boton_asesorias.clicked.connect(self.abrir_ventana_asesorias)
        self.boton_actividades.clicked.connect(self.abrir_ventana_actividades)
        self.boton_reuniones.clicked.connect(self.abrir_ventana_reuniones)
        self.boton_clases.clicked.connect(self.abrir_ventana_clases)
        self.boton_tutorias.clicked.connect(self.abrir_ventana_tutorias)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QApplication.translate
        self.boton_clases.setText(_translate("Form", "Clases"))
        self.boton_tutorias.setText(_translate("Form", "Tutorias"))
        self.boton_asesorias.setText(_translate("Form", "Asesorias"))
        self.boton_actividades.setText(_translate("Form", "Actividades universidad"))
        self.boton_reuniones.setText(_translate("Form", "Reuniones académicas"))
        self.texto_principal.setText(_translate("Form", "                    BIENVENIDO AL SISTEMA!"))



#Funcion para mostrar ventana asesorias
    def abrir_ventana_asesorias(self):
        self.ventana_asesorias = asesorias.ventanaAsesorias()
        self.ventana_asesorias.show()
        self.close()

#Funcion para mostrar ventana actividades
    def abrir_ventana_actividades(self):
        self.ventana_actividades = actividades.ventanaActividades()
        self.ventana_actividades.show()
        self.close()

  


#Funcion para mostrar ventana reuniones
    def abrir_ventana_reuniones(self):
        self.ventana_reuniones = reuniones.ventanaReuniones()
        self.ventana_reuniones.show()
        self.close()


#Funcion para mostrar ventana clases
    def abrir_ventana_clases(self):
        self.ventana_clases = clases.ventanaClases()
        self.ventana_clases.show()
        self.close()


#Funcion para mostrar ventana tutorias
    def abrir_ventana_tutorias(self):
        self.ventana_tutorias = tutorias.ventanaTutorias()
        self.ventana_tutorias.show()
        self.close()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = VentanaPrincipal()
    ui.show()
    sys.exit(app.exec_())
