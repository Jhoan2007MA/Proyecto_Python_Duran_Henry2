from app.config import ARCHIVO_JSON, MUSICA_JSON, PELICULA_JSON, LIBRO_JSON
import json
import os
import utils.screencontroler as sc

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
                    print(f"⚠️  Error al leer el archivo {ruta}.")
    return coleccion

def guardar_datos(coleccion):
    # Guardar todo en un archivo principal
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as f:
        json.dump(coleccion, f, indent=4, ensure_ascii=False)
    
    # Separar por tipo
    libros = [e for e in coleccion if e.get("tipo", "").lower() == "libro"]
    peliculas = [e for e in coleccion if e.get("tipo", "").lower() == "película"]
    musica = [e for e in coleccion if e.get("tipo", "").lower() == "música"]

    with open(LIBRO_JSON, 'w', encoding='utf-8') as f:
        json.dump(libros, f, indent=4, ensure_ascii=False)
    with open(PELICULA_JSON, 'w', encoding='utf-8') as f:
        json.dump(peliculas, f, indent=4, ensure_ascii=False)
    with open(MUSICA_JSON, 'w', encoding='utf-8') as f:
        json.dump(musica, f, indent=4, ensure_ascii=False)

    print("✅ Colección guardada correctamente en todos los archivos.")

def guardar_y_cargar():
    coleccion = cargar_datos()
    guardar_datos(coleccion)
