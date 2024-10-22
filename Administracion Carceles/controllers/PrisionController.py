class PrisionController:
    def __init__(self):
        pass

    def insertar_prison(self, conexion):
        nombre = input("Ingrese el nombre de la cárcel: ")
        direccion = input("Ingrese la dirección de la cárcel: ")
        municipio_id = input("Ingrese el ID del municipio: ")
        cursor = conexion.conexion.cursor()
        sql = "INSERT INTO Prison (name, address, municipality_id) VALUES (%s, %s, %s)"
        valores = (nombre, direccion, municipio_id)
        cursor.execute(sql, valores)
        conexion.conexion.commit()
        print(f"Cárcel {nombre} insertada correctamente.")

    def actualizar_prison(self, conexion):
        prison_id = input("Ingrese el ID de la cárcel a actualizar: ")
        nombre = input("Ingrese el nuevo nombre de la cárcel: ")
        direccion = input("Ingrese la nueva dirección de la cárcel: ")
        municipio_id = input("Ingrese el nuevo ID del municipio: ")
        cursor = conexion.conexion.cursor()
        sql = "UPDATE Prison SET name = %s, address = %s, municipality_id = %s WHERE id = %s"
        valores = (nombre, direccion, municipio_id, prison_id)
        cursor.execute(sql, valores)
        conexion.conexion.commit()
        print(f"Cárcel con ID {prison_id} actualizada correctamente.")

    def eliminar_prison(self, conexion):
        prison_id = input("Ingrese el ID de la cárcel a eliminar: ")
        cursor = conexion.conexion.cursor()
        sql = "DELETE FROM Prison WHERE id = %s"
        cursor.execute(sql, (prison_id,))
        conexion.conexion.commit()
        print(f"Cárcel con ID {prison_id} eliminada correctamente.")

    def listar_prisons(self, conexion):
        cursor = conexion.conexion.cursor()
        sql = "SELECT * FROM Prison"
        cursor.execute(sql)
        resultado = cursor.fetchall()

        if resultado:
            print("\nListado de Cárceles:")
            for row in resultado:
                print(f"ID: {row[0]}, Nombre: {row[1]}, Dirección: {row[2]}, Municipio ID: {row[3]}")
        else:
            print("No hay cárceles registradas.")

    def menu_prision(self, conexion):
        while True:
            print("\n--- Menú Cárceles ---")
            print("1. Insertar Cárcel")
            print("2. Actualizar Cárcel")
            print("3. Eliminar Cárcel")
            print("4. Listar Cárceles")
            print("0. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.insertar_prison(conexion)
            elif opcion == '2':
                self.actualizar_prison(conexion)
            elif opcion == '3':
                self.eliminar_prison(conexion)
            elif opcion == '4':
                self.listar_prisons(conexion)
            elif opcion == '0':
                break
            else:
                print("Opción no válida, intente de nuevo.")
