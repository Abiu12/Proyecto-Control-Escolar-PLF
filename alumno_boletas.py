from tkinter import messagebox
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, \
    QWidget, QLabel, QFrame
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import conexion_alumno
import moduloAlumno
import alumno_boletas
from PyQt5.QtWidgets import QComboBox


# Clase ventana Principal que hereda de la clase QMainWindow
class AlumnoBoletas(QMainWindow):
    def __init__(self, nombre, idAlumno):
        super().__init__()
        # Titulo de la ventana
        self.setWindowTitle("Boletas")
        self.setFixedSize(650, 515)
        self.setGeometry(QtCore.QRect(0, 0, 1300, 800))
        self.nombreUsuario = "" + nombre
        self.idAlumno = str(idAlumno)
        # Centrar ventana en la pantalla
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.centralWidget()
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

        # Crear un widget central y establecer el layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Diseño del FRAME
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 1300, 800))
        self.frame.setStyleSheet("border-image:url(img/fondo.png)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")

        # Crear un QLabel para el título de la tabla
        self.titulo_label = QtWidgets.QLabel(self)
        self.titulo_label.setText("Boletas")
        self.titulo_label.setGeometry(QtCore.QRect(280, 10, 150, 50))
        self.titulo_label.setStyleSheet("font: 63 20pt \"Victor Mono SemiBold\";")

        self.indicacion_label = QtWidgets.QLabel(self)
        self.indicacion_label.setText("Selecciona un semestre")
        self.indicacion_label.setGeometry(QtCore.QRect(220, 80, 350, 50))
        self.indicacion_label.setStyleSheet("font: 63 15pt \"Tahoma\";")

        self.combobox_semestre = QComboBox(self)
        self.combobox_semestre.setGeometry(QtCore.QRect(225, 180, 200, 30))  # Ajusta la geometría según tus necesidades
        self.combobox_semestre.addItem("1")
        self.combobox_semestre.addItem("2")
        self.combobox_semestre.addItem("3")
        self.combobox_semestre.addItem("4")
        self.combobox_semestre.addItem("5")
        self.combobox_semestre.addItem("6")
        self.combobox_semestre.addItem("7")
        self.combobox_semestre.addItem("8")
        self.combobox_semestre.addItem("9")
        self.combobox_semestre.addItem("10")
        self.combobox_semestre.setStyleSheet("""
            QComboBox {
                background-color: #F0F0F0;
                color: #333333;
                border: 1px solid #CCCCCC;
                border-radius: 4px;
                padding: 2px 8px;
                font-size: 12px;
            }

            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: center right;
                width: 20px;
                border-left: 1px solid #CCCCCC;
                border-radius: 4px;
            }

            QComboBox::down-arrow {
                image: url(down_arrow.png);
            }
        """)
        self.combobox_semestre.currentIndexChanged.connect(self.guardar_seleccion)

        self.boton_boletas = QtWidgets.QPushButton(self)
        self.boton_boletas.setGeometry(QtCore.QRect(50, 395, 200, 50))
        self.boton_boletas.setText("Buscar boleta")
        self.boton_boletas.setObjectName("boleta")
        self.boton_boletas.clicked.connect(self.buscar_boleta)
        self.boton_boletas.setStyleSheet(style_btn)

        # Boton de volver
        self.boton_volver = QtWidgets.QPushButton(self)
        self.boton_volver.setGeometry(QtCore.QRect(570, 395, 50, 50))
        self.boton_volver.setStyleSheet("border-image:url(img/regreso.png)")
        self.boton_volver.setText("")
        self.boton_volver.setObjectName("volver")
        self.boton_volver.clicked.connect(self.volver)

        self.seleccion_semestre = "1"

    def guardar_seleccion(self):
        self.seleccion_semestre = self.combobox_semestre.currentText()  # Obtener el texto del elemento seleccionado

    # Funcion para volver a la ventana principal. O sea esta.
    def volver(self):
        # Crea una instancia de la ventana principal y la muestra
        self.moduloAlumnitos = moduloAlumno.ModuloAlumno(self.nombreUsuario, self.idAlumno)
        self.moduloAlumnitos.show()
        self.close()

    def volver1(self):
        self.ventana_boletas = alumno_boletas.AlumnoBoletas(self.nombreUsuario, self.idAlumno)
        self.ventana_boletas.show()
        self.close()

    def buscar_boleta(self):
        # Conexion a la BD e insercion en la tabla
        datos = conexion_alumno.Registro_datos()
        resultados = datos.buscar_boleta_semestre(self.idAlumno, str(self.seleccion_semestre))

        if resultados == []:
            messagebox.showinfo("¡Sin boletas!",
                                "El alumno no cuenta con boletas registradas para el semestre seleccionado.")
        else:
            # Crear un DataFrame a partir de los resultados
            df = pd.DataFrame(resultados,
                              columns=['Nombre de la materia', 'Unidad I', 'Unidad II', 'Unidad III', 'Unidad IV'])
            table = QTableWidget()
            table.setColumnCount(len(df.columns))
            table.setColumnWidth(0, 295)
            table.setColumnWidth(1, 80)
            table.setColumnWidth(2, 80)
            table.setColumnWidth(3, 80)
            table.setColumnWidth(4, 80)
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

            self.boton_volver1 = QtWidgets.QPushButton(self)
            self.boton_volver1.setFixedSize(50, 50)  # Ajusta el tamaño del botón según tus necesidades
            self.boton_volver1.setStyleSheet("border-image:url(img/regreso.png)")
            self.boton_volver1.setText("")
            self.boton_volver1.setObjectName("volver")
            self.boton_volver1.clicked.connect(self.volver1)

            layout.addWidget(self.boton_volver1)

            # Crear un widget central y establecer el layout
            central_widget = QWidget(self)
            central_widget.setLayout(layout)
            self.setCentralWidget(central_widget)
