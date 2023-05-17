from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, \
    QWidget, QLabel, QFrame, QToolTip
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox

import alumno_cambio_contrasenia
import alumno_datos_incorrectos
import conexion_alumno
import moduloAlumno


# Clase ventana Principal que hereda de la clase QMainWindow
class AlumnoDatos(QMainWindow):
    def __init__(self, nombre, idAlumno):
        super().__init__()
        # Titulo de la ventana
        self.setWindowTitle("Datos del alumno")
        self.setFixedSize(1300, 700)
        self.resize(700,700)
        self.setGeometry(QtCore.QRect(0, 0, 1300, 800))
        self.nombreUsuario = "" + nombre
        self.idAlumno = idAlumno
        self.nombreReal = self.buscarNombreReal()
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

        font = QtGui.QFont()
        font.setPointSize(12)  # Tamaño de la fuente (en puntos)
        font.setFamily("Tahoma")  # Nombre de la fuente

        style = "QLineEdit {background-color: #ffffff; color: #000000; border: 2px solid #159CC7; border-radius: 8px; padding: 6px;}"
        style_btn = """
    QPushButton {
        font: 15pt "SimSun";
        background-color: rgb(240, 240, 240);
        border: 2px solid rgb(86, 157, 218);
        border-radius: 10px;
        padding: 5px;
    }
    QPushButton:hover {
        background-color: rgb(220, 220, 220);
    }
    QPushButton:pressed {
        background-color: rgb(200, 200, 200);
    }
    QPushButton:checked {
        background-color: rgb(86, 157, 218);
        color: white;
    }
"""

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Conexion a la BD
        datos = conexion_alumno.Registro_datos()
        # Lista de Registros
        dato1 = datos.busca_users("'" + nombre + "'")
        # Tomamos el primer registro
        alumnito = dato1[0]

        nombre_completo = alumnito[1]
        primer_apellido = alumnito[2]
        segundo_apellido = alumnito[3]
        calle = alumnito[4]
        numero = alumnito[5]
        colonia = alumnito[6]
        municipio = alumnito[7]
        telefono = alumnito[8]
        numero_imss = alumnito[9]
        numero_ine = alumnito[10]
        curp = alumnito[11]
        rfc = alumnito[12]
        nombre_madre = alumnito[13]
        telefono_madre = alumnito[14]
        nombre_padre = alumnito[15]
        telefono_padre = alumnito[16]

        # Crear la etiqueta de reporte
        self.report_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.report_label.setGeometry(QtCore.QRect(400, 20, 531, 51))
        self.report_label.setStyleSheet("font: 63 20pt \"Victor Mono SemiBold\";")

        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 150, 231, 50))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(nombre_completo)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(style)
        self.lineEdit.setReadOnly(True)

        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 150, 231, 50))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText(primer_apellido)
        self.lineEdit_2.setStyleSheet(style)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setReadOnly(True)

        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(660, 150, 231, 50))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText(segundo_apellido)
        self.lineEdit_3.setStyleSheet(style)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setReadOnly(True)

        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(970, 150, 231, 50))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText(calle)
        self.lineEdit_4.setStyleSheet(style)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setReadOnly(True)

        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 270, 231, 50))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText(numero)
        self.lineEdit_5.setStyleSheet(style)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setReadOnly(True)

        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(660, 270, 231, 50))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setText(colonia)
        self.lineEdit_6.setStyleSheet(style)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setReadOnly(True)

        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(380, 380, 231, 50))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setText(municipio)
        self.lineEdit_7.setStyleSheet(style)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setReadOnly(True)

        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(970, 270, 231, 50))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setText(telefono)
        self.lineEdit_8.setStyleSheet(style)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setReadOnly(True)

        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(380, 270, 231, 50))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setText(numero_imss)
        self.lineEdit_9.setStyleSheet(style)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setReadOnly(True)

        self.lineEdit_10 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(100, 380, 231, 50))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setText(numero_ine)
        self.lineEdit_10.setStyleSheet(style)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setReadOnly(True)

        self.lineEdit_11 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(970, 380, 231, 50))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_11.setText(curp)
        self.lineEdit_11.setStyleSheet(style)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setReadOnly(True)

        self.lineEdit_12 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(380, 520, 231, 50))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_12.setText(rfc)
        self.lineEdit_12.setStyleSheet(style)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setReadOnly(True)

        self.lineEdit_13 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(970, 510, 231, 50))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_13.setText(nombre_madre)
        self.lineEdit_13.setStyleSheet(style)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setReadOnly(True)

        self.lineEdit_14 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(660, 380, 231, 50))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.setText(telefono_madre)
        self.lineEdit_14.setStyleSheet(style)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setReadOnly(True)

        self.lineEdit_15 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(660, 520, 231, 50))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_15.setText(nombre_padre)
        self.lineEdit_15.setStyleSheet(style)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setReadOnly(True)

        self.lineEdit_16 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(100, 520, 231, 50))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_16.setText(telefono_padre)
        self.lineEdit_16.setStyleSheet(style)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setReadOnly(True)


        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 110, 121, 21))
        self.label.setStyleSheet("font: 16pt \"Trebuchet MS\";")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 110, 201, 31))
        self.label_2.setStyleSheet("font: 16pt \"Trebuchet MS\";")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(660, 110, 211, 31))
        self.label_3.setStyleSheet("font: 16pt \"Trebuchet MS\";")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1060, 110, 81, 31))
        self.label_4.setStyleSheet("font: 16pt \"Trebuchet MS\";")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 230, 121, 31))
        self.label_5.setStyleSheet("font: 16pt \"Trebuchet MS\";")
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 230, 121, 31))
        self.label_6.setStyleSheet("font: 16pt \"Trebuchet MS\";")
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(720, 230, 121, 31))
        self.label_7.setStyleSheet("font: 16pt \"Trebuchet MS\";")
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1020, 230, 121, 31))
        self.label_8.setStyleSheet("font: 16pt \"Trebuchet MS\";")
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(180, 340, 121, 31))
        self.label_9.setStyleSheet("font: 16pt \"Trebuchet MS\";")
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(470, 340, 121, 31))
        self.label_10.setStyleSheet("font: 16pt \"Trebuchet MS\";")
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(740, 340, 121, 31))
        self.label_11.setStyleSheet("font: 16pt \"Trebuchet MS\";")
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1060, 340, 121, 31))
        self.label_12.setStyleSheet("font: 16pt \"Trebuchet MS\";")
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(980, 470, 221, 31))
        self.label_13.setStyleSheet("font: 14pt \"Trebuchet MS\";")
        self.label_13.setObjectName("label_13")

        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(660, 480, 231, 31))
        self.label_14.setStyleSheet("font: 14pt \"Trebuchet MS\";")
        self.label_14.setObjectName("label_14")

        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(390, 480, 221, 31))
        self.label_15.setStyleSheet("font: 14pt \"Trebuchet MS\";")
        self.label_15.setObjectName("label_15")

        self.label_16 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(110, 480, 231, 31))
        self.label_16.setStyleSheet("font: 14pt \"Trebuchet MS\";")
        self.label_16.setObjectName("label_16")

        self.btn_actualizar_contra = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_actualizar_contra.setGeometry(QtCore.QRect(650, 590, 300, 41))
        self.btn_actualizar_contra.setObjectName("btn_actualizar_contra")
        self.btn_actualizar_contra.setStyleSheet(style_btn)
        self.btn_actualizar_contra.clicked.connect(self.abrir_ventana_cambio_contrasenia)

        self.btn_reportar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_reportar.setGeometry(QtCore.QRect(370, 590, 250, 41))
        self.btn_reportar.setObjectName("pushButton")
        self.btn_reportar.setStyleSheet(style_btn)
        self.btn_reportar.clicked.connect(self.abrir_ventana_datos_incorrectos)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_reportar.setText(_translate("MainWindow", "Reportar datos"))
        self.label.setText(_translate("MainWindow", "Nombre"))
        self.label_2.setText(_translate("MainWindow", "Primer Apellido"))
        self.label_3.setText(_translate("MainWindow", "Segundo Apellido"))
        self.label_4.setText(_translate("MainWindow", "Calle"))
        self.label_5.setText(_translate("MainWindow", "Número"))
        self.label_6.setText(_translate("MainWindow", "Colonia"))
        self.label_7.setText(_translate("MainWindow", "Municipio"))
        self.label_8.setText(_translate("MainWindow", "Telefono"))
        self.label_9.setText(_translate("MainWindow", "NSS"))
        self.label_10.setText(_translate("MainWindow", "INE"))
        self.label_11.setText(_translate("MainWindow", "CURP"))
        self.label_12.setText(_translate("MainWindow", "RFC"))
        self.label_13.setText(_translate("MainWindow", "Nombre de la madre"))
        self.label_14.setText(_translate("MainWindow", "Teléfono de la madre"))
        self.label_15.setText(_translate("MainWindow", "Nombre del padre"))
        self.label_16.setText(_translate("MainWindow", "Teléfono del padre"))
        self.btn_actualizar_contra.setText(_translate("MainWindow", "Actualizar contraseña"))
        self.report_label.setText(_translate("MainWindow", "Datos del alumno " + self.nombreReal))

        # Boton de volver
        self.boton_volver = QtWidgets.QPushButton(self)
        self.boton_volver.setGeometry(QtCore.QRect(1200, 600, 50, 50))
        self.boton_volver.setStyleSheet("border-image:url(img/regreso.png)")
        self.boton_volver.setText("")
        self.boton_volver.setObjectName("volver")
        self.boton_volver.clicked.connect(self.volver)

        # Configurar el botón de ayuda
        self.boton_ayuda = QtWidgets.QPushButton(self)
        self.boton_ayuda.setStyleSheet("border-image:url(img/ayuda3.png)")
        self.boton_ayuda.setToolTip('Ayuda')  # Texto emergente al colocar el mouse sobre el botón
        self.boton_ayuda.setGeometry(1100, 600, 50, 50)
        # Conectar las señales del botón
        self.boton_ayuda.clicked.connect(self.mostrarAyuda)
        self.boton_ayuda.enterEvent = self.mostrarToolTip
        self.boton_ayuda.leaveEvent = self.ocultarToolTip

    def mostrarAyuda(self):
        # Aquí puedes definir lo que sucede cuando se hace clic en el botón de ayuda
        print('Haz clic en el botón de ayuda')
        mensaje = QtWidgets.QMessageBox()
        mensaje.setIcon(QtWidgets.QMessageBox.Information)
        mensaje.setWindowTitle("Información de los datos")
        texto_mensaje = """Estimado alumno,

Los campos que visualizas actualmente contienen información personal importante y no se pueden editar directamente. Esto se hace para garantizar la precisión y seguridad de tus datos.

Si necesitas modificar alguno de los datos mostrados, te pedimos que sigas el siguiente proceso:

1. Haz clic en el botón "Reportar Datos" que se encuentra más abajo.
2. En el reporte, describe detalladamente qué información deseas modificar y proporciona los datos actualizados.
3. Envía el reporte completado y espera a que nuestro equipo de soporte lo revise.

Nuestro equipo se encargará de procesar tu solicitud y realizar las modificaciones necesarias en la información de tu perfil. Te informaremos una vez que los cambios hayan sido realizados.

Recuerda que estamos comprometidos con tu seguridad y la integridad de tus datos. Si tienes alguna pregunta adicional, no dudes en contactar a nuestro equipo de soporte.

¡Gracias por tu comprensión y colaboración!

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

    def abrir_ventana_datos_incorrectos(self):
        print("ventana_datos_incorrectos")
        self.ventana_datos_incorrectos = alumno_datos_incorrectos.AlumnoDatosIncorrectos(self.nombreReal,self.nombreUsuario, self.idAlumno)
        self.ventana_datos_incorrectos.show()
        self.close()

    def abrir_ventana_cambio_contrasenia(self):
        self.ventana_cambio_contrasenia = alumno_cambio_contrasenia.AlumnoCambioContrasenia(self.nombreUsuario,self.idAlumno)
        self.ventana_cambio_contrasenia.show()
        self.close()

    # Funcion para volver a la ventana principal. O sea esta.
    def volver(self):
        # Crea una instancia de la ventana principal y la muestra
        self.moduloAlumnitos = moduloAlumno.ModuloAlumno(self.nombreUsuario, self.idAlumno)
        self.moduloAlumnitos.show()
        self.close()

    def buscarNombreReal(self):
        datos = conexion_alumno.Registro_datos()
        dato1 = datos.busca_users("'" + self.nombreUsuario + "'")
        # dato1 = datos.busca_users("'a'")
        alumnito = dato1[0]
        nombre_real = alumnito[1]
        print("mi nombre real es" + nombre_real)
        return nombre_real