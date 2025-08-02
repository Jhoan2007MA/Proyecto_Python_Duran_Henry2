import utils.screencontroler as sc
from utils.corefiles import readJson
from app.config import ARCHIVO_JSON


def ver_elementos_por_categoria():
    while True:
        sc.limpiarpantalla()
        print("===========================================")
        print("        Ver elementos por categoría")
        print("===========================================")
        print("¿Qué categoría deseas ver?")
        print("1. Ver Libros")
        print("2. Ver Películas")
        print("3. Ver Música")
        print("4. Regresar al Menú Principal")
        print("===========================================")
        opcion = input("Selecciona una opción (1-4): ")

        datos = readJson(ARCHIVO_JSON)

        if opcion == "1":
            mostrar_categoria(datos, "Libros")
        elif opcion == "2":
            mostrar_categoria(datos, "Películas")
        elif opcion == "3":
            mostrar_categoria(datos, "Música")
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Presiona ENTER para intentar nuevamente.")
            input()


def mostrar_categoria(datos, categoria):
    sc.limpiarpantalla()
    print(f"======= Elementos en categoría: {categoria} =======")
    encontrados = False
    for elemento in datos:
        if elemento.get("categoria") == categoria:
            encontrados = True
            print(f"- {elemento.get('nombre', 'Nombre no disponible')}")
    if not encontrados:
        print("No se encontraron elementos en esta categoría.")
    input("\nPresiona ENTER para continuar...")

