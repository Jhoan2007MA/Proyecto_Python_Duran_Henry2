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
        opcion = input("Selecciona una opción (1-4): ").strip()

        datos = readJson(ARCHIVO_JSON)

        if opcion == "1":
            mostrar_categoria(datos, "libro")
        elif opcion == "2":
            mostrar_categoria(datos, "pelicula")
        elif opcion == "3":
            mostrar_categoria(datos, "musica")
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Presiona ENTER para intentar nuevamente.")
            input()

def mostrar_categoria(datos, categoria):
    sc.limpiarpantalla()
    print(f"======= Elementos en la categoría: {categoria.title()} =======\n")
    encontrados = False

    for elemento in datos:
        if elemento.get("categoria", "").lower() == categoria:
            encontrados = True
            print(f"- Título    : {elemento.get('nombre', 'N/A')}")
            print(f"  Autor     : {elemento.get('autor', 'N/A')}")
            print(f"  Género    : {elemento.get('genero', 'N/A')}")
            print(f"  Valoración: {elemento.get('calificacion', 'N/A')}")
            print("-------------------------------------------")

    if not encontrados:
        print("No se encontraron elementos en esta categoría.")

    input("\nPresiona ENTER para continuar...")
