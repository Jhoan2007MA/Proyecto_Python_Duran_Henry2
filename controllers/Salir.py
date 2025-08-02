import utils.screencontroler as sc
from utils.corefiles import writeJson
from app.config import ARCHIVO_JSON
import sys

def salir(coleccion):
    sc.limpiarpantalla()
    print("Estás a punto de salir del programa.")
    opcion = input("¿Deseas guardar la colección antes de salir? (s/n): ").strip().lower()

    if opcion == "s":
        writeJson(ARCHIVO_JSON, coleccion)
        print("Colección guardada correctamente.")
    elif opcion == "n":
        print("Cambios no guardados.")
    else:
        print("Opción inválida. No se guardaron los cambios.")

    print("Gracias por usar el Administrador de Colección.")
    input("Presione ENTER para cerrar...")

sys.exit()
