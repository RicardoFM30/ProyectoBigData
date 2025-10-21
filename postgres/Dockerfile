FROM postgres:15

# Variables de entorno
ENV POSTGRES_DB=proyecto
ENV POSTGRES_USER=usuario
ENV POSTGRES_PASSWORD=usuario123

COPY ./init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
