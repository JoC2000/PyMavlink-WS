# PyMavlink-WS
PyMavlink repo for introduction and simple workshop

Necessary packages
```
sudo apt install git
sudo apt install python3-pip
pip3 install pymavlink
```

ArduPilot dev env setup
```
git clone --recurse-submodules https://github.com/ArduPilot/ardupilot.git

sudo usermod -a -G dialout $USER

cd ardupilot

Tools/environment_install/install-prereqs-ubuntu.sh -y

. ~/.profile
```
