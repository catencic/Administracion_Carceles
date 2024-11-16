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
    
    
    def consultar_internos_por_prision(self, conexion):
        prison_id = input("Ingrese el ID de la cárcel: ")
    
        try:
            cursor = conexion.conexion.cursor()
            # Llamada al procedimiento almacenado
            cursor.callproc('GetInmatesByPrison', [prison_id])

            # Iterar sobre los resultados
            print("\n--- Internos en la Cárcel ---")
            for resultado in cursor.stored_results():
                internos = resultado.fetchall()
                if internos:
                    for interno in internos:

                        print(f"ID Interno: {interno[0]}, Nombre: {interno[1]}, Fecha de nacimiento: {interno[2]}")
                else:
                    print(f"No hay internos registrados para la cárcel con ID {prison_id}.")
        except Exception as e:
            print(f"Error al consultar los internos: {e}")
    
    
    def consultar_ocupacion_prisiones(self, conexion):
        try:
            cursor = conexion.conexion.cursor()
            # Llamada al procedimiento almacenado
            cursor.callproc('GetPrisonOccupancy')

            # Mostrar los resultados
            print("\n--- Ocupación de Prisiones ---")
            for resultado in cursor.stored_results():  # Obtener los resultados del procedimiento
                ocupaciones = resultado.fetchall()  # Obtener todas las filas
                if ocupaciones:
                    for ocupacion in ocupaciones:

                        print(f"Nombre de la prisión: {ocupacion[0]}, Número de internos: {ocupacion[1]}")
                else:
                    print("No se encontraron datos de ocupación de prisiones.")
        except Exception as e:
            print(f"Error al consultar la ocupación de las prisiones: {e}")

    
    def menu_prision(self, conexion):
        while True:
            print("\n--- Menú Cárceles ---")
            print("1. Insertar Cárcel")
            print("2. Actualizar Cárcel")
            print("3. Eliminar Cárcel")
            print("4. Listar Cárceles")
            print("5. Consultar Internos por Cárcel") # Nueva opción
            print("6. Consultar Ocupación de Prisiones")  # Nueva opción
            print("0. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.insertar_prison(conexion)
            elif opcion == '2':
                self.actualizar_prison(conexion)
            elif opcion == '3':
                self.eliminar_prison(conexion)
            elif opcion == '4':
                self.listar_prisiones_por_municipio(conexion)
            elif opcion == '5':  
                self.consultar_internos_por_prision(conexion)
            elif opcion == '6':
                self.consultar_ocupacion_prisiones(conexion)              
            elif opcion == '0':
                break
            else:
                print("Opción no válida, intente de nuevo.")
