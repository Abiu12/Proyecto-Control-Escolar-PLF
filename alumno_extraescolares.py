from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, \
    QWidget, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox
import conexion_alumno
import moduloAlumno
from tkinter import Label
import pandas as pd


# Clase ventana Principal que hereda de la clase QMainWindow
class Extraescolares(QMainWindow):
    def __init__(self, nombre, idAlumno):
        super().__init__()
        # Titulo de la ventana
        self.setWindowTitle("Actividades Extraescolares")
        self.setFixedSize(1300, 700)
        self.setGeometry(QtCore.QRect(0, 0, 1300, 800))
        self.setStyleSheet("border-image:url(img/fondo.png)")
        self.nombreUsuario = "" + nombre
        self.idAlumno = str(idAlumno)
        # Centrar ventana en la pantalla
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.centralWidget()

        # Conexion a la BD e insercion en la tabla
        datos = conexion_alumno.Registro_datos()
        resultados = datos.buscar_complementarias("'" + self.idAlumno + "'")

        # Crear un DataFrame a partir de los resultados
        df = pd.DataFrame(resultados,columns=['Nombre de la actividad', 'Horario', 'Estado','Nombre del docente', 'Primer Apellido','Segundo Apellido'])  # Reemplaza 'Campo1', 'Campo2', ... con los nombres reales de las columnas

        # Crear un QLabel para el título de la tabla
        self.titulo_label = QtWidgets.QLabel(self)
        self.titulo_label.setText("Actividades Extraescolares")
        self.titulo_label.setGeometry(QtCore.QRect(390, 5, 800, 50))
        self.titulo_label.setStyleSheet("font: 63 20pt \"Victor Mono SemiBold\";")


        # Crear un QTableWidget y establecer los encabezados de columna
        table = QTableWidget()
        table.setColumnCount(len(df.columns))
        table.setColumnWidth(0, 200)
        table.setColumnWidth(1, 80)
        table.setColumnWidth(2, 150)
        table.setColumnWidth(3, 270)
        table.setColumnWidth(4, 270)
        table.setColumnWidth(5, 270)
        table.setHorizontalHeaderLabels(df.columns)

        # Establecer el color de fondo de las celdas de la tabla
        table.setStyleSheet("""
            QTableWidget::item {
                background-color: #CDFFFD;
            }
        """)
        font = QFont("Open Sans", 12, QFont.ExtraLight)
        table.setFont(font)

        # Agregar los datos del DataFrame a la tabla
        table.setRowCount(len(df.index))
        for row in range(len(df.index)):
            for column in range(len(df.columns)):
                item = QTableWidgetItem(str(df.iloc[row, column]))
                table.setItem(row, column, item)

        # Crear un layout vertical y agregar la tabla
        layout = QVBoxLayout()
        layout.addWidget(self.titulo_label)
        layout.addWidget(table)

        # Crear un widget central y establecer el layout
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Boton de volver
        self.boton_volver = QtWidgets.QPushButton(self)
        self.boton_volver.setGeometry(QtCore.QRect(1200, 620, 50, 50))
        self.boton_volver.setStyleSheet("border-image:url(img/regreso.png)")
        self.boton_volver.setText("")
        self.boton_volver.setObjectName("volver")
        self.boton_volver.clicked.connect(self.volver)



    # Funcion para volver a la ventana principal. O sea esta.
    def volver(self):
        # Crea una instancia de la ventana principal y la muestra
        self.moduloAlumnitos= moduloAlumno.ModuloAlumno(self.nombreUsuario, self.idAlumno)
        self.moduloAlumnitos.show()
        self.close()
