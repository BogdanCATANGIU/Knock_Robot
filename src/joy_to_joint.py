#!/usr/bin/env python
import rospy
import rospy
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from sensor_msgs.msg import Joy
from control_msgs.msg import FollowJointTrajectoryActionGoal

    # Author: Bogdan Catangiu
    # This ROS Node converts Joystick inputs from the joy node
    # into commands for bookshelf_robot arm
def effort_callback(data):
    effort_trajectory = JointTrajectory()
    position_trajectory = JointTrajectory()
    
    effort_trajectory.joint_names = effort_joint_names
    effort_trajectory.points.append(effort_points)

    position_trajectory.joint_names = position_joint_names
    position_trajectory.points.append(position_points)

    #button that controls shoulder joint
    if data.axes[7] == 1:
        effort_points.positions[1] -= 0.005
    elif data.axes[7] == 0:
        pass
    else:
        effort_points.positions[1] += 0.005

    #button that controls elbow joint
    if data.axes[6] == 1:
        effort_points.positions[0] += 0.005
    elif data.axes[6] == 0:
        pass
    else:
        effort_points.positions[0] -= 0.005
    
    #button that controls hip joint
    if data.buttons[6]:
        position_points.positions[0] -= 0.01
    if data.buttons[7]:
        position_points.positions[0] += 0.01
    #button to knock can of the shelf
    if data.buttons[3]:
        effort_points.positions[0] += 0.15
        position_points.positions[0] -= 0.3
    #button to go to second can height
    if data.buttons[2]:
        effort_points.positions[1] = 0.845
    #button to go to third can height
    if data.buttons[0]:
        effort_points.positions[1] = 0.5
    #button to go to fourth can height
    if data.buttons[1]:
        effort_points.positions[1] = 0.14


    effort_points.time_from_start = rospy.Time(1)
    position_points.time_from_start = rospy.Time(1)
    effort_trajectory.header.stamp = rospy.Time.now()
    position_trajectory.header.stamp = rospy.Time.now()

    effort_pub.publish(effort_trajectory)
    position_pub.publish(position_trajectory)

    # Intializes everything
def start():
    # publishing to "/arm_controller_effort/command" and "/arm_controller_position/command" 
    # to control bookshelf_robot arm
    global effort_pub, position_pub
    global effort_joint_names, position_joint_names
    global effort_points, position_points
    effort_points = JointTrajectoryPoint()
    position_points = JointTrajectoryPoint()
    effort_points.positions = [0.25, 1.0]
    position_points.positions = [0, 0]
    effort_joint_names = ["elbow_joint", "shoulder_joint"]
    position_joint_names = ["hip_joint", "wrist_joint"]
    rospy.init_node('joy_to_joint_trajectory')
    effort_pub = rospy.Publisher('arm_controller_effort/command', JointTrajectory, queue_size = 1)
    position_pub = rospy.Publisher('arm_controller_position/command', JointTrajectory, queue_size = 1)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, effort_callback)
    # starts the node
    rospy.spin()

if __name__ == '__main__':
    start()
    
