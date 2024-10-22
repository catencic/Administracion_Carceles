
class Rol_PersonalController:
    def __init__(self):
        pass

    def insertar_rol(self, conexion):
        nombre_rol = input("Ingrese el nombre del rol: ")
        cursor = conexion.conexion.cursor()
        sql = "INSERT INTO StaffRole (role_name) VALUES (%s)"
        cursor.execute(sql, (nombre_rol,))
        conexion.conexion.commit()
        print(f"Rol {nombre_rol} insertado correctamente.")

    def actualizar_rol(self, conexion):
        id_rol = input("Ingrese el ID del rol a actualizar: ")
        nuevo_nombre_rol = input("Ingrese el nuevo nombre del rol: ")
        cursor = conexion.conexion.cursor()
        sql = "UPDATE StaffRole SET role_name = %s WHERE id = %s"
        cursor.execute(sql, (nuevo_nombre_rol, id_rol))
        conexion.conexion.commit()
        print(f"Rol con ID {id_rol} actualizado correctamente.")

    def eliminar_rol(self, conexion):
        id_rol = input("Ingrese el ID del rol a eliminar: ")
        cursor = conexion.conexion.cursor()
        sql = "DELETE FROM StaffRole WHERE id = %s"
        cursor.execute(sql, (id_rol,))
        conexion.conexion.commit()
        print(f"Rol con ID {id_rol} eliminado correctamente.")

    def listar_roles(self, conexion):
        cursor = conexion.conexion.cursor()
        sql = "SELECT * FROM StaffRole"
        cursor.execute(sql)
        roles = cursor.fetchall()
        for rol in roles:
            print(rol)

    def menu_roles(self, conexion):
        while True:
            print("\n--- Menú Roles del Personal ---")
            print("1. Insertar Rol")
            print("2. Actualizar Rol")
            print("3. Eliminar Rol")
            print("4. Listar Roles")
            print("0. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                self.insertar_rol(conexion)
            elif opcion == '2':
                self.actualizar_rol(conexion)
            elif opcion == '3':
                self.eliminar_rol(conexion)
            elif opcion == '4':
                self.listar_roles(conexion)
            elif opcion == '0':
                break
            else:
                print("Opción no válida, intente de nuevo.")
