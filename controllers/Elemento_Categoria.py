from app.config import ARCHIVO_JSON, MUSICA_JSON, PELICULA_JSON, LIBRO_JSON
import os
import json
import utils.screencontroler as sc

# Función para cargar datos desde múltiples archivos JSON y combinarlos en una lista
def cargar_datos():
    sc.limpiarpantalla()
    coleccion = []

    rutas = [ARCHIVO_JSON, MUSICA_JSON, PELICULA_JSON, LIBRO_JSON]
    for ruta in rutas:
        if os.path.exists(ruta):
            with open(ruta, 'r', encoding='utf-8') as f:
                try:
                    datos = json.load(f)
                    if isinstance(datos, list):
                        coleccion.extend(datos)
                    else:
                        coleccion.append(datos)
                except json.JSONDecodeError:
                    print(f"Error al leer el archivo {ruta}. Archivo corrupto o vacío.")
    return coleccion

# Función para guardar la colección completa en un único archivo JSON principal
def guardar_datos(coleccion):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as f:
        json.dump(coleccion, f, indent=4, ensure_ascii=False)
    print("Datos guardados correctamente.")

# Función para mostrar elementos filtrados por categoría
def elementos_categoria(coleccion):
    sc.limpiarpantalla()
    categoria = input("Introduce el nombre de la categoría para ver (Libro, Película, Música): ").lower()
    encontrados = [elem for elem in coleccion if elem.get('tipo', '').lower() == categoria]

    if encontrados:
        print(f"\nElementos en la categoría '{categoria}':")
        for i, elem in enumerate(encontrados, 1):
            print(f"{i}. {elem}")
    else:
        print(f"No se encontraron elementos en la categoría '{categoria}'.")
