from app.config import ARCHIVO_JSON, MUSICA_JSON, PELICULA_JSON, LIBRO_JSON
import json
import os
import utils.screencontroler as sc

def cargar_datos():
    sc.limpiarpantalla()
    if os.path.exists(ARCHIVO_JSON,MUSICA_JSON,PELICULA_JSON,LIBRO_JSON):
        with open(ARCHIVO_JSON,MUSICA_JSON,PELICULA_JSON,LIBRO_JSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    return [] 


def Guardar_datos(coleccion):
    with open(ARCHIVO_JSON,MUSICA_JSON,PELICULA_JSON,LIBRO_JSON ,'w', encoding='utf-8') as f:
        json.dump(coleccion, f, indent=4, ensure_ascii=False)
        
def Ver_Elementos(coleccion):
    sc.limpiarpantalla()
    if not coleccion:
        print("No hay elementos en la colección.")
    else:
        print("Elementos en la colección:\n")
        for idx, elemento in enumerate(coleccion, 1):
            print(f"{idx}. {elemento}")
    input("Presiona Enter para continuar...")
    