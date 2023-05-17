import mysql.connector

class Registro_datos():

    def __init__(self):
        # self.cnn = mysql.connector.connect( host='localhost',
        #                                     database ='bd_control',
        #                                     user = 'root',
        #                                     password ='1492')
        # print("Conexion a la BD exitosa")

        self.cnn = mysql.connector.connect(
            host="containers-us-west-39.railway.app",
            user="root",
            passwd="NYAmCqezCtHRPuOjzmPK",
            database="railway",
            port=6185,
            auth_plugin='mysql_native_password'
        )
        print("Conexion a la BD exitosa")

    # Buscar un alumno por un usuario
    def busca_users(self, usuario):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM alumnos WHERE usuario = {}".format(usuario)
        cur.execute(sql)
        usersx = cur.fetchall()
        cur.close()     
        return usersx

    # Buscar actividades complementarias de un alumno
    def buscar_complementarias(self, idAlumno):
        cur = self.cnn.cursor()
        sql = "SELECT ae.nombre_actividad,ae.horario,ae.estado, d.nombre AS nombre_docente, d.primer_apellido as apellido_docente, d.segundo_apellido as segundo_apellido_docente FROM actividades_extraescolares AS ae JOIN docentes AS d ON ae.idDocente = d.idDocente WHERE ae.idAlumno = {}".format(idAlumno)
        cur.execute(sql)
        usersx = cur.fetchall()
        cur.close()
        return usersx

    def buscar_materia_calificacion(self, idAlumno, semestre):
        cur = self.cnn.cursor()
        # sql = "SELECT m.nombre_materia,m.horario,m.semestre,a.nombre AS nombre_alumno,CONCAT(d.nombre, ' ', d.primer_apellido, ' ', d.segundo_apellido) AS nombre_docente,c.unidad1 AS calificacion_unidad1,c.unidad2 AS calificacion_unidad2,c.unidad3 AS calificacion_unidad3,c.unidad4 AS calificacion_unidad4 FROM materias m INNER JOIN calificaciones c ON m.idmaterias = c.id_materia INNER JOIN alumnos a ON m.id_alumno = a.idAlumno INNER JOIN docentes d ON m.id_docente = d.idDocente where a.idAlumno = {}".format(idAlumno)
        sql = "SELECT m.nombre_materia,m.horario,m.semestre,a.nombre AS nombre_alumno,CONCAT(d.nombre, ' ', d.primer_apellido, ' ', d.segundo_apellido) AS nombre_docente,c.unidad1 AS calificacion_unidad1,c.unidad2 AS calificacion_unidad2,c.unidad3 AS calificacion_unidad3,c.unidad4 AS calificacion_unidad4 FROM materias m INNER JOIN calificaciones c ON m.idmaterias = c.id_materia INNER JOIN alumnos a ON m.id_alumno = a.idAlumno INNER JOIN docentes d ON m.id_docente = d.idDocente where a.idAlumno = %s and m.semestre = %s;"
        valores = (idAlumno, semestre)
        cur.execute(sql, valores)
        usersx = cur.fetchall()
        cur.close()
        return usersx

    def buscar_maximo_semestre(self, idAlumno):
        cur = self.cnn.cursor()
        sql = "SELECT MAX(CAST(semestre AS UNSIGNED)) AS max_semestre FROM materias WHERE id_alumno = {}".format(idAlumno)
        cur.execute(sql)
        semestre = cur.fetchall()
        cur.close()
        return semestre

    # Buscar actividades complementarias de un alumno
    def buscar_actividades_de_la_u(self):
        cur = self.cnn.cursor()
        sql = "SELECT nombre,descripcion,hora,fecha,ubicacion,categoria,costo,estado,imagen FROM eventos;"
        cur.execute(sql)
        usersx = cur.fetchall()
        cur.close()
        return usersx

    # Buscar un alumno por nombre
    def busca_por_nombre(self, users):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM alumnos WHERE nombre = {}".format(users)
        cur.execute(sql)
        usersx = cur.fetchall()
        cur.close()
        return usersx

    # Buscar un alumno dada una contraseña
    def busca_password(self, password):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM alumnos WHERE contrasenia = '{}'".format(password) #
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()     
        return passwordx

    #Busca una contraseña dada un usuario
    def buscar_contrasenia(self, usuario):
            cur = self.cnn.cursor()
            sql = "SELECT contrasenia from alumnos where usuario = {}".format(usuario)  #
            cur.execute(sql)
            passwordx = cur.fetchall()
            cur.close()
            return passwordx

    def inserta_datos_reporte(self, descripcion, idAlumno):
        cur = self.cnn.cursor()
        sql = "INSERT INTO reporte_correccion_datos (descripcionReporte, idAlumno) VALUES (%s, %s)"
        valores = (descripcion, idAlumno)
        cur.execute(sql, valores)
        self.cnn.commit()
        cur.close()

    def buscar_usuario_contrasenia(self, usuario, contrasenia):
        cur = self.cnn.cursor()
        sql = "select * from alumnos where usuario = %s and contrasenia = %s;"
        valores = (usuario, contrasenia)
        cur.execute(sql, valores)
        passwordx = cur.fetchall()
        cur.close()
        return passwordx

    def buscar_boleta_semestre(self, idAlumno, semestre):
        cur = self.cnn.cursor()
        sql = "SELECT m.nombre_materia, c.unidad1, c.unidad2, c.unidad3, c.unidad4 FROM calificaciones c INNER JOIN materias m ON c.id_materia = m.idmaterias INNER JOIN alumnos a ON m.id_alumno = a.idAlumno WHERE a.idAlumno = %s AND m.semestre = %s;"
        valores = (idAlumno, semestre)
        cur.execute(sql, valores)
        boleta = cur.fetchall()
        cur.close()
        return boleta

    def actualizar_contrasenia(self, nueva_contrasenia, idAlumno):
        cur = self.cnn.cursor()
        sql = "UPDATE alumnos SET contrasenia = %s WHERE idAlumno = %s;"
        valores = (nueva_contrasenia, idAlumno)
        cur.execute(sql, valores)
        self.cnn.commit()
        cur.close()

    def inserta_datos_reporte_baja(self, descripcion, idAlumno):
        cur = self.cnn.cursor()
        sql = "INSERT INTO reporte_baja (descripcion_reporte, idAlumno) VALUES (%s, %s)"
        valores = (descripcion, idAlumno)
        cur.execute(sql, valores)
        self.cnn.commit()
        cur.close()

        