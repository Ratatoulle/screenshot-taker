FROM python:3.11

COPY . .
COPY ../database /http_api/database
COPY ../minio_work /http_api/minio_work
COPY ../selenium_work /http_api/selenium_work
COPY ../requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#RUN ["uvicorn", "http_api.main:app", "--host", "0.0.0.0", "--port", "80"]
