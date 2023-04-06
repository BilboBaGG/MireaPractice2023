FROM python:latest

COPY . /project

WORKDIR /project  

CMD ["ls", "-la"]