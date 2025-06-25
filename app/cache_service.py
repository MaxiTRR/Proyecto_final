import redis
import json
from redis import RedisError

#Configuración de Redis
REDIS_HOST = 'redis_cache' #Si lo ejecutamos en local, esta variable deberia ser 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0 # Base de datos por defecto de Redis

#Objeto de Cliente Redis (global para reutilización)
_redis_client = None

def get_redis_client():
    #Obtiene y devuelve una instancia del cliente Redis. Inicializa la conexión si aún no existe.
    global _redis_client
    if _redis_client is None:
        try:
            _redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)
            _redis_client.ping() # Prueba la conexión
            print(f"Conectado a Redis en {REDIS_HOST}:{REDIS_PORT}")
        except RedisError as e:
            print(f"Error al conectar a Redis: {e}")
            _redis_client = None # Asegurarse de que _redis_client sea None si falla la conexión
    return _redis_client

def set_cache(key, value, ex=3600):
    """
    Almacena un valor en la caché de Redis con una clave y un tiempo de expiración.
    Los valores complejos (listas de diccionarios) se serializan a JSON.
    :param key: La clave para el elemento en caché.
    :param value: El valor a almacenar.
    :param ex: Tiempo de expiración en segundos (por defecto 1 hora).
    """
    client = get_redis_client()
    if client:
        try:
            # Redis almacena strings, así que serializamos a JSON si es necesario
            if isinstance(value, (list, dict)):
                value = json.dumps(value)
            client.set(key, value, ex=ex)
            print(f"Dato almacenado en caché con clave: {key}")
        except RedisError as e:
            print(f"Error al establecer caché para la clave {key}: {e}")

def get_cache(key):
    """
    Recupera un valor de la caché de Redis.
    Intenta deserializar el valor de JSON si es posible.
    :param key: La clave del elemento a recuperar.
    :return: El valor de la caché o None si no se encuentra o hay un error.
    """
    client = get_redis_client()
    if client:
        try:
            cached_value = client.get(key)
            if cached_value:
                # Intentar deserializar de JSON
                try:
                    return json.loads(cached_value)
                except json.JSONDecodeError:
                    return cached_value # Si no es JSON, devolver el string original
            return None
        except RedisError as e:
            print(f"Error al obtener caché para la clave {key}: {e}")
            return None
    return None

def invalidate_cache(key):
    """
    Elimina una clave específica de la caché de Redis.
    :param key: La clave a eliminar.
    """
    client = get_redis_client()
    if client:
        try:
            client.delete(key)
            print(f"Caché invalidada para la clave: {key}")
        except RedisError as e:
            print(f"Error al invalidar caché para la clave {key}: {e}")

# Ejemplo de uso (opcional, para probar cache_service.py directamente)
if __name__ == "__main__":
    print("--- Probando servicio de caché Redis ---")
    
    # Probar conexión
    client = get_redis_client()
    if client:
        # Probar set y get
        test_key = "my_test_data"
        test_data = {"name": "Test Task", "status": "Pending"}
        set_cache(test_key, test_data, ex=10) # Expira en 10 segundos
        print(f"Datos originales: {test_data}")

        retrieved_data = get_cache(test_key)
        print(f"Datos recuperados de caché: {retrieved_data}")

        # Probar invalidación
        invalidate_cache(test_key)
        retrieved_data_after_invalidate = get_cache(test_key)
        print(f"Datos después de invalidar: {retrieved_data_after_invalidate} (Debería ser None)")
    else:
        print("No se pudo conectar a Redis. Asegúrate de que el servidor esté en ejecución.")
