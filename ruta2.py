from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFrame
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import folium

class mapa2(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Coordenadas de Oaxaca Centro y Cancún
        oaxaca_centro = [17.0636, -96.7255]
        cancun = [21.1619, -86.8515]

        # Coordenadas de puntos intermedios
        punto1 = [17.0656, -96.7259]
        punto2 = [17.0626, -96.7295]
        punto3 = [17.0586, -96.7325]
        punto4 = [17.0506, -96.7365]
        punto5 = [17.0336, -96.7385]
        punto6 = [19.1738, -96.1342]
        punto7 = [19.3108, -99.1838]
        punto8 = [19.4214, -99.1253]
        punto9 = [20.6889, -88.1991]
        punto10 = [20.5125, -86.9475]
        punto11 = [20.1940, -87.4651]
        punto12 = [21.0864, -86.7705]
        punto13 = [21.1474, -86.8306]
        punto14 = [21.1619, -86.8515]

        # Crea un objeto de mapa centrado en Oaxaca Centro
        mapa = folium.Map(location=oaxaca_centro, zoom_start=6)

        # Crea una PolyLine que representa la ruta de Oaxaca a Cancún
        ruta = folium.vector_layers.PolyLine(locations=[oaxaca_centro, punto1, punto2, punto3, punto4, punto5,
                                                        punto6, punto7, punto8, punto9, punto10, punto11,
                                                        punto12, punto13, punto14, cancun], color='blue', weight=5)

        # Agrega la PolyLine al mapa
        ruta.add_to(mapa)

        # Agrega un marcador en Oaxaca Centro
        folium.Marker(location=oaxaca_centro, popup="Oaxaca Centro").add_to(mapa)

        # Agrega un marcador en Cancún
        folium.Marker(location=cancun, popup="Cancún").add_to(mapa)

        # Guarda el mapa como un archivo HTML
        mapa.save("viaje2.html")

        # Crea un QFrame para mostrar el mapa
        mapa_frame = QFrame()
        mapa_frame.setMinimumSize(800, 600)

        # Crea una vista QWebEngineView y carga el archivo HTML generado por Folium
        mapa_view = QWebEngineView()
        mapa_view.load(QUrl.fromLocalFile('/viaje2.html'))

        # Crea un diseño vertical y agrega la vista del mapa a él
        mapa_layout = QVBoxLayout(mapa_frame)
        mapa_layout.addWidget(mapa_view)

        # Configura el cuadro de diálogo
        self.setWindowTitle("Mapa de Oaxaca a Cancún")
        self.setGeometry(100, 100, 800, 600)
        self.setLayout(mapa_layout)
