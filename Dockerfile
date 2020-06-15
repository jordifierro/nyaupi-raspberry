FROM raspbian/stretch

ENV LC_ALL en_US.utf-8
ENV LANG en_US.utf-8
ENV FLASK_APP switch.py
EXPOSE 5000

RUN mkdir /code
WORKDIR /code

RUN apt update && apt --yes install python3-pip
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

COPY . /code/

CMD python3 alarm.py & flask run --host=0.0.0.0
