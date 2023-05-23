DROP TABLE IF EXISTS exams;

CREATE TABLE exams (
student VARCHAR(15),
exam VARCHAR(15),
score INT
);

INSERT INTO exams (student,exam,score) values ('Bao','Math',90);
INSERT INTO exams (student,exam,score) values ('Bao','English',78);
INSERT INTO exams (student,exam,score) values ('Bao','History',88);
INSERT INTO exams (student,exam,score) values ('Bao','Art',60);
INSERT INTO exams (student,exam,score) values ('Joe','Math',69);
INSERT INTO exams (student,exam,score) values ('Joe','English',87);
INSERT INTO exams (student,exam,score) values ('Joe','History',98);
INSERT INTO exams (student,exam,score) values ('Joe','Art',79);
INSERT INTO exams (student,exam,score) values ('Jane','Math',99);
INSERT INTO exams (student,exam,score) values ('Jane','English',77);
INSERT INTO exams (student,exam,score) values ('Jane','History',83);
INSERT INTO exams (student,exam,score) values ('Jane','Art',100);

COMMIT;