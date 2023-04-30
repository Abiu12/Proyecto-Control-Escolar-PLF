from PyQt5.QtWidgets import  QFrame,QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,QDialog,QFormLayout,QMessageBox,QWidget, QFileDialog, QComboBox
from administrativos_conexion import Administrativos
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPalette, QBrush, QColor

import administrativos_interfaz_documentacion_docente

class InterfazAgregarDocumentacionDocente(QWidget):
    id_docente = "" #Variable para tener el id del docente
    def __init__(self,id_docente):
        super().__init__()
        self.resize(1200, 800)
        self.initUI(id_docente)
           
    def initUI(self, id_docente):

        #Diseño del FRAME
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 1300, 800))
        self.frame.setStyleSheet("border-image:url(img/fondo_admin.jpg)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised) 
        self.frame.setObjectName("frame")
    
        self.id_docente = id_docente

        #Label de Documentacion de docente X
        title = QLabel("Agregar documentación al docente")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 100px;")

        #Formulario para almacenar los datos
        form_layout_documento = QFormLayout()

        form_layout_documento.addRow(title)
        
        #Campo de tipo de documento 
        tipo_documento_label = QLabel("Tipo de documento:")
        tipo_documento_label.setStyleSheet("font-size: 20px;  margin-bottom: 100px;")
        self.tipo_documento_combo = QComboBox()
        self.tipo_documento_combo.addItems(["Titulo",
                                            "Cédula profesional",
                                            "CURP",
                                            "Acta de nacimiento"])
        self.tipo_documento_combo.setStyleSheet("QComboBox {font-size: 18px; background-color: #FF5733; min-height: 50px ;  border-radius: 40px; font-weight: }" "QComboBox:hover { background-color: #FF8C00; border-radius: 40px}" )
        form_layout_documento.addRow(tipo_documento_label, self.tipo_documento_combo)

        # Campo para cargar archivo PDF
        archivo_pdf_label = QLabel("Archivo PDF:")
        comodin_label = QLabel(" ")
        archivo_pdf_label.setStyleSheet("font-size: 20px;  margin-bottom: 50px;")
        archivo_btn = QPushButton("Seleccionar archivo...")
        archivo_btn.clicked.connect(self.cargar_archivo)
        self.archivo_label = QLabel("Ningún archivo seleccionado")
        self.archivo_label.setStyleSheet("font-size: 16px;")
        aplicar_estilo_seleccionar(archivo_btn,"#FF5733")
        form_layout_documento.addRow(archivo_pdf_label, archivo_btn)
        form_layout_documento.addRow(comodin_label,self.archivo_label)

        #Botón para guardar los datos
        btn_guardar_documento = QPushButton("Guardar")
        aplicar_estilo_guardar(btn_guardar_documento,"#FF5733")
        btn_guardar_documento.clicked.connect(self.insertar_documento)

        #Boton para regresar a documentacion docente
        self.btn_regresar_documentacion_docente = QPushButton('Volver a documentación del docente')
        aplicar_estilo_volver(self.btn_regresar_documentacion_docente,"#FF5733")
        self.btn_regresar_documentacion_docente.clicked.connect(self.show_interface_documentacion_docente)


        vbox = QVBoxLayout()
        # vbox.addWidget(title)

        # Agregar formulario al layout vertical
        vbox.addLayout(form_layout_documento)

        #Layout de botones
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(btn_guardar_documento)
        button_layout.addWidget(self.btn_regresar_documentacion_docente)
        
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

    def show_interface_documentacion_docente(self):
        self.interface_documentacion_docente = administrativos_interfaz_documentacion_docente.InterfaceDocumentacionDocente(self.id_docente)
        self.interface_documentacion_docente.show()
        self.close()
    
    def insertar_documento(self):
        if(self.archivo_label.text() == "Ningún archivo seleccionado"):
            QMessageBox.critical(self, "Error", "No se ha elegido ningún archivo")
            return
        administrativos = Administrativos() #Conexion con administrativos
        archivo_elegido = str(self.archivo_path)
        #INSERTAMOS UN ARCHIVO
        with open(archivo_elegido, "rb") as f:
            archivo_bytes = f.read()
            resultado = administrativos.inserta_documento_docente(self.tipo_documento_combo.currentText(),archivo_bytes,self.id_docente)
            if resultado:
                QMessageBox.information(self, "Éxito", "Documento agregado correctamente")
                self.interface_documentacion_docente = administrativos_interfaz_documentacion_docente.InterfaceDocumentacionDocente(self.id_docente)
                self.interface_documentacion_docente.show()
                self.close()
            else:
                QMessageBox.critical(self, "Error", "No se pudo agregar el documento")

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
        min-width: 350px;
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
    