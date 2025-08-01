from controllers import Añadir_Elemento, Buscar_Elemento, Editar_Elemento, Elemento_Categoria, Eliminar_Elemento, Guardar_y_Cargar, Salir, Ver_Elementos
def mostrar_menu():
    print ('====================================')
    print ('     Administrador de Coleccion     ')
    print ('===================================')
    print ('1. Añadir un Nuevo Elemento ')
    print ('2. Ver Todos los Elementos  ')
    print ('3. Buscar un Elemento ')
    print ('4. Editar un Elemento ')
    print ('5. Eliminar un Elemento ')
    print ('6. Ver Elementos por Categoria ')
    print ('7. Guardar y Cargar coleccion ')
    print ('8. salir')
    print ('====================================')
    print ('Selecciona una opcion del 1-8. Gracias')
    print()

    def mostrar_menu():
        coleccion = Añadir_Elemento.Cargar_Datos()
        while True:
            Añadir_Elemento.mostrar_menu()
            opcion = input('seleccione una opcion :')
            print()

            if opcion == "1":
                Añadir_Elemento(coleccion)
            elif opcion == "2":
                Ver_Elementos(coleccion)
            elif opcion == "3":
                Buscar_Elemento(coleccion)
            elif opcion == "4":
                Editar_Elemento(coleccion)
            elif opcion == "5":
                Eliminar_Elemento(coleccion)
            elif opcion == "6":
                Elemento_Categoria(coleccion)
            elif opcion == "7":
                Guardar_y_Cargar(coleccion)
            elif opcion == "8":
                Salir(coleccion)
                break
            else:
                print('opcion invalida intenytar de nuevo')

    if __name__=="__main__":
     mostrar_menu()