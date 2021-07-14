FROM python:3.8.11-slim-buster

RUN apt-get update
RUN pip install django django_rest_framework mysql-connector-python django-environ
RUN apt-get install libmariadb-dev-compat default-mysql-client -y
RUN apt-get install gcc -y
RUN pip install mysqlclient

RUN mkdir /opt/website/
COPY . /opt/website/

WORKDIR /opt/website/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]