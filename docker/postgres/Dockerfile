# Get base postgres image
FROM postgres:13.6-alpine

RUN mkdir -p /docker-entrypoint-initdb.d
COPY ./initdb-postgres.sh /docker-entrypoint-initdb.d/postgres.sh
