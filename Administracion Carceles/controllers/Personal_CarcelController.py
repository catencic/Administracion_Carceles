class Personal_CarcelController:
    def __init__(self):
        pass

    def insertar_personal(self, conexion):
        nombre = input("Ingrese el nombre del personal: ")
        apellido = input("Ingrese el apellido del personal: ")
        rol_id = input("Ingrese el ID del rol del personal: ")
        prision_id = input("Ingrese el ID de la prisión: ")
        cursor = conexion.conexion.cursor()
        sql = "INSERT INTO Staff (first_name, last_name, role_id, prison_id) VALUES (%s, %s, %s, %s)"
        valores = (nombre, apellido, rol_id, prision_id)
        cursor.execute(sql, valores)
        conexion.conexion.commit()
        print(f"Personal {nombre} {apellido} insertado correctamente.")

    def actualizar_personal(self, conexion):
        id_personal = input("Ingrese el ID del personal a actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del personal: ")
        nuevo_apellido = input("Ingrese el nuevo apellido del personal: ")
        nuevo_rol_id = input("Ingrese el nuevo ID del rol: ")
        cursor = conexion.conexion.cursor()
        sql = "UPDATE Staff SET first_name = %s, last_name = %s, role_id = %s WHERE id = %s"
        valores = (nuevo_nombre, nuevo_apellido, nuevo_rol_id, id_personal)
        cursor.execute(sql, valores)
        conexion.conexion.commit()
        print(f"Personal con ID {id_personal} actualizado correctamente.")

    def eliminar_personal(self, conexion):
        id_personal = input("Ingrese el ID del personal a eliminar: ")
        cursor = conexion.conexion.cursor()
        sql = "DELETE FROM Staff WHERE id = %s"
        cursor.execute(sql, (id_personal,))
        conexion.conexion.commit()
        print(f"Personal con ID {id_personal} eliminado correctamente.")

    def listar_personal(self, conexion):
        cursor = conexion.conexion.cursor()
        sql = "SELECT * FROM Staff"
        cursor.execute(sql)
        personal = cursor.fetchall()
        for persona in personal:
            print(persona)
            
            
    def consultar_personal_por_prision(self, conexion):
        prision_id = input("Ingrese el ID de la cárcel: ")

        try:
            cursor = conexion.conexion.cursor()
            # Llamar al procedimiento almacenado
            cursor.callproc('GetStaffByPrison', [prision_id])

            # Obtener y mostrar los resultados
            print("\n--- Personal en la Cárcel ---")
            for result in cursor.stored_results():  # Obtener los resultados del procedimiento
                filas = result.fetchall()  # Obtener todas las filas
                if filas:
                    for persona in filas:

                        print(f"ID Personal: {persona[0]}, Nombre Completo: {persona[1]}, Rol: {persona[2]}")
                else:
                    print(f"No se encontraron registros para la cárcel con ID {prision_id}.")
        except Exception as e:
            print(f"Error al consultar el personal: {e}")

        

    def menu_personal(self, conexion):
        while True:
            print("\n--- Menú Personal de la Cárcel ---")
            print("1. Insertar Personal")
            print("2. Actualizar Personal")
            print("3. Eliminar Personal")
            print("4. Listar Personal")
            print("5. Consultar Personal por Cárcel")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.insertar_personal(conexion)
            elif opcion == '2':
                self.actualizar_personal(conexion)
            elif opcion == '3':
                self.eliminar_personal(conexion)
            elif opcion == '4':
                self.listar_personal(conexion)
            elif opcion == '5':  
                self.consultar_personal_por_prision(conexion)    
            elif opcion == '0':
                break
            else:
                print("Opción no válida, intente de nuevo.")
