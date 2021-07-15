-- Write a script that creates a table second_table
-- add multiples rows.
-- Creating table
CREATE TABLE IF NOT EXISTS second_table(
	id INT,
	name VARCHAR(256),
	score INT);
-- Adds a row for John
INSERT INTO second_table (id, name, score) VALUES (1, "John", 10);
-- Adds a row fro Alex
INSERT INTO second_table (id, name, score) VALUES (2, "Alex", 3);
-- Adds a row for Bob
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 14);
-- Adds a row for George
INSERT INTO second_table (id, name, score) VALUES (4, "George", 8);
