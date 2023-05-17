import sys
from tkinter import messagebox

from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFrame, QApplication
from PyQt5.QtCore import Qt, QRect

import alumno_actividades_universidad
import alumno_boletas
import alumno_calificaciones
import alumno_datos
import alumno_bajas
import conexion_alumno
import alumno_extraescolares
import main_login_alumnos


class ModuloAlumno(QMainWindow):

    def __init__(self, nombre, idAlumno):
        super().__init__()

        self.setWindowTitle("BIENVENIDO ALUMNITO")
        self.nombreUsuario = "" + nombre
        self.idAlumno = idAlumno
        self.nombreReal = self.buscarNombreReal()
        self.setFixedSize(1300, 800)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("border-radius:20px;")
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

        # Diseño boton "calificaciones":
        self.boton_calificaciones = QPushButton(self)
        self.boton_calificaciones.setGeometry(QRect(700, 140, 580, 50))
        self.boton_calificaciones.setStyleSheet(style_btn)
        self.boton_calificaciones.setObjectName("boton_calificaciones")

        # Diseño boton "Extraescolares":
        self.boton_extraescolares = QPushButton(self)
        self.boton_extraescolares.setGeometry(QRect(700, 220, 580, 50))
        self.boton_extraescolares.setStyleSheet(style_btn)
        self.boton_extraescolares.setObjectName("boton_extraescolares")

        # Diseño boton "Boletas":
        self.boton_boletas = QPushButton(self)
        self.boton_boletas.setGeometry(QRect(700, 300, 580, 50))
        self.boton_boletas.setStyleSheet(style_btn)
        self.boton_boletas.setObjectName("boton_boletas")

        # Diseño boton "actividades":
        self.boton_actividades = QPushButton(self)
        self.boton_actividades.setGeometry(QRect(700, 380, 580, 50))
        self.boton_actividades.setStyleSheet(style_btn)
        self.boton_actividades.setObjectName("boton_actividades")

        # Diseño boton "dar de baja":
        self.boton_bajas = QPushButton(self)
        self.boton_bajas.setGeometry(QRect(700, 460, 580, 50))
        self.boton_bajas.setStyleSheet(style_btn)
        self.boton_bajas.setObjectName("boton_bajas")


        # Diseño boton "reportar datos":
        self.boton_datos = QPushButton(self)
        self.boton_datos.setGeometry(QRect(700, 540, 580, 50))
        self.boton_datos.setStyleSheet(style_btn)
        self.boton_datos.setObjectName("boton_datos")

        # Diseño boton "cerrar sesion":
        self.boton_cerrar_sesion = QPushButton(self)
        self.boton_cerrar_sesion.setGeometry(QRect(700, 620, 580, 50))
        self.boton_cerrar_sesion.setStyleSheet(style_btn)
        self.boton_cerrar_sesion.setObjectName("boton_cerrar_sesion")

        # Diseño boton "salir":
        self.boton_salir = QPushButton(self)
        self.boton_salir.setGeometry(QRect(700, 700, 580, 50))
        self.boton_salir.setStyleSheet(style_btn)
        self.boton_salir.setObjectName("boton_salir")

        # Diseño del FRAME
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 1300, 800))
        self.frame.setStyleSheet("border-image:url(img/fondo.png)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")


        # Diseño de la imagen que es (una etiqueta)
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(170, 200, 400, 400))
        self.label.setStyleSheet("border-image:url(img/alumnitos.png)")
        self.label.setText("")
        self.label.setObjectName("label")

        # Diseño del texto principal
        self.texto_principal = QLabel(self.frame)
        self.texto_principal.setGeometry(QRect(0, 30, 1200, 71))
        self.texto_principal.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.texto_principal.setObjectName("texto_principal")
        self.frame.raise_()

        self.boton_boletas.raise_()
        self.boton_actividades.raise_()
        self.boton_bajas.raise_()
        self.boton_calificaciones.raise_()
        self.boton_extraescolares.raise_()
        self.boton_datos.raise_()
        self.boton_cerrar_sesion.raise_()
        self.boton_salir.raise_()

        # Otorgarle una accion a los botones:
        self.boton_boletas.clicked.connect(self.abrir_ventana_boletas)
        self.boton_actividades.clicked.connect(self.abrir_ventana_actividades)
        self.boton_bajas.clicked.connect(self.abrir_ventana_bajas)
        self.boton_calificaciones.clicked.connect(self.abrir_ventana_calificaciones)
        self.boton_extraescolares.clicked.connect(self.abrir_ventana_extraescolares)
        self.boton_datos.clicked.connect(self.abrir_ventana_datos)
        self.boton_cerrar_sesion.clicked.connect(self.cerrar_sesion)
        self.boton_salir.clicked.connect(self.salir)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QApplication.translate
        self.boton_calificaciones.setText(_translate("Form", "Calificaciones"))
        self.boton_extraescolares.setText(_translate("Form", "Actividades extraescolares"))
        self.boton_actividades.setText(_translate("Form", "Actividades universidad"))
        self.boton_boletas.setText(_translate("Form", "Boletas"))
        self.boton_bajas.setText(_translate("Form", "Dar de baja"))
        self.boton_cerrar_sesion.setText(_translate("Form", "Cerrar sesion"))
        self.boton_salir.setText(_translate("Form", "Salir"))
        self.boton_datos.setText(_translate("Form", "Mis datos"))
        self.texto_principal.setText(
            _translate("Form", "                    BIENVENIDO AL SISTEMA " + self.nombreReal.upper() + "!"))

    # Funcion para mostrar ventana boletas
    def abrir_ventana_boletas(self):
        print("boletas")
        self.ventana_boletas = alumno_boletas.AlumnoBoletas(self.nombreUsuario, self.idAlumno)
        self.ventana_boletas.show()
        self.close()


    # Funcion para mostrar ventana actividades de la universidad
    def abrir_ventana_actividades(self):
        print("actividades de la U")
        self.ventana_actividades_universidad = alumno_actividades_universidad.ActividadesDeLaU(self.nombreUsuario, self.idAlumno)
        self.ventana_actividades_universidad.show()
        self.close()

    # Funcion para mostrar ventana actividades de la universidad
    def abrir_ventana_datos(self):
        print("Datos del estudiante")
        self.ventana_datos = alumno_datos.AlumnoDatos(self.nombreUsuario, self.idAlumno)
        self.ventana_datos.show()
        self.close()

    # Funcion para mostrar ventana bajas
    def abrir_ventana_bajas(self):
        print("bajas")
        self.ventana_bajas = alumno_bajas.Bajas(self.nombreReal, self.nombreUsuario, self.idAlumno)
        self.ventana_bajas.show()
        self.close()

    # Funcion para mostrar ventana calificaciones
    def abrir_ventana_calificaciones(self):
        # Obtenemos el maximo semestre
        consulta = conexion_alumno.Registro_datos()
        dato1 = consulta.buscar_maximo_semestre(self.idAlumno)
        if dato1[0][0] is None:
            messagebox.showinfo("¡Aviso!", "Este alumno aún no cuenta con calificaciones registradas.")
        else:
            self.ventana_calificaciones = alumno_calificaciones.AlumnoCalificaciones(self.nombreUsuario, self.idAlumno)
            self.ventana_calificaciones.show()
            self.close()

    # Funcion para mostrar ventana tutorias
    def abrir_ventana_extraescolares(self):
        self.ventana_extraescolares = alumno_extraescolares.Extraescolares(self.nombreUsuario, self.idAlumno)
        self.ventana_extraescolares.show()
        self.close()

    def salir(self):
        # Salir del programa
        QApplication.quit()


    def cerrar_sesion(self):
        self.main_login_alumnos = main_login_alumnos.MiApp()
        self.main_login_alumnos.show()
        self.close()

    def buscarNombreReal(self):
        datos = conexion_alumno.Registro_datos()
        dato1 = datos.busca_users("'" + self.nombreUsuario + "'")
        # dato1 = datos.busca_users("'a'")
        alumnito = dato1[0]
        nombre_real = alumnito[1]
        return nombre_real


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ui = ModuloAlumno("aaa2023", "28")
#     ui.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ui = ModuloAlumno("x", "22")
#     ui.show()
#     sys.exit(app.exec_())
