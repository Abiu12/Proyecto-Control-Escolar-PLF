from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
import conexion_alumno
import moduloAlumno
import tkinter as tk
from conexion_alumno import Registro_datos
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFrame, QApplication, QToolTip
from PyQt5.QtCore import Qt, QRect

# Clase ventana Principal que hereda de la clase QMainWindow
class Bajas(QMainWindow):
    def __init__(self, nombre, nombreUser, idAlumno):
        super().__init__()
        # Titulo de la ventana
        self.setWindowTitle("Ventana de Reportes de Baja")
        self.setFixedSize(1300, 700)
        self.setGeometry(QtCore.QRect(0, 0, 500, 500))
        # self.setStyleSheet("border-image:url(img/fondo.png)")
        self.setStyleSheet("")
        self.nombreReal = "" + nombre
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
        self.frame.setGeometry(QRect(0, 0, 1300, 700))
        self.frame.setStyleSheet("border-image:url(img/fondo.png)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")

        # Crear la etiqueta de reporte
        self.report_label = QtWidgets.QLabel(self)
        self.report_label.setText("Redacta el motivo de tu baja")
        self.report_label.setGeometry(QtCore.QRect(390, 5, 800, 50))
        self.report_label.setStyleSheet("font: 63 20pt \"Victor Mono SemiBold\";")
        # Crear el cuadro de texto
        self.cuadro_texto = QtWidgets.QTextEdit(self)
        self.cuadro_texto.setGeometry(QtCore.QRect(340, 80, 641, 511))
        self.cuadro_texto.setStyleSheet(
            "QTextEdit { background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e6e6e6, stop:1 #ffffff);"
            "font-family: Century Gothic; font-size: 21px;"
            "border: 1px solid #cccccc; border-radius: 5px; padding: 5px; }")

        # Boton enviar
        self.boton_enviar = QtWidgets.QPushButton(self)
        self.boton_enviar.setGeometry(QtCore.QRect(560, 600, 221, 41))
        self.boton_enviar.setStyleSheet(
            "QPushButton {"
            "   font: 15pt \"SimSun\";"
            "   background-color: rgb(240, 240, 240);"
            "   border: 2px solid rgb(86, 157, 218);"
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
        self.boton_enviar.setText("Enviar reporte")
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
        mensaje = QtWidgets.QMessageBox()
        mensaje.setIcon(QtWidgets.QMessageBox.Information)
        mensaje.setWindowTitle("Información de los datos")
        texto_mensaje = """Estimado alumno,

Si deseas solicitar tu baja del sistema de control de estudiantes, te pedimos que redactes un reporte detallando las razones de tu solicitud. Es importante que incluyas en tu informe todas las circunstancias relevantes que te llevan a tomar esta decisión.

Una vez que hayas completado tu reporte, el administrador del sistema revisará cuidadosamente tu solicitud. Ten en cuenta que se requiere una evaluación exhaustiva antes de tomar cualquier decisión. Asegúrate de proporcionar una explicación clara y precisa de tus motivos para la baja.

Recuerda que la solicitud de baja implica la interrupción de tu participación en el sistema de control de estudiantes. Antes de presentar tu solicitud, considera todas las alternativas y las posibles consecuencias. Nuestro objetivo es brindarte el mejor apoyo posible, por lo que te recomendamos explorar otras opciones antes de tomar esta decisión.

Una vez que hayas completado tu reporte, puedes entregarlo al administrador o seguir las instrucciones proporcionadas para su presentación. Agradecemos tu cooperación y esperamos poder brindarte la asistencia necesaria durante este proceso.

Atentamente,
El equipo del sistema de control de estudiantes"""

        mensaje.setText(texto_mensaje)
        mensaje.exec_()

    def mostrarToolTip(self, event):
        # Mostrar el texto emergente cuando el mouse se coloca sobre el botón
        QToolTip.showText(event.globalPos(), 'Ayuda', self)

    def ocultarToolTip(self, event):
        # Ocultar el texto emergente cuando el mouse se retira del botón
        QToolTip.hideText()

    def mostrar_ventana(self):
        contenido = self.cuadro_texto.toPlainText()
        if contenido == "":
            tk.messagebox.showwarning("Error", "El cuadro de texto está vacío.")
        else:
            # Clase para hacer la insercion del reporte
            nuevoReporte = Registro_datos()
            # Conexion a la BD independiente para obtener los datos del alumno
            datos = conexion_alumno.Registro_datos()
            # Lista de Registros
            dato1 = datos.busca_por_nombre("'"+self.nombreReal+"'")
            # Tomamos el primer registro
            alumnito = dato1[0]

            referenciaAlumno = alumnito[0]
            nuevoReporte.inserta_datos_reporte_baja(contenido, referenciaAlumno)
            # Separamos por campos ------------------------------------
            nombre_completo = alumnito[1]
            messagebox.showinfo("Estado del reporte", "¡Hola "+nombre_completo+" tu reporte de baja se ha creado con exito y en breve se te dara de baja.")



    # Funcion para volver a la ventana principal. O sea esta.
    def volver(self):
        # Crea una instancia de la ventana principal y la muestra
        self.moduloAlumnitos= moduloAlumno.ModuloAlumno(self.nombreUsuario, self.idAlumno)
        self.moduloAlumnitos.show()
        self.close()
