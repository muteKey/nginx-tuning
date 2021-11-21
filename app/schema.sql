DROP TABLE IF EXISTS user;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  gender TEXT,
  firstName TEXT,
  lastName TEXT,
  city TEXT,
  postcode TEXT,
  email TEXT,
  username TEXT,
  birthdate TEXT,
  phone TEXT,
  imageName TEXT
);
