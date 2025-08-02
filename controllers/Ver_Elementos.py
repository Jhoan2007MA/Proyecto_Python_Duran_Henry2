from app.config import ARCHIVO_JSON
import utils.screencontroler as sc

def ver_elementos(coleccion):
    while True:
        sc.limpiarpantalla()
        print("===========================================")
        print("         Ver Todos los Elementos")
        print("===========================================")
        print("¿Qué categoría deseas ver?                 ")
        print("1. Ver Todos los Libros                    ")
        print("2. Ver Todas las Películas                 ")
        print("3. Ver Toda la Música                      ")
        print("4. Regresar al Menú Principal              ")
        print("===========================================")
        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            mostrar_por_categoria(coleccion, "libro")
        elif opcion == "2":
            mostrar_por_categoria(coleccion, "pelicula")
        elif opcion == "3":
            mostrar_por_categoria(coleccion, "musica")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            input("Presiona ENTER para intentarlo de nuevo...")

def mostrar_por_categoria(coleccion, categoria):
    sc.limpiarpantalla()
    elementos_filtrados = [e for e in coleccion if e.get("tipo") == categoria]

    if not elementos_filtrados:
        print(f" No hay elementos en la categoría '{categoria.title()}'.")
    else:
        print(f"Elementos en la categoría: {categoria.title()}")
        print("===========================================")
        for idx, elemento in enumerate(elementos_filtrados, start=1):
            print(f"{idx}. Título   : {elemento.get('titulo', '-')}")
            if categoria == "libro":
                print(f"   Autor    : {elemento.get('autor', '-')}")
            elif categoria == "musica":
                print(f"   Artista  : {elemento.get('artista', '-')}")
            elif categoria == "pelicula":
                print(f"   Director : {elemento.get('director', '-')}")
            print(f"   Año      : {elemento.get('anio', '-')}")
            print("-------------------------------------------")

    input("Presiona ENTER para volver al menú...")