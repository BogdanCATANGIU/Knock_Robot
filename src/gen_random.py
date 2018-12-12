#!/usr/bin/env python 

import random
import rospy
import time
import tf

from gazebo_msgs.msg import ModelState

rospy.wait_for_service('gazebo/set_model_state')

pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
rospy.init_node('mover', anonymous=True)
time.sleep(1)
message=ModelState()
message.model_name = "shelf"
message.pose.position.x = random.uniform(4,6)
message.pose.position.y = random.uniform(-2,2)
quat=tf.transformations.quaternion_from_euler(0,0,random.uniform(4, 5.5))
message.pose.orientation.x=quat[0]
message.pose.orientation.y=quat[1]
message.pose.orientation.z=quat[2]
message.pose.orientation.w=quat[3]
message.reference_frame="world"
pub.publish(message)