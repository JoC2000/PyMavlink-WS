# PyMavlink-WS
PyMavlink repo for introduction to mavlink and drone programming

## Setup

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

## Software in the Loop (SITL)

Build for simulation board
```
cd ardupilot

./waf configure --board sitl

./waf copter
```

Run simulation
```
./build/sitl/bin/arducopter --model quad --defaults Tools/autotest/default_params/copter.parm
```

Run mavproxy
```
mavproxy.py --master=tcp:127.0.0.1:5760 --out=udp:127.0.0.1:14550 --console --map
```

### OR

Run sim_vehicle.py
```
sim_vehicle.py -v ArduCopter --console --map
```

**Note:** sim_vehicle.py might leave the port open when shutdown, to fix this you need to kill the process

```
sudo lsof -i :5760
```
Check whe PID number of the process and kill it
```
sudo kill -9 <PID>
```