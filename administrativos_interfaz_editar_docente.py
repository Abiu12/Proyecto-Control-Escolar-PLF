
from PyQt5.QtWidgets import  QFrame, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,QSpacerItem,QSizePolicy,QGridLayout,QMessageBox,QWidget, QLineEdit
from PyQt5.QtCore import Qt,QRect
from PyQt5.QtGui import QPalette, QBrush, QColor

import administrativos_conexion
import administrativos_interfaz_control_docentes

class InterfaceEditarDocente(QWidget):
    id_docente = ""
    def __init__(self,id_docente):
        super().__init__()
        self.resize(1200, 800)
        self.initUI(id_docente)
        
    def initUI(self,id_docente):
        self.id_docente = id_docente
        #Conexion para editar
        administrativos = administrativos_conexion.Administrativos()
        #Informacion del docente elegido
        datos_docente = administrativos.buscar_docente(id_docente)

        #Frame para el fondo
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 1200, 800))
        self.frame.setStyleSheet("border-image:url(img/fondo_admin.jpg)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised) 
        self.frame.setObjectName("frame")

        #Label de agregar docente
        title = QLabel("Editar docente")
        title.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        
        vbox = QVBoxLayout()

        # Layout para los campos del formulario y el titulo
        campos_layout = QGridLayout()

        #Agregamos titulo
        campos_layout.addWidget(title, 0, 1, 1, 2, Qt.AlignHCenter | Qt.AlignTop)

        #Campos del formulario
        nombre_label = QLabel("Nombre:")
        aplicar_estilo_label(nombre_label)
        self.nombre_input = QLineEdit()
        self.nombre_input.setText(datos_docente[1])
        aplicar_estilo_input(self.nombre_input)


        primer_apellido_label = QLabel("Primer apellido:")
        aplicar_estilo_label(primer_apellido_label)
        self.primer_apellido_input = QLineEdit()
        self.primer_apellido_input.setText(datos_docente[2])
        aplicar_estilo_input(self.primer_apellido_input)

        segundo_apellido_label = QLabel("Segundo apellido:")
        aplicar_estilo_label(segundo_apellido_label)
        self.segundo_apellido_input = QLineEdit()
        self.segundo_apellido_input.setText(datos_docente[3])
        aplicar_estilo_input(self.segundo_apellido_input)

        calle_label = QLabel("Calle:")
        aplicar_estilo_label(calle_label)
        self.calle_input = QLineEdit()
        self.calle_input.setText(datos_docente[4])
        aplicar_estilo_input(self.calle_input)

        numero_label = QLabel("Número:")
        aplicar_estilo_label(numero_label)
        self.numero_input = QLineEdit()
        self.numero_input.setText(datos_docente[5])
        aplicar_estilo_input(self.numero_input)
        
        colonia_label = QLabel("Colonia:")
        aplicar_estilo_label(colonia_label)
        self.colonia_input = QLineEdit()
        self.colonia_input.setText(datos_docente[6])
        aplicar_estilo_input(self.colonia_input)
        
        municipio_label = QLabel("Municipio:")
        aplicar_estilo_label(municipio_label)
        self.municipio_input = QLineEdit()
        self.municipio_input.setText(datos_docente[7])
        aplicar_estilo_input(self.municipio_input)
        
        telefono_label = QLabel("Telefono:")
        aplicar_estilo_label(telefono_label)
        self.telefono_input = QLineEdit()
        self.telefono_input.setText(datos_docente[8])
        aplicar_estilo_input(self.telefono_input)
        
        numero_imss_label = QLabel("Numero IMSS:")
        aplicar_estilo_label(numero_imss_label)
        self.numero_imss_input = QLineEdit()
        self.numero_imss_input.setText(datos_docente[9])
        aplicar_estilo_input(self.numero_imss_input)
        
        ine_label = QLabel("Ine:")
        aplicar_estilo_label(ine_label)
        self.ine_input = QLineEdit()
        self.ine_input.setText(datos_docente[10])
        aplicar_estilo_input(self.ine_input)
        
        curp_label = QLabel("Curp:")
        aplicar_estilo_label(curp_label)
        self.curp_input = QLineEdit()
        self.curp_input.setText(datos_docente[11])
        aplicar_estilo_input(self.curp_input)
        
        rfc_label = QLabel("Rfc:")
        aplicar_estilo_label(rfc_label)
        self.rfc_input = QLineEdit()
        self.rfc_input.setText(datos_docente[12])
        aplicar_estilo_input(self.rfc_input)
        
        nombre_madre_label = QLabel("Nombre madre:")
        aplicar_estilo_label(nombre_madre_label)
        self.nombre_madre_input = QLineEdit()
        self.nombre_madre_input.setText(datos_docente[13])
        aplicar_estilo_input(self.nombre_madre_input)
        
        telefono_madre_label = QLabel("Teléfono madre:")
        aplicar_estilo_label(telefono_madre_label)
        self.telefono_madre_input = QLineEdit()
        self.telefono_madre_input.setText(datos_docente[14])
        aplicar_estilo_input(self.telefono_madre_input)
        
        nombre_padre_label = QLabel("Nombre padre:")
        aplicar_estilo_label(nombre_padre_label)
        self.nombre_padre_input = QLineEdit()
        self.nombre_padre_input.setText(datos_docente[15])
        aplicar_estilo_input(self.nombre_padre_input)
        
        telefono_padre_label = QLabel("Teléfono padre:")
        aplicar_estilo_label(telefono_padre_label)
        self.telefono_padre_input = QLineEdit()
        self.telefono_padre_input.setText(datos_docente[16])
        aplicar_estilo_input(self.telefono_padre_input)
        
        #Botón para guardar los datos
        guardar_btn = QPushButton("Editar datos")
        aplicar_estilo_guardar(guardar_btn,"#FF5733")
        guardar_btn.clicked.connect(self.editar_datos_docente)

        #Boton para regresar a control estudiantes
        self.btnRegresarMenuAdmin = QPushButton('Volver a Control de estudiantes')
        aplicar_estilo_volver(self.btnRegresarMenuAdmin,"#FF5733")
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

    def show_interface_control_docente(self):
        self.interface_control_docente = administrativos_interfaz_control_docentes.InterfazControlDocentes()
        self.interface_control_docente.show()
        self.close()
    
    def editar_datos_docente(self):
        administrativos = administrativos_conexion.Administrativos() #Conexion con administrativos
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

        if(nombre == "" or primer_apellido == "" or segundo_apellido == "" or calle == "" or numero == "" or colonia == "" or municipio == "" or telefono == "" or numero_imss == "" or ine == "" or curp == "" or rfc == "" ):
            QMessageBox.critical(self, "Error", "Rellene todos los campos")
            return
        resultado = administrativos.editar_docente(nombre,primer_apellido,segundo_apellido,calle,numero,colonia,municipio,telefono,numero_imss,ine,curp,rfc,self.id_docente)
        if resultado:
            QMessageBox.information(self, "Éxito", "Docente editado correctamente")
            self.interface_control_docente = administrativos_interfaz_control_docentes.InterfazControlDocentes()
            self.interface_control_estudiante.show()
            self.close()
        else:
            QMessageBox.critical(self, "Error", "No se pudo editar el docente")

def aplicar_estilo_label(label):
    label.setStyleSheet("QLabel { font-size: 21px; font-weight: ;  margin-right: 10px; }")

def aplicar_estilo_input(input):
    input.setStyleSheet("QLineEdit { min-height: 35px; border: 3px solid #FF5733; border-radius: 13px; }")

def aplicar_estilo_guardar(boton,color):
    style = f"""
    QPushButton {{
        font: 11pt;
        background-color: {color};
        border-radius: 25px;
        padding: 10px 20px;
        min-width: 100;
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
        min-width: 320px;
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