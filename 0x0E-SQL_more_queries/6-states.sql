--  creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)

-- creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- creates the TABLE states
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT UNIQUE NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
);
