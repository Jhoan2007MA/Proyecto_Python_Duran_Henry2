# 📚🎬🎵 Administrador de Colecciones

Este proyecto es una aplicación de consola desarrollada en Python para administrar una colección personal de elementos como libros, películas o música. Permite al usuario añadir, editar, eliminar, buscar, ver por categorías y guardar/cargar los datos de la colección.

## 🧾 Descripción

El sistema permite:

- 📥 **Agregar nuevos elementos** a tu colección.
- 📋 **Ver todos los elementos** registrados.
- 🔍 **Buscar elementos** por nombre o categoría.
- 🛠️ **Editar información** de los elementos existentes.
- ❌ **Eliminar elementos** no deseados.
- 🗂️ **Organizar elementos por categoría** (ej. libros, películas, música).
- 💾 **Guardar la colección** en un archivo JSON y **cargarla** al iniciar el programa.
- 🚪 **Salir** del sistema de forma segura.

Ideal para quienes desean llevar un registro digital de sus pertenencias multimedia.

---

## 🗂️ Estructura del Proyecto

```
PROYECTO_PYTHON_DURAN_HENRY2/
│
├── app/
│ └── main.py # Archivo principal con el menú y control del flujo del programa
│
├── controllers/ # Lógica de negocio y controladores
│ ├── Añadir_Elemento.py
│ ├── Buscar_Elemento.py
│ ├── Editar_Elemento.py
│ ├── Elemento_Categoria.py
│ ├── Eliminar_Elemento.py
│ ├── Guardar_y_Cargar.py
│ ├── Salir.py
│ └── Ver_Elementos.py
│
├── utils/ # Utilidades auxiliares
│ ├── corefiles.py
│ ├── screencontroller.py
│ └── validatedata.py
│
└── README.md # Archivo de documentación
```

## ▶️ Cómo usar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/colecciones-python.git
   cd colecciones-python

## 📦 Requisitos

- Python 3.x
- No requiere paquetes externos (usa librerías estándar)

------

## ✅ Estado del Proyecto

✅ Funcionalidades completas
 🚧 Potenciales mejoras futuras:

- Interfaz gráfica con Tkinter o PyQt
- Exportación a formatos CSV o PDF
- Búsqueda avanzada por múltiples filtros

------

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

------

## 🙌 Autores

Henry Duran -- Sergio Abril 
 Proyecto académico de programación en Python

