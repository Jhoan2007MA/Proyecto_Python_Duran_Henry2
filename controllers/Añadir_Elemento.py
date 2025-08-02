from app.config import ARCHIVO_JSON
from utils.corefiles import readJson, writeJson
import utils.screencontroler as sc 


def añadir_elemento():
    while True:
        sc.limpiarpantalla()
        print("===========================================")
        print("        Añadir un nuevo elemento")
        print("===========================================")
        print("¿Qué tipo de elemento deseas agregar?")
        print("1. Libro")
        print("2. Película")
        print("3. Música")
        print("4. Regresar al Menú Principal")
        print("===========================================")

        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            tipo = 'Libro'
            agregar_elemento(tipo)
        elif opcion == "2":
            tipo ='Pelicula'
            agregar_elemento(tipo)
        elif opcion == "3":
            tipo = 'Musica'
            agregar_elemento(tipo)
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Presiona ENTER para continuar...")
            input()


def agregar_elemento(categoria):
    sc.limpiarpantalla()
    print(f"=== Agregar nuevo elemento a la categoría: {categoria} ===\n")

    nombre = input("Nombre del elemento: ").strip()
    if not nombre:
        print(" El nombre no puede estar vacío.")
        input("Presiona ENTER para regresar...")
        return

    # Leer datos actuales
    datos = readJson(ARCHIVO_JSON)
    if not isinstance(datos, list):
        datos = []

    # Calcular nuevo ID
    ids_existentes = [item.get("id", 0) for item in datos if isinstance(item, dict)]
    nuevo_id = max(ids_existentes, default=0) + 1

    # Verificar duplicados (opcional, puedes quitar esto si no lo necesitas)
    for item in datos:
        if item.get("nombre", "").lower() == nombre.lower() and item.get("categoria") == categoria:
            print(" Ya existe un elemento con ese nombre en esta categoría.")
            input("Presiona ENTER para regresar...")
            return

    # Crear y agregar nuevo elemento
    nuevo_elemento = {
        "id": nuevo_id,
        "nombre": nombre,
        "categoria": categoria
    }
    datos.append(nuevo_elemento)
    writeJson(ARCHIVO_JSON, datos)

    print("\n✅ Elemento agregado correctamente.")
    print(f"ID: {nuevo_id} | Nombre: {nombre} | Categoría: {categoria}")
    input("\nPresiona ENTER para continuar...")

