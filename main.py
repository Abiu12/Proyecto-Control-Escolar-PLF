import sys
import folium
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from alumnos_conexion import Alumnos
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QBrush, QColor
from PyQt5.QtWidgets import QGridLayout

class Interface1(QWidget):

    alumnos = Alumnos()

    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Control Escolar")
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
        print(self.alumnos)
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
        self.resize(1200, 800)
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
        self.resize(1200, 800)
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
        self.resize(1200, 800)
        self.setStyleSheet("background-color: #F2F2F2;")

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Administrativo")
        title = QLabel("Menú Principal Administrativo")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")

        # Crear los botones
        self.btnControlEstudiantes = QPushButton('Control de estudiantes')
        aplicar_estilos(self.btnControlEstudiantes,"#FF8C00")
        self.btnControlEstudiantes.clicked.connect(self.show_interface_control_estudiantes)

        self.btnControlDocentes = QPushButton('Control de docentes')
        aplicar_estilos(self.btnControlDocentes,"#FF8C00")
        self.btnControlDocentes.clicked.connect(self.show_interface_control_docentes)

        self.btnNomina = QPushButton('Nómina')
        aplicar_estilos(self.btnNomina,"#FF8C00")
        self.btnNomina.clicked.connect(self.show_interface_nomina)

        self.btnEventos = QPushButton('Eventos, Actividades')
        aplicar_estilos(self.btnEventos,"#FF8C00")
        self.btnEventos.clicked.connect(self.show_interface_eventos)

        self.btnRegresar = QPushButton('Volver al menu principal')
        aplicar_estilos(self.btnRegresar,"#4CAF50")
        self.btnRegresar.clicked.connect(self.show_interface1)

        # Crear la cuadrícula para los primeros cuatro botones
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.btnControlEstudiantes, 0, 0)
        grid_layout.addWidget(self.btnControlDocentes, 0, 1)
        grid_layout.addWidget(self.btnNomina, 1, 0)
        grid_layout.addWidget(self.btnEventos, 1, 1)

        # Crear un layout horizontal para el botón de regresar
        hbox_layout = QHBoxLayout()
        hbox_layout.addStretch(1)
        hbox_layout.addWidget(self.btnRegresar)

        # Crear un layout vertical para colocar la cuadrícula y el layout horizontal del botón de regresar
        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(title)
        vbox_layout.addSpacing(20)
        vbox_layout.addLayout(grid_layout)
        vbox_layout.addStretch(1)
        vbox_layout.addLayout(hbox_layout)

        # Configurar el layout principal de la ventana
        self.setLayout(vbox_layout)

    def show_interface1(self):
        self.interface1 = Interface1()
        self.interface1.show()
        self.hide()
    def show_interface_control_estudiantes(self):
        self.interface_control_estudiantes = InterfazControlEstudiantes()
        self.interface_control_estudiantes.show()
        self.hide()
    def show_interface_control_docentes(self):
        self.interface_control_docentes = InterfazControlDocentes()
        self.interface_control_docentes.show()
        self.hide()
    def show_interface_nomina(self):
        self.interface_nomina= InterfazNomina()
        self.interface_nomina.show()
        self.hide()
    def show_interface_eventos(self):
        self.interface_eventos= InterfazEventos()
        self.interface_eventos.show()
        self.hide()

class InterfazControlEstudiantes(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.initUI()

    def initUI(self):
        self.label_docentes = QLabel('Interfaz Control Estudiantes')
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

class InterfazControlDocentes(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.initUI()

    def initUI(self):
        self.label_docentes = QLabel('Interfaz Control Docentes')
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

class InterfazEventos(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.initUI()

    def initUI(self):
        self.label_docentes = QLabel('Interfaz Eventos')
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

def aplicar_estilos(boton,color):
    style = f"""
    QPushButton {{
        background-color: {color};
        color: #fff;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
    }}
    QPushButton:hover {{
        background-color: #FF5733;
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface1 = Interface1()
    interface1.show()
    sys.exit(app.exec_())