@echo off

set DBHOST=localhost
set DBUSER=turtle_master_db_admin
set DBNAME=turtle_master_db
set DBPASS=covidhub@io

@echo Please make sure the database '%DBNAME%' has been created on %DBHOST%
@echo and db user '%DBUSER%' has been set with pwd = '%DBPASS%'
@echo Please run the following SQL to do so:
@echo CREATE DATABASE %DBNAME% ;
@echo CREATE ROLE %DBUSER% WITH ENCRYPTED PASSWORD '%DBPASS%' ;
@echo ALTER ROLE %DBUSER% WITH LOGIN SUPERUSER INHERIT CREATEDB CREATEROLE REPLICATION;
@echo GRANT ALL PRIVILEGES ON DATABASE %DBNAME% TO  %DBUSER%;
@echo ALTER ROLE %DBUSER% SET client_encoding TO 'utf8';
@echo ALTER ROLE %DBUSER% SET default_transaction_isolation TO 'read committed';
@echo ALTER ROLE %DBUSER% SET timezone TO 'UTC';
