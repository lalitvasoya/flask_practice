# demo docker with jenkins
FROM python:3.8

WORKDIR /flask-structure
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /flask-structure
