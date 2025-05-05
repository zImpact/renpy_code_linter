FROM python:3.11-slim

COPY . /app
WORKDIR /app

ENTRYPOINT ["python", "/app/src/renpy_code_linter/cli.py"]