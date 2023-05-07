from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QFrame, QVBoxLayout,QDialog
import folium
from PyQt5.QtWebEngineWidgets import QWebEngineView

class mapa(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Coordenadas de Oaxaca Centro y Santa Lucía del Camino
        oaxaca_centro = [17.0636, -96.7255]
        santa_lucia = [17.0162, -96.7411]

        # Coordenadas de puntos intermedios a lo largo de la ruta
        punto1 = [17.0656, -96.7259]
        punto2 = [17.0626, -96.7295]
        punto3 = [17.0586, -96.7325]
        punto4 = [17.0506, -96.7365]
        punto5 = [17.0336, -96.7385]

        # Crea un objeto de mapa centrado en Oaxaca Centro
        mapa = folium.Map(location=oaxaca_centro, zoom_start=13)

        # Crea una PolyLine que representa la ruta de Oaxaca Centro a Santa Lucía del Camino
        ruta = folium.vector_layers.PolyLine(locations=[oaxaca_centro, punto1, punto2, punto3, punto4, punto5, santa_lucia], color='blue', weight=5)

        # Agrega la PolyLine al mapa
        ruta.add_to(mapa)

        # Agrega un marcador en Oaxaca Centro
        folium.Marker(location=oaxaca_centro, popup="Oaxaca Centro").add_to(mapa)

        # Agrega un marcador en Santa Lucía del Camino
        folium.Marker(location=santa_lucia, popup="Santa Lucía del Camino").add_to(mapa)

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
        self.setWindowTitle("Mapa de Oaxaca")
        self.setGeometry(100, 100, 800, 600)
        self.setLayout(mapa_layout)