import mysql.connector
from mysql.connector.locales.eng import client_error
import datetime
import random
import string


class Administrativos:

    def __init__(self):
        self.cnn = mysql.connector.connect(
            host= "localhost",  #"containers-us-west-202.railway.app", 
            user= "root", #"root",
            passwd= "elchidoabiu10", #"XzLlfajzeTmUzaafbQue",
            database= "bd_control",#"railway",
            #port = 7565,
            auth_plugin='mysql_native_password'
            )
        


    def __str__(self):
        datos=self.consulta_alumnos()
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
    
    def consulta_alumnos(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM alumnos")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_alumno(self, id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM alumnos WHERE idAlumno = {}".format(id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_alumno(self, nombre,primer_apellido,segundo_apellido,calle,numero,colonia,municipio,telefono,numero_imss,ine,curp,rfc,nombre_madre,telefono_madre,nombre_padre,telefono_padre):
        usuario = self.crear_usuario(nombre,primer_apellido,segundo_apellido)
        contrasenia = self.crear_contrasenia()
        cur = self.cnn.cursor()
        sql='''INSERT INTO alumnos (idAlumno, nombre,primer_apellido,segundo_apellido,calle,numero,colonia,municipio,telefono,numero_imss,ine,curp,rfc,nombre_madre,telefono_madre,nombre_padre,telefono_padre,usuario,contrasenia) 
        VALUES(NULL,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(nombre,primer_apellido,segundo_apellido,calle,numero,colonia,municipio,telefono,numero_imss,ine,curp,rfc,nombre_madre,telefono_madre,nombre_padre,telefono_padre,usuario,contrasenia)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n 
    
    def crear_usuario(self, nombre, primerApellido, segundoApellido):
        año_actual = datetime.datetime.now().year
        usuario = str(nombre[:2]+primerApellido[:2]+segundoApellido[:2]+ str(año_actual))
        return  usuario

    def crear_contrasenia(self):
        chars = string.ascii_letters + string.digits + '!:;#"$'
        contrasenia = ''.join(random.choice(chars) for i in range(10))
        return contrasenia
    
    def elimina_alumno(self,id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM alumnos WHERE idAlumno = {}'''.format(id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def editar_alumno(self,nombre,primer_apellido,segundo_apellido,calle,numero,colonia,municipio,telefono,numero_imss,ine,curp,rfc,nombre_madre,telefono_madre,nombre_padre,telefono_padre,idAlumno):
        cur = self.cnn.cursor()
        sql='''UPDATE alumnos SET nombre='{}', primer_apellido='{}', segundo_apellido='{}',
        calle='{}',numero='{}',colonia='{}',municipio='{}',telefono='{}',numero_imss='{}',ine='{}',
        curp='{}',rfc='{}',nombre_madre='{}',telefono_madre='{}',
        nombre_padre='{}',telefono_padre='{}'   WHERE idAlumno={}'''.format(nombre,primer_apellido,segundo_apellido,calle,numero,colonia,municipio,telefono,numero_imss,ine,curp,rfc,nombre_madre,telefono_madre,nombre_padre,telefono_padre,int(idAlumno))
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
    
    def consulta_documentacion_alumno(self,idAlumno):
        cur = self.cnn.cursor()
        cur.execute(f"SELECT * FROM documentacion_alumno where idAlumno = {idAlumno} ")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_documentacion_alumno(self, id_alumno,id_documento_alumno):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM documentacion_alumno WHERE idDocumentacion_alumno = {} AND idAlumno = {}".format(int(id_documento_alumno),int(id_alumno))
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos

    def inserta_documento_alumno(self,descripcion,archivo_bytes,idAlumno):
        cur = self.cnn.cursor()
        sql='''INSERT INTO documentacion_alumno (idDocumentacion_alumno, descripcion, archivo,idAlumno) 
        VALUES(NULL, %s, %s, %s)'''
        values = (descripcion,archivo_bytes,int(idAlumno))
        cur.execute(sql,values)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n 

    def elimina_documento(self,idAlumno,idDocumento):
        cur = self.cnn.cursor()
        sql='''DELETE FROM documentacion_alumno WHERE idAlumno = {} and idDocumentacion_alumno = {}'''.format(idAlumno,idDocumento)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n 
    
    def consulta_docentes(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM docentes")
        datos = cur.fetchall()
        cur.close()
        return datos
    
    def inserta_docente(self, nombre,primer_apellido,segundo_apellido,calle,numero,colonia,municipio,telefono,numero_imss,ine,curp,rfc):
        usuario = self.crear_usuario(nombre,primer_apellido,segundo_apellido)
        contrasenia = self.crear_contrasenia()
        cur = self.cnn.cursor()
        sql='''INSERT INTO docentes (idDocente, nombre,primer_apellido,segundo_apellido,calle,numero,colonia,municipio,telefono,numero_imss,ine,curp,rfc,usuario,contrasenia) 
        VALUES(NULL,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(nombre,primer_apellido,segundo_apellido,calle,numero,colonia,municipio,telefono,numero_imss,ine,curp,rfc,usuario,contrasenia)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n 
    
    def elimina_docente(self,id_docente):
        cur = self.cnn.cursor()
        sql='''DELETE FROM docentes WHERE idDocente = {}'''.format(id_docente)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n 

    def buscar_docente(self, id_docente):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM docentes WHERE idDocente = {}".format(id_docente)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos

    def editar_docente(self,nombre,primer_apellido,segundo_apellido,calle,numero,colonia,municipio,telefono,numero_imss,ine,curp,rfc,idDocente):
        cur = self.cnn.cursor()
        sql='''UPDATE docentes SET nombre='{}', primer_apellido='{}', segundo_apellido='{}',
        calle='{}',numero='{}',colonia='{}',municipio='{}',telefono='{}',numero_imss='{}',ine='{}',
        curp='{}',rfc='{}' WHERE idDocente={}'''.format(nombre,primer_apellido,segundo_apellido,calle,numero,colonia,municipio,telefono,numero_imss,ine,curp,rfc,int(idDocente))
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n 
      
    def consulta_documentacion_docente(self,id_docente):
        cur = self.cnn.cursor()
        cur.execute(f"SELECT * FROM documentacion_docente where idDocente = {id_docente} ")
        datos = cur.fetchall()
        cur.close()    
        return datos
    
    def elimina_documento_docente(self,id_docente,id_documentacion):
        cur = self.cnn.cursor()
        sql='''DELETE FROM documentacion_docente WHERE idDocente = {} and idDocumentacion_docente = {}'''.format(id_docente,id_documentacion)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n 
    
    def buscar_documentacion_docente(self, id_docente,id_documento_docente):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM documentacion_docente WHERE idDocumentacion_docente = {} AND idDocente = {}".format(int(id_documento_docente),int(id_docente))
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos

    def inserta_documento_docente(self,descripcion,archivo_bytes,id_docente):
        cur = self.cnn.cursor()
        sql='''INSERT INTO documentacion_docente (idDocumentacion_docente, descripcion, archivo,idDocente) 
        VALUES(NULL, %s, %s, %s)'''
        values = (descripcion,archivo_bytes,int(id_docente))
        cur.execute(sql,values)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n 

    def buscar_notificacion_reporte(self, id_alumno):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM reporte_correccion_datos WHERE idAlumno = {}".format(int(id_alumno))
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def buscar_notificacion_baja(self, id_alumno):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM reporte_baja WHERE idAlumno = {}".format(int(id_alumno))
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos

    def eliminar_notificacion_reporte(self, id_alumno, id_reporte):
        cur = self.cnn.cursor()
        sql= f"DELETE FROM reporte_correccion_datos WHERE idAlumno = {int(id_alumno)} and idReporte = {int(id_reporte)};"
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n 
    
    def busca_user_administrativo(self, users):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM administrativos WHERE usuario = {}".format(users)
        cur.execute(sql)
        usersx = cur.fetchall()
        cur.close()     
        return usersx 

    def busca_password_administrativo(self, password):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM administrativos WHERE contrasenia = {}".format(password)
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()     
        return passwordx 
