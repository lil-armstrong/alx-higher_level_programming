-- Write a script that creates the table id_not_null on your MySQL server.
-- Will not fail if the table id_not_null already exists        

CREATE TABLE IF NOT EXISTS id_not_null (
	-- set id to have a default value of 1
	id INT DEFAULT 1,
	name VARCHAR(256)
);
