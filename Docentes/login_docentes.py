
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QFrame, QLabel, QLineEdit, QPushButton, QApplication, QMessageBox,QGridLayout,QHBoxLayout,QTableWidget, QTableWidgetItem,QHeaderView,QDialog
from PyQt5.QtCore import Qt,QUrl
from PyQt5.QtGui import QDesktopServices,QPalette,QColor,QIcon
import rutas,conexion,notas

#VENTANA PRUEBA DE INICIO DE SESIÓN:

class LoginWindow(QMainWindow):

    def __init__(self):

        super(LoginWindow, self).__init__()
        # Configurar ventana principal

        self.setWindowTitle("Inicio de sesión")
        self.setFixedSize(1250, 730) # Tamaño fijo de la ventana
        self.setCentralWidget(QWidget()) # Widget central de la ventana
        self.centralWidget().setLayout(QVBoxLayout()) # Diseño vertical para el widget central
        self.centralWidget().layout().setAlignment(Qt.AlignCenter) # Centrar el widget central

        # Crear el marco
        frame = QFrame()
        frame.setFixedWidth(300) # Ancho fijo del marco
        frame.setLayout(QVBoxLayout()) # Diseño vertical para el marco

        # Crear etiquetas, campos de texto y botón
        label_usuario = QLabel("Usuario:")
        frame.layout().addWidget(label_usuario)

        self.edit_usuario = QLineEdit() # Cambiar a self.edit_usuario para que sea accesible en todo el objeto
        frame.layout().addWidget(self.edit_usuario)

        label_contrasena = QLabel("Contraseña:")
        frame.layout().addWidget(label_contrasena)

        self.edit_contrasena = QLineEdit() # Cambiar a self.edit_contrasena para que sea accesible en todo el objeto
        self.edit_contrasena.setEchoMode(QLineEdit.Password) # Ocultar caracteres de la contraseña

        frame.layout().addWidget(self.edit_contrasena)

        button_ingresar = QPushButton("Ingresar")
        button_ingresar.clicked.connect(self.inicio_sesion) # Conectar el botón a un slot para validar ingreso


        frame.layout().addWidget(button_ingresar)

        # Agregar el marco al widget central
        self.centralWidget().layout().addWidget(frame)
   
    #PRINCIPAL DOCENTES:
    def menu_principal_docentes(self):
       
        
        self.boton_tutorias = QPushButton(self)
        self.boton_tutorias.setFixedSize(1100, 100)
        self.boton_tutorias.setStyleSheet("QPushButton {font: 15pt \"SimSun\"; background-color: #78BDE7; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #3b83bd ; border-top-left-radius: 50px; font-weight: bold}" )

        self.boton_asesorias = QPushButton(self)
        self.boton_asesorias.setFixedSize(1100, 100)
        self.boton_asesorias.setStyleSheet("QPushButton {font: 15pt \"SimSun\"; background-color: #78BDE7; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #3b83bd; border-top-left-radius: 50px; font-weight: bold}" )


        self.boton_actividades = QPushButton(self)
        self.boton_actividades.setFixedSize(1100, 100)
        self.boton_actividades.setStyleSheet("QPushButton {font: 15pt \"SimSun\"; background-color:#78BDE7; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #3b83bd; border-top-left-radius: 50px; font-weight: bold}" )


        self.boton_reuniones = QPushButton(self)
        self.boton_reuniones.setFixedSize(1100, 100)
        self.boton_reuniones.setStyleSheet("QPushButton {font: 15pt \"SimSun\"; background-color: #78BDE7; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #3b83bd; border-top-left-radius: 50px; font-weight: bold}" )


        self.boton_clases = QPushButton(self)
        self.boton_clases.setFixedSize(1100, 100)
        self.boton_clases.setStyleSheet("QPushButton {font: 15pt \"SimSun\"; background-color: #78BDE7; border-top-left-radius: 50px; font-weight: bold}" "QPushButton:hover {font: 17pt \"SimSun\"; background-color: #3b83bd; border-top-left-radius: 50px; font-weight: bold}" )


        self.image = QLabel()
        self.image.setFixedSize(100,100)
        self.image.setStyleSheet("border-image:url(img/usu.png)")


        #Diseño del texto principal
        self.texto_principal = QLabel(self)
        self.texto_principal.setFixedSize(1600,71)
        self.texto_principal.setStyleSheet("font: bold 24pt \"Segoe UI\";")
        self.texto_principal.setObjectName("texto_principal")

        self.boton_asesorias.raise_()
        self.boton_actividades.raise_()
        self.boton_reuniones.raise_()
        self.boton_clases.raise_()
        self.boton_tutorias.raise_()

        #Aqui se le da una función al boton, que será
        self.boton_asesorias.clicked.connect(self.abrir_ventana_asesorias)
        self.boton_actividades.clicked.connect(self.abrir_ventana_actividades)
        self.boton_clases.clicked.connect(self.abrir_ventana_clases)
        self.boton_reuniones.clicked.connect(self.abrir_ventana_reuniones)
        self.boton_tutorias.clicked.connect(self.abrir_ventana_tutorias)

        _translate = QApplication.translate
        self.boton_clases.setText(_translate("Form", "Clases"))
        self.boton_tutorias.setText(_translate("Form", "Tutorias"))
        self.boton_asesorias.setText(_translate("Form", "Asesorias"))
        self.boton_actividades.setText(_translate("Form", "Actividades universidad"))
        self.boton_reuniones.setText(_translate("Form", "Reuniones académicas"))
        self.texto_principal.setText(_translate("Form", "                     ¡Bienvenido al sistema "+ self.datos[1]+'!'))


         # Crear un layout vertical y agregar la tabla a este layout
        layout = QGridLayout()
        
        layout.addWidget(self.image,2,3,alignment=Qt.AlignCenter)
        layout.addWidget(self.boton_tutorias,3,3,alignment=Qt.AlignCenter)
        layout.addWidget(self.boton_actividades,4,3,alignment=Qt.AlignCenter)
        layout.addWidget(self.boton_asesorias,5,3,alignment=Qt.AlignCenter)
        layout.addWidget(self.boton_clases,6,3,alignment=Qt.AlignCenter)
        layout.addWidget(self.boton_reuniones,7,3,alignment=Qt.AlignCenter)
        layout.addWidget(self.texto_principal,1,3,alignment=Qt.AlignCenter)

        # Configurar el widget central con el layout
        widget_central = QWidget()
        widget_central.setLayout(layout)
        self.setCentralWidget(widget_central)

