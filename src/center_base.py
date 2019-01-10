#!/usr/bin/env python
import rospy
import math
from sensor_msgs.msg import LaserScan

    # Author: Bogdan Catangiu
    # This ROS Node outputs if robot base is centered in relation to bookshelf
    # Temporary behaviour
def callback(data):
    angles = []
    ranges = []
    for index, range in enumerate(data.ranges):
        if range < 10 and range >0:
            angles.append((data.angle_min + (index * data.angle_increment))*180/math.pi)
            ranges.append(range)
    if ranges[len(angles)/2] < 0.77:
        print str(ranges[len(angles)/2]) + " BACK "
    elif ranges[len(angles)/2] > 0.79:
        print str(ranges[len(angles)/2]) + " FORWARD "
    else:
        print str(ranges[len(angles)/2]) + " OK "
    if angles[0] < -33 :
        print str(angles[0]) + " " + str(angles[-1]) + " RIGHT"
    elif angles[0] > -31:
        print str(angles[0]) + " " + str(angles[-1]) + " LEFT"
    else:
        print str(angles[0]) + " " + str(angles[-1]) + " OK"

    # Intializes everything
def start():
    rospy.init_node('center_base')
    # subscribed to joystick inputs on topic "scan"
    rospy.Subscriber("scan", LaserScan, callback)
    # starts the node
    rospy.spin()

if __name__ == '__main__':
    start()