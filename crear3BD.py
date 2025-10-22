"""
Script para crear automáticamente las tres bases de datos
(MySQL, MariaDB y PostgreSQL) usando los init.sql ubicados
en sus respectivas carpetas.

Estructura esperada:
├── mysql/init.sql
├── mariadb/init.sql
└── postgres/init.sql
"""

import os
import mysql.connector
import psycopg2

# ===============================================================
# FUNCIONES AUXILIARES
# ===============================================================

def leer_sql(path):
    """Lee el contenido de un archivo SQL y devuelve su contenido"""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def ejecutar_script_sql(sql_text, engine, user, password, host="localhost", port=None, database=None):

    engine = engine.lower()
    if engine not in ("mysql", "postgres"):
        raise ValueError("Error en el parámetro 'engine'.")

    if engine == "mysql":
        conn = mysql.connector.connect(
            host=host, port=port, user=user, password=password, database=database
        )
        cursor = conn.cursor()
        conn.autocommit = False
    else:
        conn = psycopg2.connect(
            host=host, port=port, user=user, password=password, dbname=database
        )
        conn.autocommit = True
        cursor = conn.cursor()

    comandos = sql_text.split(";")
    for comando in comandos:
        if comando.strip():
            try:
                cursor.execute(comando)
            except Exception as e:
                if engine == "mysql" and getattr(e, "errno", None) == 1050:
                    # Ignorar error de tabla ya existente
                    continue
                elif engine == "postgres" and isinstance(e, psycopg2.errors.DuplicateTable):
                    # Ignorar error de tabla duplicada
                    continue
                print(f"⚠️ Error ejecutando comando ({engine}): {e}")

    if engine == "mysql":
        conn.commit()

    cursor.close()
    conn.close()

# ===============================================================
# MAIN
# ===============================================================
if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))

    print("Creando bases de datos desde los init.sql...")

        # --- MySQL ---
    try:
        print("\n🔹 MySQL:")
        sql_mysql = leer_sql(os.path.join(base_path, "mysql", "init.sql"))
        ejecutar_script_sql(sql_mysql, "mysql", "usuario", "usuario123", host="localhost", port=3306)
        print("Base de datos MySQL creada correctamente.")
    except Exception as e:
        print(f"Error en MySQL: {e}")

    # --- MariaDB ---
    try:
        print("\n🔹 MariaDB:")
        sql_maria = leer_sql(os.path.join(base_path, "mariadb", "init.sql"))
        # Forzar collation compatible con MariaDB
        sql_maria = sql_maria.replace("utf8mb4_0900_ai_ci", "utf8mb4_general_ci")
        ejecutar_script_sql(sql_maria, "mysql", "usuario", "usuario123", host="localhost", port=3307)
        print("Base de datos MariaDB creada correctamente.")
    except Exception as e:
        print(f"Error en MariaDB: {e}")

    # --- PostgreSQL ---
    try:
        print("\n🔹 PostgreSQL:")
        sql_pg = leer_sql(os.path.join(base_path, "postgres", "init.sql"))
        ejecutar_script_sql(sql_pg, "postgres", "usuario", "usuario123", host="localhost", port=5432, database="postgres")
        print("Base de datos PostgreSQL creada correctamente.")
    except Exception as e:
        print(f"Error en PostgreSQL: {e}")

    print("\n✅ Todas las bases de datos creadas correctamente.")
