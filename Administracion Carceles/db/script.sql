CREATE USER 'admin_carcel1'@'localhost' IDENTIFIED BY 'Clas3s1Nt2024_!';
GRANT CREATE, INSERT, UPDATE, DELETE, SELECT, FILE, EXECUTE ON *.* TO 'admin_carcel1'@'localhost' WITH GRANT OPTION;

CREATE DATABASE administracion_carceles;


CREATE TABLE Municipality (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL
);

CREATE TABLE Prison (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    municipality_id INT,
    FOREIGN KEY (municipality_id) REFERENCES Municipality(id) ON DELETE CASCADE
);

#internos
CREATE TABLE Inmate (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    birth_date DATE,
    prison_id INT,
    FOREIGN KEY (prison_id) REFERENCES Prison(id) ON DELETE CASCADE
);

CREATE TABLE StaffRole (
    id INT PRIMARY KEY AUTO_INCREMENT,
    role_name VARCHAR(100) NOT NULL
);

CREATE TABLE Staff (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    role_id INT,
    prison_id INT,
    FOREIGN KEY (role_id) REFERENCES StaffRole(id) ON DELETE CASCADE,
    FOREIGN KEY (prison_id) REFERENCES Prison(id) ON DELETE CASCADE
);


CREATE TABLE Crime (
    id INT PRIMARY KEY AUTO_INCREMENT,
    crime_description VARCHAR(255) NOT NULL
);


CREATE TABLE Sentence (
    id INT PRIMARY KEY AUTO_INCREMENT,
    inmate_id INT,
    crime_id INT,
    sentence_date DATE,
    release_date DATE,
    sentence_length INT, -- Duración de la sentencia en meses
    FOREIGN KEY (inmate_id) REFERENCES Inmate(id) ON DELETE CASCADE,
    FOREIGN KEY (crime_id) REFERENCES Crime(id) ON DELETE CASCADE
);

CREATE TABLE Visitor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    visit_date DATE,
    inmate_id INT,
    FOREIGN KEY (inmate_id) REFERENCES Inmate(id) ON DELETE CASCADE
);


CREATE TABLE Incident (
    id INT PRIMARY KEY AUTO_INCREMENT,
    description TEXT NOT NULL,
    incident_date DATE,
    prison_id INT,
    FOREIGN KEY (prison_id) REFERENCES Prison(id) ON DELETE CASCADE
);

INSERT INTO Municipality (name, state) VALUES
('Medellín', 'Antioquia'),
('Bello', 'Antioquia'),
('Itagüí', 'Antioquia'),
('Envigado', 'Antioquia'),
('Rionegro', 'Antioquia');

INSERT INTO Prison (name, address, municipality_id) VALUES
('Cárcel Bellavista', 'Calle 45 # 70-20, Bello', 2),
('Centro Penitenciario El Pedregal', 'Calle 80 # 75-100, Medellín', 1),
('Cárcel La Paz', 'Carrera 25 # 15-50, Envigado', 4),
('Penitenciaría El Bosque', 'Carrera 30 # 40-20, Itagüí', 3),
('Cárcel San Antonio', 'Carrera 10 # 5-25, Rionegro', 5);

INSERT INTO Inmate (first_name, last_name, birth_date, prison_id) VALUES
('Carlos', 'Gómez', '1985-03-15', 1),
('Andrés', 'Pérez', '1990-07-21', 2),
('María', 'Rodríguez', '1988-11-30', 3),
('Juan', 'Martínez', '1975-01-12', 4),
('Ana', 'Hernández', '1995-05-05', 5);

INSERT INTO StaffRole (role_name) VALUES
('Guardia'),
('Médico'),
('Administrador'),
('Cocinero'),
('Psicólogo');

INSERT INTO Staff (first_name, last_name, role_id, prison_id) VALUES
('Pedro', 'López', 1, 1), -- Guardia en Cárcel Bellavista (Bello)
('Luisa', 'Ramírez', 2, 2), -- Médico en Centro Penitenciario El Pedregal (Medellín)
('Juan', 'Sánchez', 3, 3), -- Administrador en Cárcel La Paz (Envigado)
('Marta', 'Gómez', 4, 4), -- Cocinera en Penitenciaría El Bosque (Itagüí)
('Carlos', 'Fernández', 5, 5); -- Psicólogo en Cárcel San Antonio (Rionegro)

INSERT INTO Crime (crime_description) VALUES
('Robo a mano armada'),
('Tráfico de drogas'),
('Homicidio'),
('Fraude financiero'),
('Secuestro');

INSERT INTO Sentence (inmate_id, crime_id, sentence_date, release_date, sentence_length) VALUES
(1, 1, '2020-01-15', '2025-01-15', 60), -- Carlos Gómez sentenciado por Robo a mano armada
(2, 2, '2019-05-10', '2029-05-10', 120), -- Andrés Pérez sentenciado por Tráfico de drogas
(3, 3, '2018-07-25', '2033-07-25', 180), -- María Rodríguez sentenciada por Homicidio
(4, 4, '2021-03-30', '2026-03-30', 60), -- Juan Martínez sentenciado por Fraude financiero
(5, 5, '2022-09-10', '2032-09-10', 120); -- Ana Hernández sentenciada por Secuestro


INSERT INTO Visitor (first_name, last_name, visit_date, inmate_id) VALUES
('Laura', 'Gómez', '2023-06-15', 1), -- Visita de Laura Gómez a Carlos Gómez
('Pedro', 'Pérez', '2023-07-20', 2), -- Visita de Pedro Pérez a Andrés Pérez
('Sofía', 'Rodríguez', '2023-08-12', 3), -- Visita de Sofía Rodríguez a María Rodríguez
('Lucía', 'Martínez', '2023-09-05', 4), -- Visita de Lucía Martínez a Juan Martínez
('Javier', 'Hernández', '2023-10-01', 5); -- Visita de Javier Hernández a Ana Hernández

INSERT INTO Incident (description, incident_date, prison_id) VALUES
('Pelea entre dos internos en el patio', '2023-03-12', 1), -- Incidente en la Cárcel de Medellín
('Intento de fuga durante la noche', '2023-04-20', 2), -- Incidente en la Cárcel de Bello
('Guardia herido durante el traslado de internos', '2023-05-05', 3), -- Incidente en la Cárcel de Envigado
('Motín en la zona de celdas', '2023-06-10', 4), -- Incidente en la Cárcel de Itagüí
('Descubrimiento de drogas en una celda', '2023-07-25', 5); -- Incidente en la Cárcel de Rionegro









