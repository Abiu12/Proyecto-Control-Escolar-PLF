import mysql.connector

#Esta clase sirve para hacer conexion a la BD
class Conexion_BD:
  #Se le pasa como parametro la base de datos que se va a utilizar
  def establecer_conexion(base):
    cnn = mysql.connector.connect(
        host= 'containers-us-west-39.railway.app', 
        user= 'root',
        passwd= "NYAmCqezCtHRPuOjzmPK",
        database=base,
        port = 6185,
        auth_plugin='mysql_native_password'
    )
    return cnn
  
