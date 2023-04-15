import sys
import folium
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,QSpacerItem,QSizePolicy,QGridLayout,QDialog, QTableWidget,QTableWidgetItem,QAbstractItemView,QFormLayout,QMessageBox,QWidget, QLineEdit, QFileDialog, QComboBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from alumnos_conexion import Alumnos
from administrativos_conexion import Administrativos
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QBrush, QColor
import tempfile
import os
from mysql.connector.locales.eng import client_error

class Interface1(QWidget):

    alumnos = Alumnos()
    
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Control Escolar")
        self.label1 = QLabel('Interfaz 1')
        self.button1 = QPushButton('Alumnos')
        self.button2 = QPushButton('Docentes')
        self.button3 = QPushButton('Administrativos')
        self.button4 = QPushButton('Mostrar Ruta')
        self.button1.clicked.connect(self.show_alumnos)
        self.button2.clicked.connect(self.show_docentes)
        self.button3.clicked.connect(self.show_administrativos)
        self.button4.clicked.connect(self.show_mapa)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        vbox.addWidget(self.button3)
        vbox.addWidget(self.button4)

        self.setLayout(vbox)

    def show_alumnos(self):
        pass
        # self.interface_alumnos = InterfaceAlumnos()
        # self.interface_alumnos.show()
        # self.hide()

    def show_docentes(self):
        self.interface_docentes = InterfaceDocentes()
        self.interface_docentes.show()
        self.hide()

    def show_administrativos(self):
        self.interface_administrativos = InterfaceAdministrativos()
        self.interface_administrativos.show()
        self.hide()

    def show_mapa(self):
        self.mapa = Mapa()
        self.mapa.show()
        self.hide()


