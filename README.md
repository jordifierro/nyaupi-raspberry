# Setup

* Install docker:
```bash
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
```
* Connect buzzer & door sensor
```
connect door sensor to an I/O pin (eg: PIN 8) with one leg and ground with other one
connect buzzer VCC to 3V3 power pin (eg: PIN 1), I/O to an I/O pin (eg: PIN 7) and GND to ground
```
* Clone git repo & get into it:
```bash
git clone https://github.com/jordifierro/nyaupi-raspberry.git
cd nyapi-raspberry
```
* Build & run with docker:
```bash
sudo docker build -t nyaupi .
sudo docker run --privileged -p 5000:5000 --name nyaupi --restart=always -d -t nyaupi
```
