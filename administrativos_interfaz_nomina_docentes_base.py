from PyQt5.QtWidgets import  QFrame,QWidget,QTableWidgetItem,QTableWidget,QAbstractItemView, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,QDialog,QFormLayout,QMessageBox,QWidget, QFileDialog, QComboBox
from administrativos_conexion import Administrativos
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPalette, QBrush, QColor, QIcon


import administrativos_interfaz_nomina
import administrativos_conexion
class InterfazNominaDocentesBase(QWidget):
    def __init__(self,nombre_sesion):
        self.nombre_sesion = nombre_sesion
        super().__init__()
        self.resize(1200, 800)
        self.initUI()
           
    def initUI(self, ):

        administrativos = administrativos_conexion.Administrativos()
        #Diseño del FRAME
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 1300, 800))
        self.frame.setStyleSheet("border-image:url(img/fondo_admin.jpg)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised) 
        self.frame.setObjectName("frame")

        #Label de alumnos
        title = QLabel("Nómina de docentes de base")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")

        # Crear la tabla Alumnos 
        self.tabla_docentes_base = QTableWidget()
        self.tabla_docentes_base.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #Cargamos los datos
        self.cargar_datos()
        self.tabla_docentes_base.resizeColumnsToContents()

        #Boton para regresar a nomina
        self.btn_regresar_documentacion_docente = QPushButton()
        icono_regresar = QIcon('img/flecha-izquierda.png')
        self.btn_regresar_documentacion_docente.setIcon(icono_regresar)
        aplicar_estilo_volver(self.btn_regresar_documentacion_docente,"#FF5733")
        self.btn_regresar_documentacion_docente.clicked.connect(self.show_interface_nomina)


        vbox = QVBoxLayout()
        vbox.addWidget(title)
        #Layout de botones
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.btn_regresar_documentacion_docente)
        vbox.addWidget(self.tabla_docentes_base)
        vbox.addLayout(button_layout)

        self.setLayout(vbox)

    def cargar_datos(self):
        #Cargamos los datos de los docentes de la bd a la tabla
        administrativos =administrativos_conexion.Administrativos() #Nueva conexion
        datos_docentes_base = administrativos.consulta_docentes_tipo("BASE")
        self.tabla_docentes_base.setColumnCount(9) # Creamos las columnas necesarias para todos los datos
        self.tabla_docentes_base.setHorizontalHeaderLabels(["Id","Trabajador","Nombre", "Primer apellido","Segundo apellido","Sueldo","Bonificación","Descuento","Total $"])
        header = self.tabla_docentes_base.horizontalHeader()
        header.setStretchLastSection(True)
        
        numero_filas = len(datos_docentes_base)

        self.tabla_docentes_base.setRowCount(numero_filas)

        #Rellenamos la tabla con los datos de los docentes
        for i, fila in  enumerate(datos_docentes_base):
            id = QTableWidgetItem(str(fila[0]))
            id.setTextAlignment(Qt.AlignCenter)
            nombre = QTableWidgetItem(fila[1])
            nombre.setTextAlignment(Qt.AlignCenter)
            primer_apellido = QTableWidgetItem(fila[2])
            primer_apellido.setTextAlignment(Qt.AlignCenter)
            segundo_apellido = QTableWidgetItem(fila[3])
            segundo_apellido.setTextAlignment(Qt.AlignCenter)
            
            datos_nomina_docente_base = administrativos.consulta_nomina_docente_base(int(fila[0]))
            if (datos_nomina_docente_base !=[]):
                self.tabla_docentes_base.setItem(i,0,id)
                self.tabla_docentes_base.setItem(i,1, QTableWidgetItem("DOCENTE"))
                self.tabla_docentes_base.setItem(i,2,nombre)
                self.tabla_docentes_base.setItem(i,3,primer_apellido)
                self.tabla_docentes_base.setItem(i,4,segundo_apellido)
                sueldo = QTableWidgetItem(f"${datos_nomina_docente_base[0][1]}.00")
                sueldo.setTextAlignment(Qt.AlignCenter)
                bonificacion = QTableWidgetItem(f"${datos_nomina_docente_base[0][2]}.00")
                bonificacion.setTextAlignment(Qt.AlignCenter)
                descuento = QTableWidgetItem(f"${datos_nomina_docente_base[0][3]}.00")
                descuento.setTextAlignment(Qt.AlignCenter)
                total = int(datos_nomina_docente_base[0][1]) + int(datos_nomina_docente_base[0][2]) - int(datos_nomina_docente_base[0][3])
                total_widget = QTableWidgetItem(f"${str(total)}.00")
                total_widget.setTextAlignment(Qt.AlignCenter)
                self.tabla_docentes_base.setItem(i,5,sueldo)
                self.tabla_docentes_base.setItem(i,6,bonificacion)
                self.tabla_docentes_base.setItem(i,7, descuento)            
                self.tabla_docentes_base.setItem(i,8,total_widget)
            else:
                QMessageBox.information(self, "Aviso", "Sin nomina registrada, verifique datos")
                


    def show_interface_nomina(self):
        self.interface_nomina = administrativos_interfaz_nomina.InterfazNomina(self.nombre_sesion)
        self.interface_nomina.show()
        self.close()
    
def aplicar_estilo_guardar(boton,color):
    style = f"""
    QPushButton {{
        font: 11pt;
        background-color: {color};
        border-radius: 25px;
        padding: 10px 20px;
        min-width: 250px;
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

def aplicar_estilo_seleccionar(boton,color):
    style = f"""
    QPushButton {{
        font: 11pt;
        background-color: {color};
        border-radius: 25px;
        padding: 10px 20px;
        min-width: 320px;
        min-height: 38px;
    }}
    QPushButton:hover {{
        background-color: #FF8C00;
    }} 
    """
    boton.setStyleSheet(style)
    