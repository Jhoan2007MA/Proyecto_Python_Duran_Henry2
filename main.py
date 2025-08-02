import sys
import utils.screencontroler as sc
from controllers import Añadir_Elemento, Buscar_Elemento, Editar_Elemento, Elemento_Categoria, Eliminar_Elemento, Guardar_y_Cargar, Ver_Elementos
import app.config as config

def main():
    while True:
        sc.limpiarpantalla()
        print("===========================================")
        print("           Coleccion                       ")
        print("===========================================")
        print("1. Añadir Elemento")
        print("2. Buscar Elemento")
        print("3. Editar Elemento")
        print("4. Ver por Categoría")
        print("5. Ver Todos los Elementos")
        print("6. Eliminar Elemento")
        print("7. Guardar/Cargar Datos")
        print("8. Salir")
        print("===========================================")
        opcion = input("Selecciona una opción (1-8): ")

        if opcion == "1":
            Añadir_Elemento.añadir_elemento()
        elif opcion == "2":
            Buscar_Elemento.buscar_elemento()
        elif opcion == "3":
            Editar_Elemento.editar_elemento()
        elif opcion == "4":
            Elemento_Categoria.ver_elementos_por_categoria()
        elif opcion == "5":
            Ver_Elementos.ver_elementos()
        elif opcion == "6":
            Eliminar_Elemento.eliminar_elemento()
        elif opcion == "7":
            Guardar_y_Cargar.guardarycargar()
        elif opcion == "8":
            sys.exit()
        else:
            print("Opción inválida. Presiona ENTER para intentar de nuevo...")
            input()

if __name__ == "__main__":
    main()
