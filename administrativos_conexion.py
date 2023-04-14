import mysql.connector

class Administrativos:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="elchidoabiu10", database="bd_control")

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

    def buscar_alumnos(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM countries WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_alumno(self, nombre, apellido):
        cur = self.cnn.cursor()
        sql='''INSERT INTO alumnos (idAlumno, nombre, primerApellido) 
        VALUES(NULL, '{}', '{}')'''.format(nombre,apellido)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_alumno(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM countries WHERE Id = {}'''.format(Id)
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
