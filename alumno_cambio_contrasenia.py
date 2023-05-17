from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
import conexion_alumno
import moduloAlumno
import tkinter as tk
from conexion_alumno import Registro_datos
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFrame, QApplication, QToolTip
from PyQt5.QtCore import Qt, QRect


class AlumnoCambioContrasenia(QMainWindow):
    def __init__(self, nombreUser, idAlumno):
        super().__init__()
        # Titulo de la ventana
        self.setWindowTitle("Cambio de contraseña")
        self.setFixedSize(1300, 700)
        self.setGeometry(QtCore.QRect(0, 0, 1300, 800))
        # self.setStyleSheet("border-image:url(img/fondo.png)")
        self.setStyleSheet("")
        self.nombreUsuario = "" + nombreUser
        self.idAlumno = str(idAlumno)
        # Centrar ventana en la pantalla
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.centralWidget()

        # Diseño del FRAME
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 1300, 800))
        self.frame.setStyleSheet("border-image:url(img/fondo.png)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")

        # Crear la etiqueta de reporte
        self.report_label = QtWidgets.QLabel(self)
        self.report_label.setText("Ingresa tu contraseña actual:")
        self.report_label.setGeometry(QtCore.QRect(280, 270, 353, 41))
        self.report_label.setStyleSheet("font: 75 16pt \"Trebuchet MS\";")

        self.report_label_2 = QtWidgets.QLabel(self)
        self.report_label_2.setText("Ingresa tu nueva contraseña:")
        self.report_label_2.setGeometry(QtCore.QRect(280, 370, 350, 41))
        self.report_label_2.setStyleSheet("font: 75 16pt \"Trebuchet MS\";")

        self.imagen = QtWidgets.QLabel(self)
        self.imagen.setGeometry(QtCore.QRect(550, 50, 161, 161))
        self.imagen.setStyleSheet("border-image: url(img/contrasenia.png);")
        self.imagen.setObjectName("label_3")

        self.contrasenia_actual = QtWidgets.QLineEdit(self)
        self.contrasenia_actual.setGeometry(QtCore.QRect(650, 270, 251, 31))
        self.contrasenia_actual.setObjectName("lineEdit")
        self.contrasenia_actual.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contrasenia_actual.setStyleSheet("QLineEdit { border: 2px solid qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 red, stop: 1 blue); border-radius: 5px; }")


        self.contrasenia_nueva = QtWidgets.QLineEdit(self)
        self.contrasenia_nueva.setGeometry(QtCore.QRect(650, 380, 251, 31))
        self.contrasenia_nueva.setObjectName("lineEdit_2")
        self.contrasenia_nueva.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contrasenia_nueva.setStyleSheet("QLineEdit { border: 2px solid qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 red, stop: 1 blue); border-radius: 5px; }")


        # Boton enviar
        self.boton_enviar = QtWidgets.QPushButton(self)
        self.boton_enviar.setGeometry(QtCore.QRect(500, 470, 381, 41))
        self.boton_enviar.setStyleSheet(
            "QPushButton {"
            "   font: 15pt \"SimSun\";"
            "   background-color: rgb(240, 240, 240);"
            "   border: 2px solid qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 red, stop: 1 blue);"
            "   border-radius: 10px;"
            "   padding: 5px;"
            "}"
            "QPushButton:hover {"
            "   background-color: rgb(220, 220, 220);"
            "}"
            "QPushButton:pressed {"
            "   background-color: rgb(200, 200, 200);"
            "}"
            "QPushButton:checked {"
            "   background-color: rgb(86, 157, 218);"
            "   color: white;"
            "}"
        )
        self.boton_enviar.setObjectName("boton_calificaciones")
        self.boton_enviar.setText("Actualizar contraseña")
        self.boton_enviar.clicked.connect(self.mostrar_ventana)

        # Boton de volver
        self.boton_volver = QtWidgets.QPushButton(self)
        self.boton_volver.setGeometry(QtCore.QRect(1060, 80, 61, 61))
        self.boton_volver.setStyleSheet("border-image:url(img/regreso.png)")
        self.boton_volver.setText("")
        self.boton_volver.setObjectName("volver")
        self.boton_volver.clicked.connect(self.volver)

        # Configurar el botón de ayuda
        self.boton_ayuda = QPushButton(self)
        self.boton_ayuda.setStyleSheet("border-image:url(img/ayuda3.png)")
        self.boton_ayuda.setToolTip('Ayuda')  # Texto emergente al colocar el mouse sobre el botón
        self.boton_ayuda.setGeometry(1170, 80, 61, 61)
        self.boton_ayuda.clicked.connect(self.mostrarAyuda)
        self.boton_ayuda.enterEvent = self.mostrarToolTip
        self.boton_ayuda.leaveEvent = self.ocultarToolTip

    def mostrarAyuda(self):
        # Aquí puedes definir lo que sucede cuando se hace clic en el botón de ayuda
        print('Haz clic en el botón de ayuda')
        mensaje = QtWidgets.QMessageBox()
        mensaje.setIcon(QtWidgets.QMessageBox.Information)
        mensaje.setWindowTitle("Información de los datos")
        texto_mensaje = """Para cambiar tu contraseña, sigue estos pasos:

1. Ingresa tu contraseña actual en el campo correspondiente.
2. Luego, ingresa tu nueva contraseña en el campo designado.
3. Finalmente, presiona el botón 'Actualizar Contraseña' para realizar el cambio.

Recuerda que es importante utilizar una contraseña segura y fácil de recordar. ¡Mantén tus datos protegidos!"""

        mensaje.setText(texto_mensaje)
        mensaje.exec_()

    def mostrarToolTip(self, event):
        # Mostrar el texto emergente cuando el mouse se coloca sobre el botón
        QToolTip.showText(event.globalPos(), 'Ayuda', self)

    def ocultarToolTip(self, event):
        # Ocultar el texto emergente cuando el mouse se retira del botón
        QToolTip.hideText()

    def mostrar_ventana(self):
        contrasenia_actual = self.contrasenia_actual.text()
        contrasenia_nueva = self.contrasenia_nueva.text()

        #Si falta llenar alguna contraseña
        if contrasenia_actual == "" or contrasenia_nueva == "":
            tk.messagebox.showwarning("Error", "Necesitas ingresar ambas contraseñas.")
        else:
            #Validacion que la contraseña actual sea igual a la de la BD
            mi_busqueda = conexion_alumno.Registro_datos()
            dato1 = mi_busqueda.buscar_contrasenia("'" + self.nombreUsuario + "'")
            mi_contrasenia_capturada = dato1[0]
            #Componemos la de la consulta
            contrasenia_buscada = str(mi_contrasenia_capturada)
            contrasenia_buscada = contrasenia_buscada[2:-3]

            if  contrasenia_actual == str(contrasenia_buscada):
                print("las contraseñas son iguales")
                mi_sentencia = conexion_alumno.Registro_datos()
                mi_sentencia.actualizar_contrasenia(contrasenia_nueva, self.idAlumno)
                messagebox.showinfo("Aviso", "¡Felicitaciones! Tu contraseña se actualizo correctamente")
            else:
                messagebox.showwarning("¡Alerta!","Tu contraseña actual no es correcta")

    # Funcion para volver a la ventana principal. O sea esta.
    def volver(self):
        # Crea una instancia de la ventana principal y la muestra
        self.moduloAlumnitos = moduloAlumno.ModuloAlumno(self.nombreUsuario, self.idAlumno)
        self.moduloAlumnitos.show()
        self.close()