class InterfaceAlumnos(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.initUI()

    def initUI(self):
        self.label_alumnos = QLabel('Interfaz Alumnos')
        self.button_back = QPushButton('Volver a Interfaz 1')
        self.button_back.clicked.connect(self.show_interface1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_alumnos)
        vbox.addWidget(self.button_back)

        self.setLayout(vbox)

    def show_interface1(self):
        self.interface1 = Interface1()
        self.interface1.show()
        self.hide()


class InterfaceDocentes(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.initUI()

    def initUI(self):
        self.label_docentes = QLabel('Interfaz Docentes')
        self.button_back = QPushButton('Volver a Interfaz 1')
        self.button_back.clicked.connect(self.show_interface1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_docentes)
        vbox.addWidget(self.button_back)

        self.setLayout(vbox)

    def show_interface1(self):
        self.interface1 = Interface1()
        self.interface1.show()
        self.hide()


class InterfaceAdministrativos(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.setStyleSheet("background-color: #F2F2F2;")

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Administrativo")
        title = QLabel("Menú Principal Administrativo")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")

        # Crear los botones
        self.btnControlAlumnos = QPushButton('Control de alumnos')
        aplicar_estilos(self.btnControlAlumnos,"#FF8C00")
        self.btnControlAlumnos.clicked.connect(self.show_interface_control_alumnos)

        self.btnControlDocentes = QPushButton('Control de docentes')
        aplicar_estilos(self.btnControlDocentes,"#FF8C00")
        self.btnControlDocentes.clicked.connect(self.show_interface_control_docentes)

        self.btnNomina = QPushButton('Nómina')
        aplicar_estilos(self.btnNomina,"#FF8C00")
        self.btnNomina.clicked.connect(self.show_interface_nomina)

        self.btnEventos = QPushButton('Eventos, Actividades')
        aplicar_estilos(self.btnEventos,"#FF8C00")
        self.btnEventos.clicked.connect(self.show_interface_eventos)

        self.btnRegresar = QPushButton('Volver al menu principal')
        aplicar_estilos(self.btnRegresar,"#4CAF50")
        self.btnRegresar.clicked.connect(self.show_interface1)

        # Crear la cuadrícula para los primeros cuatro botones
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.btnControlAlumnos, 0, 0)
        grid_layout.addWidget(self.btnControlDocentes, 0, 1)
        grid_layout.addWidget(self.btnNomina, 1, 0)
        grid_layout.addWidget(self.btnEventos, 1, 1)

        # Crear un layout horizontal para el botón de regresar
        hbox_layout = QHBoxLayout()
        hbox_layout.addStretch(1)
        hbox_layout.addWidget(self.btnRegresar)

        # Crear un layout vertical para colocar la cuadrícula y el layout horizontal del botón de regresar
        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(title)
        vbox_layout.addSpacing(150)
        vbox_layout.addLayout(grid_layout)
        vbox_layout.addStretch(1)
        vbox_layout.addLayout(hbox_layout)

        # Configurar el layout principal de la ventana
        self.setLayout(vbox_layout)

    def show_interface1(self):
        self.interface1 = Interface1()
        self.interface1.show()
        self.hide()
    def show_interface_control_alumnos(self):
        self.interface_control_alumnos = InterfazControlAlumnos()
        self.interface_control_alumnos.show()
        self.hide()
    def show_interface_control_docentes(self):
        self.interface_control_docentes = InterfazControlDocentes()
        self.interface_control_docentes.show()
        self.hide()
    def show_interface_nomina(self):
        self.interface_nomina= InterfazNomina()
        self.interface_nomina.show()
        self.hide()
    def show_interface_eventos(self):
        self.interface_eventos= InterfazEventos()
        self.interface_eventos.show()
        self.hide()


class InterfazControlAlumnos(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.initUI()
    
    def initUI(self):
        #Label de alumnos
        title = QLabel("Lista de alumnos")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        
        #Boton de inscribir alumno
        self.btnInscribirAlumno= QPushButton('Inscribir alumno')
        self.btnInscribirAlumno.setStyleSheet("background-color: #4CAF50; color: #fff; padding: 10px 20px; border-radius: 5px; font-size: 16px;")
        self.btnInscribirAlumno.clicked.connect(self.show_interface_inscripcion_alumno)

        # Crear la tabla Alumnos 
        self.tablaAlumnos = QTableWidget()
        self.tablaAlumnos.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #Cargamos los datos
        self.cargar_datos()
        
        #Boton de regreso
        self.btnRegresarMenuAdmin = QPushButton('Volver a Menu de Administrativos')
        self.btnRegresarMenuAdmin.setStyleSheet("background-color: #4CAF50; color: #fff; padding: 10px 20px; border-radius: 5px; font-size: 16px;")
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
        self.tablaAlumnos.setColumnCount(19) # Creamos las columnas necesarias para todos los datos
        self.tablaAlumnos.setHorizontalHeaderLabels(["Id","Nombre", "Primer apellido","Segundo apellido","Calle","Numero","Colonia","Municipio","Telefono","Numero IMSS","INE","CURP","RFC","Madre","Télefono madre","Padre","Teléfono padre","Acción","Documentación"])
        self.tablaAlumnos.setRowCount(len(datos))

        # Ajustamos el tamaño de la última columna para que ocupe todo el espacio disponible
        # self.tablaAlumnos.setColumnWidth(0, 50)
        # self.tablaAlumnos.setColumnWidth(1, 120)
        # self.tablaAlumnos.setColumnWidth(2, 50)
        # self.tablaAlumnos.setColumnWidth(3, 50)
        # self.tablaAlumnos.setColumnWidth(4, 50)
        header = self.tablaAlumnos.horizontalHeader()
        header.setStretchLastSection(True)
        
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
            
        #Añadimos botones baja, ver documentacion
        for row in range(self.tablaAlumnos.rowCount()):
            #Borrar
            btn_borrar = QPushButton('Baja')
            btn_borrar.setObjectName('baja_' + str(row))
            btn_borrar.clicked.connect(self.borrar_fila)
            self.tablaAlumnos.setCellWidget(row, 17, btn_borrar)
            #Documentación
            btn_documentacion = QPushButton('Ver')
            btn_documentacion.setObjectName('documentacion_' + str(row))
            btn_documentacion.clicked.connect(self.show_interface_documentacion_alumno)
            self.tablaAlumnos.setCellWidget(row, 18, btn_documentacion)
    
    def borrar_fila(self):
        administrativos = Administrativos()
        boton = self.sender()
        fila = int(boton.objectName().split('_')[1])
        id_alumno = self.tablaAlumnos.item(fila, 0).text()  # Suponiendo que el ID está en la primera columna
        self.tablaAlumnos.removeRow(fila)
        administrativos.elimina_alumno(id_alumno)
        self.cargar_datos()
    
    def show_interface_documentacion_alumno(self):
        #Obtenemos el id del alumno para traer sus documentos
        boton = self.sender()
        fila = int(boton.objectName().split('_')[1])
        id_alumno = self.tablaAlumnos.item(fila, 0).text()
        self.interface_documentacion = InterfaceDocumentacionAlumno(id_alumno)
        self.interface_documentacion.show()
        self.hide()
    def show_interface_menu_administrativo(self):
        self.interface_administrativos = InterfaceAdministrativos()
        self.interface_administrativos.show()
        self.hide()
    def show_interface_inscripcion_alumno(self):
        self.interface_inscripcion_alumno = InterfaceInscripcionAlumno()
        self.interface_inscripcion_alumno.show()
        self.hide()

class InterfaceDocumentacionAlumno(QWidget):
    idAlumno = "" #Variable global para tener presente en todo el programa el idAlumno
    def __init__(self,id):
        super().__init__()
        self.resize(1200, 800)
        self.initUI(id)
        
    def initUI(self,id):
        administrativo = Administrativos()
        datos = administrativo.buscar_alumno(id)
        self.idAlumno = id
        
        #Label documentacion del alumno X
        title = QLabel(f"Documentación del alumno {datos[1]}")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")

        #Boton de agregar documentacion
        self.btn_agregar_documentacion = QPushButton('Agregar documentación')
        self.btn_agregar_documentacion.setStyleSheet("background-color: #4CAF50; color: #fff; padding: 10px 20px; border-radius: 5px; font-size: 16px;")
        self.btn_agregar_documentacion.clicked.connect(self.show_interface_agregar_documentacion)
    
        #Tabla de documentacion
        self.tablaDocumentacion = QTableWidget()
        self.tablaDocumentacion.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cargar_datos_documentos();

        #Boton de regresar
        self.btn_regresar_control_alumnos = QPushButton('Volver a control alumnos')
        self.btn_regresar_control_alumnos.setStyleSheet("background-color: #4CAF50; color: #fff; padding: 10px 20px; border-radius: 5px; font-size: 16px;")
        self.btn_regresar_control_alumnos.clicked.connect(self.show_interface_control_alumnos)

        #Layout para el boton a la derecha de agregar documentacion
        hbox_layout_btn_agregar_documentacion = QHBoxLayout()
        hbox_layout_btn_agregar_documentacion.addStretch(1)
        hbox_layout_btn_agregar_documentacion.addWidget(self.btn_agregar_documentacion)
        

        #Layout para el boton a la derecha de regresar
        hbox_layout_boton_regresar = QHBoxLayout()
        hbox_layout_boton_regresar.addStretch(1)
        hbox_layout_boton_regresar.addWidget(self.btn_regresar_control_alumnos)

        vbox = QVBoxLayout()
        vbox.addWidget(title)
        vbox.addLayout(hbox_layout_btn_agregar_documentacion)
        vbox.addWidget(self.tablaDocumentacion)
        vbox.addLayout(hbox_layout_boton_regresar)

        self.setLayout(vbox)

    def show_interface_control_alumnos(self):
        self.interface_control_alumnos = InterfazControlAlumnos()
        self.interface_control_alumnos.show()
        self.hide()
        
    def show_interface_agregar_documentacion(self):
        self.interface_agregar_documentacion = InterfazAgregarDocumentacionAlumno(self.idAlumno)
        self.interface_agregar_documentacion.show()
        self.hide()

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
        datos = administrativos.consulta_documentacion_alumno(self.idAlumno)
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
            btn_ver_archivo = QPushButton('Ver')
            btn_ver_archivo.setObjectName('ver_' + str(row))
            btn_ver_archivo.clicked.connect(self.ver_archivo)
            self.tablaDocumentacion.setCellWidget(row, 2, btn_ver_archivo)
            
            #Borrar
            btn_borrar_archivo = QPushButton('Borrar')
            btn_borrar_archivo.setObjectName('baja_' + str(row))
            btn_borrar_archivo.clicked.connect(self.borrar_archivo)
            self.tablaDocumentacion.setCellWidget(row, 3, btn_borrar_archivo)
    
    def ver_archivo(self):
        administrativo = Administrativos()
        #Sabemos el id del archivo que se quiere ver
        boton = self.sender()
        fila = int(boton.objectName().split('_')[1])
        id_documentacion_alumno = self.tablaDocumentacion.item(fila, 0).text()
        datos = administrativo.buscar_documentacion_alumno(self.idAlumno,id_documentacion_alumno)
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
        self.tablaDocumentacion.removeRow(fila)
        administrativos.elimina_documento(self.idAlumno,id_documento)
        self.cargar_datos_documentos()


class InterfazAgregarDocumentacionAlumno(QWidget):
    idAlumno = "" #Variable para tener el id del alumno
    def __init__(self,idAlumno):
        super().__init__()
        self.resize(1200, 800)
        self.initUI(idAlumno)
           
    def initUI(self, idAlumno):

    
        self.idAlumno = idAlumno

        #Label de Documentacion de alumno X
        title = QLabel("Agregar documentacion del alumno")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 100px;")

        #Formulario para almacenar los datos
        form_layout_documento = QFormLayout()

        form_layout_documento.addRow(title)
        
        #Campo de tipo de documento 
        tipo_documento_label = QLabel("Tipo de documento:")
        tipo_documento_label.setStyleSheet("font-size: 20px;  margin-bottom: 100px;")
        self.tipo_documento_combo = QComboBox()
        self.tipo_documento_combo.addItems(["CURP", "Acta de nacimiento"])
        self.tipo_documento_combo.setStyleSheet("font-size: 16px; padding: 5px;  margin-bottom: 100px;")
        form_layout_documento.addRow(tipo_documento_label, self.tipo_documento_combo)

        # Campo para cargar archivo PDF
        archivo_pdf_label = QLabel("Archivo PDF:")
        comodin_label = QLabel(" ")
        archivo_pdf_label.setStyleSheet("font-size: 20px;  margin-bottom: 50px;")
        archivo_btn = QPushButton("Seleccionar archivo...")
        archivo_btn.clicked.connect(self.cargar_archivo)
        self.archivo_label = QLabel("Ningún archivo seleccionado")
        self.archivo_label.setStyleSheet("font-size: 16px;")
        archivo_btn.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; padding: 10px;")
        form_layout_documento.addRow(archivo_pdf_label, archivo_btn)
        form_layout_documento.addRow(comodin_label,self.archivo_label)

        #Botón para guardar los datos
        btn_guardar_documento = QPushButton("Guardar")
        btn_guardar_documento.setStyleSheet("background-color: #4CAF50; color: #fff; padding: 10px 20px; border-radius: 5px; font-size: 16px;")
        btn_guardar_documento.clicked.connect(self.insertar_documento)

        #Boton para regresar a documentacion alumno
        self.btn_regresar_documentacion_alumno = QPushButton('Volver a documentacion de alumno')
        self.btn_regresar_documentacion_alumno.setStyleSheet("background-color: #4CAF50; color: #fff; padding: 10px 20px; border-radius: 5px; font-size: 16px;")
        self.btn_regresar_documentacion_alumno.clicked.connect(self.show_interface_documentacion_alumno)


        vbox = QVBoxLayout()
        # vbox.addWidget(title)

        # Agregar formulario al layout vertical
        vbox.addLayout(form_layout_documento)

        #Layout de botones
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(btn_guardar_documento)
        button_layout.addWidget(self.btn_regresar_documentacion_alumno)
        
        vbox.addLayout(button_layout)

        self.setLayout(vbox)

    def cargar_archivo(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Archivos PDF (*.pdf)")
        file_dialog.setDefaultSuffix(".pdf")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_() == QDialog.Accepted:
            self.archivo_path = file_dialog.selectedFiles()[0]
            self.archivo_label.setText(self.archivo_path)

    def show_interface_documentacion_alumno(self):
        self.interface_documentacion_alumno = InterfaceDocumentacionAlumno(self.idAlumno)
        self.interface_documentacion_alumno.show()
        self.hide()
    
    def insertar_documento(self):
        administrativos = Administrativos() #Conexion con administrativos
        archivo_elegido = str(self.archivo_path)
        #INSERTAMOS UN ARCHIVO
        with open(archivo_elegido, "rb") as f:
            archivo_bytes = f.read()
            resultado = administrativos.inserta_documento_alumno(self.tipo_documento_combo.currentText(),archivo_bytes,self.idAlumno)
            if resultado:
                QMessageBox.information(self, "Éxito", "Documento insertado correctamente")
                self.interface_documentacion_alumno = InterfaceDocumentacionAlumno(self.idAlumno)
                self.interface_documentacion_alumno.show()
                self.hide()
            else:
                QMessageBox.critical(self, "Error", "No se pudo insertar el alumno")
        
      
class InterfaceInscripcionAlumno(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.initUI()
        
    def initUI(self):
        
        #Label de inscripcion de alumnos
        title = QLabel("Inscripción de un alumno")
        title.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        
        vbox = QVBoxLayout()

        # Layout para los campos del formulario y el titulo
        campos_layout = QGridLayout()

        #Agregamos titulo
        campos_layout.addWidget(title, 0, 1, 1, 2, Qt.AlignHCenter | Qt.AlignTop)

        #Campos del formulario
        nombre_label = QLabel("Nombre:")
        nombre_label.setStyleSheet("QLabel { font-size: 18px; font-weight: bold; color: #555; margin-right: 10px; }")
        self.nombre_input = QLineEdit()
        self.nombre_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 6px; }")

        primer_apellido_label = QLabel("Primer apellido:")
        primer_apellido_label.setStyleSheet("QLabel {font-size: 18px; font-weight: bold; color: #555; margin-right: 10px; }")
        self.primer_apellido_input = QLineEdit()
        self.primer_apellido_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 6px; }")

        segundo_apellido_label = QLabel("Segundo apellido:")
        segundo_apellido_label.setStyleSheet("QLabel {font-size: 18px; font-weight: bold; color: #555; margin-right: 10px; }")
        self.segundo_apellido_input = QLineEdit()
        self.segundo_apellido_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 6px; }")
        
        calle_label = QLabel("Calle:")
        calle_label.setStyleSheet("QLabel {font-size: 18px; font-weight: bold; color: #555; margin-right: 10px; }")
        self.calle_input = QLineEdit()
        self.calle_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 6px; }")

        numero_label = QLabel("Número:")
        numero_label.setStyleSheet("QLabel {font-size: 18px; font-weight: bold; color: #555; margin-right: 10px; }")
        self.numero_input = QLineEdit()
        self.numero_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 6px; }")

        colonia_label = QLabel("Colonia:")
        colonia_label.setStyleSheet("QLabel {font-size: 18px; font-weight: bold; color: #555; margin-right: 10px; }")
        self.colonia_input = QLineEdit()
        self.colonia_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 6px; }")

        municipio_label = QLabel("Municipio:")
        municipio_label.setStyleSheet("QLabel {font-size: 18px; font-weight: bold; color: #555; margin-right: 10px; }")
        self.municipio_input = QLineEdit()
        self.municipio_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 6px; }")

        telefono_label = QLabel("Telefono:")
        telefono_label.setStyleSheet("QLabel {font-size: 18px; font-weight: bold; color: #555; margin-right: 10px; }")
        self.telefono_input = QLineEdit()
        self.telefono_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 6px; }")

        numero_imss_label = QLabel("Numero IMSS:")
        numero_imss_label.setStyleSheet("QLabel {font-size: 18px; font-weight: bold; color: #555; margin-right: 10px; }")
        self.numero_imss_input = QLineEdit()
        self.numero_imss_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 6px; }")

        ine_label = QLabel("Ine:")
        ine_label.setStyleSheet("QLabel {font-size: 18px; font-weight: bold; color: #555; margin-right: 10px; }")
        self.ine_input = QLineEdit()
        self.ine_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 6px; }")

        curp_label = QLabel("Curp:")
        curp_label.setStyleSheet("QLabel {font-size: 18px; font-weight: bold; color: #555; margin-right: 10px; }")
        self.curp_input = QLineEdit()
        self.curp_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 6px; }")

        rfc_label = QLabel("Rfc:")
        rfc_label.setStyleSheet("QLabel {font-size: 18px; font-weight: bold; color: #555; margin-right: 10px; }")
        self.rfc_input = QLineEdit()
        self.rfc_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 6px; }")

        nombre_madre_label = QLabel("Nombre madre:")
        nombre_madre_label.setStyleSheet("QLabel {font-size: 18px; font-weight: bold; color: #555; margin-right: 10px; }")
        self.nombre_madre_input = QLineEdit()
        self.nombre_madre_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 6px; }")

        telefono_madre_label = QLabel("Teléfono madre:")
        telefono_madre_label.setStyleSheet("QLabel {font-size: 18px; font-weight: bold; color: #555; margin-right: 10px; }")
        self.telefono_madre_input = QLineEdit()
        self.telefono_madre_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 6px; }")

        nombre_padre_label = QLabel("Nombre padre:")
        nombre_padre_label.setStyleSheet("QLabel {font-size: 18px; font-weight: bold; color: #555; margin-right: 10px; }")
        self.nombre_padre_input = QLineEdit()
        self.nombre_padre_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 6px; }")

        telefono_padre_label = QLabel("Teléfono padre:")
        telefono_padre_label.setStyleSheet("QLabel {font-size: 18px; font-weight: bold; color: #555; margin-right: 10px; }")
        self.telefono_padre_input = QLineEdit()
        self.telefono_padre_input.setStyleSheet("QLineEdit { border: 1px solid #ccc; border-radius: 4px; padding: 6px; }")

        #Botón para guardar los datos
        guardar_btn = QPushButton("Guardar")
        guardar_btn.setStyleSheet("background-color: #4CAF50; color: #fff; padding: 10px 20px; border-radius: 5px; font-size: 16px;")
        guardar_btn.clicked.connect(self.inscribirAlumno)

        #Boton para regresar a control estudiantes
        self.btnRegresarMenuAdmin = QPushButton('Volver a Control de estudiantes')
        self.btnRegresarMenuAdmin.setStyleSheet("background-color: #4CAF50; color: #fff; padding: 10px 20px; border-radius: 5px; font-size: 16px;")
        self.btnRegresarMenuAdmin.clicked.connect(self.show_interface_control_estudiante)
        
        
        
        #Primer renglon
        campos_layout.addWidget(nombre_label, 1, 0)  # fila 0, columna 0
        campos_layout.addWidget(primer_apellido_label, 1, 1)  # fila 0, columna 1
        campos_layout.addWidget(segundo_apellido_label, 1, 2)  # fila 0, columna 2
        campos_layout.addWidget(calle_label, 1, 3)  # fila 0, columna 3

        #Segundo renglon
        campos_layout.addWidget(self.nombre_input, 2, 0)  # fila 1, columna 0
        campos_layout.addWidget(self.primer_apellido_input, 2, 1)  # fila 1, columna 1
        campos_layout.addWidget(self.segundo_apellido_input, 2, 2)  # fila 1, columna 2
        campos_layout.addWidget(self.calle_input, 2, 3)  # fila 1, columna 3

        #Tercer renglon
        campos_layout.addWidget(numero_label, 3, 0)  # fila 2, columna 0
        campos_layout.addWidget(colonia_label, 3, 1)  # fila 2, columna 1
        campos_layout.addWidget(municipio_label, 3, 2)  # fila 2, columna 2
        campos_layout.addWidget(telefono_label, 3, 3)  # fila 2, columna 3

        #Cuarto renglon
        campos_layout.addWidget(self.numero_input, 4, 0)  # fila 3, columna 0
        campos_layout.addWidget(self.colonia_input, 4, 1)  # fila 3, columna 1
        campos_layout.addWidget(self.municipio_input, 4, 2)  # fila 3, columna 2
        campos_layout.addWidget(self.telefono_input, 4, 3)  # fila 3, columna 3

        #Quinto renglon
        campos_layout.addWidget(numero_imss_label, 5, 0)  # fila 4, columna 0
        campos_layout.addWidget(ine_label, 5, 1)  # fila 4, columna 1
        campos_layout.addWidget(curp_label, 5, 2)  # fila 4, columna 2
        campos_layout.addWidget(rfc_label, 5, 3)  # fila 4, columna 3

        #Sexto renglon
        campos_layout.addWidget(self.numero_imss_input, 6, 0)  # fila 5, columna 0
        campos_layout.addWidget(self.ine_input, 6, 1)  # fila 5, columna 1
        campos_layout.addWidget(self.curp_input, 6, 2)  # fila 5, columna 2
        campos_layout.addWidget(self.rfc_input, 6, 3)  # fila 5, columna 3

        #Septimo renglon
        campos_layout.addWidget(nombre_madre_label, 7, 0)  # fila 6, columna 0
        campos_layout.addWidget(telefono_madre_label, 7, 1)  # fila 6, columna 1
        campos_layout.addWidget(nombre_padre_label, 7, 2)  # fila 6, columna 2
        campos_layout.addWidget(telefono_padre_label, 7, 3)  # fila 6, columna 3

        #Octavo renglon
        campos_layout.addWidget(self.nombre_madre_input, 8, 0)  # fila 7, columna 0
        campos_layout.addWidget(self.telefono_madre_input, 8, 1)  # fila 7, columna 1
        campos_layout.addWidget(self.nombre_padre_input, 8, 2)  # fila 7, columna 2
        campos_layout.addWidget(self.telefono_padre_input, 8, 3)  # fila 7, columna 3

        

        #Agregamos Layout de formulario
        vbox.addLayout(campos_layout)

        # Spacer para separar el formulario de los botones
        spacer = QSpacerItem(60, 60, QSizePolicy.Fixed, QSizePolicy.Fixed)
        vbox.addItem(spacer)

        #Layout de botones
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(guardar_btn)
        button_layout.addWidget(self.btnRegresarMenuAdmin)
        
        vbox.addLayout(button_layout)

        self.setLayout(vbox)

    def show_interface_control_estudiante(self):
        self.interface_control_estudiante = InterfazControlAlumnos()
        self.interface_control_estudiante.show()
        self.hide()
    
    def inscribirAlumno(self):
        administrativos = Administrativos() #Conexion con administrativos
        # Conectar la señal textChanged de los campos de entrada de texto a una función
        nombre = self.nombre_input.text()
        primer_apellido = self.primer_apellido_input.text()
        segundo_apellido = self.segundo_apellido_input.text()
        calle = self.calle_input.text()
        numero = self.numero_input.text()
        colonia = self.colonia_input.text()
        municipio = self.municipio_input.text()
        telefono = self.telefono_input.text()
        numero_imss = self.numero_imss_input.text()
        ine = self.ine_input.text()
        curp = self.curp_input.text()
        rfc = self.rfc_input.text()
        nombre_madre = self.nombre_madre_input.text()
        telefono_madre = self.telefono_madre_input.text()
        nombre_padre = self.nombre_padre_input.text()
        telefono_padre = self.telefono_padre_input.text()

        if(nombre == "" or primer_apellido == "" or segundo_apellido == "" or calle == "" or numero == "" or colonia == "" or municipio == "" or telefono == "" or numero_imss == "" or ine == "" or curp == "" or rfc == "" or nombre_madre == "" or telefono_madre == "" or nombre_padre == "" or telefono_padre == "" ):
            QMessageBox.critical(self, "Error", "Rellenar todos los campos")
            return
        resultado = administrativos.inserta_alumno(nombre,primer_apellido,segundo_apellido,calle,numero,colonia,municipio,telefono,numero_imss,ine,curp,rfc,nombre_madre,telefono_madre,nombre_padre,telefono_padre)
        if resultado:
            QMessageBox.information(self, "Éxito", "Alumno insertado correctamente")
            self.interface_control_estudiante = InterfazControlAlumnos()
            self.interface_control_estudiante.show()
            self.hide()
        else:
            QMessageBox.critical(self, "Error", "No se pudo insertar el alumno")
       



