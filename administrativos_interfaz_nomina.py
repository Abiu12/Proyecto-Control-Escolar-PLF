
from PyQt5.QtWidgets import  QFrame,QComboBox,QHBoxLayout,QWidget, QVBoxLayout,  QLabel, QPushButton, QWidget, QTableWidgetItem,QAbstractItemView,QTableWidget
from PyQt5.QtGui import QPalette, QBrush, QColor,QIcon 
from PyQt5.QtCore import Qt, QRect

import administrativos_interfaz_principal
import administrativos_interfaz_nomina_docentes_base
import administrativos_interfaz_nomina_docentes_honorarios
import administrativos_interfaz_nomina_administrativos_base
import administrativos_interfaz_nomina_administrativos_honorarios

class InterfazNomina(QWidget):
    def __init__(self,nombre_sesion):
        self.nombre_sesion = nombre_sesion
        super().__init__()
        self.resize(1200, 800)
        self.initUI()

    def initUI(self):
        #Diseño del FRAME
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 1200, 800))
        self.frame.setStyleSheet("border-image:url(img/fondo_admin.jpg)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised) 
        self.frame.setObjectName("frame")

        #Label de alumnos
        title = QLabel("Seleccion de nómina")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")


        #Boton de consultar
        self.boton_consultar = QPushButton("Consultar")
        aplicar_estilo_consultar(self.boton_consultar,"#FF5733")
        self.boton_consultar.clicked.connect(self.show_interfaz_nomina)

        #Boton de regreso
        self.btnRegresarMenuAdmin = QPushButton()
        icono_regresar = QIcon('img/flecha-izquierda.png')
        self.btnRegresarMenuAdmin.setIcon(icono_regresar)
        aplicar_estilo_volver(self.btnRegresarMenuAdmin,"#FF5733")
        self.btnRegresarMenuAdmin.clicked.connect(self.show_interface_menu_administrativo)
        

        # Crear los QComboBox para las opciones
        self.combo_tipo_trabajador = QComboBox()
        self.combo_tipo_trabajador.setStyleSheet("QComboBox { font-size: 16px; min-height: 35px; border: 3px solid #FF5733; border-radius: 13px; }")
        self.combo_tipo_trabajador.addItems(["Docentes", "Administrativos"])

        self.combo_tipo_contrato = QComboBox()
        self.combo_tipo_contrato.setStyleSheet("QComboBox { font-size: 16px; min-height: 35px; border: 3px solid #FF5733; border-radius: 13px; }")
        self.combo_tipo_contrato.addItems(["Base", "Honorarios"])


        # Layout de las opciones
        options_layout = QHBoxLayout()
        options_layout.setContentsMargins(0, 300, 0, 330)
        tipo_trabajador = QLabel("Tipo de trabajador:")
        tipo_trabajador.setStyleSheet("font-size: 20px;  ")
        options_layout.addWidget(tipo_trabajador)
        options_layout.addWidget(self.combo_tipo_trabajador)

        tipo_contrato = QLabel("Tipo de contrato:")
        tipo_contrato.setStyleSheet("font-size: 20px;  ")

        options_layout.addWidget(tipo_contrato)
        options_layout.addWidget(self.combo_tipo_contrato)
        
        #Layout de botones
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.boton_consultar)
        button_layout.addWidget(self.btnRegresarMenuAdmin)
        
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignTop)
        # vbox.setContentsMargins(0, 100, 0, 100)
        vbox.addWidget(title)
        vbox.addLayout(options_layout)
        vbox.addLayout(button_layout)
        
        self.setLayout(vbox)

    
        

    def show_interfaz_nomina(self):
        if(self.combo_tipo_trabajador.currentText() == "Docentes" and self.combo_tipo_contrato.currentText() == "Base" ):
            self.interface_nomina_docente_base = administrativos_interfaz_nomina_docentes_base.InterfazNominaDocentesBase(self.nombre_sesion)
            self.interface_nomina_docente_base.show()
            self.close()
        if(self.combo_tipo_trabajador.currentText() == "Docentes" and self.combo_tipo_contrato.currentText() == "Honorarios" ):
            self.interface_nomina_docente_honorarios = administrativos_interfaz_nomina_docentes_honorarios.InterfazNominaDocentesHonorarios(self.nombre_sesion)
            self.interface_nomina_docente_honorarios.show()
            self.close()
            pass
        if(self.combo_tipo_trabajador.currentText() == "Administrativos" and self.combo_tipo_contrato.currentText() == "Base" ):
            self.interface_nomina_administrativo_base = administrativos_interfaz_nomina_administrativos_base.InterfazNominaAdministrativosBase(self.nombre_sesion)
            self.interface_nomina_administrativo_base.show()
            self.close()
        if(self.combo_tipo_trabajador.currentText() == "Administrativos" and self.combo_tipo_contrato.currentText() == "Honorarios" ):
            self.interface_nomina_administrativos_honorarios = administrativos_interfaz_nomina_administrativos_honorarios.InterfazNominaAdministrativosHonorarios(self.nombre_sesion)
            self.interface_nomina_administrativos_honorarios.show()
            self.close()
            pass



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
    

def aplicar_estilo_consultar(boton,color):
    style = f"""
    QPushButton {{
        font: 11pt;
        background-color: {color};
        border-radius: 25px;
        padding: 10px 20px;
        min-width: 100px;
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