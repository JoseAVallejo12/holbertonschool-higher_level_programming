-- Creates the database hbtn_0d_usa and the table states on your MySQL server.
CREATE DATABASE
IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE
IF NOT EXISTS hbtn_0d_usa.cities
(
	id INT NOT NULL UNIQUE AUTO_INCREMENT,
	state_id INT NOT NULL FOREIGN KEY(state_id) REFERENCES state(id),
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
);
