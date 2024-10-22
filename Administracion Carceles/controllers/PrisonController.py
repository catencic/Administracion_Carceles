class PrisonController:
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

    # Puedes agregar los métodos para actualizar, eliminar y listar cárceles

    def menu_prison(self, conexion):
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
            # Agrega las demás opciones
            elif opcion == '0':
                break
            else:
                print("Opción no válida, intente de nuevo.")
