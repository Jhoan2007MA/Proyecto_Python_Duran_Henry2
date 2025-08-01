import utils.screencontroler as sc
from utils.corefiles import readJson, writeJson
from app.config import ARCHIVO_JSON

def editar_Elemento():
    while True:
        sc.limpiarpantalla()
        coleccion = readJson(ARCHIVO_JSON)
        if not coleccion:
            print("No hay elementos para editar.")
            sc.pausar_pantalla()
            return

        tituloBuscar = input("Ingrese el Título del elemento que desea editar: ").strip().lower()
        encontrado = None
        for i, e in enumerate(coleccion):
            if tituloBuscar in e["titulo"].lower():
                encontrado = (i, e)
                break

        if not encontrado:
            print(" No se encontro el elemento.")
            sc.pausar_pantalla()
            return

        index, elemento = encontrado
        tipo = elemento["tipo"].lower()
        autor_label = {
            "libro": "Autor",
            "película": "Director",
            "música": "Artista"
        }.get(tipo, "Autor")

        while True:
            sc.limpiarpantalla()
            print("========================================")
            print("          Editar un Elemento            ")
            print("========================================")
            print(f"Título actual: {elemento['titulo']}    ")
            print(f"{autor_label} actual: {elemento['autor']}")
            print(f"Género actual: {elemento['genero']}")
            print(f"Valoración actual: {elemento['valoracion']}")
            print("========================================")
            print("¿Qué tipo de cambio deseas realizar?")
            print("1. Editar Título")
            print(f"2. Editar {autor_label}")
            print("3. Editar Género")
            print("4. Editar Valoración")
            print("5. Regresar al menú anterior")
            print("========================================")
            editar = input("Seleccione una opción: ").strip()

            match editar:
                case "1":
                    nuevo = input("Nuevo Título: ").strip()
                    if nuevo:
                        elemento["titulo"] = nuevo
                case "2":
                    nuevo = input(f"Nuevo {autor_label}: ").strip()
                    if nuevo:
                        elemento["autor"] = nuevo
                case "3":
                    nuevo = input("Nuevo Género: ").strip()
                    if nuevo:
                        elemento["genero"] = nuevo
                case "4":
                    try:
                        nuevaValoracion = float(input("Nueva Valoración (0.0 - 5.0): ").strip())
                        if 0 <= nuevaValoracion <= 5:
                            elemento["valoracion"] = nuevaValoracion
                        else:
                            print("Valoración fuera de rango.")
                    except ValueError:
                        print("Valor inválido.")
                case "5":
                    break
                case _:
                    print("Opción no válida.")
            
        
            coleccion[index] = elemento
            writeJson(ARCHIVO_JSON, coleccion)
            print("\n Cambios guardados.")
            sc.pausar_pantalla()

