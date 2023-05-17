from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QFont, QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel
from PyQt5 import QtCore, QtWidgets
import pandas as pd
import requests
import conexion_alumno
import moduloAlumno


# Clase ventana Principal que hereda de la clase QMainWindow
class ActividadesDeLaU(QMainWindow):
    def __init__(self, nombre, idAlumno):
        super().__init__()
        # Titulo de la ventana
        self.setWindowTitle("Actividades de la universidad")
        self.setFixedSize(1800, 800)
        self.setGeometry(QtCore.QRect(0, 0, 1300, 800))
        self.setStyleSheet("border-image:url(img/fondo.png)")
        # self.setStyleSheet("border-image:url(img/fondo_admin.jpg)")
        self.nombreUsuario = "" + nombre
        self.idAlumno = str(idAlumno)
        # Centrar ventana en la pantalla
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.centralWidget()

        # Crear un QLabel para el título de la tabla
        self.titulo_label = QtWidgets.QLabel(self)
        self.titulo_label.setText("Actividades de la universidad")
        self.titulo_label.setGeometry(QtCore.QRect(390, 5, 800, 50))
        self.titulo_label.setStyleSheet("font: 63 20pt \"Victor Mono SemiBold\";")

        # Conexion a la BD e insercion en la tabla
        datos = conexion_alumno.Registro_datos()
        resultados = datos.buscar_actividades_de_la_u()

        # Crear un DataFrame a partir de los resultados
        df = pd.DataFrame(resultados,columns=['Nombre de la actividad', 'Descripción', 'Hora','Fecha', 'Ubicación','Categoria','Costo','Estado','Imagen'])  # Reemplaza 'Campo1', 'Campo2', ... con los nombres reales de las columnas

        # Crear un QTableWidget y establecer los encabezados de columna
        table = QTableWidget()
        table.setColumnCount(len(df.columns))
        table.setColumnWidth(0, 200) #Nombre
        table.setColumnWidth(1, 250) #Descripcion
        table.setColumnWidth(2, 80) #Hora
        table.setColumnWidth(3, 100) #Fecha
        table.setColumnWidth(4, 220) #Ubicacion
        table.setColumnWidth(5, 120) #Categoria
        table.setColumnWidth(6, 80) #Costo
        table.setColumnWidth(7, 120) #Estado
        table.setColumnWidth(8, 370) #Imagen
        table.setHorizontalHeaderLabels(df.columns)

        # Iterar sobre los resultados y agregar las filas a la tabla
        for i, row in enumerate(resultados):
            table.insertRow(i)
            for j, item in enumerate(row):
                if j == 8:  # Si es la columna de la imagen
                    try:
                        # Descargar la imagen desde la URL utilizando requests
                        response = requests.get(item)
                        image_data = response.content

                        # Crear una imagen desde los datos descargados
                        image = QImage.fromData(image_data)

                        # Redimensionar la imagen para ajustarse al ancho de la columna
                        column_width = table.columnWidth(j) + 130
                        scaled_image = image.scaledToWidth(column_width)

                        # Crear un widget de imagen y establecer la imagen redimensionada
                        image_widget = QTableWidgetItem()
                        image_widget.setData(Qt.DecorationRole, QPixmap.fromImage(scaled_image))

                        # Insertar el widget de imagen en la tabla
                        table.setItem(i, j, image_widget)

                    except requests.exceptions.RequestException:
                        # Error de conexión, mostrar un mensaje en la celda
                        error_widget = QTableWidgetItem("Error de conexión")
                        table.setItem(i, j, error_widget)

                else:
                    # Crear un widget de texto y establecer el valor del campo
                    text_widget = QTableWidgetItem(str(item))

                    # Insertar el widget de texto en la tabla
                    table.setItem(i, j, text_widget)

        # Establecer el color de fondo de las celdas de la tabla
        table.setStyleSheet("""
            QTableWidget::item {
                background-color: #CDFFFD;
            }
        """)
        font = QFont("Open Sans", 10, QFont.ExtraLight)
        table.setFont(font)

        # Iterar sobre todas las filas de la tabla y establecer el mismo ancho
        for i in range(table.rowCount()):
            table.setRowHeight(i, 300)  # Establecer el ancho deseado para cada fila

        table.setColumnWidth(8, 500)  # Ancho inicial


        # # Agregar los datos del DataFrame a la tabla
        # table.setRowCount(len(df.index))
        # for row in range(len(df.index)):
        #     for column in range(len(df.columns)):
        #         item = QTableWidgetItem(str(df.iloc[row, column]))
        #         table.setItem(row, column, item)

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
        self.boton_volver.setGeometry(QtCore.QRect(1730, 720, 50, 50))
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
