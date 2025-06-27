# Mi Proyecto: Sistema de Tareas

## Descripción
Una aplicación web para gestionar tareas, con una API REST, base de datos y sistema de caché.

## Arquitectura
- **Web**: Aplicación Flask (Python) que sirve la API.
- **DB**: PostgreSQL para almacenar tareas.
- **Cache**: Redis para caché de consultas frecuentes.
Los servicios se comunican a través de una red bridge.

## Requisitos
- Docker
- Docker Compose

## Instrucciones
1. Clona el repositorio:
   ```bash
   git clone <URL>
Navega al directorio:
cd mi-proyecto
Levanta los contenedores:
docker-compose up --build
Accede a la API en http://localhost:8080.

