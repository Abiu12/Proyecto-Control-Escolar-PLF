import mysql.connector
from mysql.connector.locales.eng import client_error
class Administrativos:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="elchidoabiu10", database="bd_control",auth_plugin='mysql_native_password')

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
        cur = self.cnn.cursor()
        sql='''INSERT INTO alumnos (idAlumno, nombre,primer_apellido,segundo_apellido,calle,numero,colonia,municipio,telefono,numero_imss,ine,curp,rfc,nombre_madre,telefono_madre,nombre_padre,telefono_padre) 
        VALUES(NULL,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(nombre,primer_apellido,segundo_apellido,calle,numero,colonia,municipio,telefono,numero_imss,ine,curp,rfc,nombre_madre,telefono_madre,nombre_padre,telefono_padre)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n 

    def elimina_alumno(self,id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM alumnos WHERE idAlumno = {}'''.format(id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_alumno(self,Id, ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cnn.cursor()
        sql='''UPDATE countries SET ISO3='{}', CountryName='{}', Capital='{}',
        CurrencyCode='{}' WHERE Id={}'''.format(ISO3, CountryName, Capital, CurrencyCode,Id)
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