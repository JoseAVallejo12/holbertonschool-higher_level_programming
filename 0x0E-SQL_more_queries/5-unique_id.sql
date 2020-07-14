-- Creates the database hbtn_0d_usa and the table states on your MySQL server.
CREATE DATABASE
IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE
IF NOT EXISTS unique_id
(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
);
