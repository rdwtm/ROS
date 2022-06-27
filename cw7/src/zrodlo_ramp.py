#!/usr/bin/python3

import rospy
from std_msgs.msg import Float32

try:
  rospy.init_node("zrodlo_ramp")
  initial_value = rospy.get_param("~x0", 0.0)
  slope = rospy.get_param("~dx", 1.0)
  rate = rospy.get_param("~rate", 10.0)
  # print "Parametry:"
  # print " * x0 = ", initial_value
  # print " * dx = ", slope
  # print " * rate = ", rate
  pub = rospy.Publisher("u", Float32, queue_size=10)
  loop_rate = rospy.Rate(rate)
  dt = 1.0/rate
  u = initial_value
  while not rospy.is_shutdown():
    slope = rospy.get_param("~dx", 1.0)
    pub.publish(u)
    u = u + slope * dt
    loop_rate.sleep()
  
except rospy.ROSInterruptException:
  pass
