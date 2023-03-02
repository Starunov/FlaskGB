FROM python:3.9.1-buster

WORKDIR /app

RUN apt-get update \
&& apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY wsgi.py wsgi.py
COPY ./blog/ ./blog

COPY wait-for-postgres.sh .
RUN chmod +x wait-for-postgres.sh

EXPOSE 5000

