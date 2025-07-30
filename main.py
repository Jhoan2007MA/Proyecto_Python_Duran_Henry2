from app.gestor import cargar_datos, añadir_elemento, ver_elementos, buscar_elemento, editar_elemento, eliminar_elemento, Elementos_categoria, Guardar_y_Cargar, Salir
def mostrar_menu():
    print ('=== Coleccion Multimedia ===')
    print ('1. añadir un  nuevo elemento')
    print ('2. ver todos los elementos')
    print ('3. buscar un elemento')
    print ('4. editar un elemento')
    print ('5. editar un elemento')
    print ('6. ver elementos por categoria')
    print ('7. guardar y cargar colecccion')
    print ('8. salir')
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