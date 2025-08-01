from controllers import Añadir_Elemento, Buscar_Elemento, Editar_Elemento, Elemento_Categoria, Eliminar_Elemento, Guardar_y_Cargar, Salir, Ver_Elementos

def mostrar_menu():
    print('====================================')
    print('     Administrador de Coleccion     ')
    print('====================================')
    print('1. Añadir un Nuevo Elemento')
    print('2. Ver Todos los Elementos')
    print('3. Buscar un Elemento')
    print('4. Editar un Elemento')
    print('5. Eliminar un Elemento')
    print('6. Ver Elementos por Categoria')
    print('7. Guardar y Cargar coleccion')
    print('8. Salir')
    print('====================================')
    print('Selecciona una opcion del 1-8. Gracias')
    print()

def main():
     Añadir_Elemento.readJson()
while True:
        mostrar_menu()
        opcion = input('Seleccione una opción: ')
        print()

        if opcion == "1":
            Añadir_Elemento.agregar_elemento()
        elif opcion == "2":
            Ver_Elementos.Ver_Elementos()
        elif opcion == "3":
            Buscar_Elemento.Buscar_Elemento()
        elif opcion == "4":
            Editar_Elemento.editar_Elemento()
        elif opcion == "5":
            Eliminar_Elemento.eliminar_elemento()
        elif opcion == "6":
            Elemento_Categoria.elementos_categoria()
        elif opcion == "7":
            Guardar_y_Cargar.Guardar_datos()
        elif opcion == "8":
            Salir.Salir()
            break
        else:
            print('Opción inválida. Intenta de nuevo.')

if __name__ == "__main__":
    main()