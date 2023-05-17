import sys
from PyQt5.QtWidgets import QApplication
from alumno_login import *
import conexion_alumno
import moduloAlumno

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

        self.ui.btn_salir.clicked.connect(self.salir)

        # Conexión a la base de datos independiente-----------
        self.datos = conexion_alumno.Registro_datos()

    def iniciar_sesion(self):
        # Reseteo de los etiquetas que dicen si el usuario es correcto y su contraseña
        self.ui.credencial_incorrecta.setText('')

        # Guardamos en una variable tanto el usuario capturado como la contraseña
        users_entry = self.ui.users.text()
        mi_user = self.ui.users.text()
        password_entry = self.ui.password.text()
        password = self.ui.password.text()

        # Le damos el siguiente formato para posteriormente hacer la búsqueda en la base de datos y realizar todas las validaciones
        users_entry = str(users_entry)
        password_entry = str(password_entry)

        dato1 = self.datos.buscar_usuario_contrasenia(users_entry,password_entry)
        # dato2 = self.datos.busca_password(password_entry)


        if dato1 == []:
            self.ui.credencial_incorrecta.setText('Credenciales incorrectas')
        else:
            # Conexion a la BD independiente
            datos = conexion_alumno.Registro_datos()
            dato1 = datos.busca_users("'" + mi_user + "'")
            alumnito = dato1[0]
            idAlumno = alumnito[0]
            self.moduloAlumnitos = moduloAlumno.ModuloAlumno(mi_user, idAlumno)
            self.moduloAlumnitos.show()
            self.close()


        #
        # fila1 = dato1
        # fila2 = dato2
        #
        # if fila1 == fila2:
        #     if dato1 == [] and dato2 == []:
        #         self.ui.credencial_incorrecta.setText('Credenciales incorrectas')
        #     else:
        #         if dato1 == []:
        #             self.ui.credencial_incorrecta.setText('Usuario incorrecto')
        #         else:
        #             dato1 = dato1[0][1]
        #
        #         if dato2 == []:
        #             self.ui.credencial_incorrecta.setText('Contraseña incorrecta')
        #         else:
        #             dato2 = dato2[0][2]
        #
        #         if dato1 != [] and dato2 != []:
        #             print("VALIDADO")
        #
        #             # Conexion a la BD independiente
        #             datos = conexion.Registro_datos()
        #             dato1 = datos.busca_users("'" + mi_user + "'")
        #             alumnito = dato1[0]
        #             idAlumno = alumnito[0]
        #
        #             # self.moduloAlumnitos = moduloAlumno.ModuloAlumno("a", "20")
        #             self.moduloAlumnitos = moduloAlumno.ModuloAlumno(mi_user, idAlumno)
        #             self.moduloAlumnitos.show()
        #             self.close()
        #
        # else:
        #     self.ui.credencial_incorrecta.setText('Credenciales incorrectas')

    def salir(self):
        # Salir del programa
        QApplication.quit()

# if __name__ == "__main__":
#     appPrincipal = QApplication(sys.argv)
#     mi_app = MiApp()
#     mi_app.show()
#     sys.exit(appPrincipal.exec_())
