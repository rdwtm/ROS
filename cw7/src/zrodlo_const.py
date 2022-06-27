#!/usr/bin/python3

import rospy
from std_msgs.msg import Float32

try:
  rospy.init_node("zrodlo_const")
  value = rospy.get_param("~x0", 1.0)
  rate = rospy.get_param("~rate", 10.0)
  # print "Parametry:"
  # print " * x0 = ", value
  # print " * rate = ", rate
  pub = rospy.Publisher("u", Float32, queue_size=10)
  loop_rate = rospy.Rate(rate)
  while not rospy.is_shutdown():
    value = rospy.get_param("~x0", 1.0)
    pub.publish(value)
    loop_rate.sleep()
  
except rospy.ROSInterruptException:
  pass
