from pymavlink import mavutil
import math
import time

def arm(connection):
    connection.mav.command_long_send(connection.target_system,
                                     connection.target_component,
                                     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                                     0,
                                     1,
                                     0,
                                     0,0,0,0,0)
    
    # Wait for ACK
    msg = connection.recv_match(type="COMMAND_ACK", blocking=True)
    print(msg)


def disarm(connection):
    connection.mav.command_long_send(connection.target_system,
                                     connection.target_component,
                                     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                                     0,
                                     0,
                                     0,
                                     0,0,0,0,0)
    
    # Wait for ACK
    msg = connection.recv_match(type="COMMAND_ACK", blocking=True)
    print(msg)


def takeoff(connection):
    connection.mav.command_long_send(connection.target_system,
                                     connection.target_component,
                                     mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
                                     0,
                                     0,0,0,0,0,0,10)
    
    # Wait for ACK
    msg = connection.recv_match(type="COMMAND_ACK", blocking=True)
    print(msg)

    # Wait for desired altitude
    is_takeoff = 1

    while is_takeoff:
        pos_msg = connection.recv_match(type="LOCAL_POSITION_NED", blocking=True)
        print("Altitude: ", -pos_msg.z) 
        if pos_msg.z < -9.8:
            print("Reached altitude")
            is_takeoff = 0


def req_local_pos(connection):
    # TODO: MAV_CMD_SET_MESSAGE_INTERVAL
    connection.mav.command_long_send(connection.target_system,
                                     connection.target_component,
                                     mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,
                                     0,
                                     mavutil.mavlink.MAVLINK_MSG_ID_LOCAL_POSITION_NED,
                                     100000,
                                     0,0,0,0,0)
    
    # Wait for ACK
    msg = connection.recv_match(type="COMMAND_ACK", blocking=True)
    print(msg)


def set_local_pos(connection, x, y, z):
    """
    Set target location in local frame NED.

    Parameters:
        x : distance in meters
        y : distance in meters
        z : distance in meters
    """

    connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(
                        10,
                        connection.target_system,
                        connection.target_component,
                        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
                        int(0b110111111000),
                        x, y, z,
                        0,0,0,
                        0,0,0,
                        0,0
                        ))
    
    moving = 1
    tolerance = 0.2
    while moving:
        pos_msg = connection.recv_match(type="LOCAL_POSITION_NED", blocking=True)
        print("x: %f y: %f z: %f\n" % (pos_msg.x,pos_msg.y,pos_msg.z))

        ex = x - pos_msg.x
        ey = y - pos_msg.y
        ez = z - pos_msg.z

        distance = math.sqrt(ex*ex + ey*ey + ez*ez)
        print("Distance: ", distance)

        if distance < tolerance:
            print("Reached point")
            moving = 0


def land(connection):
    #TODO: MAV_CMD_NAV_LAND
    connection.mav.command_long_send(connection.target_system,
                                     connection.target_component,
                                     mavutil.mavlink.MAV_CMD_NAV_LAND,
                                     0,
                                     0,0,0,0,0,0,0)
    
    # Wait for ACK
    msg = connection.recv_match(type="COMMAND_ACK", blocking=True)
    print(msg)