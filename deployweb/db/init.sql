CREATE DATABASE postcodes;
\c postcodes;
CREATE USER postcodes WITH PASSWORD 'postcodes';
ALTER ROLE postcodes SET client_encoding TO 'utf8';
ALTER ROLE postcodes SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE postcodes TO postcodes;

CREATE TABLE IF NOT EXISTS "postcodes" ("postcode" varchar(10) NOT NULL PRIMARY KEY );
CREATE TABLE IF NOT EXISTS "party" ("id" integer NOT NULL PRIMARY KEY , "name" varchar(200) NOT NULL);
INSERT INTO party VALUES(1,'Rebooting Democracy');
INSERT INTO party VALUES(2,'Conservatives');
INSERT INTO postcodes VALUES('CB43HR');

