-- ========================================
-- Script de creación de base de datos PostgreSQL
-- Proyecto Instituto (DER simplificado)
-- ========================================

-- Eliminar tablas en orden inverso a sus dependencias
DROP TABLE IF EXISTS Recomendaciones;
DROP TABLE IF EXISTS Retroalimentaciones;
DROP TABLE IF EXISTS PerfilesTalento;
DROP TABLE IF EXISTS Proyectos;
DROP TABLE IF EXISTS Tutorias;
DROP TABLE IF EXISTS Participaciones;
DROP TABLE IF EXISTS Actividades;
DROP TABLE IF EXISTS HabilidadesBlandas;
DROP TABLE IF EXISTS Calificaciones;
DROP TABLE IF EXISTS Asignaturas;
DROP TABLE IF EXISTS Profesores;
DROP TABLE IF EXISTS Estudiantes;

-- Crear tablas
CREATE TABLE Estudiantes (
  id_estudiante SERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  apellidos VARCHAR(100),
  edad INT,
  curso VARCHAR(20),
  grupo VARCHAR(10),
  email VARCHAR(100),
  telefono VARCHAR(20)
);

CREATE TABLE Profesores (
  id_profesor SERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  apellidos VARCHAR(100),
  email VARCHAR(100),
  telefono VARCHAR(20),
  materia VARCHAR(100)
);

CREATE TABLE Asignaturas (
  id_asignatura SERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  descripcion TEXT,
  curso VARCHAR(20),
  id_profesor INT REFERENCES Profesores(id_profesor)
);

CREATE TABLE Calificaciones (
  id_calificacion SERIAL PRIMARY KEY,
  id_estudiante INT REFERENCES Estudiantes(id_estudiante),
  id_asignatura INT REFERENCES Asignaturas(id_asignatura),
  nota DECIMAL(5,2),
  fecha_evaluacion DATE,
  asistencia BOOLEAN
);

CREATE TABLE HabilidadesBlandas (
  id_habilidad SERIAL PRIMARY KEY,
  id_estudiante INT REFERENCES Estudiantes(id_estudiante),
  habilidad VARCHAR(100),
  puntuacion DECIMAL(5,2),
  fecha_registro DATE
);

CREATE TABLE Actividades (
  id_actividad SERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  tipo VARCHAR(50),
  fecha_inicio DATE,
  fecha_fin DATE,
  descripcion TEXT
);

CREATE TABLE Participaciones (
  id_participacion SERIAL PRIMARY KEY,
  id_estudiante INT REFERENCES Estudiantes(id_estudiante),
  id_actividad INT REFERENCES Actividades(id_actividad),
  rol VARCHAR(50),
  fecha_participacion DATE,
  horas_dedicadas INT,
  resultado VARCHAR(100)
);

CREATE TABLE Tutorias (
  id_tutoria SERIAL PRIMARY KEY,
  id_estudiante INT REFERENCES Estudiantes(id_estudiante),
  id_profesor INT REFERENCES Profesores(id_profesor),
  fecha DATE,
  tema VARCHAR(100),
  observaciones TEXT
);

CREATE TABLE Proyectos (
  id_proyecto SERIAL PRIMARY KEY,
  id_estudiante INT REFERENCES Estudiantes(id_estudiante),
  nombre VARCHAR(100),
  descripcion TEXT,
  fecha_entrega DATE,
  calificacion_final DECIMAL(5,2),
  evaluador INT REFERENCES Profesores(id_profesor),
  material_adjunto VARCHAR(255)
);

CREATE TABLE PerfilesTalento (
  id_perfil SERIAL PRIMARY KEY,
  id_estudiante INT UNIQUE REFERENCES Estudiantes(id_estudiante),
  promedio_general DECIMAL(5,2),
  habilidades_destacadas TEXT,
  intereses TEXT,
  fortalezas TEXT,
  recomendaciones_generadas TEXT
);

CREATE TABLE Retroalimentaciones (
  id_feedback SERIAL PRIMARY KEY,
  id_estudiante INT REFERENCES Estudiantes(id_estudiante),
  autor_feedback VARCHAR(100),
  tipo_feedback VARCHAR(50),
  comentario TEXT,
  fecha DATE
);

CREATE TABLE Recomendaciones (
  id_recomendacion SERIAL PRIMARY KEY,
  id_estudiante INT REFERENCES Estudiantes(id_estudiante),
  tipo VARCHAR(50),
  detalle TEXT,
  fecha_generacion DATE
);
