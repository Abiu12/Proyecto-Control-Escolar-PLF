from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QFrame, QLabel, QLineEdit, QPushButton, QApplication, QMessageBox,QGridLayout,QHBoxLayout,QTableWidget, QTableWidgetItem,QHeaderView,QDialog
from PyQt5.QtCore import Qt,QUrl,QRect
from PyQt5.QtGui import QDesktopServices,QPalette,QColor,QIcon,QTextCursor,QTextDocument
from PyQt5.QtPrintSupport import QPrinter
import ruta1,ruta2,conexion,notas
import os
from PyQt5.QtGui import QTextTableFormat, QTextLength
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot


#VENTANA PRUEBA DE INICIO DE SESIÓN:

class LoginWindow(QMainWindow):

    def __init__(self):

        super(LoginWindow, self).__init__()
        # Configurar ventana principal
        self.inicio()

    def inicio(self):

        # Diseño del FRAME
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 1300, 800))
        self.frame.setStyleSheet("border-image:url(img/fondof.jpg)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")

        self.setWindowTitle("Inicio de sesión")
        self.setFixedSize(1250, 800)  # Tamaño fijo de la ventana
        self.setCentralWidget(QWidget())  # Widget central de la ventana
        self.centralWidget().setLayout(QVBoxLayout())  # Diseño vertical para el widget central
        self.centralWidget().layout().setAlignment(Qt.AlignCenter)  # Centrar el widget central

        # Crear el marco
        frame = QFrame()
        frame.setFixedWidth(800)  # Ancho fijo del marco
        frame.setStyleSheet("background-color: white; border-radius: 10px;")  # Estilo del marco
        frame.setLayout(QVBoxLayout())  # Diseño vertical para el marco

        label = QLabel(self.frame)
        label.setFixedSize(200, 200)
        label.setStyleSheet("border-image:url(img/usur.png)")
        label.setObjectName("label")


        # Crear etiquetas, campos de texto y botón
        label_usuario = QLabel("Usuario")
        label_usuario.setStyleSheet("QLabel {font: 15pt \"Segoe UI\"; font-weight: bold;}")

        frame.layout().addWidget(label_usuario)

        self.edit_usuario = QLineEdit()  # Cambiar a self.edit_usuario para que sea accesible en todo el objeto
        self.edit_usuario.setFixedSize(300, 40)
        self.edit_usuario.setStyleSheet("QLineEdit {border-radius: 5px;}")
        self.edit_usuario.setPlaceholderText("Ingrese su nombre de usuario")

        frame.layout().addWidget(self.edit_usuario)

        label_contrasena = QLabel("Contraseña:")
        label_contrasena.setStyleSheet("QLabel {font: 15pt \"Segoe UI\"; font-weight: bold;}")

        frame.layout().addWidget(label_contrasena)

        self.edit_contrasena = QLineEdit()  # Cambiar a self.edit_contrasena para que sea accesible en todo el objeto
        self.edit_contrasena.setFixedSize(300, 40)
        self.edit_contrasena.setStyleSheet("QLineEdit {border-radius: 5px;}")
        self.edit_contrasena.setPlaceholderText("Ingrese su contraseña")
        self.edit_contrasena.setEchoMode(QLineEdit.Password)  # Ocultar caracteres de la contraseña

        frame.layout().addWidget(self.edit_contrasena)

        button_ingresar = QPushButton("Ingresar")
        button_ingresar.clicked.connect(self.inicio_sesion)  # Conectar el botón a un slot para validar ingreso
        button_ingresar.setFixedSize(300, 50)
        button_ingresar.setStyleSheet("QPushButton {font: 10pt \"Segoe UI\"; background-color: #3498db; color: white; border-radius: 5px; font-weight: bold}"
                                    "QPushButton:hover {background-color: #2980b9;}")
        
        
        frame.layout().addWidget(button_ingresar, alignment=Qt.AlignCenter)

        label.setAlignment(Qt.AlignCenter)
        self.centralWidget().layout().addWidget(label, alignment=Qt.AlignCenter)


        # Agregar el marco al widget central
        self.centralWidget().layout().addWidget(frame)





    #PRINCIPAL DOCENTES:
    def menu_principal_docentes(self):
       
        self.boton_tutorias = QPushButton(self)
        self.boton_tutorias.setFixedSize(700, 80)
        self.boton_tutorias.setStyleSheet("QPushButton {font: 15pt \"SimSun\"; background-color: #78BDE7; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #3b83bd ; border-top-left-radius: 50px; font-weight: bold}" )

        self.boton_asesorias = QPushButton(self)
        self.boton_asesorias.setFixedSize(700, 80)
        self.boton_asesorias.setStyleSheet("QPushButton {font: 15pt \"SimSun\"; background-color: #78BDE7; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #3b83bd; border-top-left-radius: 50px; font-weight: bold}" )


        self.boton_actividades = QPushButton(self)
        self.boton_actividades.setFixedSize(700, 80)
        self.boton_actividades.setStyleSheet("QPushButton {font: 15pt \"SimSun\"; background-color:#78BDE7; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #3b83bd; border-top-left-radius: 50px; font-weight: bold}" )


        self.boton_reuniones = QPushButton(self)
        self.boton_reuniones.setFixedSize(700,80)
        self.boton_reuniones.setStyleSheet("QPushButton {font: 15pt \"SimSun\"; background-color: #78BDE7; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #3b83bd; border-top-left-radius: 50px; font-weight: bold}" )


        self.boton_clases = QPushButton(self)
        self.boton_clases.setFixedSize(700, 80)
        self.boton_clases.setStyleSheet("QPushButton {font: 15pt \"SimSun\"; background-color: #78BDE7; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #3b83bd; border-top-left-radius: 50px; font-weight: bold}" )
        #Diseño del texto principal


        self.boton_cerrarsesion = QPushButton(self)
        self.boton_cerrarsesion.setFixedSize(700, 80)
        self.boton_cerrarsesion.setStyleSheet("QPushButton {font: 15pt \"SimSun\"; background-color: #78BDE7; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #3b83bd; border-top-left-radius: 50px; font-weight: bold}" )
        #Diseño del texto principal

        self.boton_regresarinicio = QPushButton(self)
        self.boton_regresarinicio.setFixedSize(700, 80)
        self.boton_regresarinicio.setStyleSheet("QPushButton {font: 15pt \"SimSun\"; background-color: #78BDE7; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #3b83bd; border-top-left-radius: 50px; font-weight: bold}" )
        #Diseño del texto principal


        self.texto_principal = QLabel(self)
        self.texto_principal.setFixedSize(1600,71)
        self.texto_principal.setStyleSheet("font: bold 24pt \"Segoe UI\";")
        self.texto_principal.setObjectName("texto_principal")


        self.label = QLabel(self.frame)
        self.label.setFixedSize(570,570)
        self.label.setStyleSheet("border-image:url(img/profesor.png)")
        self.label.setText("")
        self.label.setObjectName("label")


        self.boton_asesorias.raise_()
        self.boton_actividades.raise_()
        self.boton_reuniones.raise_()
        self.boton_clases.raise_()
        self.boton_tutorias.raise_()
        self.boton_cerrarsesion.raise_()
        self.boton_regresarinicio.raise_()


        #Aqui se le da una función al boton, que será
        self.boton_asesorias.clicked.connect(self.abrir_ventana_asesorias)
        self.boton_actividades.clicked.connect(self.abrir_ventana_actividades)
        self.boton_clases.clicked.connect(self.abrir_ventana_clases)
        self.boton_reuniones.clicked.connect(self.abrir_ventana_reuniones)
        self.boton_tutorias.clicked.connect(self.abrir_ventana_tutorias)
        self.boton_cerrarsesion.clicked.connect(self.cerrar_sesion)
        self.boton_regresarinicio.clicked.connect(self.regresar_inicio)

        _translate = QApplication.translate
        self.boton_clases.setText(_translate("Form", "Clases"))
        self.boton_tutorias.setText(_translate("Form", "Tutorias"))
        self.boton_asesorias.setText(_translate("Form", "Asesorias"))
        self.boton_actividades.setText(_translate("Form", "Actividades universidad"))
        self.boton_reuniones.setText(_translate("Form", "Reuniones académicas"))
        self.boton_cerrarsesion.setText(_translate("Form", "Cerrar sesión"))
        self.boton_regresarinicio.setText(_translate("Form", "menu principal"))
        self.texto_principal.setText(_translate("Form", "              ¡Bienvenido al sistema "+ self.datos[1]+ " " +self.datos[2]+'!'))


         # Crear un layout vertical y agregar la tabla a este layout
        layout = QGridLayout()
        layout2= QHBoxLayout()
        
        layout.addWidget(self.boton_tutorias,4,2,alignment=Qt.AlignCenter)
        layout.addWidget(self.boton_actividades,5,2,alignment=Qt.AlignCenter)
        layout.addWidget(self.boton_asesorias,6,2,alignment=Qt.AlignCenter)
        layout.addWidget(self.boton_clases,7,2,alignment=Qt.AlignCenter)
        layout.addWidget(self.boton_reuniones,8,2,alignment=Qt.AlignCenter)
        layout.addWidget(self.boton_cerrarsesion,9,2,alignment=Qt.AlignCenter)
        layout.addWidget(self.boton_regresarinicio,10,2,alignment=Qt.AlignCenter)
        layout.addWidget(self.texto_principal,1,0,alignment=Qt.AlignCenter)
        
        
        layout2.addWidget(self.label)

        layout.addLayout(layout2,3,0,alignment=Qt.AlignCenter)
        # Configurar el widget central con el layout
        widget_central = QWidget()
        widget_central.setLayout(layout)

        self.setCentralWidget(widget_central)



