CREATE USER 'admin_carcel'@'localhost' IDENTIFIED BY 'Clas3s1Nt2024_!';
GRANT CREATE, INSERT, UPDATE, DELETE, SELECT, FILE, EXECUTE ON *.* TO 'admin_carcel'@'localhost' WITH GRANT OPTION;

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
