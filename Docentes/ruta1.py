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
        punto1 = [17.0656, -96.7259]
        punto2 = [17.0626, -96.7295]
        punto3 = [17.0586, -96.7325]
        punto4 = [17.0506, -96.7365]
        punto5 = [17.0336, -96.7385]
        punto6 = [19.0516, -96.9497]
        punto7 = [19.0859, -96.9493]
        punto8 = [19.1201, -96.9183]
        punto9 = [19.1471, -96.8968]

        # Crea un objeto de mapa centrado en Oaxaca Centro
        mapa = folium.Map(location=oaxaca_centro, zoom_start=7)

        # Crea una PolyLine que representa la ruta de Oaxaca a Veracruz
        ruta = folium.vector_layers.PolyLine(locations=[oaxaca_centro, punto1, punto2, punto3, punto4, punto5, punto6, punto7, punto8, punto9, veracruz], color='blue', weight=5)

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
