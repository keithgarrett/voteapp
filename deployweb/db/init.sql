CREATE DATABASE postcodes;
\c postcodes;
CREATE USER postcodes WITH PASSWORD 'postcodes';
ALTER ROLE postcodes SET client_encoding TO 'utf8';
ALTER ROLE postcodes SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE postcodes TO postcodes;

CREATE TABLE IF NOT EXISTS "postcodes" ("postcode" varchar(10) NOT NULL PRIMARY KEY,
                                        "constituency" varchar(10));

CREATE TABLE IF NOT EXISTS "constituencies" ("constituency_code" varchar(10) NOT NULL PRIMARY KEY,
                                             "constituency_name" varchar(255));

CREATE TABLE IF NOT EXISTS "elections" ("election_code" varchar(10) NOT NULL PRIMARY KEY,
                                        "election_name" varchar(255),
                                        "constituency_code" varchar(10));

CREATE TABLE IF NOT EXISTS "parties" ("party_code" varchar(10) NOT NULL PRIMARY KEY,
                                      "party_name" varchar(255));

CREATE TABLE IF NOT EXISTS "partieslink" ( "election_code" varchar(10),
                                           "party_code" varchar(10));

INSERT INTO postcodes VALUES('CB43HR',1);
INSERT INTO postcodes VALUES('HA14RL',2);

INSERT INTO constituencies VALUES(1,'Cambridge');
INSERT INTO constituencies VALUES(2,'Harrow');

INSERT INTO elections VALUES(1,'Cambridge Byelection', 1);
INSERT INTO elections VALUES(2,'Harrow Binlection',2);

INSERT INTO parties VALUES(1,'Labour');
INSERT INTO parties VALUES(2,'Green');
INSERT INTO parties VALUES(3,'Conservative');
INSERT INTO parties VALUES(4,'Rebooting Democracy');

INSERT INTO partieslink VALUES(1,1);
INSERT INTO partieslink VALUES(1,2);
INSERT INTO partieslink VALUES(1,3);
INSERT INTO partieslink VALUES(1,4);
INSERT INTO partieslink VALUES(2,1);
INSERT INTO partieslink VALUES(2,2);
INSERT INTO partieslink VALUES(2,3);
