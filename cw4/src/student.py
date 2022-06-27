#!/usr/bin/env python3

import rospy
from cw4.msg import Student

def student_cb(msg):
	rospy.loginfo('{}'.format(msg))
	
rospy.init_node('cw4')
sub= rospy.Subscriber('/student', Student, student_cb)
rospy.spin()
