
class VisitasController:
    def __init__(self):
        pass

    def insertar_visita(self, conexion):
        interno_id = input("Ingrese el ID del interno a quien se visita: ")
        nombre_visitante = input("Ingrese el nombre del visitante: ")
        apellido_visitante = input("Ingrese el apellido del visitante: ")
        fecha_visita = input("Ingrese la fecha de la visita (YYYY-MM-DD): ")
        cursor = conexion.conexion.cursor()
        sql = "INSERT INTO Visitor (inmate_id, first_name, last_name, visit_date) VALUES (%s, %s, %s, %s)"
        valores = (interno_id, nombre_visitante, apellido_visitante, fecha_visita)
        cursor.execute(sql, valores)
        conexion.conexion.commit()
        print(f"Visita para el interno con ID {interno_id} registrada correctamente.")

    def actualizar_visita(self, conexion):
        id_visita = input("Ingrese el ID de la visita a actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del visitante: ")
        nuevo_apellido = input("Ingrese el nuevo apellido del visitante: ")
        nueva_fecha_visita = input("Ingrese la nueva fecha de la visita (YYYY-MM-DD): ")
        cursor = conexion.conexion.cursor()
        sql = "UPDATE Visitor SET first_name = %s, last_name = %s, visit_date = %s WHERE id = %s"
        valores = (nuevo_nombre, nuevo_apellido, nueva_fecha_visita, id_visita)
        cursor.execute(sql, valores)
        conexion.conexion.commit()
        print(f"Visita con ID {id_visita} actualizada correctamente.")

    def eliminar_visita(self, conexion):
        id_visita = input("Ingrese el ID de la visita a eliminar: ")
        cursor = conexion.conexion.cursor()
        sql = "DELETE FROM Visitor WHERE id = %s"
        cursor.execute(sql, (id_visita,))
        conexion.conexion.commit()
        print(f"Visita con ID {id_visita} eliminada correctamente.")

    def listar_visitas(self, conexion):
        cursor = conexion.conexion.cursor()
        sql = "SELECT * FROM Visitor"
        cursor.execute(sql)
        visitas = cursor.fetchall()
        for visita in visitas:
            print(visita)
            
            
    def consultar_historial_visitas(self, conexion):
        interno_id = input("Ingrese el ID del interno: ")

        try:
            cursor = conexion.conexion.cursor()
            # Llamar al procedimiento almacenado
            cursor.callproc('GetVisitsByInmate', [interno_id])

            # Obtener y mostrar los resultados
            print("\n--- Historial de Visitas ---")
            for result in cursor.stored_results():  # Obtener los resultados del procedimiento
                filas = result.fetchall()  # Obtener todas las filas
                if filas:
                    for visita in filas:

                        print(f"ID Visitante: {visita[0]}, Nombre Visitante: {visita[1]}, Fecha de Visita: {visita[2]}")
                else:
                    print(f"No se encontraron visitas para el interno con ID {interno_id}.")
        except Exception as e:
            print(f"Error al consultar el historial de visitas: {e}")
    

    def menu_visitas(self, conexion):
        while True:
            print("\n--- Menú Visitas ---")
            print("1. Insertar Visita")
            print("2. Actualizar Visita")
            print("3. Eliminar Visita")
            print("4. Listar Visitas")
            print("5. Consultar Historial de Visitas por Interno")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.insertar_visita(conexion)
            elif opcion == '2':
                self.actualizar_visita(conexion)
            elif opcion == '3':
                self.eliminar_visita(conexion)
            elif opcion == '4':
                self.listar_visitas(conexion)
            elif opcion == '5':
                self.consultar_historial_visitas(conexion)          
            elif opcion == '0':
                break
            else:
                print("Opción no válida, intente de nuevo.")
