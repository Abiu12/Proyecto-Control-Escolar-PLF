from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QFont, QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel
from PyQt5 import QtCore, QtWidgets
import pandas as pd
import requests
import administrativos_conexion
import administrativos_interfaz_principal
from PyQt5.QtGui import QPalette, QBrush, QColor, QIcon,QRegExpValidator

# Clase ventana Principal que hereda de la clase QMainWindow
class ActividadesDeLaU(QMainWindow):
    def __init__(self,nombre_sesion):
        self.nombre_sesion =  nombre_sesion
        super().__init__()
        # Titulo de la ventana
        self.setWindowTitle("Actividades de la universidad")
        self.setFixedSize(1800, 800)
        self.setGeometry(QtCore.QRect(0, 0, 1300, 800))
        self.setStyleSheet("border-image:url(img/fondo_admin.jpg)")
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
        datos = administrativos_conexion.Administrativos()
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
        self.boton_volver.setGeometry(QtCore.QRect(1680, 720, 50, 50))
        icono_regresar = QIcon('img/flecha-izquierda.png')
        self.boton_volver.setIcon(icono_regresar)
        aplicar_estilo_volver(self.boton_volver,"#FF5733")
        self.boton_volver.setText("")
        self.boton_volver.setObjectName("volver")
        self.boton_volver.clicked.connect(self.show_interface_menu_administrativo)

    

    def show_interface_menu_administrativo(self):
        self.interface_administrativos = administrativos_interfaz_principal.InterfazAdministrativo(self.nombre_sesion)
        self.interface_administrativos.show()
        self.hide()

def aplicar_estilo_volver(boton,color):
    style = f"""
    QPushButton {{
        font: 11pt;
        background-color: {color};
        border-radius: 25px;
        padding: 10px 20px;
        min-width: 60px;
        min-height: 40px;
    }}
    QPushButton:hover {{
        background-color: #FF8C00;
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