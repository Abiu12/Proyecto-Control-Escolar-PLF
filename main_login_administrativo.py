
import sys
from login_administrativo import *
import administrativos_conexion
import time
import administrativos_interfaz_principal
class MiApp(QMainWindow):
	def __init__(self):
		super().__init__()

		# Instancia de el login --------------------------
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)


		#eliminar barra de estado -------------------------
		self.setWindowFlag(Qt.FramelessWindowHint)
		#transparente
		self.setAttribute(Qt.WA_TranslucentBackground)
		# Conexión de el botón con el método iniciar sesión
		self.ui.bt_ingresar.clicked.connect(self.iniciar_sesion)

     	#Conexión a la base de datos independiente-----------
		self.datos = administrativos_conexion.Administrativos()


	def iniciar_sesion(self):
		# Reseteo de los etiquetas que dicen sí el usuario es correcto y su contraseña
		self.ui.contrasena_incorrecta.setText('')
		self.ui.usuario_incorrecto.setText('')

		# Guardamos en una variable tanto el usuario capturado y también la contraseña
		users_entry = self.ui.users.text()
		password_entry = self.ui.password.text()

		# Le damos el siguiente formato para posteriormente hacer la búsqueda en la base de datos y realizar todas las validaciones
		users_entry = str("'" + users_entry + "'")
		password_entry = str("'" + password_entry + "'")

		dato1 = self.datos.busca_user_administrativo(users_entry)
		dato2 = self.datos.busca_password_administrativo(password_entry)

		fila1 = dato1
		fila2 = dato2

		if fila1 == fila2:	
			if dato1 == [] and dato2 ==[]:
				self.ui.contrasena_incorrecta.setText('Credenciales incorrectas')
			else:

				if dato1 ==[]:
					self.ui.contrasena_incorrecta.setText('Credenciales incorrectas')
				else:
					dato1 = dato1[0][1]

				if dato2 ==[]:
					self.ui.contrasena_incorrecta.setText('Credenciales incorrectas')
				else:
					dato2 = dato2[0][2]

				if dato1 != [] and dato2 != []:
					for i in range(0,99):
						time.sleep(0.000002)
						self.ui.progressBar.setValue(i)
						self.ui.cargando.setText('Cargando...')

					self.close()
					self.ventana = administrativos_interfaz_principal.InterfazAdministrativo()
					self.ventana.show()
		else:
			self.ui.contrasena_incorrecta.setText('Credenciales incorrectas')
			# self.ui.usuario_incorrecto.setText(' El usuario es incorrecto  ')
			#




if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())	