class InterfazControlDocentes(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.initUI()

    def initUI(self):
        self.label_docentes = QLabel('Interfaz Control Docentes')
        self.btnRegresarMenuAdmin = QPushButton('Volver a Menu de Administrativos')
        self.btnRegresarMenuAdmin.setStyleSheet("background-color: #4CAF50; color: #fff; padding: 10px 20px; border-radius: 5px; font-size: 16px;")
        self.btnRegresarMenuAdmin.clicked.connect(self.show_interface_menu_administrativo)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_docentes)
        vbox.addWidget(self.btnRegresarMenuAdmin)

        self.setLayout(vbox)

    def show_interface_menu_administrativo(self):
        self.interface_administrativos = InterfaceAdministrativos()
        self.interface_administrativos.show()
        self.hide()
    

class InterfazNomina(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.initUI()

    def initUI(self):
        self.label_docentes = QLabel('Interfaz Nomina')
        self.btnRegresarMenuAdmin = QPushButton('Volver a Menu de Administrativos')
        self.btnRegresarMenuAdmin.setStyleSheet("background-color: #4CAF50; color: #fff; padding: 10px 20px; border-radius: 5px; font-size: 16px;")
        self.btnRegresarMenuAdmin.clicked.connect(self.show_interface_menu_administrativo)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_docentes)
        vbox.addWidget(self.btnRegresarMenuAdmin)

        self.setLayout(vbox)

    def show_interface_menu_administrativo(self):
        self.interface_administrativos = InterfaceAdministrativos()
        self.interface_administrativos.show()
        self.hide()

