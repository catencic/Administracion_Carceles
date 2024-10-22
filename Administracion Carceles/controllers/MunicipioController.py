class MunicipioController:
    def __init__(self):
        pass

    def insertar_municipio(self, conexion):
        nombre = input("Ingrese el nombre del municipio: ")
        estado = input("Ingrese el estado del municipio: ")
        cursor = conexion.conexion.cursor()
        sql = "INSERT INTO Municipality (name, state) VALUES (%s, %s)"
        valores = (nombre, estado)
        cursor.execute(sql, valores)
        conexion.conexion.commit()
        print(f"Municipio {nombre} insertado correctamente.")

    def actualizar_municipio(self, conexion):
        id_municipio = input("Ingrese el ID del municipio a actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del municipio: ")
        nuevo_estado = input("Ingrese el nuevo estado del municipio: ")
        cursor = conexion.conexion.cursor()
        sql = "UPDATE Municipality SET name = %s, state = %s WHERE id = %s"
        valores = (nuevo_nombre, nuevo_estado, id_municipio)
        cursor.execute(sql, valores)
        conexion.conexion.commit()
        print(f"Municipio con ID {id_municipio} actualizado correctamente.")

    def eliminar_municipio(self, conexion):
        id_municipio = input("Ingrese el ID del municipio a eliminar: ")
        cursor = conexion.conexion.cursor()
        sql = "DELETE FROM Municipality WHERE id = %s"
        cursor.execute(sql, (id_municipio,))
        conexion.conexion.commit()
        print(f"Municipio con ID {id_municipio} eliminado correctamente.")

    def listar_municipios(self, conexion):
        cursor = conexion.conexion.cursor()
        sql = "SELECT * FROM Municipality"
        cursor.execute(sql)
        municipios = cursor.fetchall()
        for municipio in municipios:
            print(municipio)

    def menu_municipio(self, conexion):
        while True:
            print("\n--- Menú Municipio ---")
            print("1. Insertar Municipio")
            print("2. Actualizar Municipio")
            print("3. Eliminar Municipio")
            print("4. Listar Municipios")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.insertar_municipio(conexion)
            elif opcion == '2':
                self.actualizar_municipio(conexion)
            elif opcion == '3':
                self.eliminar_municipio(conexion)
            elif opcion == '4':
                self.listar_municipios(conexion)
            elif opcion == '0':
                break
            else:
                print("Opción no válida, intente de nuevo.")
