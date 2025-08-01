from app.config import ARCHIVO_JSON, MUSICA_JSON, PELICULA_JSON, LIBRO_JSON
import os 
import utils.screencontroler as sc
import json

def Cargar_Datos():
    sc.limpiarpantalla()
    if os.path.exists(ARCHIVO_JSON,MUSICA_JSON,PELICULA_JSON,LIBRO_JSON):
        with open(ARCHIVO_JSON,MUSICA_JSON,PELICULA_JSON,LIBRO_JSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    return [] 

def Guardar_datos(coleccion):
    with open(ARCHIVO_JSON,MUSICA_JSON,PELICULA_JSON,LIBRO_JSON ,'w', encoding='utf-8') as f:
        json.dump(coleccion, f, indent=4, ensure_ascii=False)
        
def buscar_elemento(coleccion):
    sc.limpiarpantalla()
    criterio = input("Buscar por (1) Título o (2) Autor/Género: ")
    termino = input("Introduce el término de búsqueda: ").lower()

    if criterio == "1":
        resultados = [e for e in coleccion if termino in e["titulo"].lower()]
    else:
        resultados = [e for e in coleccion if termino in e["autor"].lower() or termino in e["genero"].lower()]

    if resultados:
        for e in resultados:
            print(f"{e['titulo']} - {e['autor']} ({e['categoria']}) | Género: {e['genero']} | Valoración: {e.get('valoracion', 'N/A')}")
    else:
        print("No se encontraron resultados.\n")
    print()
    os.system('clear')