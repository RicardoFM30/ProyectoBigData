# Imagen base oficial de MariaDB compatible con utf8mb4_general_ci
FROM mariadb:10.11

# Variables de entorno
ENV MARIADB_ROOT_PASSWORD=admin123
ENV MARIADB_DATABASE=proyecto
ENV MARIADB_USER=usuario
ENV MARIADB_PASSWORD=usuario123

# Copiar el script SQL
COPY ./init.sql /docker-entrypoint-initdb.d/

# Puerto de MariaDB
EXPOSE 3307
