"""
Script Python para generar JSON con los datos más relevantes de MySQL, MariaDB y PostgreSQL.
Se crean tres archivos distintos con nombres descriptivos según el tipo de consulta:
- consulta_examenes_mysql.json
- consulta_actividades_participaciones_mariadb.json
- consulta_proyectos_tutorias_postgres.json
"""

import mysql.connector
import psycopg2
import json
from decimal import Decimal

# =======================
# Convertir Decimal a float para JSON
# =======================
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super().default(o)

# =======================
# Conexiones
# =======================
# MySQL (puerto 3306)
conn_mysql = mysql.connector.connect(
    host="localhost", port=3306,
    user="usuario", password="usuario123",
    database="proyecto"
)
cursor_mysql = conn_mysql.cursor(dictionary=True)

# MariaDB (puerto 3307)
conn_maria = mysql.connector.connect(
    host="localhost", port=3307,
    user="usuario", password="usuario123",
    database="proyecto"
)
cursor_maria = conn_maria.cursor(dictionary=True)

# PostgreSQL (puerto 5432)
conn_pg = psycopg2.connect(
    host="localhost", port=5432,
    user="usuario",
    password="usuario123",
    dbname="proyecto"
)
cursor_pg = conn_pg.cursor()

# =======================
# MYSQL - Datos más importantes
# Solo exámenes
# =======================
cursor_mysql.execute("""
    SELECT 
        e.id_estudiante,
        CONCAT(e.nombre, ' ', e.apellidos) AS nombre_completo,
        COUNT(c.id_calificacion) AS total_examenes,
        AVG(c.nota) AS promedio_examenes
    FROM Estudiantes e
    LEFT JOIN Calificaciones c ON e.id_estudiante = c.id_estudiante
    GROUP BY e.id_estudiante
""")

data_mysql = []
for row in cursor_mysql.fetchall():
    data_mysql.append({
        "id_estudiante": row["id_estudiante"],
        "nombre_completo": row["nombre_completo"],
        "total_examenes": row["total_examenes"],
        "promedio_examenes": float(row["promedio_examenes"]) if row["promedio_examenes"] is not None else None
    })

# =======================
# MARIA DB - Actividades y participaciones
# =======================
cursor_maria.execute("""
    SELECT 
        a.id_actividad,
        a.nombre AS actividad,
        COUNT(p.id_participacion) AS total_participantes,
        AVG(p.horas_dedicadas) AS horas_promedio
    FROM Actividades a
    LEFT JOIN Participaciones p ON a.id_actividad = p.id_actividad
    GROUP BY a.id_actividad
""")

data_maria = []
for row in cursor_maria.fetchall():
    data_maria.append({
        "id_actividad": row["id_actividad"],
        "actividad": row["actividad"],
        "total_participantes": row["total_participantes"],
        "horas_promedio": float(row["horas_promedio"]) if row["horas_promedio"] is not None else None
    })

# =======================
# POSTGRES - Proyectos y tutorías
# Mostramos cuántos proyectos y tutorías tiene cada estudiante
# =======================
cursor_pg.execute("""
    SELECT 
        e.id_estudiante,
        e.nombre || ' ' || e.apellidos AS nombre_completo,
        COUNT(DISTINCT pr.id_proyecto) AS total_proyectos,
        COUNT(DISTINCT t.id_tutoria) AS total_tutorias
    FROM Estudiantes e
    LEFT JOIN Proyectos pr ON e.id_estudiante = pr.id_estudiante
    LEFT JOIN Tutorias t ON e.id_estudiante = t.id_estudiante
    GROUP BY e.id_estudiante, e.nombre, e.apellidos
""")

data_pg = []
for row in cursor_pg.fetchall():
    data_pg.append({
        "id_estudiante": row[0],
        "nombre_completo": row[1],
        "total_proyectos": row[2],
        "total_tutorias": row[3]
    })

# =======================
# Guardar JSON con nombres descriptivos
# =======================
with open("consulta_examenes_mysql.json", "w", encoding="utf-8") as f:
    json.dump(data_mysql, f, indent=4, ensure_ascii=False, cls=DecimalEncoder)

with open("consulta_actividades_participaciones_mariadb.json", "w", encoding="utf-8") as f:
    json.dump(data_maria, f, indent=4, ensure_ascii=False, cls=DecimalEncoder)

with open("consulta_proyectos_tutorias_postgres.json", "w", encoding="utf-8") as f:
    json.dump(data_pg, f, indent=4, ensure_ascii=False)

# =======================
# Cerrar conexiones
# =======================
cursor_mysql.close()
conn_mysql.close()
cursor_maria.close()
conn_maria.close()
cursor_pg.close()
conn_pg.close()

print("✅ JSON generados correctamente para MySQL, MariaDB y PostgreSQL.")
