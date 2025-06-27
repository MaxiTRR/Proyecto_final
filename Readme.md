# Mi Proyecto: Lite Task App

Version: 1.0

## Descripción
Una aplicación web para gestionar tareas de manera simplificada (solo permite añadir tareas, consultar y traer todas las tareas y actualizar su estado segun se hayan realizado). La app usa un sistema de base de datos MySQL para registar y consultar tareas, asi como tambien un sistema de cache Redis por si es necesario volver a consultar informacion previamente cosultada, evitando volver a llamar a la base de datos y asi mejorar el rendimiento.
<br>
La app puede ejecutarse tanto de manera local o levantando los servicios en contenedores de Docker (cambiando las variables de creacion de la base de datos y el servidor Redis en los scripts por los parametros correspondientes)

## Arquitectura
- **APP**: Aplicación Python 3.9 usando las lib mysql-connector, json, redis
- **DB**: MySQL para almacenar tareas.
- **Cache**: Redis para caché de consultas frecuentes.
Los servicios se comunican a través de una red bridge.

## Requisitos
- Docker
- Docker Compose
- Xampp (Si se quisiera ejecutar la app en localhost, cambiando los parametros de creacion y conexion a la base de datos por los correspondientes. La base de datos se crea desde el mismo script de python)

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
4. Accede a la consola para ejecutar el menu de la app (es necesario apretar 'enter' para que aparezca el menu): 
   ```
   docker attach task_python_app
   ```
5. Añadir nueva tarea: ingresar 1 y escribir el titulo/descripcion de la tarea (solo 255 caracteres)
6. Ver todas las tareas: ingresar 2
7. Actualizar tarea (estado): ingresar 3 --> ingresar el id de la tarea a actualizar --> ingresar 'y' para confirmar, 'n' para volver al menu
8. Salir y cerrar el programa: ingresar 4
9. Volver a iniciar la app de python:
    ```
    docker-compose up -d python_app
    ```
10. Detener y eliminar los contenedores y volumenes de Docker (si fuera necesario por cambios en el codigo, luego se deberian repetir los pasos desde el Nro. 3):
    ```
    docker-compose down -v
    ```


# Ejemplo de Uso
## Habilitar menu en la consola cmd
![menu attach](https://github.com/user-attachments/assets/2df26c90-7c1b-4fe3-9e52-842a8c8750d0)
## Añadir tarea
![agregar](https://github.com/user-attachments/assets/b706e3a5-3d61-4a0e-8d09-cf03b8121b3a)

## Ver tarea
![ver](https://github.com/user-attachments/assets/b7339a98-80a4-429b-9468-582df4f5f03d)

## Actualizar tarea
![Actualizar](https://github.com/user-attachments/assets/8cae2276-1212-4c9f-838e-a6be6551a68f)

## Salir de la app
![salir](https://github.com/user-attachments/assets/b21b8854-4cf8-45c1-a1ee-153ed6b63f33)

## Levantar python_app
![levantar python app](https://github.com/user-attachments/assets/6ac9be86-8f3d-453d-a9eb-490b05f026bd)

# Notas adicionales
Esta app presenta una funcionalidad simple con el fin de probar rapidamente la misma levantando cada servicio en contenedores de Docker distintos. La base de datos solo posee tres columnas correspondientes a un id autoincremental, un titulo/descripcion de las tareas y un estado de la misma que puede ser 'Pendiente' o 'Completado' (correspondiendo esto con una eliminacion logica de la base de datos)
<br>
La app puede ser mejorada agregandole mas funcionalidades:
<ul>
   <li>Consultar tareas por ID</li>
   <li>Consulta de tareas diferenciadas por estado</li>
   <li>Campo con la fecha de creacion de la tarea</li>
   <li>Campo con la fecha de finalizacion de la tarea</li>
   <li>Control y verificacion de los formatos de entrada de los input del formulario</li>
   <li>Eliminacion fisica de las tareas completadas</li>
</ul>





