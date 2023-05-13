from PyQt5.QtWidgets import  QFrame,QWidget, QTextEdit,QVBoxLayout, QHBoxLayout, QLabel, QPushButton,QWidget
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPalette, QBrush, QColor, QIcon
from administrativos_conexion import Administrativos
import administrativos_interfaz_control_alumnos
import administrativos_interfaz_editar_alumno

class InterfazVerReporteAlumno(QWidget):
    id_alumno = "" #Variable para tener el id del alumno
    id_reporte = ""
    def __init__(self,idAlumno,nombre_sesion):
        self.nombre_sesion = nombre_sesion
        super().__init__()
        self.resize(1200, 800)
        self.initUI(idAlumno)
           
    def initUI(self, idAlumno):
        self.id_alumno = idAlumno #Variable global
        administrativos = Administrativos()
        reporte = administrativos.buscar_notificacion_reporte(idAlumno)
        alumno = administrativos.buscar_alumno(idAlumno)
        self.id_reporte = reporte[0]

        #Label de alumnos
        title = QLabel(f"Reporte generado por  {alumno[1]} {alumno[2]}")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")

        #Diseño del FRAME
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 1300, 800))
        self.frame.setStyleSheet("border-image:url(img/fondo_admin.jpg)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised) 
        self.frame.setObjectName("frame")
    

        # Cuadro de texto para el reporte
        self.reporteTextEdit = QTextEdit()
        self.reporteTextEdit.setReadOnly(True)
        self.reporteTextEdit.setStyleSheet("QTextEdit { background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e6e6e6, stop:1 #ffffff);"
                                 "border: 1px solid #cccccc; border-radius: 5px; font-size: 18pt ; padding: 5px; }")
        self.reporteTextEdit.setPlaceholderText(reporte[1])

        #Boton para regresar a control estudiantes
        self.btn_corregir_datos = QPushButton('Corregir datos')
        aplicar_estilo_corregir(self.btn_corregir_datos,"#FF5733")
        self.btn_corregir_datos.clicked.connect(self.show_interface_editar_alumno)

        #Boton para regresar a control estudiantes
        self.btnRegresarMenuAdmin = QPushButton()
        icono_regresar = QIcon('img/flecha-izquierda.png')
        self.btnRegresarMenuAdmin.setIcon(icono_regresar)
        aplicar_estilo_volver(self.btnRegresarMenuAdmin,"#FF5733")
        self.btnRegresarMenuAdmin.clicked.connect(self.show_interface_control_estudiante)

        vbox = QVBoxLayout()

        hbox_layout = QHBoxLayout()
        hbox_layout.addStretch(1)
        hbox_layout.addWidget(self.btn_corregir_datos)
        hbox_layout.addWidget(self.btnRegresarMenuAdmin)
        vbox.addWidget(title)
        vbox.addWidget(self.reporteTextEdit) # Agregar el QTextEdit al layout
        vbox.addLayout(hbox_layout)        
        self.setLayout(vbox)

    def show_interface_control_estudiante(self):
        self.interface_control_estudiante = administrativos_interfaz_control_alumnos.InterfazControlAlumnos(self.nombre_sesion)
        self.interface_control_estudiante.show()
        self.close()
    def show_interface_editar_alumno(self):
        #Obtenemos el id del alumno para traer sus datos
        self.interface_editar_alumno = administrativos_interfaz_editar_alumno.InterfaceEditarAlumno(self.id_alumno,self.id_reporte,self.nombre_sesion)
        self.interface_editar_alumno.show()
        self.close()
    
def aplicar_estilo_corregir(boton,color):
    style = f"""
    QPushButton {{
        font: 11pt;
        background-color: {color};
        border-radius: 25px;
        padding: 10px 20px;
        min-width: 200px;
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
    