FROM python:3.8.2-slim-buster

WORKDIR /app

COPY /app /app
COPY pyproject.toml /app


RUN apt-get update
RUN pip install --upgrade pip
RUN pip install poetry 
RUN poetry install

EXPOSE 5000

#CMD pipenv run flask run --host 0.0.0.0
CMD sleep 10000
