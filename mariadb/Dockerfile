FROM mariadb:10.11

# Variables de entorno
ENV MARIADB_ROOT_PASSWORD=admin123
ENV MARIADB_DATABASE=proyecto
ENV MARIADB_USER=usuario
ENV MARIADB_PASSWORD=usuario123

COPY ./init.sql /docker-entrypoint-initdb.d/

EXPOSE 3307
