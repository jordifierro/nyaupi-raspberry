FROM raspbian/stretch

RUN mkdir /code
WORKDIR /code

RUN apt update && apt --yes install python3-pip
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

COPY . /code/

CMD python3 status && python3 alarm.py
