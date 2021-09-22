FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /regula
COPY requirements.txt /regula
RUN pip install --upgrade pip -r requirements.txt
RUN apt-get update
COPY . /regula