# Nyaupi Raspberry

![Nyaupi](/images/nyaupi_art.png)

Nyaupi raspberry is a handmade house alarm made with a raspberry.
Here I'm going to briefly document it
but you can find more information about the creation process on
[this blog post](https://jordifierro.com/nyaupi-raspberry-alarm).

## Requirements

* Detect when a door is opened
* Make some noise
* Notify outside
* Be deactivable
* High availability

## Pieces

* Raspberry Pi 4
* Memory card
* Power connector + extension cable
* Active buzzer
* Magnetic sensor switch
* Breadbord + connection clabes
* Battery shield + battery
* Wooden board + screws

## Wiring

Before starting building the system we must install
an operative system to our Raspberry and connect it to the network.
In my case I've chosen
[Raspberry Pi OS (32-bit) Lite](https://www.raspberrypi.org/downloads/raspberry-pi-os/)
(previously called Raspbian)
because it officially supports GPIO.

![Wiring](/images/nyaupi_wiring.png)

Insert the battery to the shield (check the + and - sides)
and then insert it between raspberry power supply and raspberry itself.
**(Poweroff your raspberry before disconnecting it to prevent memory corruption!)**

_In my case I picked the wrong usb shield and I had to buy two micro-usb to usb-c adapters._

After battery is charged, disconnect your raspberry power supply 
to check the battery shield keeps raspberry working correctly.

_Again, in my case battery shield doesn't work correctly.
When a power interruption occurs, battery starts giving power to raspberry
but after a quick restart so unfortunately raspberry loses power for a second,
which is not recommended..._

For the door sensor, connect one leg to PIN 8 and
the other to the breadboard ground (which comes from PIN 6).
Then, place the wired side of the sensor switch on the door frame
and the other on the door itself.

For the active buzzer, connect VCC buzzer pin to 3V3 power raspberry PIN 1,
I/O buzzer pin to PIN 7 and GND buzzer pin to breadboard ground (shared again from PIN 6).

## Code

Alarm code is made of some scripts, each one with an specific task:
* `storage.py`: store and retrieve door and alarm state on an sqlite3 db.
* `buzzer.py`: beep & alarm sounds.
* `door.py`: checks door sensor state and stores it to db.
* `mail.py`: send a notification email.
* `switch.py` (not an script but a flask api):
exposes on port 5000 methods `/on` and `/off` to handle alarm state,
and `/status` to get alarm and door state.
* `alarm.py`: the core script. Starts storage and door scripts. Then checks state changes on a loop.
It has 3 functionalities. When alarm is activated beep twice. When alarm is deactivated beep once.
And when door is opened and alarm active start alert sound and send notification emails.

All scripts also have a `__main__` function to be tested alone. For example:
```bash
python3 buzzer.py beep times 7
```
will make buzzer beep seven times.

### Setup

* Make raspberry LAN ip static. You can do it from the router or using raspberry DHCP client daemon (DHCPCD).
* Install docker:
```bash
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
```
* Clone git repo & get into it:
```bash
git clone https://github.com/jordifierro/nyaupi-raspberry.git
cd nyapi-raspberry
```
* Some configuration has been parametrized to be easily changed:
```bash
SECRET_KEY=X                # Used later for authenticate from the client
ALARM_SOUND_MINUTES=1       # How long buzzer in case of alarm
DOOR_SENSOR_PIN=8           # Your connected pins
BUZZER_PIN=7
EMAIL_HOST=smtp.mail.io     # Set up an email server to send notifications and paste config here
EMAIL_PORT=587
EMAIL_HOST_USER=user@mail.com
EMAIL_HOST_PASSWORD=X
EMAIL_FROM=alarm@mail.com   # Define the content and receiver of the alarm notification email
EMAIL_TO=receiver1@mail.com, receiver2@mail.com
EMAIL_SUBJECT=ALARM
EMAIL_MESSAGE=Door has been opened!
```
Set your own params to `env.list` file:
```bash
cp env.list.sample env.list
```
* Build & run with docker:
```bash
sudo docker build -t nyaupi .
sudo docker run --privileged -p 5000:5000 --name nyaupi --restart=always -d -t nyaupi
```

You can use [nyaupi-android](https://github.com/jordifierro/nyaupi-android)
as remote controller to active/deactivate the alarm. Check it out!
