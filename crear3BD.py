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

def ejecutar_script_mysql(sql_text, host, port, user, password):
    """Ejecuta un script SQL en MySQL o MariaDB"""
    conn = mysql.connector.connect(host=host, port=port, user=user, password=password)
    cursor = conn.cursor()
    # Separar comandos por ';' y ejecutar solo si no está vacío
    comandos = sql_text.split(";")
    for comando in comandos:
        if comando.strip():
            try:
                cursor.execute(comando)
            except mysql.connector.Error as e:
                # Ignorar errores de tabla ya existente
                if e.errno == 1050:  
                    continue
                print(f"⚠️ Error ejecutando comando en {host}:{port}: {e}")
    conn.commit()
    cursor.close()
    conn.close()

def ejecutar_script_postgres(sql_text, user, password, host="localhost", port=5432):
    """Ejecuta un script SQL en PostgreSQL"""
    conn = psycopg2.connect(host=host, port=port, user=user, password=password, dbname="postgres")
    conn.autocommit = True
    cursor = conn.cursor()
    comandos = sql_text.split(";")
    for comando in comandos:
        if comando.strip():
            try:
                cursor.execute(comando)
            except psycopg2.errors.DuplicateTable:
                continue
            except Exception as e:
                print(f"⚠️ Error ejecutando comando PostgreSQL: {e}")
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
        ejecutar_script_mysql(sql_mysql, "localhost", 3306, "root", "admin123")
        print("Base de datos MySQL creada correctamente.")
    except Exception as e:
        print(f"Error en MySQL: {e}")

    # --- MariaDB ---
    try:
        print("\n🔹 MariaDB:")
        sql_maria = leer_sql(os.path.join(base_path, "mariadb", "init.sql"))
        # Forzar collation compatible con MariaDB
        sql_maria = sql_maria.replace("utf8mb4_0900_ai_ci", "utf8mb4_general_ci")
        ejecutar_script_mysql(sql_maria, "localhost", 3307, "usuario", "usuario123")
        print("Base de datos MariaDB creada correctamente.")
    except Exception as e:
        print(f"Error en MariaDB: {e}")

    # --- PostgreSQL ---
    try:
        print("\n🔹 PostgreSQL:")
        sql_pg = leer_sql(os.path.join(base_path, "postgres", "init.sql"))
        ejecutar_script_postgres(sql_pg, "usuario", "usuario123")
        print("Base de datos PostgreSQL creada correctamente.")
    except Exception as e:
        print(f"Error en PostgreSQL: {e}")

    print("\nTodas las bases de datos creadas correctamente.")
