
from PyQt5.QtWidgets import  QMessageBox,QWidget,QFrame, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget,QTableWidgetItem,QAbstractItemView,QWidget
from administrativos_conexion import Administrativos
from PyQt5.QtCore import Qt,QRect
import tempfile
import os
from PyQt5.QtGui import QPalette, QBrush, QColor,QIcon

import administrativos_interfaz_control_docentes
import administrativos_interfaz_agregar_documentacion_docente

class InterfaceDocumentacionDocente(QWidget):
    id_docente = "" #Variable global para tener presente en todo el programa el docente elegido
    def __init__(self,id_docente,nombre_sesion):
        self.nombre_sesion = nombre_sesion
        super().__init__()
        self.resize(1200, 800)
        self.initUI(id_docente)
        
    def initUI(self,id_docente):

        #Frame para el fondo
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 1200, 800))
        self.frame.setStyleSheet("border-image:url(img/fondo_admin.jpg)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised) 
        self.frame.setObjectName("frame")

        administrativo = Administrativos()
        datos = administrativo.buscar_docente(id_docente)
        self.id_docente = id_docente
        
        #Label documentacion del docente X
        title = QLabel(f"Documentación del docente - {datos[1]} {datos[2]} {datos[3]}")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")

        #Boton de agregar documentacion
        self.btn_agregar_documentacion = QPushButton('Agregar documentación')
        aplicar_estilo_guardar(self.btn_agregar_documentacion,"#FF5733")
        self.btn_agregar_documentacion.clicked.connect(self.show_interface_agregar_documentacion)
    
        #Tabla de documentacion
        self.tablaDocumentacion = QTableWidget()
        self.tablaDocumentacion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cargar_datos_documentos();

        #Boton de regresar
        self.btn_regresar_control_docentes = QPushButton('')
        icono_regresar = QIcon('img/flecha-izquierda.png')
        self.btn_regresar_control_docentes.setIcon(icono_regresar)
        aplicar_estilo_volver(self.btn_regresar_control_docentes,"#FF5733")
        self.btn_regresar_control_docentes.clicked.connect(self.show_interface_control_docentes)

        #Layout para el boton a la derecha de agregar documentacion
        hbox_layout_btn_agregar_documentacion = QHBoxLayout()
        hbox_layout_btn_agregar_documentacion.addStretch(1)
        hbox_layout_btn_agregar_documentacion.addWidget(self.btn_agregar_documentacion)
        

        #Layout para el boton a la derecha de regresar
        hbox_layout_boton_regresar = QHBoxLayout()
        hbox_layout_boton_regresar.addStretch(1)
        hbox_layout_boton_regresar.addWidget(self.btn_regresar_control_docentes)

        vbox = QVBoxLayout()
        vbox.addWidget(title)
        vbox.addLayout(hbox_layout_btn_agregar_documentacion)
        vbox.addWidget(self.tablaDocumentacion)
        vbox.addLayout(hbox_layout_boton_regresar)

        self.setLayout(vbox)

    def show_interface_control_docentes(self):
        self.interface_control_docentes = administrativos_interfaz_control_docentes.InterfazControlDocentes(self.nombre_sesion)
        self.interface_control_docentes.show()
        self.close()
        
    def show_interface_agregar_documentacion(self):
        self.interface_agregar_documentacion = administrativos_interfaz_agregar_documentacion_docente.InterfazAgregarDocumentacionDocente(self.id_docente,self.nombre_sesion)
        self.interface_agregar_documentacion.show()
        self.close()

    def cargar_datos_documentos(self):
        administrativos = Administrativos() #Nueva conexion

        #Estructura de la tabla
        self.tablaDocumentacion.setColumnCount(4) # Creamos las columnas necesarias para todos los datos
        self.tablaDocumentacion.setHorizontalHeaderLabels(["Id","Descripcion","Acción", "Acción"])

        #Ajustamos el tamaño de la tabla
        self.tablaDocumentacion.setColumnWidth(0, 50)
        self.tablaDocumentacion.setColumnWidth(1, 700)
        self.tablaDocumentacion.setColumnWidth(2, 200)
        self.tablaDocumentacion.setColumnWidth(3, 200)

        #Cargamos los datos de los documentos en la tabla
        datos = administrativos.consulta_documentacion_docente(self.id_docente)
        self.tablaDocumentacion.setRowCount(len(datos))

        #Rellenamos la tabla con los datos
        for i, fila in  enumerate(datos):
            id_documento = QTableWidgetItem(str(fila[0]))
            descripcion = QTableWidgetItem(str(fila[1]))
            self.tablaDocumentacion.setItem(i,0,id_documento)
            self.tablaDocumentacion.setItem(i,1,descripcion)
            
        #Añadimos botones ver, borrar
        for row in range(self.tablaDocumentacion.rowCount()):
            #Ver archivo
            btn_ver_archivo = QPushButton()
            icono_ver = QIcon('img/ver.png')
            btn_ver_archivo.setIcon(icono_ver)
            btn_ver_archivo.setObjectName('ver_' + str(row))
            btn_ver_archivo.clicked.connect(self.ver_archivo)
            self.tablaDocumentacion.setCellWidget(row, 2, btn_ver_archivo)
            
            #Borrar
            btn_borrar_archivo = QPushButton()
            icono_borrar = QIcon('img/borrar.png')
            btn_borrar_archivo.setIcon(icono_borrar)
            btn_borrar_archivo.setObjectName('baja_' + str(row))
            btn_borrar_archivo.clicked.connect(self.borrar_archivo)
            self.tablaDocumentacion.setCellWidget(row, 3, btn_borrar_archivo)
    
    def ver_archivo(self):
        administrativo = Administrativos()
        #Sabemos el id del archivo que se quiere ver
        boton = self.sender()
        fila = int(boton.objectName().split('_')[1])
        id_documentacion_docente = self.tablaDocumentacion.item(fila, 0).text()
        datos = administrativo.buscar_documentacion_docente(self.id_docente,id_documentacion_docente)
        # Crear un archivo temporal y guardar el contenido binario
        temp_archivo = tempfile.NamedTemporaryFile(prefix= str(datos[1]) ,suffix='Student.pdf' , delete=False) 
        temp_archivo.write(datos[2])
        temp_archivo.close()

        # Abrir el archivo temporal con el programa adecuado
        os.startfile(temp_archivo.name)
    
    def borrar_archivo(self):
        administrativos = Administrativos()
        boton = self.sender()
        fila = int(boton.objectName().split('_')[1])
        id_documento = self.tablaDocumentacion.item(fila, 0).text()  # Suponiendo que el ID está en la primera columna
        
        # Agregar cuadro de mensaje de confirmación
        mensaje_box = QMessageBox()
        mensaje_box.setWindowTitle("Confirmación")
        mensaje_box.setText("¿Está seguro de que desea eliminar la documentación?")
        mensaje_box.setIcon(QMessageBox.Warning)
        mensaje_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resultado = mensaje_box.exec_()

        if resultado == QMessageBox.Yes:
            self.tablaDocumentacion.removeRow(fila)
            administrativos.elimina_documento_docente(self.id_docente,id_documento)
            self.cargar_datos_documentos()

def aplicar_estilo_guardar(boton,color):
    style = f"""
    QPushButton {{
        font: 11pt;
        background-color: {color};
        border-radius: 25px;
        padding: 10px 20px;
        min-width: 250;
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