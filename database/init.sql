CREATE DATABASE mydatabase;
\c mydatabase;
CREATE TABLE mytable (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT
);
INSERT INTO mytable (name, age) VALUES ('John', 30);
INSERT INTO mytable (name, age) VALUES ('Jane', 25);
