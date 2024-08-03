# Usar una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requerimientos al contenedor
COPY requirements.txt requirements.txt

# Instalar las dependencias
RUN pip install -r requirements.txt

# Verificar la instalación
RUN pip show gunicorn flask

# Copiar el contenido de la aplicación al contenedor
COPY . .

# Establecer la variable de entorno para que Python no genere archivos .pyc
ENV PYTHONUNBUFFERED=1

# Exponer el puerto que usará la aplicación Flask
EXPOSE 5000

# Definir el comando por defecto para ejecutar la aplicación
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
