from db_setup import create_database
from crud import add_task, view_tasks, update_task

def main_menu():
    print("\nIniciando configuración inicial de la base de datos...")
    create_database()
    print("\n¡Configuración de la base de datos completada!")

    while True:
        print("\n--- Menú de Gestión de Tareas ---")
        print("1. Añadir nueva tarea")
        print("2. Ver todas las tareas")
        print("3. Actualizar tarea")
        print("4. Salir")
        
        choice = input("Introduce tu opción (1-4): ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            print("Saliendo de la aplicación. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, elige un número del 1 al 4.")

if __name__ == "__main__":
    # Este bloque se ejecuta cuando main_app.py es el script principal
    main_menu()