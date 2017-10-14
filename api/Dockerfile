FROM python:3.6.2
LABEL maintainer twtrubiks
ENV PYTHONUNBUFFERED 1
RUN mkdir /api
WORKDIR /api
COPY . /api/
RUN pip install -r requirements.txt