#mETODOS
#metodo para iniciar sesion:
    def inicio_sesion(self):
        self.usuario = self.edit_usuario.text()
        self.contrasena = self.edit_contrasena.text()
        cnn=conexion.Conexion_BD.establecer_conexion('baqafswarxtmfft3blx4')
        with cnn.cursor() as cur:
            cur.execute("SELECT * FROM usuario WHERE usuario = %s AND pass = %s", (self.usuario, self.contrasena))
            self.datos = cur.fetchone()
        if self.datos is not None:
                QMessageBox.information(self, "Inicio de sesión", "Inicio de sesión exitoso")
                self.menu_principal_docentes()
        else:
            QMessageBox.warning(self, "Inicio de sesión", "Usuario y/o contraseña incorrecto")
        cnn.close()

#metodo para consultar datos de las asesorias:
    def consulta_datos_asesoria(self):
     cnn=conexion.Conexion_BD.establecer_conexion('baqafswarxtmfft3blx4')   
     with cnn.cursor() as cur:
        cur.execute("SELECT * FROM asesoria WHERE id_usuario = %s",[self.datos[0]])
        self.datos_asesorias = cur.fetchall()
        self.mostrar_datos_asesorias()

#metodo para consultar datos de las actividades:
    def consulta_datos_actividad(self):
        cnn=conexion.Conexion_BD.establecer_conexion('baqafswarxtmfft3blx4')
        with cnn.cursor() as cur: 
             cur.execute("SELECT * FROM actividades")
             self.datos_actividades = cur.fetchall()
             self.mostrar_datos_actividades()
        cnn.close()