#metodo para iniciar sesion:
    def inicio_sesion(self):
        self.usuario = self.edit_usuario.text()
        self.contrasena = self.edit_contrasena.text()
        cnn=conexion.Conexion_BD.establecer_conexion('railway')
        with cnn.cursor() as cur:
            cur.execute("SELECT * FROM docentes WHERE usuario= %s AND contrasenia = %s", (self.usuario, self.contrasena))
            self.datos = cur.fetchone()
        if self.datos is not None:
                QMessageBox.information(self, "Inicio de sesión", "Inicio de sesión exitoso")
                self.menu_principal_docentes()
        else:
            QMessageBox.warning(self, "Inicio de sesión", "Usuario y/o contraseña incorrecto")
        cnn.close()

#metodo para consultar datos de las asesorias:
    def consulta_datos_asesoria(self):
     cnn=conexion.Conexion_BD.establecer_conexion('railway')   
     with cnn.cursor() as cur:
        cur.execute("SELECT * FROM asesorias WHERE idDocente = %s",[self.datos[0]])
        self.datos_asesorias = cur.fetchall()
        self.mostrar_datos_asesorias()

#metodo para consultar datos de las actividades:
    def consulta_datos_actividad(self):
        cnn=conexion.Conexion_BD.establecer_conexion('railway')
        with cnn.cursor() as cur: 
             cur.execute("SELECT * FROM actividades")
             self.datos_actividades = cur.fetchall()
             self.mostrar_datos_actividades()
        cnn.close()


