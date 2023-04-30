
from PyQt5.QtWidgets import  QWidget, QVBoxLayout,  QLabel, QPushButton, QWidget

from administrativos_interfaz_principal import InterfaceAdministrativos
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
