DROP TABLE IF EXISTS Accounts;

CREATE TABLE IF NOT EXISTS Accounts (
  account_id INT NOT NULL,
  income INT NOT NULL
);

TRUNCATE TABLE Accounts;

INSERT INTO Accounts (account_id, income) VALUES
  (3, 108939),
  (2, 12747),
  (8, 87709),
  (6, 91796);
