FROM python

RUN apt-get update
RUN apt-get install python3 -y

COPY test.py "/opt/test.py"

CMD ["python3", "/opt/test.py"]