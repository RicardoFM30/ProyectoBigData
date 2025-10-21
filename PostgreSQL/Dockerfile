# ==========================================
# Dockerfile para base de datos PostgreSQL: instituto
# ==========================================

# Imagen base oficial de PostgreSQL
FROM postgres:16

# Variables de entorno
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin123
ENV POSTGRES_DB=instituto

# Copiar el script de inicialización
COPY ./init.sql /docker-entrypoint-initdb.d/

# Exponer el puerto por defecto
EXPOSE 5432
