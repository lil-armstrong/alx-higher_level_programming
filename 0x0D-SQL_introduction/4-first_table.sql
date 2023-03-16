-- creates a table called first_table in the current database
-- The database name will be passed as an argument of the mysql command
-- Will not fail if the table first_table already exists

CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
