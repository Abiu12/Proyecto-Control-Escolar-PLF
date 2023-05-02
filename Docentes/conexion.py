import mysql.connector

#Esta clase sirve para hacer conexion a la BD
class Conexion_BD:
  #Se le pasa como parametro la base de datos que se va a utilizar
  def establecer_conexion(base):
    cnn = mysql.connector.connect(
        host='baqafswarxtmfft3blx4-mysql.services.clever-cloud.com',
        user='ufwcfaejvkr7ueph',
        password='ptNrg3nIr3FypMPduNWj',
        database=base
    )
    return cnn
  
  