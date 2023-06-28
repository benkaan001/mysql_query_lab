DROP TABLE IF EXISTS Transactions;

CREATE TABLE IF NOT EXISTS Transactions (
  id INT NOT NULL AUTO_INCREMENT,
  country VARCHAR(4) NOT NULL,
  state ENUM('approved', 'declined') NOT NULL,
  amount INT NOT NULL,
  trans_date DATE NOT NULL,
  PRIMARY KEY (id)
);

TRUNCATE TABLE Transactions;

INSERT INTO Transactions (id, country, state, amount, trans_date) VALUES
  (121, 'US', 'approved', 1000, '2018-12-18'),
  (122, 'US', 'declined', 2000, '2018-12-19'),
  (123, 'US', 'approved', 2000, '2019-01-01'),
  (124, 'DE', 'approved', 2000, '2019-01-07');
