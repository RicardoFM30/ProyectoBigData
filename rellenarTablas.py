"""
Script para rellenar las bases de datos MySQL, PostgreSQL y MariaDB con datos falsos usando Faker.
Los providers empleados son los siguientes

1. faker.name()           → nombres de estudiantes/profesores
2. faker.last_name()      → apellidos
3. faker.email()          → correos electrónicos
4. faker.phone_number()   → teléfonos
5. faker.word()           → habilidades, materias, etc.
6. faker.sentence()       → descripciones o temas
7. faker.date()           → fechas
8. faker.boolean()        → valores de asistencia
9. faker.random_int()     → edades, calificaciones, etc.
10. faker.text()          → observaciones o comentarios
"""

from faker import Faker
import random
import mysql.connector
import psycopg2

faker = Faker('es_ES')

# ===================================================
# CONEXIONES A LAS BASES DE DATOS
# ===================================================

# MySQL (puerto 3306)
conn_mysql = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="usuario",
    password="usuario123",
    database="proyecto"
)
cursor_mysql = conn_mysql.cursor()

# MariaDB (puerto 3307)
conn_maria = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="usuario",
    password="usuario123",
    database="proyecto",
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
)
cursor_maria = conn_maria.cursor()

# PostgreSQL (puerto 5432)
conn_pg = psycopg2.connect(
    host="localhost",
    port=5432,
    user="usuario",
    password="usuario123",
    dbname="proyecto"
)
cursor_pg = conn_pg.cursor()

# ===================================================
# FUNCIONES PARA INSERTAR DATOS
# ===================================================

def insertar_estudiantes(cursor, cantidad=10):
    for _ in range(cantidad):
        cursor.execute("""
            INSERT INTO Estudiantes (nombre, apellidos, edad, curso, grupo, email, telefono)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            faker.first_name(),
            faker.last_name(),
            faker.random_int(16, 25),
            f"Curso {faker.random_int(1,4)}",
            f"Grupo {faker.random_int(1,3)}",
            faker.email(),
            faker.phone_number()
        ))

def insertar_profesores(cursor, cantidad=5):
    for _ in range(cantidad):
        cursor.execute("""
            INSERT INTO Profesores (nombre, apellidos, email, telefono, materia)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            faker.first_name(),
            faker.last_name(),
            faker.email(),
            faker.phone_number(),
            faker.word()
        ))

def insertar_asignaturas(cursor, cantidad=5):
    for _ in range(cantidad):
        cursor.execute("""
            INSERT INTO Asignaturas (nombre, descripcion, curso, id_profesor)
            VALUES (%s, %s, %s, %s)
        """, (
            faker.word().capitalize(),
            faker.sentence(),
            f"Curso {faker.random_int(1,4)}",
            faker.random_int(1, 5)
        ))

def insertar_calificaciones(cursor, cantidad=20):
    for _ in range(cantidad):
        cursor.execute("""
            INSERT INTO Calificaciones (id_estudiante, id_asignatura, nota, fecha_evaluacion, asistencia)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            faker.random_int(1,10),
            faker.random_int(1,5),
            round(random.uniform(0,10),2),
            faker.date(),
            faker.boolean()
        ))

def insertar_habilidades(cursor, cantidad=10):
    habilidades = ["Liderazgo", "Comunicación", "Trabajo en equipo", "Creatividad", "Responsabilidad"]
    for _ in range(cantidad):
        cursor.execute("""
            INSERT INTO HabilidadesBlandas (id_estudiante, habilidad, puntuacion, fecha_registro)
            VALUES (%s, %s, %s, %s)
        """, (
            faker.random_int(1,10),
            random.choice(habilidades),
            round(random.uniform(0,10),2),
            faker.date()
        ))

def insertar_actividades(cursor, cantidad=5):
    for _ in range(cantidad):
        cursor.execute("""
            INSERT INTO Actividades (nombre, tipo, fecha_inicio, fecha_fin, descripcion)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            faker.word().capitalize(),
            random.choice(["Taller", "Concurso", "Proyecto", "Charla"]),
            faker.date(),
            faker.date(),
            faker.sentence()
        ))

def insertar_participaciones(cursor, cantidad=10):
    for _ in range(cantidad):
        cursor.execute("""
            INSERT INTO Participaciones (id_estudiante, id_actividad, rol, fecha_participacion, horas_dedicadas, resultado)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            faker.random_int(1,10),
            faker.random_int(1,5),
            faker.word(),
            faker.date(),
            round(random.uniform(1,20),2),
            random.choice(["Ganador", "Participante", "Finalista"])
        ))

def insertar_tutorias(cursor, cantidad=5):
    for _ in range(cantidad):
        cursor.execute("""
            INSERT INTO Tutorias (id_estudiante, id_profesor, fecha, tema, observaciones)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            faker.random_int(1,10),
            faker.random_int(1,5),
            faker.date(),
            faker.sentence(),
            faker.text()
        ))

def insertar_proyectos(cursor, cantidad=5):
    for _ in range(cantidad):
        cursor.execute("""
            INSERT INTO Proyectos (id_estudiante, nombre, descripcion, fecha_entrega, calificacion_final, evaluador, material_adjunto)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            faker.random_int(1,10),
            faker.word().capitalize(),
            faker.text(),
            faker.date(),
            round(random.uniform(0,10),2),
            faker.random_int(1,5),
            faker.word() + ".pdf"
        ))


def insertar_retroalimentaciones(cursor, cantidad=10):
    for _ in range(cantidad):
        cursor.execute("""
            INSERT INTO Retroalimentaciones (id_estudiante, autor_feedback, tipo_feedback, comentario, fecha)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            faker.random_int(1,10),
            faker.name(),
            random.choice(["Positivo", "Negativo", "Neutral"]),
            faker.text(),
            faker.date()
        ))

def insertar_recomendaciones(cursor, cantidad=10):
    for _ in range(cantidad):
        cursor.execute("""
            INSERT INTO Recomendaciones (id_estudiante, tipo, detalle, fecha_generacion)
            VALUES (%s, %s, %s, %s)
        """, (
            faker.random_int(1,10),
            random.choice(["Academia", "Extraescolar", "Carrera"]),
            faker.text(),
            faker.date()
        ))

# ===================================================
# RELLENAR BASES DE DATOS
# ===================================================

def poblar(cursor, conexion):
    insertar_estudiantes(cursor)
    insertar_profesores(cursor)
    insertar_asignaturas(cursor)
    insertar_calificaciones(cursor)
    insertar_habilidades(cursor)
    insertar_actividades(cursor)
    insertar_participaciones(cursor)
    insertar_tutorias(cursor)
    insertar_proyectos(cursor)
    insertar_retroalimentaciones(cursor)
    insertar_recomendaciones(cursor)
    conexion.commit()
    print("Datos insertados correctamente")

print("Rellenando MySQL...")
poblar(cursor_mysql, conn_mysql)

print("Rellenando MariaDB...")
poblar(cursor_maria, conn_maria)

print("Rellenando PostgreSQL...")
poblar(cursor_pg, conn_pg)

# Cerrar conexiones
cursor_mysql.close()
conn_mysql.close()
cursor_maria.close()
conn_maria.close()
cursor_pg.close()
conn_pg.close()

print("Bases de datos rellenadas con datos falsos.")
