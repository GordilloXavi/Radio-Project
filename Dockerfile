FROM python:3.8.2-slim-buster

WORKDIR /app

# Copy only the source code (maybe do a .dockerignore instead)
COPY /app /app/app
COPY pyproject.toml /app
COPY start.py /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE $PORT

CMD gunicorn -b 0.0.0.0:$PORT start:app
