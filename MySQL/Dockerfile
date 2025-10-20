# ==========================================
# Dockerfile para base de datos MySQL: proyecto
# ==========================================

FROM mysql:8.0

# Variables de entorno para inicializar MySQL
ENV MYSQL_ROOT_PASSWORD=admin123
ENV MYSQL_DATABASE=proyecto

# Copia el script SQL que crea las tablas a la carpeta de inicialización de MySQL
COPY ./init.sql /docker-entrypoint-initdb.d/

# Expone el puerto por defecto
EXPOSE 3310
