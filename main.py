import sys
import folium
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from alumnos_conexion import Alumnos

class Interface1(QWidget):

    paises = Alumnos()

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.label1 = QLabel('Interfaz 1')
        self.button1 = QPushButton('Alumnos')
        self.button2 = QPushButton('Docentes')
        self.button3 = QPushButton('Administrativos')
        self.button4 = QPushButton('Mostrar Ruta')
        self.button1.clicked.connect(self.show_alumnos)
        self.button2.clicked.connect(self.show_docentes)
        self.button3.clicked.connect(self.show_administrativos)
        self.button4.clicked.connect(self.show_mapa)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        vbox.addWidget(self.button3)
        vbox.addWidget(self.button4)

        self.setLayout(vbox)

    def show_alumnos(self):
        print(self.paises)
        # self.interface_alumnos = InterfaceAlumnos()
        # self.interface_alumnos.show()
        # self.hide()

    def show_docentes(self):
        self.interface_docentes = InterfaceDocentes()
        self.interface_docentes.show()
        self.hide()

    def show_administrativos(self):
        self.interface_administrativos = InterfaceAdministrativos()
        self.interface_administrativos.show()
        self.hide()

    def show_mapa(self):
        self.mapa = Mapa()
        self.mapa.show()
        self.hide()


class InterfaceAlumnos(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label_alumnos = QLabel('Interfaz Alumnos')
        self.button_back = QPushButton('Volver a Interfaz 1')
        self.button_back.clicked.connect(self.show_interface1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_alumnos)
        vbox.addWidget(self.button_back)

        self.setLayout(vbox)

    def show_interface1(self):
        self.interface1 = Interface1()
        self.interface1.show()
        self.hide()


class InterfaceDocentes(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label_docentes = QLabel('Interfaz Docentes')
        self.button_back = QPushButton('Volver a Interfaz 1')
        self.button_back.clicked.connect(self.show_interface1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_docentes)
        vbox.addWidget(self.button_back)

        self.setLayout(vbox)

    def show_interface1(self):
        self.interface1 = Interface1()
        self.interface1.show()
        self.hide()


class InterfaceAdministrativos(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label_administrativos = QLabel('Interfaz Administrativos')
        self.button_back = QPushButton('Volver a Interfaz 1')
        self.button_back.clicked.connect(self.show_interface1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label_administrativos)
        vbox.addWidget(self.button_back)

        self.setLayout(vbox)

    def show_interface1(self):
        self.interface1 = Interface1()
        self.interface1.show()
        self.hide()

class Mapa(QWidget):
    def __init__(self):
        super().__init__()

        # Coordenadas del origen y destino
        origen = [17.0802048, -96.7465228]
        destino = [19.403557, -99.163246]

        # Crear un objeto Map
        m = folium.Map(location=origen, zoom_start=12)

        # Agregar marcadores para el origen y destino
        folium.Marker(location=origen, icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=destino, icon=folium.Icon(color='red')).add_to(m)

        # Crear una línea entre el origen y el destino
        folium.PolyLine(locations=[origen, destino], color='blue').add_to(m)

        # Guardar el mapa en un archivo HTML temporal
        m.save('temp_map.html')

        # Crear un objeto QWebEngineView para mostrar el mapa en un widget de navegador web
        self.web = QWebEngineView()
        self.web.load(QUrl.fromLocalFile('/temp_map.html'))

        # Agregar el objeto QWebEngineView al layout vertical del widget
        layout = QVBoxLayout()
        layout.addWidget(self.web)
        self.setLayout(layout)

        # Configurar las dimensiones del widget
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Mapa')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface1 = Interface1()
    interface1.show()
    sys.exit(app.exec_())