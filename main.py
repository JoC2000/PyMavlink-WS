from pymavlink import mavutil
from utils import *

# Create mavlink connection with ardupilot sim

# System requests protocol version for mavlink protocol negotiation
connection = mavutil.mavlink_connection("udpin:localhost:14550")

# Wait for first heartbeat
connection.wait_heartbeat()
print("Heartbeat from system (system: %u component: %u)" % (connection.target_system, connection.target_component))

# Start data streaming
req_local_pos(connection)

# Arm the vehicle
arm(connection)

# Takeoff
takeoff(connection)

# Move to local position, NED coordinates

set_local_pos(connection, 10, 0, -10)

# Land
land(connection)
