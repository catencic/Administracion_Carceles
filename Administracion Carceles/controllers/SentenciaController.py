class SentenciaController:
    def __init__(self):
        pass

    def insertar_sentencia(self, conexion):
        interno_id = input("Ingrese el ID del interno: ")
        crimen_id = input("Ingrese el ID del crimen: ")
        duracion = input("Ingrese la duración de la sentencia (en años): ")
        fecha_inicio = input("Ingrese la fecha de inicio de la sentencia (YYYY-MM-DD): ")
        cursor = conexion.conexion.cursor()
        sql = "INSERT INTO Sentence (inmate_id, crime_id, duration, start_date) VALUES (%s, %s, %s, %s)"
        valores = (interno_id, crimen_id, duracion, fecha_inicio)
        cursor.execute(sql, valores)
        conexion.conexion.commit()
        print(f"Sentencia para el interno con ID {interno_id} insertada correctamente.")

    def actualizar_sentencia(self, conexion):
        id_sentencia = input("Ingrese el ID de la sentencia a actualizar: ")
        nueva_duracion = input("Ingrese la nueva duración de la sentencia (en años): ")
        nueva_fecha_inicio = input("Ingrese la nueva fecha de inicio de la sentencia (YYYY-MM-DD): ")
        cursor = conexion.conexion.cursor()
        sql = "UPDATE Sentence SET duration = %s, start_date = %s WHERE id = %s"
        valores = (nueva_duracion, nueva_fecha_inicio, id_sentencia)
        cursor.execute(sql, valores)
        conexion.conexion.commit()
        print(f"Sentencia con ID {id_sentencia} actualizada correctamente.")

    def eliminar_sentencia(self, conexion):
        id_sentencia = input("Ingrese el ID de la sentencia a eliminar: ")
        cursor = conexion.conexion.cursor()
        sql = "DELETE FROM Sentence WHERE id = %s"
        cursor.execute(sql, (id_sentencia,))
        conexion.conexion.commit()
        print(f"Sentencia con ID {id_sentencia} eliminada correctamente.")

    def listar_sentencias(self, conexion):
        cursor = conexion.conexion.cursor()
        sql = "SELECT * FROM Sentence"
        cursor.execute(sql)
        sentencias = cursor.fetchall()
        for sentencia in sentencias:
            print(sentencia)

    def menu_sentencias(self, conexion):
        while True:
            print("\n--- Menú Sentencias ---")
            print("1. Insertar Sentencia")
            print("2. Actualizar Sentencia")
            print("3. Eliminar Sentencia")
            print("4. Listar Sentencias")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.insertar_sentencia(conexion)
            elif opcion == '2':
                self.actualizar_sentencia(conexion)
            elif opcion == '3':
                self.eliminar_sentencia(conexion)
            elif opcion == '4':
                self.listar_sentencias(conexion)
            elif opcion == '0':
                break
            else:
                print("Opción no válida, intente de nuevo.")