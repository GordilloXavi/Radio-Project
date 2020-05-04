FROM python:3.8.2-slim-buster

# Need these packages to compile psycopg2 from source
RUN apt-get update
RUN apt-get install -y \
    libpq-dev \
    python-dev \
    gcc

WORKDIR /app

# Copy only the source code (maybe do a .dockerignore instead)
COPY /app /app/app
COPY pyproject.toml /app
COPY start.py /app

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE $PORT

# CMD gunicorn --worker-class eventlet -w 1 start:app #with eventlet installed
CMD gunicorn -k gevent -w 1 start:app #with gevent installed