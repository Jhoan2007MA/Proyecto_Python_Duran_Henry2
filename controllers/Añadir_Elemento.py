from app.config import ARCHIVO_JSON, MUSICA_JSON, PELICULA_JSON, LIBRO_JSON
import json
import os 

def cargar_datos():
    if os.path.exists(ARCHIVO_JSON,MUSICA_JSON,PELICULA_JSON,LIBRO_JSON ):
            with open(ARCHIVO_JSON,MUSICA_JSON,PELICULA_JSON,LIBRO_JSON  'r', encoding='utf-8') as f:
            return json.load(f)
    return [] 


def Guardar_datos(coleccion):
    with open(ARCHIVO_JSON,MUSICA_JSON,PELICULA_JSON,LIBRO_JSON 'w', encoding='utf-8') as f:
        json.dump(coleccion, f, indent=4, ensure_ascii=False)
        

def Añadir_Elemento(coleccion):
    titulo = input("Título: ")
    autor = input("Autor/Director/Artista: ")
    genero = input("Género: ")
    categoria = input("Categoría (libro/película/música): ")
    valoracion = input("Valoración (opcional): ")

    elemento = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "categoria": categoria,
        "valoracion": valoracion if valoracion else None
    }
    coleccion.append(elemento)
    Guardar_datos(coleccion)
    print("Elemento añadido correctamente.")