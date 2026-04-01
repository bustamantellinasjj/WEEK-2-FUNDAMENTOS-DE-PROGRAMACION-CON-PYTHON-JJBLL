# WEEK-2-FUNDAMENTOS-DE-PROGRAMACION-CON-PYTHON-JJBLL

# Inventory Management System (Python)

Sistema de inventario en consola desarrollado en Python que permite gestionar productos mediante un menú interactivo. Implementa buenas prácticas como modularidad, validación de datos y separación de responsabilidades.

---

## Features

- CRUD completo de productos (Create, Read, Update, Delete)
- Validación de entradas del usuario
- Cálculo de estadísticas del inventario
- Persistencia de datos en archivos CSV
- Arquitectura modular

---

## Tech Stack

- Python 3  
- Listas y diccionarios  
- Control de flujo (`if`, `while`, `for`)  
- Manejo de errores (`try/except`)  
- Archivos CSV  

---

## Project Structure

```
 inventory-system
 ┣  main.py        # Punto de entrada
 ┣  menu.py        # Interfaz y flujo
 ┣  servicios.py   # Lógica del negocio
 ┗  archivos.py    # Manejo de CSV
```

---

## How to Run

```bash
git clone https://github.com/your-username/inventory-system.git
cd inventory-system
python main.py
```

---

## Functionalities

- Agregar productos  
- Mostrar inventario  
- Buscar productos  
- Actualizar datos  
- Eliminar productos  
- Ver estadísticas  
- Guardar en CSV  
- Cargar desde CSV  

---

## Validations

- Campos no vacíos  
- Números positivos  
- Manejo de errores  
- Control de opciones inválidas  

---

## Design Principles

- Separación de responsabilidades  
- Código modular  
- Funciones reutilizables  
- Legibilidad  

---

## Future Improvements

- Interfaz gráfica (GUI)  
- Base de datos  
- Programación orientada a objetos  
- Exportación a otros formatos  

---

## Author

Juan José Bustamante  

---

## Notes

Proyecto académico que evidencia la evolución desde lógica básica (semana 2) hacia una estructura modular y escalable (semana 3).
