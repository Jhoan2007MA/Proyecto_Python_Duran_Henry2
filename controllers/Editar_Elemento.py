from app.config import ARCHIVO_JSON, MUSICA_JSON, PELICULA_JSON, LIBRO_JSON
import os
import json
import utils.screencontroler as sc 

def Cargar_Datos():
    sc.limpiarpantalla()
    if os.path.exists(ARCHIVO_JSON,MUSICA_JSON,PELICULA_JSON,LIBRO_JSON):
        with open(ARCHIVO_JSON,MUSICA_JSON,PELICULA_JSON,LIBRO_JSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    return [] 

def Guardar_datos(coleccion):
    with open(ARCHIVO_JSON,MUSICA_JSON,PELICULA_JSON,LIBRO_JSON ,'w', encoding='utf-8') as f:
        json.dump(coleccion, f, indent=4, ensure_ascii=False)

def editar_elemento(coleccion):
    sc.limpiarpantalla()
    titulo = input("Introduce el título del elemento a editar: ").lower()
    for elem in coleccion:
        if elem["titulo"].lower() == titulo:
            print("Elemento encontrado. Deja vacío si no deseas cambiar un campo.")
            nuevo_titulo = input(f"Título actual: {elem['titulo']} > ")
            nuevo_autor = input(f"Autor actual: {elem['autor']} > ")
            nuevo_genero = input(f"Género actual: {elem['genero']} > ")
            nueva_valoracion = input(f"Valoración actual: {elem.get('valoracion', 'N/A')} > ")

            if nuevo_titulo: elem["titulo"] = nuevo_titulo
            if nuevo_autor: elem["autor"] = nuevo_autor
            if nuevo_genero: elem["genero"] = nuevo_genero
            if nueva_valoracion: elem["valoracion"] = nueva_valoracion

            Guardar_datos(coleccion)
            print("Elemento actualizado.")
            return
    print("Elemento no encontrado.")
    os.system('clear')