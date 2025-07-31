from app.gestor import cargar_datos, añadir_elemento, ver_elementos, buscar_elemento, editar_elemento, eliminar_elemento, Elementos_categoria, Guardar_y_Cargar, Salir
def mostrar_menu():
    print ('====================================')
    print ('     Administrador de Coleccion     ')
    print ('====================================')
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

def main ():
    coleccion = cargar_datos()
    while True:
        mostrar_menu()
        opcion = input('seleccione una opcion :')
        print()

        if opcion == "1":
            añadir_elemento(coleccion)
        elif opcion == "2":
            ver_elementos(coleccion)
        elif opcion == "3":
            buscar_elemento(coleccion)
        elif opcion == "4":
            editar_elemento(coleccion)
        elif opcion == "5":
            eliminar_elemento(coleccion)
        elif opcion == "6":
            Elementos_categoria(coleccion)
        elif opcion == "7":
            Guardar_y_Cargar(coleccion)
        elif opcion == "8":
            Salir(coleccion)
            break
        else:
            print('opcion invalida intenytar de nuevo')

if __name__=="__main__":
    main()