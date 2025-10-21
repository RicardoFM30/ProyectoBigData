FROM mysql:8.0

# Variables de entorno para inicializar MySQL
ENV MYSQL_ROOT_PASSWORD=admin123
ENV MYSQL_DATABASE=proyecto
ENV MYSQL_USER=usuario
ENV MYSQL_PASSWORD=usuario123

COPY ./init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
