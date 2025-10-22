"""
Script Python para obtener los mismos datos de la tabla Estudiantes
desde MySQL, MariaDB y PostgreSQL, unificarlos y guardarlos en un único JSON.

Archivo de salida:
- estudiantes_unificados.json
"""

import mysql.connector
import psycopg2
import json
from decimal import Decimal

# =======================
# Clase para convertir Decimals a float (por si acaso)
# =======================
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super().default(o)

# =======================
# Conexiones a las bases de datos
# =======================
# MySQL
conn_mysql = mysql.connector.connect(
    host="localhost", port=3306,
    user="usuario", password="usuario123",
    database="proyecto"
)
cursor_mysql = conn_mysql.cursor(dictionary=True)

# MariaDB
conn_maria = mysql.connector.connect(
    host="localhost", port=3307,
    user="usuario", password="usuario123",
    database="proyecto"
)
cursor_maria = conn_maria.cursor(dictionary=True)

# PostgreSQL
conn_pg = psycopg2.connect(
    host="localhost", port=5432,
    user="usuario", password="usuario123",
    dbname="proyecto"
)
cursor_pg = conn_pg.cursor()

# =======================
# Consulta común a las tres bases
# =======================
consulta_estudiantes = """
    SELECT 
        id_estudiante,
        nombre,
        apellidos,
        edad,
        curso,
        grupo,
        email,
        telefono
    FROM Estudiantes
"""

# =======================
# MySQL
# =======================
cursor_mysql.execute(consulta_estudiantes)
data_mysql = cursor_mysql.fetchall()
for row in data_mysql:
    row["origen"] = "MySQL"

# =======================
# MariaDB
# =======================
cursor_maria.execute(consulta_estudiantes)
data_maria = cursor_maria.fetchall()
for row in data_maria:
    row["origen"] = "MariaDB"

# =======================
# PostgreSQL
# =======================
cursor_pg.execute(consulta_estudiantes)
columnas_pg = [desc[0] for desc in cursor_pg.description]
data_pg = [dict(zip(columnas_pg, row)) for row in cursor_pg.fetchall()]
for row in data_pg:
    row["origen"] = "PostgreSQL"

# =======================
# Unificar todos los resultados
# =======================
data_unificada = data_mysql + data_maria + data_pg

# =======================
# Guardar en JSON
# =======================
with open("estudiantes_unificados.json", "w", encoding="utf-8") as f:
    json.dump(data_unificada, f, indent=4, ensure_ascii=False, cls=DecimalEncoder)

# =======================
# Cerrar conexiones
# =======================
cursor_mysql.close()
conn_mysql.close()
cursor_maria.close()
conn_maria.close()
cursor_pg.close()
conn_pg.close()

print("✅ Datos unificados correctamente y guardados en estudiantes_unificados.json")