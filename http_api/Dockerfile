FROM python:3.11-slim

COPY . .
COPY ../database /http_api/database
COPY ../minio_work /http_api/minio_work
COPY ../selenium_work /http_api/selenium_work
COPY ../requirements.txt .

RUN pip install -r requirements.txt
