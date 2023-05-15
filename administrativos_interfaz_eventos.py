from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem
import administrativos_interfaz_principal

class InterfazEventos(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.initUI()

    def initUI(self):
        self.label_eventos = QLabel('Eventos de Administrativos')
        self.btnRegresarMenuAdmin = QPushButton('Volver a Menú de Administrativos')
        self.btnRegresarMenuAdmin.setStyleSheet("background-color: #4CAF50; color: #fff; padding: 10px 20px; border-radius: 5px; font-size: 16px;")
        self.btnRegresarMenuAdmin.clicked.connect(self.show_interface_menu_administrativo)

        self.table_eventos = QTableWidget()
        self.table_eventos.setColumnCount(2)
        self.table_eventos.setHorizontalHeaderLabels(['Fecha', 'Descripción'])
        self.table_eventos.setRowCount(3)
        # Poblar la tabla con los eventos
        self.table_eventos.setItem(0, 0, QTableWidgetItem('2023-05-15'))
        self.table_eventos.setItem(0, 1, QTableWidgetItem('Reunión de Administrativos'))
        self.table_eventos.setItem(1, 0, QTableWidgetItem('2023-06-01'))
        self.table_eventos.setItem(1, 1, QTableWidgetItem('Inicio del semestre'))
        self.table_eventos.setItem(2, 0, QTableWidgetItem('2023-12-15'))
        self.table_eventos.setItem(2, 1, QTableWidgetItem('Fin del semestre'))

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_eventos)
        vbox.addWidget(self.table_eventos)
        vbox.addWidget(self.btnRegresarMenuAdmin)

        self.setLayout(vbox)

    def show_interface_menu_administrativo(self):
        self.interface_administrativos = administrativos_interfaz_principal.InterfaceAdministrativos("Admin")
        self.interface_administrativos.show()
        self.hide()