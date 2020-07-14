-- Creates the table force_name on your MySQL server.
CREATE TABLE
IF NOT EXISTS id_not_null
(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256) NOT NULL
);
