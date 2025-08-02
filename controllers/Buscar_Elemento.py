import utils.screencontroler as sc
from utils.corefiles import readJson
from app.config import ARCHIVO_JSON

def buscar_elemento():
    while True:
        sc.limpiarpantalla()
        print("========================================")
        print("          Buscar un Elemento            ")
        print("========================================")
        print("¿Qué deseas buscar?")
        print("1. Buscar por Título")
        print("2. Buscar por Autor/Director/Artista")
        print("3. Buscar por Género")
        print("4. Regresar al menú principal")
        print("========================================")
        Opciones = input("Seleccione una opción: ").strip()

        match Opciones:
            case "1":
                Buscar("nombre", "Nombre")
            case "2":
                Buscar("autor", "Autor / Director / Artista")
            case "3":
                Buscar("genero", "Género")
            case "4":
                break
            case _:
                print("Opción inválida.")
                sc.pausar_pantalla()

def Buscar(clave, etiqueta):
    sc.limpiarpantalla()
    coleccion = readJson(ARCHIVO_JSON)

    if not coleccion:
        print("No hay elementos registrados.")
        sc.pausar_pantalla()
        return

    termino = input(f"Ingrese el {etiqueta} a buscar: ").strip().lower()
    encontrados = []

    for e in coleccion:
        tipo = e.get("categoria", "").lower()
        valor_clave = e.get(clave, "").lower()

        if not valor_clave:
            continue

        autor_label = {
            "libro": "Autor",
            "película": "Director",
            "música": "Artista"
        }.get(tipo, "Autor")

        if termino in valor_clave:
            encontrados.append((e, autor_label))

    if not encontrados:
        print("No se encontraron coincidencias.")
    else:
        print(" Resultados encontrados:")
        for i, (item, etiqueta_autor) in enumerate(encontrados, 1):
            print(f"{i}. Título: {item.get('nombre', 'N/A')}")
            print(f"   {etiqueta_autor}: {item.get('autor', 'N/A')}")
            print(f"   Género: {item.get('genero', 'N/A')}")
            print(f"   Valoración: {item.get('calificacion', 'N/A')}\n")

    sc.pausar_pantalla()
