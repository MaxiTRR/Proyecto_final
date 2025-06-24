import mysql.connector
from mysql.connector import Error

def db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='', 
            database='task_seminario_db' # Se conecta directamente a la DB
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def create_database():
    conn = None 
    cursor = None   

    try:
        #Al usar los contenedeores en Docker es posible que se deban cambiar estas credenciales
        conn = mysql.connector.connect(
            host='localhost',          
            user='root',               
            password=''                
        )

        if conn.is_connected():
            cursor = conn.cursor()

            #Crear la base de datos si no existe
            db_name = "task_seminario_db"
            try:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
                print(f"Base de datos '{db_name}' creada o ya existente.")
            except Error as err:
                print(f"Error al crear la base de datos '{db_name}': {err}")
                return 

            #Conectarse a la base de datos específica
            conn.database = db_name
            print(f"Conectado a la base de datos '{db_name}'.")

            #Crear la tabla 'tasks' si no existe
            create_table_query = """
            CREATE TABLE IF NOT EXISTS tasks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                status VARCHAR(50) DEFAULT 'Pendiente'
            );
            """
            try:
                cursor.execute(create_table_query)
                print("Tabla 'tasks' creada o ya existente.")
            except Error as err:
                print(f"Error al crear la tabla 'tasks': {err}")
                return 

            # Insertar datos de ejemplo si la tabla está vacía
            # Esto evita duplicados si ejecutas el script varias veces.
            cursor.execute("SELECT COUNT(*) FROM tasks")
            if cursor.fetchone()[0] == 0: # Si no hay filas en la tabla
                insert_query = """
                INSERT INTO tasks (title, status) VALUES
                ('Comprar leche y pan', 'Pendiente'),
                ('Hacer el tp de seminario', 'Pendiente'),
                ('Salir a andar en bicicleta', 'Pendiente')
                """
                try:
                    cursor.execute(insert_query)
                    conn.commit()
                    print("Datos de ejemplo insertados en la tabla 'tasks'.")
                except Error as err:
                    print(f"Error al insertar datos de ejemplo: {err}")
            else:
                print("La tabla 'tasks' ya contiene datos.")

    except Error as err:
        print(f"Error general de MySQL: {err}")

    finally:
        # Asegurarse de cerrar el cursor y la conexión
        if cursor:
            cursor.close()
            print("Cursor de MySQL cerrado.")
        if conn and conn.is_connected():
            conn.close()
            print("Conexión a MySQL cerrada.")

if __name__ == "__main__":
    create_database()