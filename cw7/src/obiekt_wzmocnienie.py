#!/usr/bin/python3

import rospy
from std_msgs.msg import Float32

class Wzmocnienie:
  def __init__(self):
    self._sub = rospy.Subscriber("u", Float32, self._cb)
    self._pub = rospy.Subscriber("y", Float32, queue_size=10)
    
  def _cb(msg):
    self.k = rospy.get_param("~k", 1.0)
    u = msg.data
    y = self.k * u
    self._pub.publish(y)
    

try:
  rospy.init_node("obiekt_wzmocnienie")
  plant = Wzmocnienie()
  rospy.spin()
  
except rospy.ROSInterruptException:
  pass
