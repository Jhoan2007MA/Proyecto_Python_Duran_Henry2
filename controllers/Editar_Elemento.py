import utils.screencontroler as sc
from utils.corefiles import readJson, writeJson
from app.config import ARCHIVO_JSON

def editar_elemento():
    datos = readJson(ARCHIVO_JSON)
    if not datos:
        print("No hay elementos para editar.")
        input("Presiona ENTER para continuar...")
        return

    sc.limpiarpantalla()
    try:
        id_edit = int(input("Ingrese el ID del elemento a editar: "))
    except ValueError:
        print("ID inválido. Presiona ENTER para continuar...")
        input()
        return

    elemento = next((item for item in datos if item.get("id") == id_edit), None)

    if not elemento:
        print("Elemento no encontrado.")
        input("Presiona ENTER para continuar...")
        return

    while True:
        sc.limpiarpantalla()
        print("===========================================")
        print("        Editar un elemento")
        print("===========================================")
        print("¿Qué tipo de cambio deseas realizar?")
        print("1. Editar Título")
        print("2. Editar Autor/Director/Artista")
        print("3. Editar Género")
        print("4. Editar Valoración")
        print("5. Regresar al Menú Principal")
        print("===========================================")
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            nuevo = input("Nuevo título: ").strip()
            if nuevo:
                elemento["nombre"] = nuevo
        elif opcion == "2":
            nuevo = input("Nuevo autor/director/artista: ").strip()
            if nuevo:
                elemento["autor"] = nuevo
        elif opcion == "3":
            nuevo = input("Nuevo género: ").strip()
            if nuevo:
                elemento["genero"] = nuevo
        elif opcion == "4":
            nuevo = input("Nueva valoración (ej. 4.5/5): ").strip()
            if nuevo:
                elemento["valoracion"] = nuevo
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Presiona ENTER para continuar...")
            input()
            continue

        writeJson(ARCHIVO_JSON, datos)
        print("Elemento actualizado correctamente.")
        input("Presiona ENTER para continuar...")
      
