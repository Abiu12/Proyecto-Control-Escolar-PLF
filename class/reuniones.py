from PyQt5.QtWidgets import QMainWindow,QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import principal

# Clase ventana Principal que hereda de la clase QMainWindow
class ventanaReuniones(QMainWindow):
    def __init__(self):
        super().__init__()
        # Titulo de la ventana
        self.setWindowTitle("Ventana reuniones")
        self.setFixedSize(1300, 700)
        self.setGeometry(QtCore.QRect(0, 0, 1300, 800))
        self.setStyleSheet("border-image:url(img/fondo.png)")

        # Centrar ventana en la pantalla
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.centralWidget()

        self.boton_volver = QtWidgets.QPushButton(self)
        self.boton_volver.setGeometry(QtCore.QRect(1200, 20, 70, 50))
        self.boton_volver.setStyleSheet("border-image:url(img/regreso.png)")
        self.boton_volver.setText("")
        self.boton_volver.setObjectName("volver")
        self.boton_volver.clicked.connect(self.volver)


   
#Funcion para volver a la ventana principal. O sea esta.
    def volver(self):
        # Crea una instancia de la ventana principal y la muestra
        self.ventana_principal = principal.VentanaPrincipal()
        self.ventana_principal.show()
        self.close()
      