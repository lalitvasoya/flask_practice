# demo docker with jenkins
FROM python:3.8

COPY requirements.txt /flask-structure/
RUN pip install -r requirements.txt

COPY . /flask-structure
WORKDIR /flask-structure
