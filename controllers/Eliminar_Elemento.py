from app.config import ARCHIVO_JSON, MUSICA_JSON, PELICULA_JSON, LIBRO_JSON
import json
import os
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

def eliminar_elemento(coleccion):
    titulo = input("Introduce el título del elemento a eliminar: ").lower()
    for i, elem in enumerate(coleccion):
        if elem["titulo"].lower() == titulo:
            confirmacion = input(f"¿Estás seguro de eliminar '{elem['titulo']}'? (s/n): ")
            if confirmacion.lower() == "s":
                coleccion.pop(i)
                Guardar_datos(coleccion)
                print("Elemento eliminado.")
                return
    print("Elemento no encontrado.") 
    os.system('clear')