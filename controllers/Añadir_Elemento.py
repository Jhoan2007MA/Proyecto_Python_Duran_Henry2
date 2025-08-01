from app.config import ARCHIVO_JSON
from utils.corefiles import readJson, writeJson
import utils.screencontroler as sc 

def agregar_elemento():
    while True:
        sc.limpiarpantalla()
        print("========================================")
        print("       Añadir un Nuevo Elemento         ")
        print("========================================")
        print("¿Qué tipo de elemento deseas añadir?")
        print("1. Libro")
        print("2. Película")
        print("3. Música")
        print("4. Regresar al menú principal")
        print("========================================")
        print('Seleccione una opcion del (1-3)')


tipos ={
    "1": ("Libro", "Autor"),
            "2": ("Película", "Director"),
            "3": ("Música", "Artista")
    }

tipo_info = tipos.get()
if not tipo_info:
    print("Opción inválida")
    sc.pausar_pantalla()

tipo, etiqueta_autor = tipo_info
print(f" Añadiendo nuevo {tipo}")

titulo = input("Título: ").strip()
autor = input(f"{etiqueta_autor}: ").strip()
genero = input("Género: ").strip()

if not titulo or not autor or not genero:
    print("Título, autor/director/artista y género no pueden estar vacios")
    sc.pausar_pantalla() 

    while True:
            valoracion = input("Valoración (1 a 10): ").strip()
            if valoracion == "":
                valoracion = None
                break
            if valoracion.isdigit():
                valoracion_num = int(valoracion)
                if 1 <= valoracion_num <= 10:
                    break
            print("Valoración inválida. Debe ser un número del 1 al 10 o dejarlo vacío.")

    nuevo = {
            "tipo": tipo,
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "valoracion": valoracion 
        }

coleccion = readJson(ARCHIVO_JSON)
coleccion.append(nuevo)
writeJson(ARCHIVO_JSON, coleccion)
print(f"{tipo} agregado correctamente")
sc.pausar_pantalla()