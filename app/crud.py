from mysql.connector import Error
from db_setup import db_connection
from cache_service import get_cache, set_cache, invalidate_cache

# Clave de caché para todas las tareas
ALL_TASKS_CACHE_KEY = "all_tasks"

#Funciones CRUD de Tareas
def add_task():
    conn = db_connection()
    if not conn:
        return

    try:
        title = input("Título de la tarea: ").strip()
        if not title:
            print("El título no puede estar vacío.")
            return
        cursor = conn.cursor()
        query = "INSERT INTO tasks (title) VALUES (%s)"
        task_data = (title,)
        cursor.execute(query, task_data)
        conn.commit()
        print(f"Tarea '{title}' añadida con éxito. ID: {cursor.lastrowid}")

        #Invalida la caché después de una modificación
        invalidate_cache(ALL_TASKS_CACHE_KEY)

    except Error as e:
        print(f"Error al añadir tarea: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

def view_tasks():
    # Intentar obtener las tareas de la caché
    cached_tasks_data = get_cache(ALL_TASKS_CACHE_KEY)
    if cached_tasks_data:
        print("\n--- Lista de Tareas (desde caché) ---")
        tasks = cached_tasks_data
    else:
        # Si no están en caché, obtener de la base de datos
        conn = db_connection()
        if not conn:
            return

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title,status FROM tasks ORDER BY CASE WHEN status='Pendiente' THEN 1 WHEN status='Completado' THEN 2 END ASC")
            tasks = cursor.fetchall()
            if not tasks:
                print("\nNo hay tareas registradas.")
                return
            
            # Convertir las tuplas de la base de datos a un formato más manejable
            tasks_to_redis = []
            for task_row in tasks:
                tasks_to_redis.append({
                    "id": task_row[0],
                    "title": task_row[1],
                    "status": task_row[2]
                })
            # Almacenar las tareas en caché para futuras solicitudes
            set_cache(ALL_TASKS_CACHE_KEY, tasks)
            print("\n--- Lista de Tareas (desde DB y almacenadas en caché) ---")
        except Error as e:
            print(f"Error al ver tareas: {e}")
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()
    
    # Si hay tareas (ya sea de caché o DB), imprimirlas
    if tasks:
            print("\n--- Lista de Tareas ---")
            # Formato para la cabecera de la tabla
            print("{:<5} {:<30} {:<15}".format("ID", "Título","Estado"))
            print("-" * 125) # Línea separadora

            for task in tasks:
                # Formato para cada fila de tarea
                print("{:<5} {:<30} {:<15}".format(
                    task[0], task[1], task[2]
                ))
            print("-" * 125)

def update_task():
    conn = db_connection()
    if not conn:
        return

    try:
        task_id =input("Introduce el ID de la tarea a actualizar: ").strip()
        if not task_id.isdigit():
            print("ID de tarea inválido. Debe ser un número.")
            return

        task_id = int(task_id)
        cursor = conn.cursor(buffered=True) # buffered=True para permitir múltiples fetchone()/execute()

        # Verificar si la tarea existe
        cursor.execute("SELECT id, title, status FROM tasks WHERE id = %s", (task_id,))
        task_exists = cursor.fetchone()
        if not task_exists:
            print(f"No se encontró ninguna tarea con el ID {task_id}.")
            return

        print(f"\nTarea actual: ID {task_exists[0]}, Título: '{task_exists[1]}', Estado actual: '{task_exists[2]}'")
        choice = input("Queres actualizar la tarea a 'Completado'?(y/n): ").strip().upper()

        if choice == 'Y':
            status='Completado'
        elif choice == 'N':
            print('Elegiste No')
            return
        else:
            print("Opción inválida.")
            return

        # Construir la consulta UPDATE dinámicamente
        update_query = f"UPDATE tasks SET status='{status}' WHERE id = {task_id}"
        
        cursor.execute(update_query)
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Tarea con ID {task_id} actualizada con éxito.")
            # Invalida la caché después de una modificación
            invalidate_cache(ALL_TASKS_CACHE_KEY)
        else:
            print("No se realizó ninguna actualización (quizás el nuevo valor es el mismo).")

    except Error as e:
        print(f"Error al actualizar tarea: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
