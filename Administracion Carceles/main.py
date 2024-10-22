from controllers.DelitoController import DelitoController
from controllers.IncidentesController import IncidentesController
from controllers.InternoController import InternoController
from controllers.Personal_CarcelController import Personal_CarcelController
from controllers.MunicipioController import MunicipioController
from controllers.PrisionController import PrisionController
from controllers.Rol_PersonalController import Rol_PersonalController
from controllers.SentenciaController import SentenciaController
from controllers.VisitasController import VisitasController

from db.conexion import Conexion

def mostrar_menu():
    print("\nMenú de Administración de Cárceles")
    print("1. Municipio")
    print("2. Cárceles")
    print("3. Internos")
    print("4. Personal")
    print("5. Roles del Personal")
    print("6. Delitos")
    print("7. Sentencias")
    print("8. Visitas")
    print("9. Incidentes")
    print("0. Salir")

def main():
    conexion = Conexion()
    conexion.conectar()

    # Instanciar los controladores
    municipio_controller = MunicipioController()
    prison_controller = PrisionController()
    interno_controller = InternoController()
    personal_controller = Personal_CarcelController()
    rol_personal_controller = Rol_PersonalController()
    delito_controller = DelitoController()
    sentencia_controller = SentenciaController()
    visitas_controller = VisitasController()
    incidentes_controller = IncidentesController()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            municipio_controller.menu_municipio(conexion)
        elif opcion == '2':
            prison_controller.menu_prision(conexion)
        elif opcion == '3':
            interno_controller.menu_interno(conexion)
        elif opcion == '4':
            personal_controller.menu_personal(conexion)
        elif opcion == '5':
            rol_personal_controller.menu_rol_personal(conexion)
        elif opcion == '6':
            delito_controller.menu_delitos(conexion)
        elif opcion == '7':
            sentencia_controller.menu_sentencias(conexion)
        elif opcion == '8':
            visitas_controller.menu_visitas(conexion)
        elif opcion == '9':
            incidentes_controller.menu_incidentes(conexion)
        elif opcion == '0':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

    conexion.desconectar()

if __name__ == "__main__":
    main()