#metodo para consultar datos de las clases:
    def consulta_datos_clases(self):
        cnn=conexion.Conexion_BD.establecer_conexion('railway')
        with cnn.cursor() as cur: 
             cur.execute("SELECT * FROM materias WHERE id_docente = %s",[self.datos[0]])
             self.datos_clases = cur.fetchall()
             self.mostrar_datos_clases()
        cnn.close()



#metodo para consultar datos de las clases:
    def consulta_datos_reuniones(self):
        cnn=conexion.Conexion_BD.establecer_conexion('railway')
        with cnn.cursor() as cur: 
             cur.execute("SELECT * FROM reuniones WHERE idDocente = %s",[self.datos[0]])
             self.datos_reuniones = cur.fetchall()
             self.mostrar_datos_reuniones()
        cnn.close()

#metodo para consultar datos de los alumnos:
    def consulta_alumnos(self,datos_fila):
        cnn=conexion.Conexion_BD.establecer_conexion('railway')
        with cnn.cursor() as cur: 
             cur.execute("SELECT m.*, a.nombre, a.primer_apellido, a.segundo_apellido, a.telefono FROM materias m JOIN alumnos a ON m.id_alumno = a.idAlumno WHERE m.id_docente = %s and m.nombre_materia = %s", (self.datos[0], datos_fila))
             self.datos_alu = cur.fetchall()
             self.mostrar_lista_estudiantes()
        cnn.close()


#metodo para consultar datos de los alumnos:
    def consulta_grupo1(self):
        cnn=conexion.Conexion_BD.establecer_conexion('railway')
        with cnn.cursor() as cur: 
            cur.execute("SELECT t.*, a.nombre, a.primer_apellido, a.segundo_apellido, a.telefono FROM tutoria t JOIN alumnos a ON t.idAlumno = a.idAlumno WHERE t.idDocente =" + str(self.datos[0]) + " and t.grupo=1")
            self.datos_grupo1 = cur.fetchall()
            self.abrir_grupo1()
        cnn.close()


#metodo para consultar datos de los alumnos:
    def consulta_grupo2(self):
        cnn=conexion.Conexion_BD.establecer_conexion('railway')
        with cnn.cursor() as cur: 
            cur.execute("SELECT t.*, a.nombre, a.primer_apellido, a.segundo_apellido, a.telefono FROM tutoria t JOIN alumnos a ON t.idAlumno = a.idAlumno WHERE t.idDocente =" + str(self.datos[0]) + " and t.grupo=2")
            self.datos_grupo2 = cur.fetchall()
            self.abrirgrup2()
        cnn.close()


#Funcion para mostrar ventanas
    def abrir_ventana_asesorias(self):
        self.consulta_datos_asesoria()

    def abrir_ventana_actividades(self):
        self.consulta_datos_actividad()

    def abrir_ventana_clases(self):
        self.consulta_datos_clases()

    def abrir_ventana_reuniones(self):
        self.consulta_datos_reuniones()


    def abrir_ventana_tutorias(self):
        self.mostrar_datos_tutorias()

    def regresar_inicio (self):
        self.mostrar_regresar_inicio()
    
    def abrir_grupo (self):
        self.consulta_grupo1()

    def abrir_grupo2 (self):
        self.consulta_grupo2()






