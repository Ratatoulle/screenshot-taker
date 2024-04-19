FROM python:3.11-slim
FROM bitnami/minio:latest

COPY . .
COPY ../requirements.txt .

RUN pip install -r requirements.txt

#CMD openssl ecparam -genkey -name prime256v1 | openssl ec -out private.key
#CMD openssl req -new -x509 -days 3650 -key private.key -out public.crt
#
#COPY public.key .minio_work/certs
#COPY public.crt .minio_work/certs

