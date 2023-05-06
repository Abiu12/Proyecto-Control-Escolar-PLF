
from PyQt5.QtWidgets import  QWidget, QMessageBox,QFrame, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget,QTableWidgetItem,QAbstractItemView,QWidget
from administrativos_conexion import Administrativos
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPalette, QBrush, QColor,QIcon

import administrativos_interfaz_documentacion_docente
import administrativos_interfaz_agregar_docente
import administrativos_interfaz_principal
import administrativos_interfaz_editar_docente

class InterfazControlDocentes(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.initUI()
    
    def initUI(self):

        #Frame para el fondo
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 1200, 800))
        self.frame.setStyleSheet("border-image:url(img/fondo_admin.jpg)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised) 
        self.frame.setObjectName("frame")

        #Label de docentes
        title = QLabel("Lista de docentes")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        
        #Boton de agregar docente
        self.btn_agregar_docente= QPushButton('Agregar docente')
        aplicar_estilo_agregar(self.btn_agregar_docente,"#FF5733")
        self.btn_agregar_docente.clicked.connect(self.show_interfaz_agregar_docente)

        # Crear la tabla docentes 
        self.tabla_docentes = QTableWidget()
        self.tabla_docentes.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #Cargamos los datos
        self.cargar_datos()
        
        #Boton de regreso
        self.btnRegresarMenuAdmin = QPushButton()
        icono_regresar = QIcon('img/flecha-izquierda.png')
        self.btnRegresarMenuAdmin.setIcon(icono_regresar)
        aplicar_estilo_volver(self.btnRegresarMenuAdmin,"#FF5733")
        self.btnRegresarMenuAdmin.clicked.connect(self.show_interfaz_menu_administrativo)

        #Distribucion
        vbox = QVBoxLayout()

        vbox.addWidget(title)

        #Layout para el boton a la derecha de agregar docente
        hbox_layout_btn_docente = QHBoxLayout()
        hbox_layout_btn_docente.addStretch(1)
        hbox_layout_btn_docente.addWidget(self.btn_agregar_docente)
        vbox.addLayout(hbox_layout_btn_docente)

        vbox.addWidget(self.tabla_docentes)

        #Layout para el boton a la derecha de regresar
        hbox_layout = QHBoxLayout()
        hbox_layout.addStretch(1)
        hbox_layout.addWidget(self.btnRegresarMenuAdmin)
        
        vbox.addLayout(hbox_layout)
        self.setLayout(vbox)

    def cargar_datos(self):
        #Cargamos los datos de los docentes de la bd a la tabla
        administrativos = Administrativos() #Nueva conexion
        datos = administrativos.consulta_docentes()
        self.tabla_docentes.setColumnCount(18) # Creamos las columnas necesarias para todos los datos
        self.tabla_docentes.setHorizontalHeaderLabels(["Id","Nombre", "Primer apellido","Segundo apellido","Calle","Numero","Colonia","Municipio","Telefono","Numero IMSS","INE","CURP","RFC","Usuario","Contraseña","Documentación","Acción","Acción"])
        header = self.tabla_docentes.horizontalHeader()
        header.setStretchLastSection(True)
        self.tabla_docentes.setRowCount(len(datos))

        #Rellenamos la tabla con los datos
        for i, fila in  enumerate(datos):
            id = QTableWidgetItem(str(fila[0]))
            nombre = QTableWidgetItem(fila[1])
            primer_apellido = QTableWidgetItem(fila[2])
            segundo_apellido = QTableWidgetItem(fila[3])
            calle = QTableWidgetItem(fila[4])
            numero = QTableWidgetItem(fila[5])
            colonia = QTableWidgetItem(fila[6])
            municipio = QTableWidgetItem(fila[7])
            telefono = QTableWidgetItem(fila[8])
            numero_imss = QTableWidgetItem(fila[9])
            ine = QTableWidgetItem(fila[10])
            curp = QTableWidgetItem(fila[11])
            rfc = QTableWidgetItem(fila[12])
            usuario = QTableWidgetItem(fila[13])
            contrasenia = QTableWidgetItem(fila[14])

            self.tabla_docentes.setItem(i,0,id)
            self.tabla_docentes.setItem(i,1,nombre)
            self.tabla_docentes.setItem(i,2,primer_apellido)
            self.tabla_docentes.setItem(i,3,segundo_apellido)
            self.tabla_docentes.setItem(i,4,calle)
            self.tabla_docentes.setItem(i,5,numero)
            self.tabla_docentes.setItem(i,6,colonia)
            self.tabla_docentes.setItem(i,7,municipio)
            self.tabla_docentes.setItem(i,8,telefono)
            self.tabla_docentes.setItem(i,9,numero_imss)
            self.tabla_docentes.setItem(i,10,ine)
            self.tabla_docentes.setItem(i,11,curp)
            self.tabla_docentes.setItem(i,12,rfc)
            self.tabla_docentes.setItem(i,13,usuario)
            self.tabla_docentes.setItem(i,14,contrasenia)
            
        #Añadimos botones baja, ver documentacion
        for row in range(self.tabla_docentes.rowCount()):
            #Documentación
            btn_documentacion = QPushButton()
            icono_ver = QIcon('img/ver.png')
            btn_documentacion.setIcon(icono_ver)
            btn_documentacion.setObjectName('documentacion_' + str(row))
            btn_documentacion.clicked.connect(self.show_interfaz_documentacion_docente)
            self.tabla_docentes.setCellWidget(row, 15, btn_documentacion)
            #Editar
            btn_editar = QPushButton()
            icono_editar = QIcon('img/editar.png')
            btn_editar.setIcon(icono_editar)
            btn_editar.setObjectName('documentacion_' + str(row))
            btn_editar.clicked.connect(self.show_interface_editar_docente)
            self.tabla_docentes.setCellWidget(row, 16, btn_editar)
            #Borrar
            btn_borrar = QPushButton()
            icono_borrar = QIcon('img/borrar.png')
            btn_borrar.setIcon(icono_borrar)
            btn_borrar.setObjectName('baja_' + str(row))
            btn_borrar.clicked.connect(self.borrar_fila)
            self.tabla_docentes.setCellWidget(row, 17, btn_borrar)
            
    
    def borrar_fila(self):
        administrativos = Administrativos()
        boton = self.sender()
        fila = int(boton.objectName().split('_')[1])
        id_docente = self.tabla_docentes.item(fila, 0).text()  # Suponiendo que el ID está en la primera columna

        # Agregar cuadro de mensaje de confirmación
        mensaje_box = QMessageBox()
        mensaje_box.setWindowTitle("Confirmación")
        mensaje_box.setText("¿Está seguro de que desea dar de baja a este docente?")
        mensaje_box.setIcon(QMessageBox.Warning)
        mensaje_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resultado = mensaje_box.exec_()

        if resultado == QMessageBox.Yes:
            self.tabla_docentes.removeRow(fila)
            administrativos.elimina_docente(id_docente)
            self.cargar_datos()
    
    def show_interfaz_documentacion_docente(self):
        #Obtenemos el id del docente para traer sus documentos
        boton = self.sender()
        fila = int(boton.objectName().split('_')[1])
        id_docente = self.tabla_docentes.item(fila, 0).text()
        self.interface_documentacion = administrativos_interfaz_documentacion_docente.InterfaceDocumentacionDocente(id_docente)
        self.interface_documentacion.show()
        self.close()
    
    def show_interface_editar_docente(self):
        #Obtenemos el id del docente para traer sus datos
        boton = self.sender()
        fila = int(boton.objectName().split('_')[1])
        id_docente = self.tabla_docentes.item(fila, 0).text()
        self.interface_editar_docente = administrativos_interfaz_editar_docente.InterfaceEditarDocente(id_docente)
        self.interface_editar_docente.show()
        self.close()

    def show_interfaz_menu_administrativo(self):
        self.interface_administrativos = administrativos_interfaz_principal.InterfazAdministrativo()
        self.interface_administrativos.show()
        self.close()
    def show_interfaz_agregar_docente(self):
        self.interface_agregar_docente = administrativos_interfaz_agregar_docente.InterfaceAgregarDocente()
        self.interface_agregar_docente.show()
        self.close()

def aplicar_estilo_agregar(boton,color):
    style = f"""
    QPushButton {{
        font: 11pt;
        background-color: {color};
        border-radius: 25px;
        padding: 10px 20px;
        min-width: 179px;
        min-height: 36px;
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

