-- creates the table unique_id on your MySQL server.

CREATE TABLE IF NOT EXISTS unique_id (
	-- set id with default value of 1, and make id unique
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
