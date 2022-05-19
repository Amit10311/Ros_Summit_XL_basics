#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2018, Delft University of Technology
# TU Delft Robotics Institute. All rights reserved.

# Node to drive the summit in circles.

import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':

    rospy.init_node('drive_summit_circle')
    pub = rospy.Publisher('/robot/robotnik_base_control/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(4)
    move = Twist()
    move.linear.x = 0.2  # Move the robot with a linear velocity in the x axis
    move.angular.z = 0.5  # Move the with an angular velocity in the z axis

    while not rospy.is_shutdown():
        pub.publish(move)
        rate.sleep()
