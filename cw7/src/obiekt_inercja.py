#!/usr/bin/python3

import rospy
from std_msgs.msg import Float32

class Inercja:
  def __init__(self):
    self._x = 0.0
    self._t = rospy.Time.now()
    self._sub = rospy.Subscriber("u", Float32, self._cb)
    self._pub = rospy.Publisher("y", Float32, queue_size=10)
    
  def _cb(self, msg):
    self.k = rospy.get_param("~k", 1.0)
    self.T = rospy.get_param("~T", 1.0)
    t_now = rospy.Time.now()
    dt = (t_now - self._t).to_sec()
    self._t = t_now
    u = msg.data
    self._x = self._x + dt * 1.0/self.T * (u - self._x)
    y = self.k * self._x
    self._pub.publish(y)
    

try:
  rospy.init_node("obiekt_inercja")
  plant = Inercja()
  rospy.spin()
  
except rospy.ROSInterruptException:
  pass
