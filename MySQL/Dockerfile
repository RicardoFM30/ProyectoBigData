# ==========================================
# Dockerfile para base de datos MySQL: proyecto
# ==========================================

# Imagen base oficial de MySQL
FROM mysql:8.0

# Variables de entorno para inicializar MySQL
ENV MYSQL_ROOT_PASSWORD=admin123
ENV MYSQL_DATABASE=proyecto
ENV MYSQL_USER=usuario
ENV MYSQL_PASSWORD=usuario123

# Copia el script SQL de inicialización a la carpeta especial
# Esta ruta es donde MySQL ejecuta automáticamente los scripts .sql al arrancar por primera vez
COPY ./init.sql /docker-entrypoint-initdb.d/

# Exponer el puerto del contenedor (internamente 3306)
EXPOSE 3306
