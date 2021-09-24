# demo docker with jenkins
FROM python:3.8

COPY . /flask-structure
WORKDIR /flask-structure

RUN pip install -r requirements.txt