-- ======================================================
-- SCRIPTS SQL PARA EL SISTEMA DE INSCRIPCIÓN "FITLIFE"
-- ======================================================

-- 1. CREACIÓN DE TABLAS (Definición de claves primarias y foráneas)

-- Tabla Miembros
CREATE TABLE IF NOT EXISTS Miembros (
    cedula TEXT PRIMARY KEY,
    nombre_completo TEXT NOT NULL,
    telefono TEXT
);

-- Tabla Clases
CREATE TABLE IF NOT EXISTS Clases (
    id_clase INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_clase TEXT NOT NULL,
    dia_semana TEXT NOT NULL,
    horario TEXT NOT NULL
);

-- Tabla Inscripciones (Resolución de relación Muchos a Muchos)
CREATE TABLE IF NOT EXISTS Inscripciones (
    id_inscripcion INTEGER PRIMARY KEY AUTOINCREMENT,
    cedula_miembro TEXT NOT NULL,
    id_clase INTEGER NOT NULL,
    fecha_inscripcion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cedula_miembro) REFERENCES Miembros(cedula) ON DELETE CASCADE,
    FOREIGN KEY (id_clase) REFERENCES Clases(id_clase) ON DELETE CASCADE
);

-- 2. INSERCIÓN DE REGISTROS (Al menos 5 por tabla)

-- Insertar Miembros
INSERT INTO Miembros (cedula, nombre_completo, telefono) VALUES
('1-1111-1111', 'Juan Perez', '8888-1111'),
('2-2222-2222', 'Maria Lopez', '8888-2222'),
('3-3333-3333', 'Carlos Solis', '8888-3333'),
('4-4444-4444', 'Ana Garcia', '8888-4444'),
('5-5555-5555', 'Elena Ruiz', '8888-5555');

-- Insertar Clases
INSERT INTO Clases (nombre_clase, dia_semana, horario) VALUES
('Yoga', 'Lunes', '08:00'),
('Spinning', 'Martes', '18:00'),
('Zumba', 'Miercoles', '19:00'),
('Crossfit', 'Jueves', '07:00'),
('Pilates', 'Viernes', '17:00');

-- Insertar Inscripciones
INSERT INTO Inscripciones (cedula_miembro, id_clase) VALUES
('1-1111-1111', 1),
('2-2222-2222', 2),
('3-3333-3333', 3),
('4-4444-4444', 4),
('5-5555-5555', 5);

-- 3. CONSULTA DE VERIFICACIÓN
SELECT 
    M.nombre_completo AS Miembro,
    C.nombre_clase AS Clase,
    C.dia_semana AS Dia
FROM Inscripciones I
JOIN Miembros M ON I.cedula_miembro = M.cedula
JOIN Clases C ON I.id_clase = C.id_clase;
