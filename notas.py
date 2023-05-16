
from PyQt5.QtWidgets import QVBoxLayout,QPushButton, QDialog, QTextEdit
class NotasDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Agregar reporte de la reunión")
        self.resize(300, 150)

        # Crear un QLineEdit para ingresar la nota
        self.nota_edit = QTextEdit()
        self.nota_edit.setPlaceholderText("Ingrese su reporte")

        # Crear dos botones: Guardar y Cancelar
        self.guardar_button = QPushButton("Guardar")
        self.cancelar_button = QPushButton("Cancelar")

        # Crear un QVBoxLayout para los widgets
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.nota_edit)
        layout_vertical.addWidget(self.guardar_button)
        layout_vertical.addWidget(self.cancelar_button)



        # Establecer el QVBoxLayout como el layout de la ventana
        self.setLayout(layout_vertical)

        # Conectar la señal clicked de los botones a sus respectivos slots
        self.guardar_button.clicked.connect(self.accept)
        self.cancelar_button.clicked.connect(self.reject)
        