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
Navega al directorio utilizando el cmd de windows: 
   ``` 
   cd mi-proyecto
   ```
Levanta los contenedores: 
   ```
   docker-compose up --build -d
   ```
Accede a la consola para ejecutar el menu de la app: 
   ```
   docker attach task_python_app
   ```

