from PyQt5.QtWidgets import  QFrame,QWidget, QMessageBox, QTextEdit,QVBoxLayout, QHBoxLayout, QLabel, QPushButton,QWidget
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPalette, QBrush, QColor, QIcon
from administrativos_conexion import Administrativos
import administrativos_interfaz_control_alumnos
import administrativos_interfaz_editar_alumno

class InterfazVerReporteBajaAlumno(QWidget):
    id_alumno = "" #Variable para tener el id del alumno
    id_reporte = ""
    def __init__(self,idAlumno):
        super().__init__()
        self.resize(1200, 800)
        self.initUI(idAlumno)
           
    def initUI(self, idAlumno):
        self.id_alumno = idAlumno #Variable global
        administrativos = Administrativos()
        reporte = administrativos.buscar_notificacion_baja(idAlumno)
        alumno = administrativos.buscar_alumno(idAlumno)
        self.id_reporte = reporte[0]

        #Label de alumnos
        title = QLabel(f"Reporte de baja generado por  {alumno[1]} {alumno[2]}")
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
        self.reporteTextEdit.setStyleSheet("font-size: 18pt")
        self.reporteTextEdit.setPlaceholderText(reporte[1])

        #Boton para eliminar
        self.btn_eliminar_alumno = QPushButton('Dar de baja alumno')
        aplicar_estilo_corregir(self.btn_eliminar_alumno,"#FF5733")
        self.btn_eliminar_alumno.clicked.connect(self.eliminar_alumno)

        #Boton para regresar a control estudiantes
        self.btnRegresarMenuAdmin = QPushButton()
        icono_regresar = QIcon('img/flecha-izquierda.png')
        self.btnRegresarMenuAdmin.setIcon(icono_regresar)
        aplicar_estilo_volver(self.btnRegresarMenuAdmin,"#FF5733")
        self.btnRegresarMenuAdmin.clicked.connect(self.show_interface_control_estudiante)

        vbox = QVBoxLayout()

        hbox_layout = QHBoxLayout()
        hbox_layout.addStretch(1)
        hbox_layout.addWidget(self.btn_eliminar_alumno)
        hbox_layout.addWidget(self.btnRegresarMenuAdmin)
        vbox.addWidget(title)
        vbox.addWidget(self.reporteTextEdit) # Agregar el QTextEdit al layout
        vbox.addLayout(hbox_layout)        
        self.setLayout(vbox)

    def show_interface_control_estudiante(self):
        self.interface_control_estudiante = administrativos_interfaz_control_alumnos.InterfazControlAlumnos()
        self.interface_control_estudiante.show()
        self.close()
    
    def eliminar_alumno(self):
        administrativos = Administrativos()
        # Agregar cuadro de mensaje de confirmación
        mensaje_box = QMessageBox()
        mensaje_box.setWindowTitle("Confirmación")
        mensaje_box.setText("¿Está seguro de que desea dar de baja a este alumno?")
        mensaje_box.setIcon(QMessageBox.Warning)
        mensaje_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resultado = mensaje_box.exec_()

        if resultado == QMessageBox.Yes:
            administrativos.elimina_alumno(self.id_alumno)
            self.interface_control_estudiante = administrativos_interfaz_control_alumnos.InterfazControlAlumnos()
            self.interface_control_estudiante.show()
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
    