import json
import os

ARCHIVO_JSON = 'datos.json'
MUSICA_JSON = 'musica.json'
PELICULA_JSON = 'pelicula.json'
LIBRO_JSON = 'libro.json'

def cargar_datos():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def Guardar_datos(coleccion):
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as f:
        json.dump(coleccion, f, indent=4, ensure_ascii=False)

def añadir_elemento(coleccion):
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
    print("Elemento añadido correctamente.\n")

def ver_elementos(coleccion):
    if not coleccion:
        print("No hay elementos en la colección.\n")
        return

    filtro = input("¿Deseas filtrar por (1) Categoría, (2) Género o (Enter) para ver todo? ")
    if filtro == "1":
        categoria = input("Introduce la categoría: ").lower()
        filtrado = [e for e in coleccion if e["categoria"].lower() == categoria]
    elif filtro == "2":
        genero = input("Introduce el género: ").lower()
        filtrado = [e for e in coleccion if e["genero"].lower() == genero]
    else:
        filtrado = coleccion

    for i, elem in enumerate(filtrado, 1):
        print(f"{i}. {elem['titulo']} ({elem['categoria'].capitalize()}) - {elem['autor']} | Género: {elem['genero']} | Valoración: {elem.get('valoracion', 'N/A')}")
    print()

def buscar_elemento(coleccion):
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

def editar_elemento(coleccion):
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
            print("Elemento actualizado.\n")
            return
    print("Elemento no encontrado.\n")

def eliminar_elemento(coleccion):
    titulo = input("Introduce el título del elemento a eliminar: ").lower()
    for i, elem in enumerate(coleccion):
        if elem["titulo"].lower() == titulo:
            confirmacion = input(f"¿Estás seguro de eliminar '{elem['titulo']}'? (s/n): ")
            if confirmacion.lower() == "s":
                coleccion.pop(i)
                Guardar_datos(coleccion)
                print("Elemento eliminado.\n")
                return
    print("Elemento no encontrado.\n") 
    
def Elementos_categoria(coleccion):
    Categoria = input("Introduce el nombre de la categoria para ver : ")
    for i, elem in enumerate(coleccion):
        if elem['Categoria'].lower() == Categoria:
            
        
    
    
    
    
    
def Guardar_y_Cargar(coleccion):
    Guardar_datos(coleccion)

def Salir(coleccion):
    Guardar_datos(coleccion)
    
            