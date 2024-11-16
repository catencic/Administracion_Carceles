class InternoController:
    def __init__(self):
        pass

    def insertar_interno(self, conexion):
        nombre = input("Ingrese el nombre del interno: ")
        apellido = input("Ingrese el apellido del interno: ")
        edad = input("Ingrese la edad del interno: ")
        prision_id = input("Ingrese el ID de la prisión: ")
        cursor = conexion.conexion.cursor()
        sql = "INSERT INTO Inmate (first_name, last_name, age, prison_id) VALUES (%s, %s, %s, %s)"
        valores = (nombre, apellido, edad, prision_id)
        cursor.execute(sql, valores)
        conexion.conexion.commit()
        print(f"Interno {nombre} {apellido} insertado correctamente.")

    def actualizar_interno(self, conexion):
        id_interno = input("Ingrese el ID del interno a actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del interno: ")
        nuevo_apellido = input("Ingrese el nuevo apellido del interno: ")
        nueva_edad = input("Ingrese la nueva edad del interno: ")
        cursor = conexion.conexion.cursor()
        sql = "UPDATE Inmate SET first_name = %s, last_name = %s, age = %s WHERE id = %s"
        valores = (nuevo_nombre, nuevo_apellido, nueva_edad, id_interno)
        cursor.execute(sql, valores)
        conexion.conexion.commit()
        print(f"Interno con ID {id_interno} actualizado correctamente.")

    def eliminar_interno(self, conexion):
        id_interno = input("Ingrese el ID del interno a eliminar: ")
        cursor = conexion.conexion.cursor()
        sql = "DELETE FROM Inmate WHERE id = %s"
        cursor.execute(sql, (id_interno,))
        conexion.conexion.commit()
        print(f"Interno con ID {id_interno} eliminado correctamente.")

    def listar_internos(self, conexion):
        cursor = conexion.conexion.cursor()
        sql = "SELECT * FROM Inmate"
        cursor.execute(sql)
        internos = cursor.fetchall()
        for interno in internos:
            print(interno)
            
        

    def menu_interno(self, conexion):
        while True:
            print("\n--- Menú Interno ---")
            print("1. Insertar Interno")
            print("2. Actualizar Interno")
            print("3. Eliminar Interno")
            print("4. Listar Internos")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.insertar_interno(conexion)
            elif opcion == '2':
                self.actualizar_interno(conexion)
            elif opcion == '3':
                self.eliminar_interno(conexion)
            elif opcion == '4':
                self.listar_internos(conexion)  
            elif opcion == '0':
                break
            else:
                print("Opción no válida, intente de nuevo.")
