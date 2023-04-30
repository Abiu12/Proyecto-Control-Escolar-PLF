
from PyQt5.QtWidgets import  QWidget, QMessageBox,QFrame, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget,QTableWidgetItem,QAbstractItemView,QWidget
from administrativos_conexion import Administrativos
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPalette, QBrush, QColor,QIcon

import administrativos_interfaz_documentacion_alumno
import administrativos_interfaz_inscripcion_alumno
import administrativos_interfaz_principal
import administrativos_interfaz_editar_alumno
import administrativos_interfaz_ver_reporte_alumno

class InterfazControlAlumnos(QWidget):
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

        #Label de alumnos
        title = QLabel("Lista de alumnos")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        
        #Boton de inscribir alumno
        self.btnInscribirAlumno= QPushButton('Inscribir alumno')
        aplicar_estilo_inscribir(self.btnInscribirAlumno,"#FF5733")
        self.btnInscribirAlumno.clicked.connect(self.show_interface_inscripcion_alumno)

        # Crear la tabla Alumnos 
        self.tablaAlumnos = QTableWidget()
        self.tablaAlumnos.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #Cargamos los datos
        self.cargar_datos()
        
        #Boton de regreso
        self.btnRegresarMenuAdmin = QPushButton('Volver a menú administrativo')
        # icono_regresar = QIcon('img/flecha-izquierda.png')
        # self.btnRegresarMenuAdmin.setIcon(icono_regresar)
        aplicar_estilo_volver(self.btnRegresarMenuAdmin,"#FF5733")
        self.btnRegresarMenuAdmin.clicked.connect(self.show_interface_menu_administrativo)

        #Distribucion
        vbox = QVBoxLayout()

        vbox.addWidget(title)

        #Layout para el boton a la derecha de inscribir alumno
        hbox_layout_btnAlumno = QHBoxLayout()
        hbox_layout_btnAlumno.addStretch(1)
        hbox_layout_btnAlumno.addWidget(self.btnInscribirAlumno)
        vbox.addLayout(hbox_layout_btnAlumno)

        vbox.addWidget(self.tablaAlumnos)

        #Layout para el boton a la derecha de regresar
        hbox_layout = QHBoxLayout()
        hbox_layout.addStretch(1)
        hbox_layout.addWidget(self.btnRegresarMenuAdmin)
        
        vbox.addLayout(hbox_layout)
        self.setLayout(vbox)

    def cargar_datos(self):
        #Cargamos los datos de los alumnos de la bd a la tabla
        administrativos = Administrativos() #Nueva conexion
        datos = administrativos.consulta_alumnos()
        self.tablaAlumnos.setColumnCount(23) # Creamos las columnas necesarias para todos los datos
        self.tablaAlumnos.setHorizontalHeaderLabels(["Id","Nombre", "Primer apellido","Segundo apellido","Calle","Numero","Colonia","Municipio","Telefono","Numero IMSS","INE","CURP","RFC","Madre","Télefono madre","Padre","Teléfono padre","Usuario","Contraseña","Documentación","Acción","Acción","Reporte"])
        header = self.tablaAlumnos.horizontalHeader()
        header.setStretchLastSection(True)
        self.tablaAlumnos.setRowCount(len(datos))

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
            nombre_madre = QTableWidgetItem(fila[13])
            telefono_madre = QTableWidgetItem(fila[14])
            nombre_padre = QTableWidgetItem(fila[15])
            telefono_padre = QTableWidgetItem(fila[16])
            usuario = QTableWidgetItem(fila[17])
            contrasenia = QTableWidgetItem(fila[18])

            self.tablaAlumnos.setItem(i,0,id)
            self.tablaAlumnos.setItem(i,1,nombre)
            self.tablaAlumnos.setItem(i,2,primer_apellido)
            self.tablaAlumnos.setItem(i,3,segundo_apellido)
            self.tablaAlumnos.setItem(i,4,calle)
            self.tablaAlumnos.setItem(i,5,numero)
            self.tablaAlumnos.setItem(i,6,colonia)
            self.tablaAlumnos.setItem(i,7,municipio)
            self.tablaAlumnos.setItem(i,8,telefono)
            self.tablaAlumnos.setItem(i,9,numero_imss)
            self.tablaAlumnos.setItem(i,10,ine)
            self.tablaAlumnos.setItem(i,11,curp)
            self.tablaAlumnos.setItem(i,12,rfc)
            self.tablaAlumnos.setItem(i,13,nombre_madre)
            self.tablaAlumnos.setItem(i,14,telefono_madre)
            self.tablaAlumnos.setItem(i,15,nombre_padre)
            self.tablaAlumnos.setItem(i,16,telefono_padre)
            self.tablaAlumnos.setItem(i,17,usuario)
            self.tablaAlumnos.setItem(i,18,contrasenia)
            
        #Añadimos botones baja, ver documentacion
        for row in range(self.tablaAlumnos.rowCount()):
            #Documentación
            btn_documentacion = QPushButton()
            icono_ver = QIcon('img/ver.png')
            btn_documentacion.setIcon(icono_ver)
            btn_documentacion.setObjectName('documentacion_' + str(row))
            btn_documentacion.clicked.connect(self.show_interface_documentacion_alumno)
            self.tablaAlumnos.setCellWidget(row, 19, btn_documentacion)
            #Editar
            btn_editar = QPushButton()
            icono_editar = QIcon('img/editar.png')
            btn_editar.setIcon(icono_editar)
            btn_editar.setObjectName('documentacion_' + str(row))
            btn_editar.clicked.connect(self.show_interface_editar_alumno)
            self.tablaAlumnos.setCellWidget(row, 20, btn_editar)
            #Borrar
            btn_borrar = QPushButton()
            icono_borrar = QIcon('img/borrar.png')
            btn_borrar.setIcon(icono_borrar)
            btn_borrar.setObjectName('baja_' + str(row))
            btn_borrar.clicked.connect(self.borrar_fila)
            self.tablaAlumnos.setCellWidget(row, 21, btn_borrar)

            #Reporte
            administrativos = Administrativos()
            btn_notificacion = QPushButton()
            id_alumno = self.tablaAlumnos.item(row, 0).text()

            reporte = administrativos.buscar_notificacion_reporte(id_alumno)

            if(reporte):
                icono_notificacion = QIcon('img/activo.png')
                btn_notificacion.clicked.connect(self.ver_notificacion)
            else:
                icono_notificacion = QIcon('img/notificacion.png')
            btn_notificacion.setIcon(icono_notificacion)
            btn_notificacion.setObjectName('baja_' + str(row))
            self.tablaAlumnos.setCellWidget(row, 22, btn_notificacion)

            
    def ver_notificacion(self):
        boton = self.sender()
        fila = int(boton.objectName().split('_')[1])
        id_alumno = self.tablaAlumnos.item(fila, 0).text()  # Suponiendo que el ID está en la primera columna
        self.interface_notificacion = administrativos_interfaz_ver_reporte_alumno.InterfazVerReporteAlumno(id_alumno)
        self.interface_notificacion.show()
        self.close()
    
    def borrar_fila(self):
        administrativos = Administrativos()
        boton = self.sender()
        fila = int(boton.objectName().split('_')[1])
        id_alumno = self.tablaAlumnos.item(fila, 0).text()  # Suponiendo que el ID está en la primera columna

        # Agregar cuadro de mensaje de confirmación
        mensaje_box = QMessageBox()
        mensaje_box.setWindowTitle("Confirmación")
        mensaje_box.setText("¿Está seguro de que desea dar de baja a este alumno?")
        mensaje_box.setIcon(QMessageBox.Warning)
        mensaje_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resultado = mensaje_box.exec_()

        if resultado == QMessageBox.Yes:
            self.tablaAlumnos.removeRow(fila)
            administrativos.elimina_alumno(id_alumno)
            self.cargar_datos()
    
    def show_interface_documentacion_alumno(self):
        #Obtenemos el id del alumno para traer sus documentos
        boton = self.sender()
        fila = int(boton.objectName().split('_')[1])
        id_alumno = self.tablaAlumnos.item(fila, 0).text()
        self.interface_documentacion = administrativos_interfaz_documentacion_alumno.InterfaceDocumentacionAlumno(id_alumno)
        self.interface_documentacion.show()
        self.close()
    
    def show_interface_editar_alumno(self):
        #Obtenemos el id del alumno para traer sus datos
        boton = self.sender()
        fila = int(boton.objectName().split('_')[1])
        id_alumno = self.tablaAlumnos.item(fila, 0).text()
        self.interface_editar_alumno = administrativos_interfaz_editar_alumno.InterfaceEditarAlumno(id_alumno)
        self.interface_editar_alumno.show()
        self.close()

    def show_interface_menu_administrativo(self):
        self.interface_administrativos = administrativos_interfaz_principal.InterfazAdministrativo()
        self.interface_administrativos.show()
        self.close()
    def show_interface_inscripcion_alumno(self):
        self.interface_inscripcion_alumno = administrativos_interfaz_inscripcion_alumno.InterfaceInscripcionAlumno()
        self.interface_inscripcion_alumno.show()
        self.close()

def aplicar_estilo_inscribir(boton,color):
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
        min-width: 325px;
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

