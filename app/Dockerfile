# Usa una imagen base de Python oficial
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos los archivos de la aplicación al contenedor
COPY . .

#Expone la app al puerto especificado (esta linea es opcional)
EXPOSE 5000

# Comando para ejecutar la aplicación cuando el contenedor se inicie
CMD ["python", "main.py"]