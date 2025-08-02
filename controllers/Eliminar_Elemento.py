from app.config import ARCHIVO_JSON
import json
import os
import utils.screencontroler as sc


def eliminar_elemento():
    while True:
        sc.limpiarpantalla()
        print("===========================================")
        print("        Eliminar un elemento")
        print("===========================================")
        print("¿Cómo deseas eliminar?")
        print("1. Eliminar por título")
        print("2. Eliminar por Identificador Único")
        print("3. Regresar al Menú Principal")
        print("===========================================")
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            eliminar_por_titulo()
        elif opcion == "2":
            eliminar_por_id()
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Presiona ENTER para continuar...")
            input()


def cargar_datos():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    return []


def guardar_datos(datos):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def eliminar_por_titulo():
    sc.limpiarpantalla()
    datos = cargar_datos()
    titulo = input("Ingresa el título del elemento a eliminar: ")

    nuevo_datos = [item for item in datos if item.get("nombre") != titulo]

    if len(nuevo_datos) < len(datos):
        guardar_datos(nuevo_datos)
        print(f"Elemento con título '{titulo}' eliminado correctamente.")
    else:
        print(f"No se encontró ningún elemento con el título '{titulo}'.")

    input("Presiona ENTER para continuar...")


def eliminar_por_id():
    sc.limpiarpantalla()
    datos = cargar_datos()
    identificador = input("Ingresa el identificador único del elemento a eliminar: ")

    nuevo_datos = [item for item in datos if str(item.get("id")) != identificador]

    if len(nuevo_datos) < len(datos):
        guardar_datos(nuevo_datos)
        print(f"Elemento con ID '{identificador}' eliminado correctamente.")
    else:
        print(f"No se encontró ningún elemento con el ID '{identificador}'.")

    input("Presiona ENTER para continuar...")
