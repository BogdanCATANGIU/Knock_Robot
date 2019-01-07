#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

    # Author: Bogdan Catangiu
    # This ROS Node converts Joystick inputs from the joy node
    # into commands for bookshelf_robot
def callback(data):
    twist = Twist()
    if data.buttons[4] == 1: #slow movement
        twist.linear.x = 0.1*data.axes[1]
        twist.angular.z = -0.1*data.axes[0]
    else: # fast movement
        twist.linear.x = 2*data.axes[1]
        twist.angular.z = -2*data.axes[0]
    pub.publish(twist)

    # Intializes everything
def start():
    # publishing to "/cmd_vel" to control bookshelf_robot base
    global pub
    rospy.init_node('joy_to_twist')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.spin()

if __name__ == '__main__':
    start()
    
