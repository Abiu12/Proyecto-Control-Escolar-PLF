import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium

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
    mapa = Mapa()
    mapa.show()
    sys.exit(app.exec_())
