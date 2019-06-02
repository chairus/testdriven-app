# base image
FROM postgres:11.2-alpine

# extend the postgres image by adding the create.sql file which will run on init
ADD create.sql /docker-entrypoint-initdb.d