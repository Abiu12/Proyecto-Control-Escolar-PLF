from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFrame
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import folium

class mapa1(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Coordenadas de Oaxaca Centro y Veracruz
        oaxaca_centro = [17.0636, -96.7255]
        veracruz = [19.1738, -96.1342]

        # Coordenadas de puntos intermedios
        oaxaca_centro = [17.0636, -96.7255]
        Punto1 = [17.0813, -96.5582]
        Punto2 = [17.1108, -96.3921]
        Punto3 = [17.1449, -96.2297]
        Punto4 = [17.1836, -96.0721]
        Tuxtepec = [18.0858, -96.1297]
        Punto5 = [18.1597, -96.1894]
        Punto6 = [18.2352, -96.2516]
        Punto7 = [18.3123, -96.3164]
        Punto8 = [18.3911, -96.3840]
        Veracruz = [19.1738, -96.1342]

        # Crea un objeto de mapa centrado en Oaxaca Centro
        mapa = folium.Map(location=oaxaca_centro, zoom_start=10)

        # Crea una PolyLine que representa la ruta de Oaxaca a Veracruz
        ruta = folium.vector_layers.PolyLine(locations=[oaxaca_centro,Punto1,Punto2,Punto3,Punto4,Tuxtepec,Punto5,Punto6,Punto7,Punto8,Veracruz], color='blue', weight=5)

        # Agrega la PolyLine al mapa
        ruta.add_to(mapa)

        # Agrega un marcador en Oaxaca Centro
        folium.Marker(location=oaxaca_centro, popup="Oaxaca Centro").add_to(mapa)

        # Agrega un marcador en Veracruz
        folium.Marker(location=veracruz, popup="Veracruz").add_to(mapa)

        # Guarda el mapa como un archivo HTML
        mapa.save("viaje1.html")

        # Crea un QFrame para mostrar el mapa
        mapa_frame = QFrame()
        mapa_frame.setMinimumSize(800, 600)

        # Crea una vista QWebEngineView y carga el archivo HTML generado por Folium
        mapa_view = QWebEngineView()
        mapa_view.load(QUrl.fromLocalFile('/viaje1.html'))

        # Crea un diseño vertical y agrega la vista del mapa a él
        mapa_layout = QVBoxLayout(mapa_frame)
        mapa_layout.addWidget(mapa_view)

        # Configura el cuadro de diálogo
        self.setWindowTitle("Mapa de Oaxaca a Veracruz")
        self.setGeometry(100, 100, 800, 600)
        self.setLayout(mapa_layout)
