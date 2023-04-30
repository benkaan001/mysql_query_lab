-- make sure to follow the order due to FK references

DROP TABLE IF EXISTS universities.country;

CREATE TABLE universities.country (
  id INT NOT NULL AUTO_INCREMENT,
  country_name varchar(100) DEFAULT NULL,
  CONSTRAINT pk_country PRIMARY KEY (id)
);

DROP TABLE IF EXISTS universities.ranking_system;

CREATE TABLE universities.ranking_system (
  id INT NOT NULL AUTO_INCREMENT,
  system_name VARCHAR(100) DEFAULT NULL,
  CONSTRAINT pk_ranksys PRIMARY KEY (id)
);


DROP TABLE IF EXISTS universities.ranking_criteria;

CREATE TABLE universities.ranking_criteria (
  id INT NOT NULL AUTO_INCREMENT,
  ranking_system_id INT DEFAULT NULL,
  criteria_name VARCHAR(200) DEFAULT NULL,
  CONSTRAINT pk_rankcrit PRIMARY KEY (id),
  CONSTRAINT fk_rc_rs FOREIGN KEY (ranking_system_id) REFERENCES universities.ranking_system (id)
);



DROP TABLE IF EXISTS universities.university;

CREATE TABLE universities.university (
  id INT NOT NULL AUTO_INCREMENT,
  country_id INT DEFAULT NULL,
  university_name VARCHAR(200) DEFAULT NULL,
  CONSTRAINT pk_uni PRIMARY KEY (id),
  CONSTRAINT fk_uni_cnt FOREIGN KEY (country_id) REFERENCES universities.country (id)
);

DROP TABLE IF EXISTS universities.university_year;

CREATE TABLE universities.university_year (
  university_id INT DEFAULT NULL,
  year INT DEFAULT NULL,
  num_students INT DEFAULT NULL,
  student_staff_ratio DECIMAL(6,2) DEFAULT NULL,
  pct_international_students INT DEFAULT NULL,
  pct_female_students INT DEFAULT NULL,
  CONSTRAINT fk_uy_uni FOREIGN KEY (university_id) REFERENCES universities.university (id)
);

DROP TABLE IF EXISTS universities.university_ranking_year;

CREATE TABLE universities.university_ranking_year (
  university_id INT DEFAULT NULL,
  ranking_criteria_id INT DEFAULT NULL,
  year INT DEFAULT NULL,
  score INT DEFAULT NULL,
  CONSTRAINT fk_ury_rc FOREIGN KEY (ranking_criteria_id) REFERENCES universities.ranking_criteria (id),
  CONSTRAINT fk_ury_uni FOREIGN KEY (university_id) REFERENCES universities.university (id)
);

COMMIT;