#!/bin/sh
# wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD="adminadmin" psql -h "$host" -d "blog" -U "admin" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 ls -a /var/run/postgresql/

>&2 echo "Postgres is up - executing command"
exec $cmd