#metodo para consultar datos de las clases:
    def consulta_datos_clases(self):
        cnn=conexion.Conexion_BD.establecer_conexion('baqafswarxtmfft3blx4')
        with cnn.cursor() as cur: 
             cur.execute("SELECT * FROM clases")
             self.datos_clases = cur.fetchall()
             self.mostrar_datos_clases()
        cnn.close()



#metodo para consultar datos de las clases:
    def consulta_datos_reuniones(self):
        cnn=conexion.Conexion_BD.establecer_conexion('baqafswarxtmfft3blx4')
        with cnn.cursor() as cur: 
             cur.execute("SELECT * FROM reuniones")
             self.datos_reuniones = cur.fetchall()
             self.mostrar_datos_reuniones()
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

#metodo para mostrar los datos de las asesorias

    def mostrar_datos_asesorias(self):
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(3) # Número de columnas en la tabla
        self.tabla.setHorizontalHeaderLabels(["Nombre materia", "Horario", "Lugar"]) # Etiquetas de las columnas       
        
        
         # Crear una nueva lista de tuplas sin el primer elemento 
        self.datos_sin_primero = [(datos[1], datos[2], datos[3]) for datos in self.datos_asesorias]


        # Agregar filas a la tabla con los datos obtenidos de la base de datos
        print(self.datos_asesorias)
        for fila, datos in enumerate(self.datos_sin_primero):
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
        texto_principal = QLabel("                          HORARIO DE ASESORIAS")
        texto_principal.setAlignment(Qt.AlignCenter) # Centrar el texto
        texto_principal.setStyleSheet("font: bold 22pt \"MS Shell Dlg 2\"; color: #5d9b9b;")
        
        

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
        texto_principal.setStyleSheet("font: bold 22pt \"MS Shell Dlg 2\"; color: #5d9b9b;")
        

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
        self.tabla.setColumnCount(3) # Número de columnas en la tabla
        self.tabla.setHorizontalHeaderLabels(["Fecha", "Actividad", "Departamento"]) # Etiquetas de las columnas

        # Agregar filas a la tabla con los datos obtenidos de la base de datos
        for fila, datos in enumerate(self.datos_clases):
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
        texto_principal = QLabel("                            HORARIO DE CLASES")
        texto_principal.setAlignment(Qt.AlignCenter) # Centrar el texto
        texto_principal.setStyleSheet("font: bold 22pt \"MS Shell Dlg 2\"; color: #5d9b9b;")
        

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






    def mostrar_datos_reuniones(self):
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(2) # Número de columnas en la tabla
        self.tabla.setHorizontalHeaderLabels(["Fecha", "Notas"]) # Etiquetas de las columnas

        # Agregar filas a la tabla con los datos obtenidos de la base de datos
        for fila, datos in enumerate(self.datos_reuniones):
            self.tabla.insertRow(fila)

            for columna, dato in enumerate(datos):
                item = QTableWidgetItem(str(dato))
                self.tabla.setItem(fila, 0, item)

                nota_item = QTableWidgetItem()
                nota_icon = QIcon("img/nota.png") # Reemplaza "ruta/a/tu/icono/nota.png" con la ruta a tu imagen de la nota
                nota_item.setData(Qt.DecorationRole, nota_icon)
                self.tabla.setItem(fila, 1, nota_item)


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
        texto_principal.setStyleSheet("font: bold 22pt \"MS Shell Dlg 2\"; color: #5d9b9b;")
        

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
                        nota = dialogo.nota_edit.text()
                        # Guardar la nota en la base de datos o hacer cualquier otra cosa que necesites


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
            color: #5d9b9b;
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
        contenedor_botones.setStyleSheet("""
            background-color: #FFF;
            border-radius: 25px;
            padding: 50px;
            margin: 50px;
        """)

        
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
        self.boton_grup1.clicked.connect(self.mostrar_pdf)
        self.boton_viajes.clicked.connect(self.mostrar_mapas)

    def mostrar_mapas(self):
        dialogo = rutas.mapa(self)
        resultado = dialogo.exec_()

    def mostrar_pdf(self):
            # Ruta del archivo PDF
            ruta_pdf = "pdf/Libro1.pdf"
            # Abre el archivo PDF en el visor de PDF predeterminado del sistema
            QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_pdf))

           

if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec_()
