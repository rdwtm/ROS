#!/usr/bin/python3

import rospy
from std_msgs.msg import Float32

class RegulatorP:
  def __init__(self):
    self._sub = rospy.Subscriber("e", Float32, self._cb)
    self._pub = rospy.Subscriber("u", Float32, queue_size=10)
    
  def _cb(msg):
    self.kp = rospy.get_param("~kp", 1.0)
    e = msg.data
    u = self.kp * e
    self._pub.publish(u)
    

try:
  rospy.init_node("regulator_p")
  plant = RegulatorP()
  rospy.spin()
  
except rospy.ROSInterruptException:
  pass
