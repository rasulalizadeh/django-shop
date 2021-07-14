FROM python:3.8.11-slim-buster

RUN apt-get update && apt-get install libmariadb-dev-compat default-mysql-client gcc -y
RUN pip install django django_rest_framework mysql-connector-python django-environ mysqlclient

RUN mkdir /opt/website/
COPY . /opt/website/

WORKDIR /opt/website/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]