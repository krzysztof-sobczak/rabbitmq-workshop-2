FROM python:3

RUN pip install pika;
RUN pip install requests;

WORKDIR /usr/src/app