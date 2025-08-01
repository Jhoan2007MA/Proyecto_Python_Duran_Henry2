from app.config import ARCHIVO_JSON, MUSICA_JSON, PELICULA_JSON, LIBRO_JSON
import json
import os
import utils.screencontroler as sc 

tipo = ''
def mostrar_menu():
    print('===========================================')
    print('        Añadir un Nuevo Elemento           ')
    print('===========================================')
    print('¿Qué tipo de elemento deseas añadir?')
    print('1. Libro')
    print('2. Película')
    print('3. Música')
    print('4. Regresar al Menú Principal')
    print('===========================================')
    print('Selecciona una opción (1-4):')
    opcion = input("Elija una opción: ").strip()
    match opcion:
        case 1:
            tipo = 'Libro'
            return(tipo)
        case 2:
            pass



def Cargar_Datos():
    sc.limpiarpantalla()
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    return [] 


def Guardar_datos(coleccion):
    with open(ARCHIVO_JSON,'w', encoding='utf-8') as f:
        json.dump(coleccion, f, indent=4, ensure_ascii=False) 
        

def Anadir_Elemento(coleccion,tipo):
    tipo_2 = mostrar_menu()
    titulo = input("Título: ")
    autor = input("Autor/Director/Artista: ")
    genero = input("Género: ")
    valoracion = input("Valoración (opcional): ")

    elemento = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "categoria": tipo ,
        "valoracion": valoracion if valoracion else None
    }
    coleccion.append(elemento)
    Guardar_datos(coleccion)
    print("Elemento añadido correctamente.")