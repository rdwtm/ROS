#!/usr/bin/python3

import math
import rospy
from std_msgs.msg import Float32

try:
  rospy.init_node("zrodlo_sin")
  A = rospy.get_param("~A", 1.0)
  f = rospy.get_param("~f", 1.0)
  rate = rospy.get_param("~rate", 10.0)
  # print "Parametry:"
  # print " * A = ", A
  # print " * f = ", f
  # print " * rate = ", rate
  pub = rospy.Publisher("u", Float32, queue_size=10)
  loop_rate = rospy.Rate(rate)
  w = 2*math.pi*f
  t = 0.0
  dt = 1.0/rate
  while not rospy.is_shutdown():
    A = rospy.get_param("~A", 1.0)
    f = rospy.get_param("~f", 1.0)
    pub.publish(A*math.sin(w*t))
    t = t + dt
    loop_rate.sleep()
  
except rospy.ROSInterruptException:
  pass
