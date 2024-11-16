class IncidentesController:
    def __init__(self):
        pass

    def insertar_incidente(self, conexion):
        prision_id = input("Ingrese el ID de la prisión: ")
        descripcion = input("Ingrese una descripción del incidente: ")
        fecha_incidente = input("Ingrese la fecha del incidente (YYYY-MM-DD): ")
        cursor = conexion.conexion.cursor()
        sql = "INSERT INTO Incident (prison_id, description, incident_date) VALUES (%s, %s, %s)"
        valores = (prision_id, descripcion, fecha_incidente)
        cursor.execute(sql, valores)
        conexion.conexion.commit()
        print(f"Incidente en la prisión con ID {prision_id} registrado correctamente.")

    def actualizar_incidente(self, conexion):
        id_incidente = input("Ingrese el ID del incidente a actualizar: ")
        nueva_descripcion = input("Ingrese la nueva descripción del incidente: ")
        nueva_fecha = input("Ingrese la nueva fecha del incidente (YYYY-MM-DD): ")
        cursor = conexion.conexion.cursor()
        sql = "UPDATE Incident SET description = %s, incident_date = %s WHERE id = %s"
        valores = (nueva_descripcion, nueva_fecha, id_incidente)
        cursor.execute(sql, valores)
        conexion.conexion.commit()
        print(f"Incidente con ID {id_incidente} actualizado correctamente.")

    def eliminar_incidente(self, conexion):
        id_incidente = input("Ingrese el ID del incidente a eliminar: ")
        cursor = conexion.conexion.cursor()
        sql = "DELETE FROM Incident WHERE id = %s"
        cursor.execute(sql, (id_incidente,))
        conexion.conexion.commit()
        print(f"Incidente con ID {id_incidente} eliminado correctamente.")

    def listar_incidentes(self, conexion):
        cursor = conexion.conexion.cursor()
        sql = "SELECT * FROM Incident"
        cursor.execute(sql)
        incidentes = cursor.fetchall()
        for incidente in incidentes:
            print(incidente)
            
    def consultar_incidentes_por_carcel(self, conexion):
        prison_id = input("Ingrese el ID de la prisión: ")

        try:
            cursor = conexion.conexion.cursor()
            # Llamar al procedimiento almacenado
            cursor.callproc('GetIncidentsByPrison', [prison_id])

            # Obtener y mostrar los resultados
            print("\n--- Incidentes de la Prisión ---")
            for result in cursor.stored_results():  # Obtener los resultados del procedimiento
                incidentes = result.fetchall()  # Obtener todas las filas
                if incidentes:
                    for incidente in incidentes:
                        # Los índices corresponden a las columnas devueltas por el procedimiento
                        print(f"ID: {incidente[0]}, Descripción: {incidente[1]}, Fecha: {incidente[2]}")
                else:
                    print(f"No se encontraron incidentes para la prisión con ID {prison_id}.")
        except Exception as e:
            print(f"Error al consultar los incidentes: {e}")
        

    def menu_incidentes(self, conexion):
        while True:
            print("\n--- Menú Incidentes ---")
            print("1. Insertar Incidente")
            print("2. Actualizar Incidente")
            print("3. Eliminar Incidente")
            print("4. Listar Incidentes")
            print("5. Consultar Incidentes por Prisión")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.insertar_incidente(conexion)
            elif opcion == '2':
                self.actualizar_incidente(conexion)
            elif opcion == '3':
                self.eliminar_incidente(conexion)
            elif opcion == '4':
                self.listar_incidentes(conexion)
            elif opcion == '5':
                self.consultar_incidentes_por_carcel(conexion)    
            elif opcion == '0':
                break
            else:
                print("Opción no válida, intente de nuevo.")
