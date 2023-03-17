-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) 

-- creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use database
USE hbtn_0d_usa;

-- creates the table cities 
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	-- set state_id as foreign key
	state_id INT NOT NULL ,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES states(id)
);