#metodo para mostrar los datos de las asesorias
    def mostrar_datos_asesorias(self):

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(3) # Número de columnas en la tabla
        self.tabla.setHorizontalHeaderLabels(["Nombre materia", "Horario", "Lugar"]) # Etiquetas de las columnas       
        
        # Agregar filas a la tabla con los datos obtenidos de la base de datos
        for fila, datos in enumerate(self.datos_asesorias):
            self.tabla.insertRow(fila)
            for columna, dato in enumerate(datos):
                item = QTableWidgetItem(str(dato))
                self.tabla.setItem(fila, columna, item)


        # Cambiar color de los encabezados
        header = self.tabla.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { background-color: #78BDE7 }")

        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers) # Deshabilitar la edición de celdas
        self.tabla.setSelectionBehavior(QTableWidget.SelectRows) # Seleccionar filas completas

        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # Ajustar ancho de columnas al ancho disponible
        self.tabla.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents) # Ajustar alto de filas al contenido

        # Crear un QLabel para el texto principal
        texto_principal = QLabel("                           HORARIO DE ASESORIAS")
        texto_principal.setAlignment(Qt.AlignCenter) # Centrar el texto
        texto_principal.setStyleSheet("font: bold 22pt \"MS Shell Dlg 2\"; color: #FFFFFF;")
        

        # Agregar un botón de regresar al layout
        boton_regresar = QPushButton()
        boton_regresar.setFixedSize(50,50)
        boton_regresar.setStyleSheet("border-image:url(img/anterior.png)")
        # Crear un QHBoxLayout para el texto principal y el botón de regresar
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(texto_principal,alignment=Qt.AlignCenter)
        layout_horizontal.addWidget(boton_regresar, alignment=Qt.AlignRight | Qt.AlignVCenter) # Alinear el botón a la derecha y centrarlo verticalmente


        # Crear un QVBoxLayout para el QHBoxLayout y la tabla
        layout_vertical = QVBoxLayout()
        layout_vertical.addLayout(layout_horizontal)
        layout_vertical.addWidget(self.tabla)

        # Configurar el widget central con el QVBoxLayout
        widget_central = QWidget()
        widget_central.setLayout(layout_vertical)
        self.setCentralWidget(widget_central)

        boton_regresar.clicked.connect(self.menu_principal_docentes) # Conectar el botón a un slot para validar ingreso

    def mostrar_datos_actividades(self):
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(3) # Número de columnas en la tabla
        self.tabla.setHorizontalHeaderLabels(["Fecha", "Actividad", "Departamento"]) # Etiquetas de las columnas

        # Agregar filas a la tabla con los datos obtenidos de la base de datos
        for fila, datos in enumerate(self.datos_actividades):
            self.tabla.insertRow(fila)
            for columna, dato in enumerate(datos):
                item = QTableWidgetItem(str(dato))
                self.tabla.setItem(fila, columna, item)



            for i in range(self.tabla.rowCount()):
              if i % 2 == 0:
                palette = QPalette()
                for j in range(self.tabla.columnCount()):
                    self.tabla.item(i,j).setBackground(QColor('#78BDE7' ))

                
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers) # Deshabilitar la edición de celdas
        self.tabla.setSelectionBehavior(QTableWidget.SelectRows) # Seleccionar filas completas

        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # Ajustar ancho de columnas al ancho disponible
        self.tabla.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents) # Ajustar alto de filas al contenido


        # Crear un QLabel para el texto principal
        texto_principal = QLabel("                      ACTIVIDADES UNIVERSIDAD")
        texto_principal.setAlignment(Qt.AlignCenter) # Centrar el texto
        texto_principal.setStyleSheet("font: bold 22pt \"MS Shell Dlg 2\"; color: #FFFFFF;")

        # Agregar un botón de regresar al layout
        boton_regresar = QPushButton()
        boton_regresar.setFixedSize(50,50)
        boton_regresar.setStyleSheet("border-image:url(img/anterior.png)")
        # Crear un QHBoxLayout para el texto principal y el botón de regresar
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(texto_principal,alignment=Qt.AlignCenter)
        layout_horizontal.addWidget(boton_regresar, alignment=Qt.AlignRight | Qt.AlignVCenter) # Alinear el botón a la derecha y centrarlo verticalmente


        # Crear un QVBoxLayout para el QHBoxLayout y la tabla
        layout_vertical = QVBoxLayout()
        layout_vertical.addLayout(layout_horizontal)
        layout_vertical.addWidget(self.tabla)

        # Configurar el widget central con el QVBoxLayout
        widget_central = QWidget()
        widget_central.setLayout(layout_vertical)
        self.setCentralWidget(widget_central)
        boton_regresar.clicked.connect(self.menu_principal_docentes) # Conectar el botón a un slot para validar ingreso



    def mostrar_datos_clases(self):

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5) # Número de columnas en la tabla
        self.tabla.setHorizontalHeaderLabels(["materia", "Horario", "Salon", "Semestre","Ver"]) # Etiquetas de las columnas
       

       # Crear un diccionario para almacenar los datos de las materias
        self.datos_materias = {}


         # Crear una nueva lista de tuplas sin el primer elemento 
        self.datos_sin_primero = [(datos[1], datos[2], datos[3], datos[4]) for datos in self.datos_clases]


        # Agregar filas a la tabla con los datos obtenidos de la base de datos
        for fila, datos in enumerate(self.datos_sin_primero):
            materia = datos[0]
            if materia in self.datos_materias:
                continue
            
            self.datos_materias[materia]={}

            print(self.datos_materias)
            
            self.tabla.insertRow(fila)
            for columna, dato in enumerate(datos):
                    
                item = QTableWidgetItem(str(dato))
                self.tabla.setItem(fila, columna, item)
                
                nota_item = QTableWidgetItem()
                nota_icon = QIcon("img/ver.png") # Reemplaza "ruta/a/tu/icono/nota.png" con la ruta a tu imagen de la nota
                nota_item.setData(Qt.DecorationRole, nota_icon)
                self.tabla.setItem(fila, 4, nota_item)                            


        # Cambiar color de los encabezados
        header = self.tabla.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { background-color: #78BDE7 }")
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers) # Deshabilitar la edición de celdas
        self.tabla.setSelectionBehavior(QTableWidget.SelectRows) # Seleccionar filas completas

        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # Ajustar ancho de columnas al ancho disponible
        self.tabla.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents) # Ajustar alto de filas al contenido


        # Crear un QLabel para el texto principal
        texto_principal = QLabel("                            HORARIO DE CLASES")
        texto_principal.setAlignment(Qt.AlignCenter) # Centrar el texto
        texto_principal.setStyleSheet("font: bold 22pt \"MS Shell Dlg 2\"; color: #FFFFFF;")
        

        # Agregar un botón de regresar al layout
        boton_regresar = QPushButton()
        boton_regresar.setFixedSize(50,50)
        boton_regresar.setStyleSheet("border-image:url(img/anterior.png)")
        # Crear un QHBoxLayout para el texto principal y el botón de regresar
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(texto_principal,alignment=Qt.AlignCenter)
        layout_horizontal.addWidget(boton_regresar, alignment=Qt.AlignRight | Qt.AlignVCenter) # Alinear el botón a la derecha y centrarlo verticalmente


        # Crear un QVBoxLayout para el QHBoxLayout y la tabla
        layout_vertical = QVBoxLayout()
        layout_vertical.addLayout(layout_horizontal)
        layout_vertical.addWidget(self.tabla)

        # Configurar el widget central con el QVBoxLayout
        widget_central = QWidget()
        widget_central.setLayout(layout_vertical)
        self.setCentralWidget(widget_central)
        
        boton_regresar.clicked.connect(self.menu_principal_docentes) # Conectar el botón a un slot para validar ingreso
        self.tabla.cellClicked.connect(self.fila_seleccionada_alu)


    @pyqtSlot(int, int)
    def fila_seleccionada_alu(self, fila, columna):
                datos_fila = []
                for c in range(self.tabla.columnCount()):
                    item = self.tabla.item(fila, c)
                    if item is not None:
                        datos_fila.append(item.text())
                    else:
                        datos_fila.append("")
                prueba=datos_fila[0]
                self.consulta_alumnos(prueba)



    def mostrar_lista_estudiantes(self):

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4) # Número de columnas en la tabla
        self.tabla.setHorizontalHeaderLabels(["Nombre", "Apellido materno", "Apellido paterno", "Numero telefónico"]) # Etiquetas de las columnas
       
        self.dato_alumno = [(dat[7], dat[8], dat[9], dat[10]) for dat in self.datos_alu]
 

        # Agregar filas a la tabla con los datos obtenidos de la base de datos
        for fila, datos in enumerate(self.dato_alumno):
            self.tabla.insertRow(fila)
            for columna, dato in enumerate(datos):
                item = QTableWidgetItem(str(dato))
                self.tabla.setItem(fila, columna, item)    


        # Cambiar color de los encabezados
        header = self.tabla.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { background-color: #78BDE7 }")

                
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers) # Deshabilitar la edición de celdas
        self.tabla.setSelectionBehavior(QTableWidget.SelectRows) # Seleccionar filas completas

        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # Ajustar ancho de columnas al ancho disponible
        self.tabla.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents) # Ajustar alto de filas al contenido


        # Crear un QLabel para el texto principal
        texto_principal = QLabel("                           ALUMNOS INSCRITOS")
        texto_principal.setAlignment(Qt.AlignCenter) # Centrar el texto
        texto_principal.setStyleSheet("font: bold 22pt \"MS Shell Dlg 2\"; color: #FFFFFF;")
        

        # Agregar un botón de regresar al layout
        boton_regresar = QPushButton()
        boton_regresar.setFixedSize(50,50)
        boton_regresar.setStyleSheet("border-image:url(img/anterior.png)")
        # Crear un QHBoxLayout para el texto principal y el botón de regresar
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(texto_principal,alignment=Qt.AlignCenter)
        layout_horizontal.addWidget(boton_regresar, alignment=Qt.AlignRight | Qt.AlignVCenter) # Alinear el botón a la derecha y centrarlo verticalmente


        # Crear un QVBoxLayout para el QHBoxLayout y la tabla
        layout_vertical = QVBoxLayout()
        layout_vertical.addLayout(layout_horizontal)
        layout_vertical.addWidget(self.tabla)

        # Configurar el widget central con el QVBoxLayout
        widget_central = QWidget()
        widget_central.setLayout(layout_vertical)
        self.setCentralWidget(widget_central)
        
        boton_regresar.clicked.connect(self.abrir_ventana_clases) # Conectar el botón a un slot para validar ingreso





    def mostrar_datos_reuniones(self):
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(3) # Número de columnas en la tabla
        self.tabla.setHorizontalHeaderLabels(["Fecha", "Generar reporte","Visualizar reporte"]) # Etiquetas de las columnas

       

        # Agregar filas a la tabla con los datos obtenidos de la base de datos
        for fila, datos in enumerate(self.datos_reuniones):
            self.tabla.insertRow(fila)
            for columna, dato in enumerate(datos):
                item = QTableWidgetItem(str(dato))
                self.tabla.setItem(fila, columna, item)


                nota_item = QTableWidgetItem()
                nota_icon = QIcon("img/nota.png")
                nota_item.setData(Qt.DecorationRole, nota_icon)
                self.tabla.setItem(fila, 1, nota_item)

                nota_item = QTableWidgetItem()
                nota_icon = QIcon("img/ver.png") # Reemplaza "ruta/a/tu/icono/nota.png" con la ruta a tu imagen de la nota
                nota_item.setData(Qt.DecorationRole, nota_icon)
                self.tabla.setItem(fila, 2, nota_item)

                # Centrar el icono en la columna
        self.tabla.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tabla.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tabla.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.tabla.itemClicked.connect(self.mostrar_dialogo_notas)

        # Cambiar color de los encabezados
        header = self.tabla.horizontalHeader()
        header.setStyleSheet("QHeaderView::section { background-color: #78BDE7 }")

                
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers) # Deshabilitar la edición de celdas
        self.tabla.setSelectionBehavior(QTableWidget.SelectRows) # Seleccionar filas completas

        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # Ajustar ancho de columnas al ancho disponible
        self.tabla.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents) # Ajustar alto de filas al contenido


        # Crear un QLabel para el texto principal
        texto_principal = QLabel("                            HORARIO DE REUNIONES")
        texto_principal.setAlignment(Qt.AlignCenter) # Centrar el texto
        texto_principal.setStyleSheet("font: bold 22pt \"MS Shell Dlg 2\"; color: #FFFFFF;")
        

        # Agregar un botón de regresar al layout
        boton_regresar = QPushButton()
        boton_regresar.setFixedSize(50,50)
        boton_regresar.setStyleSheet("border-image:url(img/anterior.png)")
        # Crear un QHBoxLayout para el texto principal y el botón de regresar
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(texto_principal,alignment=Qt.AlignCenter)
        layout_horizontal.addWidget(boton_regresar, alignment=Qt.AlignRight | Qt.AlignVCenter) # Alinear el botón a la derecha y centrarlo verticalmente


        # Crear un QVBoxLayout para el QHBoxLayout y la tabla
        layout_vertical = QVBoxLayout()
        layout_vertical.addLayout(layout_horizontal)
        layout_vertical.addWidget(self.tabla)

        # Configurar el widget central con el QVBoxLayout
        widget_central = QWidget()
        widget_central.setLayout(layout_vertical)
        self.setCentralWidget(widget_central)

        boton_regresar.clicked.connect(self.menu_principal_docentes) # Conectar el botón a un slot para validar ingreso


    def mostrar_dialogo_notas(self, item):
                # Obtener la fila y columna del elemento clickeado
                fila = item.row()
                columna = item.column()

                # Verificar que se hizo clic en el icono de la nota
                if columna == 1:
                    # Crear una nueva instancia de NotasDialog y mostrarla
                    dialogo = notas.NotasDialog(self)
                    resultado = dialogo.exec_()

                    # Procesar el resultado de la ventana secundaria
                    if resultado == QDialog.Accepted:
                        # Obtener la nota ingresada por el usuario
                        nota = dialogo.nota_edit.toPlainText()

                        # Guardar la nota en un archivo de texto
                        with open("nota"+str(self.datos[0])+str(self.datos_reuniones[0])+".pdf", "w") as f:
                            f.write(nota)

                        # Cerrar la ventana
                        dialogo.accept()



    def mostrar_datos_tutorias(self):
        # Crear los botones
        self.boton_grup1 = QPushButton("Grupo 1", self)
        self.boton_grup2 = QPushButton("Grupo 2", self)
        self.boton_viajes = QPushButton("Viajes Planeados", self)

        # Establecer las hojas de estilo de los botones
        estilo_botones = """QPushButton {font: 18pt "SimSun";color: #000000;background-color: #78BDE7;border-radius: 50px;padding: 10px;margin: 10px;} QPushButton:hover { background-color: #3b83bd;}"""

        self.boton_grup1.setStyleSheet(estilo_botones)
        self.boton_grup2.setStyleSheet(estilo_botones)
        self.boton_viajes.setStyleSheet(estilo_botones)

        self.boton_grup1.setFixedSize(1000, 100)
        self.boton_grup2.setFixedSize(1000, 100)
        self.boton_viajes.setFixedSize(1000, 100)

        # Crear el título de la ventana
        self.texto_tutorias = QLabel("                    TUTORIAS")
        self.texto_tutorias.setAlignment(Qt.AlignCenter)
        self.texto_tutorias.setStyleSheet("""
            font: 28pt "MS Shell Dlg 2";
            color: #FFFFFF;
            margin-top: 50px;
            margin-bottom: 50px;
        """)

        # Crear el layout principal de la ventana
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.boton_grup1)
        layout_principal.addWidget(self.boton_grup2)
        layout_principal.addWidget(self.boton_viajes)
        layout_principal.addWidget(self.texto_tutorias)
        layout_principal.setAlignment(Qt.AlignCenter)

        # Configurar el widget central con el layout principal
        widget_central = QWidget()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)


        # Agregar un botón de regresar al layout
        boton_regresar = QPushButton()
        boton_regresar.setFixedSize(50,50)
        boton_regresar.setStyleSheet("border-image:url(img/anterior.png)")
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(self.texto_tutorias,alignment=Qt.AlignCenter)
        layout_horizontal.addWidget(boton_regresar, alignment=Qt.AlignRight | Qt.AlignVCenter) # Alinear el botón a la derecha y centrarlo verticalmente

        # Crear un contenedor para los botones
        contenedor_botones = QWidget()


        layout_botones = QVBoxLayout()
        layout_botones.addWidget(self.boton_grup1)
        layout_botones.addWidget(self.boton_grup2)
        layout_botones.addWidget(self.boton_viajes)
        contenedor_botones.setLayout(layout_botones)
        
        # Crear el layout principal de la ventana
        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_horizontal)
        layout_principal.addWidget(contenedor_botones)
        layout_principal.setAlignment(Qt.AlignCenter)
        # Configurar el widget central con el layout principal
        widget_central = QWidget()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

        boton_regresar.clicked.connect(self.menu_principal_docentes) # Conectar el botón a un slot para validar ingreso


        self.boton_grup1.clicked.connect(self.abrir_grupo)
        self.boton_grup2.clicked.connect(self.abrir_grupo2)
        self.boton_viajes.clicked.connect(self.mostrar_mapas)


    def mostrar_mapas(self):
        # Crear los botones
        self.boton_grup1 = QPushButton("Viaje 1 (Oaxaca-Veracruz)", self)
        self.boton_grup2 = QPushButton("Viaje 2 (Oaxaca-Cancun)", self)


        estilo_botones = """QPushButton {font: 18pt "SimSun";color: #000000;background-color: #78BDE7;border-radius: 50px;padding: 10px;margin: 10px;} QPushButton:hover { background-color: #3b83bd;}"""

        self.boton_grup1.setStyleSheet(estilo_botones)
        self.boton_grup2.setStyleSheet(estilo_botones)

        self.boton_grup1.setFixedSize(1000, 100)
        self.boton_grup2.setFixedSize(1000, 100)

        # Crear el título de la ventana
        self.texto_tutorias = QLabel("                        VIAJES")
        self.texto_tutorias.setAlignment(Qt.AlignCenter)
        self.texto_tutorias.setStyleSheet("""
            font: 28pt "MS Shell Dlg 2";
            color: #FFFFFF;
            margin-top: 50px;
            margin-bottom: 50px;
        """)

        # Crear el layout principal de la ventana
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.boton_grup1)
        layout_principal.addWidget(self.boton_grup2)
        layout_principal.addWidget(self.texto_tutorias)
        layout_principal.setAlignment(Qt.AlignCenter)

        # Configurar el widget central con el layout principal
        widget_central = QWidget()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)


        # Agregar un botón de regresar al layout
        boton_regresar = QPushButton()
        boton_regresar.setFixedSize(50,50)
        boton_regresar.setStyleSheet("border-image:url(img/anterior.png)")
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(self.texto_tutorias,alignment=Qt.AlignCenter)
        layout_horizontal.addWidget(boton_regresar, alignment=Qt.AlignRight | Qt.AlignVCenter) # Alinear el botón a la derecha y centrarlo verticalmente

        # Crear un contenedor para los botones
        contenedor_botones = QWidget()


        layout_botones = QVBoxLayout()
        layout_botones.addWidget(self.boton_grup1)
        layout_botones.addWidget(self.boton_grup2)
        contenedor_botones.setLayout(layout_botones)
        
        # Crear el layout principal de la ventana
        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_horizontal)
        layout_principal.addWidget(contenedor_botones)
        layout_principal.setAlignment(Qt.AlignCenter)
        # Configurar el widget central con el layout principal
        widget_central = QWidget()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

        boton_regresar.clicked.connect(self.abrir_ventana_tutorias) # Conectar el botón a un slot para validar ingreso
        self.boton_grup1.clicked.connect(self.mapa1) # Conectar el botón a un slot para validar ingreso
        self.boton_grup2.clicked.connect(self.mapa2) # Conectar el botón a un slot para validar ingreso


    def mapa1(self):
        dialogo = ruta1.mapa1(self)
        resultado = dialogo.exec_()

    def mapa2(self):
        dialogo = ruta2.mapa2(self)
        resultado = dialogo.exec_()


    def abrir_grupo1(self):
        self.tablaalu = QTableWidget()
        self.tablaalu.setColumnCount(4) # Número de columnas en la tabla
        self.dato_alumno = [(dat[3], dat[4], dat[5], dat[6]) for dat in self.datos_grupo1]
 

        # Agregar filas a la tabla con los datos obtenidos de la base de datos
        for fila, datos in enumerate(self.dato_alumno):
            self.tablaalu.insertRow(fila)
            for columna, dato in enumerate(datos):
                item = QTableWidgetItem(str(dato))
                self.tablaalu.setItem(fila, columna, item)    

        printer = QPrinter()
        printer.setPageSize(QPrinter.A4)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("tabla.pdf")

        documento = QTextDocument()
        font = documento.defaultFont()
        font.setPointSize(12)
        documento.setDefaultFont(font)


        cursor = QTextCursor(documento)
        encabezado = QTextTableFormat()
        encabezado.setAlignment(Qt.AlignCenter)
        encabezado.setCellPadding(4)
        encabezado.setCellSpacing(0)
        encabezado.setBorder(0)

        
        encabezado.setWidth(1600) 


        # Insertar filas y columnas en la tabla del encabezado
        tabla_encabezado = cursor.insertTable(1, 1, encabezado)
        cursor = tabla_encabezado.cellAt(0, 0).firstCursorPosition()
        cursor.insertHtml("<h1>Grupo1</h1>")
        cursor.insertHtml("<br></br>")
        cursor.insertHtml("<h2>Lista de alumnos</h2>")
        cursor.insertHtml("<br></br>")

        

        for row in range(self.tablaalu.model().rowCount()):
            cursor.insertText("\n")
            for col in range(self.tablaalu.model().columnCount()):
                cursor.insertText(str(self.tablaalu.item(row, col).text()))
                cursor.insertText(" ")
                cursor.movePosition(QTextCursor.NextCell)

        documento.print_(printer)

        file_path = os.path.abspath("tabla.pdf")
        QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))


    def abrirgrup2(self):
        self.tablaalu = QTableWidget()
        self.tablaalu.setColumnCount(4) # Número de columnas en la tabla
        self.dato_alumno = [(dat[3], dat[4], dat[5], dat[6]) for dat in self.datos_grupo2]
 

        # Agregar filas a la tabla con los datos obtenidos de la base de datos
        for fila, datos in enumerate(self.dato_alumno):
            self.tablaalu.insertRow(fila)
            for columna, dato in enumerate(datos):
                item = QTableWidgetItem(str(dato))
                self.tablaalu.setItem(fila, columna, item)    

        printer = QPrinter()
        printer.setPageSize(QPrinter.A4)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("tabla.pdf")

        documento = QTextDocument()
        font = documento.defaultFont()
        font.setPointSize(12)
        documento.setDefaultFont(font)


        cursor = QTextCursor(documento)
        encabezado = QTextTableFormat()
        encabezado.setAlignment(Qt.AlignCenter)
        encabezado.setCellPadding(4)
        encabezado.setCellSpacing(0)
        encabezado.setBorder(0)

        
        encabezado.setWidth(1600) 


        # Insertar filas y columnas en la tabla del encabezado
        tabla_encabezado = cursor.insertTable(1, 1, encabezado)
        cursor = tabla_encabezado.cellAt(0, 0).firstCursorPosition()
        cursor.insertHtml("<h1>Grupo2</h1>")
        cursor.insertHtml("<br></br>")
        cursor.insertHtml("<h2>Lista de alumnos</h2>")
        cursor.insertHtml("<br></br>")

        

        for row in range(self.tablaalu.model().rowCount()):
            cursor.insertText("\n")
            for col in range(self.tablaalu.model().columnCount()):
                cursor.insertText(str(self.tablaalu.item(row, col).text()))
                cursor.insertText(" ")
                cursor.movePosition(QTextCursor.NextCell)

        documento.print_(printer)

        file_path = os.path.abspath("tabla.pdf")
        QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))


    def cerrar_sesion(self):
        self.inicio()


    def mostrar_regresar_inicio(self):
        self.close()


if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec_()
