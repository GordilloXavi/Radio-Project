FROM python:3.8-slim-buster

RUN pip install poetry 

COPY . /app
WORKDIR /app

RUN poetry install

EXPOSE 5000

CMD pipenv run flask run --host 0.0.0.0
