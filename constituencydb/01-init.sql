CREATE DATABASE votes;
\c votes;
CREATE USER votes WITH PASSWORD 'votes';
ALTER ROLE votes SET client_encoding TO 'utf8';
ALTER ROLE votes SET default_transaction_isolation TO 'read committed';
ALTER ROLE votes SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE votes TO votes;

