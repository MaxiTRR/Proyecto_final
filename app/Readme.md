# Mi Proyecto: Lite Task App

##Version: 1.0

## Descripción
Una aplicación web para gestionar tareas de manera simplificada (solo permite añadir tareas, consultar y traer todas las tareas y actualizar su estado segun se hayan realizado). La app usa un sistema de base de datos MySQL para registar y consultar tareas, asi como tambien un sistema de cache Redis por si es necesario volver a consultar informacion previamente cosultada, evitando volver a llamar a la base de datos y asi mejorar el rendimiento.
La app puede ejecutarse tanto de manera local o levantando los servicios en contenedores de Docker (cambiando las variables de creacion de la base de datos y el servidor Redis en los scripts por los parametros correspondientes)

## Arquitectura
- **APP**: Aplicación Python 3.9 usando las lib mysql-connector, json, redis
- **DB**: MySQL para almacenar tareas.
- **Cache**: Redis para caché de consultas frecuentes.
Los servicios se comunican a través de una red bridge.

## Requisitos
- Docker
- Docker Compose
- Xampp (Si se quisiera ejecutar la app en localhost, cambiando los parametros de creacion y conexion a la base de datos por los correspondientes)

## Instrucciones
1. Clona el repositorio:
   ```
   bash git clone https://github.com/MaxiTRR/Proyecto_final.git
   ```
2. Navega al directorio utilizando el cmd de windows: 
   ``` 
   cd mi-proyecto
   ```
3. Levanta los contenedores: 
   ```
   docker-compose up --build -d
   ```
4. Accede a la consola para ejecutar el menu de la app: 
   ```
   docker attach task_python_app
   ```
5. Añadir nueva tarea: ingresar 1 y escribir el titulo/descripcion de la tarea (solo 255 caracteres)
6. Ver todas las tareas: ingresar 2
7. Actualizar tarea (estado): ingresar 3 --> ingresar el id de la tarea a actualizar
8. Salir y cerrar el programa: ingresar 4
9. Volver a iniciar la app de python:
    ```
    docker-compose up -d python_app
    ```
10. Detener y eliminar los contenedores y volumenes de Docker (si fuera necesario por cambios en el codigo, luego se deberian repetir los pasos desde el Nro. 3):
    ```
    docker-compose down -v
    ```

