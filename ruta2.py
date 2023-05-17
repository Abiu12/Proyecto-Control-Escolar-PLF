from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFrame
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import folium

class mapa2(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Coordenadas de Oaxaca Centro y Cancún
        oaxaca_centro = [17.0636, -96.7255]
        punto1 = [17.0656, -96.7259]
        punto2 = [17.0626, -96.7295]
        punto3 = [17.0586, -96.7325]
        punto4 = [17.0506, -96.7365]
        punto5 = [17.0336, -96.7385]
        punto6 = [16.7569, -93.1292] 
        punto7 = [19.8301, -90.5349] 
        punto8 = [21.1619, -86.8515] 
        # Crea un objeto de mapa centrado en Oaxaca Centro
        mapa = folium.Map(location=oaxaca_centro, zoom_start=10)

        # Crea una PolyLine que representa la ruta de Oaxaca a Cancún
        ruta = folium.vector_layers.PolyLine(locations=[oaxaca_centro, punto1, punto2, punto3, punto4, punto5,
                                                        punto6,punto7, punto8], color='blue', weight=6)

        # Agrega la PolyLine al mapa
        ruta.add_to(mapa)

        # Agrega un marcador en Oaxaca Centro
        folium.Marker(location=oaxaca_centro, popup="Oaxaca Centro").add_to(mapa)

        # Agrega un marcador en Cancún
        folium.Marker(location=punto8, popup="Cancún").add_to(mapa)

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