class InterfazEventos(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.initUI()

    def initUI(self):
        self.label_docentes = QLabel('Interfaz Eventos')
        self.btnRegresarMenuAdmin = QPushButton('Volver a Menu de Administrativos')
        self.btnRegresarMenuAdmin.setStyleSheet("background-color: #4CAF50; color: #fff; padding: 10px 20px; border-radius: 5px; font-size: 16px;")
        self.btnRegresarMenuAdmin.clicked.connect(self.show_interface_menu_administrativo)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_docentes)
        vbox.addWidget(self.btnRegresarMenuAdmin)

        self.setLayout(vbox)

    def show_interface_menu_administrativo(self):
        self.interface_administrativos = InterfaceAdministrativos()
        self.interface_administrativos.show()
        self.hide()
        
class Mapa(QWidget):
    def __init__(self):
        super().__init__()

        # Coordenadas del origen y destino
        origen = [17.0802048, -96.7465228]
        destino = [19.403557, -99.163246]

        # Crear un objeto Map
        m = folium.Map(location=origen, zoom_start=12)

        # Agregar marcadores para el origen y destino
        folium.Marker(location=origen, icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=destino, icon=folium.Icon(color='red')).add_to(m)

        # Crear una línea entre el origen y el destino
        folium.PolyLine(locations=[origen, destino], color='blue').add_to(m)

        # Guardar el mapa en un archivo HTML temporal
        m.save('temp_map.html')

        # Crear un objeto QWebEngineView para mostrar el mapa en un widget de navegador web
        self.web = QWebEngineView()
        self.web.load(QUrl.fromLocalFile('/temp_map.html'))

        # Agregar el objeto QWebEngineView al layout vertical del widget
        layout = QVBoxLayout()
        layout.addWidget(self.web)
        self.setLayout(layout)

        # Configurar las dimensiones del widget
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Mapa')

def aplicar_estilos(boton,color):
    style = f"""
    QPushButton {{
        background-color: {color};
        color: #fff;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
    }}
    QPushButton:hover {{
        background-color: #FF5733;
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface1 = Interface1()
    interface1.show()
    sys.exit(app.exec_())