FROM python:3.12.1

RUN apt-get update && \
    apt-get install -yq tzdata


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY matrix /app