class DelitoController:
    def __init__(self):
        pass

    def insertar_delito(self, conexion):
        nombre_delito = input("Ingrese el nombre del delito: ")
        descripcion = input("Ingrese una descripción del delito: ")
        cursor = conexion.conexion.cursor()
        sql = "INSERT INTO Crime (name, description) VALUES (%s, %s)"
        cursor.execute(sql, (nombre_delito, descripcion))
        conexion.conexion.commit()
        print(f"Delito {nombre_delito} insertado correctamente.")

    def actualizar_delito(self, conexion):
        id_delito = input("Ingrese el ID del delito a actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del delito: ")
        nueva_descripcion = input("Ingrese la nueva descripción del delito: ")
        cursor = conexion.conexion.cursor()
        sql = "UPDATE Crime SET name = %s, description = %s WHERE id = %s"
        cursor.execute(sql, (nuevo_nombre, nueva_descripcion, id_delito))
        conexion.conexion.commit()
        print(f"Delito con ID {id_delito} actualizado correctamente.")

    def eliminar_delito(self, conexion):
        id_delito = input("Ingrese el ID del delito a eliminar: ")
        cursor = conexion.conexion.cursor()
        sql = "DELETE FROM Crime WHERE id = %s"
        cursor.execute(sql, (id_delito,))
        conexion.conexion.commit()
        print(f"Delito con ID {id_delito} eliminado correctamente.")

    def listar_delitos(self, conexion):
        cursor = conexion.conexion.cursor()
        sql = "SELECT * FROM Crime"
        cursor.execute(sql)
        delitos = cursor.fetchall()
        for delito in delitos:
            print(delito)

    def menu_delitos(self, conexion):
        while True:
            print("\n--- Menú Delitos ---")
            print("1. Insertar Delito")
            print("2. Actualizar Delito")
            print("3. Eliminar Delito")
            print("4. Listar Delitos")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.insertar_delito(conexion)
            elif opcion == '2':
                self.actualizar_delito(conexion)
            elif opcion == '3':
                self.eliminar_delito(conexion)
            elif opcion == '4':
                self.listar_delitos(conexion)
            elif opcion == '0':
                break
            else:
                print("Opción no válida, intente de nuevo.")
