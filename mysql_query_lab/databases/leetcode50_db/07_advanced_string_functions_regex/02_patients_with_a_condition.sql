DROP TABLE IF EXISTS Patients;

CREATE TABLE IF NOT EXISTS Patients (
  patient_id INT,
  patient_name VARCHAR(30),
  conditions VARCHAR(100)
);

TRUNCATE TABLE Patients;

INSERT INTO Patients (patient_id, patient_name, conditions)
VALUES (1, 'Daniel', 'YFEV COUGH'),
       (2, 'Alice', ''),
       (3, 'Bob', 'DIAB100 MYOP'),
       (4, 'George', 'ACNE DIAB100'),
       (5, 'Alain', 'DIAB201');
