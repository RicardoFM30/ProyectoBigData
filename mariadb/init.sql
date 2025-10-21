-- Script creación base de datos MariaDB --

DROP DATABASE IF EXISTS proyecto;
CREATE DATABASE proyecto 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_general_ci;

USE proyecto;

CREATE TABLE IF NOT EXISTS Estudiantes (
    id_estudiante INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(150) NOT NULL,
    edad INT,
    curso VARCHAR(50),
    grupo VARCHAR(50),
    email VARCHAR(150) UNIQUE,
    telefono VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Profesores (
    id_profesor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE,
    telefono VARCHAR(20),
    materia VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Asignaturas (
    id_asignatura INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    curso VARCHAR(50),
    id_profesor INT,
    FOREIGN KEY (id_profesor) REFERENCES Profesores(id_profesor)
);

CREATE TABLE IF NOT EXISTS Calificaciones (
    id_calificacion INT PRIMARY KEY AUTO_INCREMENT,
    id_estudiante INT,
    id_asignatura INT,
    nota DECIMAL(5,2),
    fecha_evaluacion DATE,
    asistencia BOOLEAN,
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id_estudiante),
    FOREIGN KEY (id_asignatura) REFERENCES Asignaturas(id_asignatura)
);

CREATE TABLE IF NOT EXISTS HabilidadesBlandas (
    id_habilidad INT PRIMARY KEY AUTO_INCREMENT,
    id_estudiante INT,
    habilidad VARCHAR(100),
    puntuacion DECIMAL(5,2),
    fecha_registro DATE,
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id_estudiante)
);

CREATE TABLE IF NOT EXISTS Actividades (
    id_actividad INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    tipo VARCHAR(50),
    fecha_inicio DATE,
    fecha_fin DATE,
    descripcion TEXT
);

CREATE TABLE IF NOT EXISTS Participaciones (
    id_participacion INT PRIMARY KEY AUTO_INCREMENT,
    id_estudiante INT,
    id_actividad INT,
    rol VARCHAR(100),
    fecha_participacion DATE,
    horas_dedicadas DECIMAL(5,2),
    resultado VARCHAR(100),
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id_estudiante),
    FOREIGN KEY (id_actividad) REFERENCES Actividades(id_actividad)
);

CREATE TABLE IF NOT EXISTS Tutorias (
    id_tutoria INT PRIMARY KEY AUTO_INCREMENT,
    id_estudiante INT,
    id_profesor INT,
    fecha DATE,
    tema VARCHAR(200),
    observaciones TEXT,
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id_estudiante),
    FOREIGN KEY (id_profesor) REFERENCES Profesores(id_profesor)
);

CREATE TABLE IF NOT EXISTS Proyectos (
    id_proyecto INT PRIMARY KEY AUTO_INCREMENT,
    id_estudiante INT,
    nombre VARCHAR(150),
    descripcion TEXT,
    fecha_entrega DATE,
    calificacion_final DECIMAL(5,2),
    evaluador INT,
    material_adjunto VARCHAR(255),
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id_estudiante),
    FOREIGN KEY (evaluador) REFERENCES Profesores(id_profesor)
);

CREATE TABLE IF NOT EXISTS PerfilesTalento (
    id_perfil INT PRIMARY KEY AUTO_INCREMENT,
    id_estudiante INT,
    promedio_general DECIMAL(5,2),
    habilidades_destacadas TEXT,
    intereses TEXT,
    fortalezas TEXT,
    recomendaciones_generadas TEXT,
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id_estudiante)
);

CREATE TABLE IF NOT EXISTS Retroalimentaciones (
    id_feedback INT PRIMARY KEY AUTO_INCREMENT,
    id_estudiante INT,
    autor_feedback VARCHAR(100),
    tipo_feedback VARCHAR(50),
    comentario TEXT,
    fecha DATE,
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id_estudiante)
);

CREATE TABLE IF NOT EXISTS Recomendaciones (
    id_recomendacion INT PRIMARY KEY AUTO_INCREMENT,
    id_estudiante INT,
    tipo VARCHAR(100),
    detalle TEXT,
    fecha_generacion DATE,
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id_estudiante)
);
