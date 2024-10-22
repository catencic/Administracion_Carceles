import mysql.connector

class Conexion:
    def __init__(self):
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                database="administracion_carceles",
                user="admin_carcel",
                password="Clas3s1Nt2024_!",
                port=3306
            )
            print("Conexión exitosa a la base de datos")
        except mysql.connector.Error as err:
            print(f"Error al conectar: {err}")
        return self.conexion

    def desconectar(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada")
