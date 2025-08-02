import utils.screencontroler as sc
from utils.corefiles import readJson, writeJson
from app.config import ARCHIVO_JSON

def guardarycargar(coleccion):
    while True:
        sc.limpiarpantalla()
        print('======= Guardar / Cargar Colección =======')
        print('Que deseas hacer                         ?')
        print('1. Guardar la colección actual            ')
        print('2. Cargar una colección guardada          ')
        print('3. Volver al menú principal               ')
        print('==========================================')
        print('seleccione una opcion (1-3) :             ')
        opcion = input('Seleccione una opción (1-3):     ')
        print()

        if opcion == "1":
            writeJson(ARCHIVO_JSON, coleccion)
            print('Colección guardada exitosamente.\n')
        elif opcion == "2":
            datos = readJson(ARCHIVO_JSON)
            if datos:
                coleccion.clear()
                coleccion.extend(datos)
                print('Colección cargada exitosamente desde el archivo.')
            else:
                print(' No se encontró información válida para cargar.')
        elif opcion == "3":
            break
        else:
            print(' Opción inválida. Intente nuevamente.')

        input("Presione ENTER para continuar...")